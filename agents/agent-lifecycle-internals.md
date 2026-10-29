# Agent lifecycle internals

Deep mechanics of the **agent loop**: hooks around model and tool steps, validation, retries, loop control, session persistence, and memory—what interviewers mean by “agent internals.”

## Prerequisites

- [Agent platform starter-kit primitives](./agent-platform-starter-kit-primitives.md)
- [LLM retry, fallbacks, and routing](../llm/llm-retry-fallbacks-routing.md)
- [Secure tool execution flow](../output/output-secure-tool-execution-flow.md)

## Core idea

An agent run is a **state machine** driven by model turns and tool results. Production quality comes from explicit phases—each with hooks, budgets, and persistence—not from an unbounded `while True` calling the model.

## Lifecycle phases

```
START → load session/checkpoint
     → PRE_MODEL hooks (policy, context assembly)
     → MODEL turn (may emit tool calls)
     → POST_MODEL hooks (parse, validate proposals)
     → for each tool call:
           PRE_TOOL hooks → validate → authorize → execute → POST_TOOL hooks
     → merge results into state
     → loop control (continue / finish / escalate)
     → PRE_RESPONSE hooks → return or checkpoint
END
```

## Hooks

| Hook | Typical responsibilities | Fail mode |
|------|-------------------------|-----------|
| **Pre-model** | Inject system policy, trim context, redact PII from history, attach trace IDs | Block or strip unsafe context |
| **Post-model** | Parse structured output; reject malformed tool JSON; detect empty or policy-violating text | Retry within budget or safe failure |
| **Pre-tool** | Schema validation, argument sanitization, authz, rate limits, human approval queue | Do not execute; record denial |
| **Post-tool** | Truncate oversized results, redact secrets, map errors to agent-readable messages | Never pass raw stack traces to the model |
| **Pre-response** | Output schema, citation checks, moderation | Block response; offer safe template |

Implement hooks as a **ordered chain** with short-circuit on deny. Business authorization stays in application code, not in model instructions ([guardrails strategy](../guard-rails/guardrails-strategy.md)).

## Tool-call validation

Treat every proposed call as **untrusted** until validated:

1. Tool name ∈ allowlist for this principal and agent profile.
2. Arguments match registered JSON Schema (types, enums, max length).
3. Business rules (amount limits, account ownership, date ranges) pass server-side.
4. Side-effect class matches approval policy ([secure tool execution flow](../output/output-secure-tool-execution-flow.md)).

Do **not** auto-retry denied or unauthorized calls; retry only transient infrastructure errors on the **executor**, not policy failures.

## Retries and loop control

| Situation | Retry? | Control |
|-----------|--------|---------|
| Network blip on model or tool HTTP | Yes, bounded backoff | Count against latency budget |
| Invalid JSON / schema from model | Limited repair turn | Max repair attempts in config |
| Tool 4xx policy / auth failure | No | Stop or escalate |
| Model repeats same failing tool | No | Loop detector on (tool, args hash) |
| Max steps / time / tokens exceeded | No | Graceful handoff or abstain |

Align step limits with [LLM retry and fallbacks](../llm/llm-retry-fallbacks-routing.md) and graph-level stop conditions (LangGraph `recursion_limit`, explicit `END` transitions).

## State and session persistence

| Store | Holds | Use when |
|-------|-------|----------|
| **Thread state (hot)** | Messages, pending tool calls, turn counter | Single request or short conversation |
| **Checkpoint (warm)** | Serializable graph state + versions | Resume after crash, human approval pause, multi-worker |
| **Long-term memory (cold)** | User facts, summaries, embeddings | Cross-session personalization within policy |

Persistence rules:

- Checkpoints include **policy and tool schema versions** so resume does not mix incompatible behavior.
- Idempotent **run IDs** tie traces, audits, and approvals to one logical task.
- Secrets and full PII never belong in checkpoint payloads—store references and redacted summaries ([reliable architecture](../contexting/context-reliable-architecture.md)).

## Memory management

| Memory type | What goes in | Risk if mishandled |
|-------------|--------------|-------------------|
| **Working context** | Recent turns + tool results (trimmed) | Context overflow, cost, leakage across tenants |
| **Retrieved memory** | RAG chunks with tenant filters | Cross-tenant exfiltration |
| **Summarized history** | Compressed older turns | Lost nuance; hallucinated “facts” |
| **Structured memory** | Key-value facts with provenance | Stale or wrong user profile |

Apply **tenant-scoped retrieval**, TTL on summaries, and explicit “forget” for compliance. Prefer retrieving memory at pre-model hook time with the same ACL as tools.

## Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| **Explicit hook pipeline** | Testable; clear compliance story | More boilerplate than raw SDK loops |
| **All logic in prompts** | Fast prototype | Unreliable validation and loop control |
| **Checkpoint every step** | Strong recovery | Storage cost and latency |

## Practical checklist

- [ ] Document hook order and which hooks can block execution.
- [ ] Validate tool calls before any side effect; log redacted args.
- [ ] Separate retry policies for model, tool transport, and policy errors.
- [ ] Enforce max steps, time, tokens, and duplicate-tool detection.
- [ ] Persist checkpoints for HITL and crash recovery; version policy with state.
- [ ] Trim and redact tool results before the next model call.

## See also

- [Agent platform starter-kit primitives](./agent-platform-starter-kit-primitives.md)
- [Context conversation strategies](../contexting/context-conversation-strategies.md)
- [Context assembly LangGraph](../contexting/context-assembly-langchain-langgraph.md)
- [Agentic AI evaluation and improvement](./agentic-ai-evaluation-and-improvement.md)
