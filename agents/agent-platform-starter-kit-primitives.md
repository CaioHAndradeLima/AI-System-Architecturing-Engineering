# Agent platform and starter-kit primitives

How to design an **Agent Starter Kit**—a framework or SDK other engineers extend—using reusable primitives and **vendor-agnostic interfaces** instead of one-off agent scripts.

## Prerequisites

- [Example Python directories](./multi-agent-architecture/example-python-directories.md) (application layout vs platform packages)
- [LLM architecturing — gateway](../llm/llm-architecturing.md) (provider abstraction)

## Core idea

Platform work optimizes for **composition and policy**, not a single demo workflow. Product teams should configure agents (tools, prompts, policies) while the platform owns orchestration contracts, observability hooks, and safe execution boundaries. Ad-hoc agents inline provider SDK calls and tool logic; a starter kit exposes stable types and extension points so implementations can swap vendors without rewriting graphs.

## Layer model

```
Product team config          Platform SDK                 Adapters (swappable)
-------------------          -------------                --------------------
agent definitions     -->    run loop + state      -->    LLM provider
tool manifests               hook pipeline                vector store
policies / quotas            tool registry                MCP transport
prompt templates             trace + audit emitters       secret store
```

| Primitive | Responsibility | Keep vendor-specific code here |
|-----------|----------------|--------------------------------|
| **`AgentRun` / session handle** | Identity, tenant, budgets, correlation IDs | Never |
| **`ModelClient` interface** | Chat, structured output, streaming, token usage | Adapter only |
| **`ToolSpec` + `ToolExecutor`** | Schema, idempotency hints, side-effect class | Transport in adapter |
| **`HookChain`** | Pre/post model and pre/post tool interception | Hook implementations call adapters |
| **`StateStore`** | Checkpoint, thread history, durable facts | Storage backend adapter |
| **`MemoryPolicy`** | What enters context vs long-term store | Embedding/index adapters |
| **`PolicyEngine`** | Authz, allowlists, approval gates | Identity provider adapter |

## Vendor-agnostic interfaces

Define narrow interfaces in the SDK; ship one reference adapter per capability (OpenAI-compatible, Anthropic, Vertex, Bedrock, etc.).

| Interface method (conceptual) | Why it belongs in the platform |
|------------------------------|--------------------------------|
| `complete(messages, tools, options) → ModelTurn` | Single place for retries, tracing, redaction |
| `invoke_tool(call, context) → ToolResult` | Validation, authz, hooks, audit |
| `persist_checkpoint(run_id, state)` | Same resume semantics across hosts |
| `emit_span(event)` | Consistent trace shape for all agents |

Product code depends on **interfaces and DTOs**, not on `openai`, `google.cloud`, or LangChain provider classes directly. Framework integrations (LangGraph nodes, LangChain runnables) sit **behind** adapters as optional backends, not as the public API surface.

## Reusable abstractions (interview talking points)

1. **Tool as data + executor** — JSON Schema (or equivalent) registered centrally; executors are injectable. Models see the same tool list regardless of host runtime.
2. **Effect classification** — Read-only, idempotent write, destructive write. Drives approval requirements and retry policy ([secure tool execution](../output/output-secure-tool-execution-flow.md)).
3. **Budget envelope** — Max steps, wall time, tokens, and tool calls enforced by the runtime, not scattered `if` checks in agent prompts.
4. **Extension registry** — Hooks, tools, and memory backends register at startup; products enable subsets via configuration.
5. **Versioned contracts** — Prompt packs, tool schemas, and policy bundles are versioned and pinned per deployment ([prompt versioning](../prompting/prompt-versioning.md)).

## Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| **Thin SDK + adapters (this note)** | Swappable vendors; consistent safety and traces | Up-front design; adapter maintenance |
| **Framework-first (LangChain/LangGraph as API)** | Fast bootstrap | Vendor and framework coupling; harder uniform policy |
| **Copy-paste agent templates** | Quick for one team | Divergent guardrails; no shared eval or rollback story |

## Practical checklist

- [ ] Public API is interfaces + typed state/events, not provider SDKs.
- [ ] One code path executes all tools (validation → authz → hooks → executor).
- [ ] Hooks are first-class (see [agent lifecycle internals](./agent-lifecycle-internals.md)).
- [ ] Golden tests run against the SDK runtime, not only product prompts.
- [ ] Document which layers product teams may override vs platform-owned.

## See also

- [Agent lifecycle internals](./agent-lifecycle-internals.md)
- [MCP — native tools vs servers](./mcp-native-tools-vs-servers.md)
- [Agent production guardrails at scale](./agent-production-guardrails-at-scale.md)
- [Agents overview](./README.md)

## References

- [Model Context Protocol](https://modelcontextprotocol.io/) (capability exposure pattern)
