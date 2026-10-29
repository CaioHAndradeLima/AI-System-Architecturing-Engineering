# Guardrails strategy

A **defense-in-depth pipeline** for agent systems: validate and authorize before execution, constrain tool and retrieval access during the run, then validate again before anything reaches the user.

## Prerequisites

- [Example Python directories](../agents/multi-agent-architecture/example-python-directories.md) (`guardrails/` package placement)
- Basic [multi-agent orchestration](../agents/README.md)

## Core idea

Guardrails are not a single filter at the end. They wrap **every boundary** where untrusted input enters, privileged actions run, or generated content exits. Fail closed: block, strip, or escalate rather than silently proceeding when policy or schema checks fail.

## Architecture

```
User request
     |
     v
+-------------------------+
| Input guardrails        |
| Schema · size · policy  |
+-------------------------+
     |
     v
+-------------------------+
| Authentication / ACL    |
| Who can access what?    |
+-------------------------+
     |
     v
+-------------------------+
| Supervisor / Agents     |
| Routing and execution   |
+-------------------------+
     |
     v
+-------------------------+
| Tool / retrieval checks |
| Permissions · validation|
+-------------------------+
     |
     v
+-------------------------+
| Output guardrails       |
| Schema · policy · checks|
+-------------------------+
     |
     v
   Response
```

## Layer responsibilities

| Layer | What to enforce | Typical mechanisms |
|-------|-----------------|-------------------|
| **Input guardrails** | Request shape, max tokens/attachments, blocked topics, injection heuristics | JSON schema, length limits, classifiers, allow/deny lists |
| **Authentication / ACL** | Identity, tenant, role, feature flags | OAuth/API keys, RBAC, row-level or collection-level access |
| **Supervisor / agents** | Routing only within entitled capabilities | Supervisor prompts scoped to allowed agents; no tool exposure in system prompt for forbidden actions |
| **Tool / retrieval checks** | Every side effect and data read | Tool allowlists per user, query filters on vector stores, parameter validation, human approval for destructive ops |
| **Output guardrails** | Safe, on-policy, correctly shaped replies | Output schema, PII redaction, citation requirements, moderation, refusal templates |
| **Response** | What the client receives | Strip internal chain-of-thought; log redacted copies for audit |

## How it works

1. **Input** runs before any LLM call so oversized, malformed, or clearly abusive requests never consume model budget or touch retrieval.
2. **ACL** binds the session to a **principal** (user, service account, tenant). Downstream checks use the same identity—do not re-trust user text for authorization.
3. **Agents** execute inside that envelope; guardrails here are mostly **configuration** (which agents/tools exist for this principal), not post-hoc moderation alone.
4. **Tool / retrieval** is the highest-risk zone: validate arguments, enforce server-side permissions (never rely on the model to “choose not to”), and log tool names + args (redacted).
5. **Output** validates structure for API contracts and content for policy; optionally run a separate critic step for regulated domains.

Order matters: authentication after basic input parsing is common (you need a body to parse), but **authorization must precede** any retrieval or tool that reads sensitive data.

## Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| **Layered pipeline (this strategy)** | Clear ownership per stage; easier compliance mapping | Latency from multiple checks; must keep policies in sync |
| **Output-only moderation** | Simple to add late | Injection and data exfiltration already happened |
| **Model-only “be safe” instructions** | Zero infra | Unreliable under adversarial or ambiguous prompts |

## Practical checklist

- [ ] Separate **input_validation**, **access_control**, and **output_validation** modules (see example app layout)
- [ ] Centralize policy definitions; avoid duplicating rules in every agent prompt
- [ ] Test guardrails with **adversarial inputs** and golden “must refuse” cases (see [test use cases](./guard-rails-test-use-cases.md))
- [ ] Emit spans/metrics per layer to see where requests die
- [ ] Document **fail-closed** behavior for each layer (HTTP code, user message, internal alert)

## Reference implementation

**[guardrails-strategies](https://github.com/CaioHAndradeLima/guardrails-strategies)** — Layered pipeline in `policy_pipeline.py` / `strategies.py`. Keys: `guardrails_strategy`, `strategy_comparison`.

Recommended gate: `ci-guardrails-eval` (`evaluate-pipeline` + `check-measure`). Coverage: [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/guardrails-strategies/blob/main/docs/LAB_COVERAGE.md) (14/14).

## See also

- [Example Python directories](../agents/multi-agent-architecture/example-python-directories.md)
- [Guard-rails overview](./README.md)
