# Platform agent interview cheat sheet

Quick talking points for **Agent Starter Kit / platform**, lifecycle, MCP, production guardrails, **GCP microservices**, and **fintech**—with links to full guides in this repo.

## Platform mindset (Agent Starter Kit)

- Build a **runtime + contracts**, not one demo agent: `ModelClient`, `ToolSpec`/`ToolExecutor`, `HookChain`, `StateStore`, `PolicyEngine` behind **adapters** (vendor code stays at the edge).
- Product teams configure **agents, tools, prompts**; platform owns **budgets, hooks, tracing, authz path for every tool call**.
- **Version** prompts, tool schemas, and policy bundles together at deploy; rollback is config + image, not prompt edits in prod.

→ [Agent platform starter-kit primitives](./agent-platform-starter-kit-primitives.md)

## Agent internals & lifecycle

- Loop: **pre-model → model → post-model → (pre-tool → validate → authz → execute → post-tool)* → loop control → pre-response**.
- **Validate tool calls before side effects**; never auto-retry policy/auth failures; retry transport with backoff inside latency budget.
- **Loop control**: max steps/time/tokens, duplicate (tool, args) detection, repair attempts capped.
- **Persistence**: hot thread state, warm **checkpoints** (resume, HITL pause), cold memory with tenant scope and TTL; no secrets/PII in checkpoints.
- **Memory**: trim tool results; retrieve with same ACL as tools.

→ [Agent lifecycle internals](./agent-lifecycle-internals.md)

## MCP vs native tools

- **Native**: low latency, same trust zone, needs session/graph state.
- **MCP**: separate team, credentials, language, sandbox, reuse across hosts (IDE + prod).
- **Host always** runs hooks, authz, tracing, breakers—one `invoke_tool` for both.

→ [MCP — native tools vs servers](./mcp-native-tools-vs-servers.md)

## Production guardrails & observability

- **Traces**: span per model/tool step; run id, tenant, policy version; redact args in logs.
- **Metrics**: task success, tool error rate, tokens/cost, p95 latency, breaker state, HITL queue depth.
- **PII**: minimize ingress, tenant-scoped retrieval, redact traces, no PII in golden sets.
- **Circuit breakers** on LLM, retrieval, MCP, core APIs; fail closed (abstain) when evidence path is down.
- **Rollback/canary**: versioned prompts/tools; eval gate; feature-flag disable tool class.
- **HITL**: checkpoint pending action → approve/deny → audit; timeouts explicit.

→ [Agent production guardrails at scale](./agent-production-guardrails-at-scale.md) · [Secure tool execution](../output/output-secure-tool-execution-flow.md) · [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md)

## Tech stack: TypeScript, Python, GCP, microservices

- Edge API (often **TS**) → **orchestrator** (Python or TS SDK) → **retrieval service** → **Vertex** LLM/embeddings; **Pub/Sub** for async; **Firestore/Spanner/Redis** checkpoints; **Secret Manager**; Cloud Trace + LLM trace vendor.
- Authz at **every** service, not only API gateway.

→ [GCP microservices agent platform](../design/gcp-microservices-agent-platform.md)

## Fintech narrative (PayPal, Itaú, Banco Master)

- **Identity + least privilege** on every run; **idempotency keys** on money/account writes.
- **Dual control / HITL** for irreversible or high-value actions; **audit** (who, what, policy version, trace id).
- **Explainability**: grounded policy/rates/fees; no customer-facing numbers without retrieval or approved snippets.
- Stories → **controls**: breakers on ledger APIs, tenant isolation, rollback prompt/tool version, golden tasks for disclosures.

→ [Fintech reliable agents](../design/fintech-reliable-agents.md)

## 60-second closing structure

Baseline → failure mode with labeled example → smallest targeted change → held-out **quality + latency + cost** → canary/rollback plan.

## See also

- [Agentic AI evaluation and improvement](./agentic-ai-evaluation-and-improvement.md)
- [Guardrails strategy](../guard-rails/guardrails-strategy.md)
- [Retrieval reranker evaluation](../retrieval/search/retrieval-reranker-evaluation-and-fine-tuning.md)
