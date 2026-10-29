# Agent production guardrails at scale

Running agents **safely in production**: tracing and metrics, PII handling, circuit breakers, rollback and recovery, and human-in-the-loop (HITL)—mapped to platform and lifecycle mechanics.

## Prerequisites

- [Agent lifecycle internals](./agent-lifecycle-internals.md)
- [Guardrails strategy](../guard-rails/guardrails-strategy.md)
- [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md)

## Core idea

At scale, guardrails are **operational systems**: every agent step is observable, bounded, and recoverable. Safety is not only content filters—it includes dependency health, data handling, and governed change.

## Observability for agents

| Signal | What to capture | Why |
|--------|-----------------|-----|
| **Trace span per model/tool step** | Model id, latency, token usage, tool name (redacted args) | Debug wrong tool choice and slow paths |
| **Run-level attributes** | Tenant, agent profile, policy version, run id | Audit and cost allocation |
| **Quality metrics** | Task success, groundedness, tool error rate | SLOs and regression gates |
| **Cost metrics** | Tokens and tool calls per task | FinOps and abuse detection |

Use the same trace shape for all agents ([tracing for observability](../observability-evaluation/tracing-for-observability.md)). Inspect **trajectories**, not only final answers ([agentic AI evaluation](./agentic-ai-evaluation-and-improvement.md)).

## PII and sensitive data

- **Ingress**: classify and minimize user input; DLP at boundaries ([guard-rails decision assistance](../guard-rails/guard-rails-decision-architecturing-assistance.md)).
- **Context**: tenant-scoped retrieval; no cross-user memory without explicit consent.
- **Traces and logs**: redact payloads; store hashes/IDs for correlation ([tracing metrics](../observability-evaluation/tracing-for-observability-metrics.md)).
- **Tool results**: strip account numbers, government IDs, and auth tokens before the next model turn.
- **Golden datasets**: no real PII in stored eval cases ([production retrieval regression testing](../deployment/production-retrieval-regression-testing.md)).

## Circuit breakers and dependency protection

Apply breakers at **model providers**, **MCP servers**, **retrieval**, and **downstream microservices**:

```
Call dependency
      |
      v
Breaker open? ──Yes──→ Fail fast / degraded path / queue
      |
     No
      v
Execute with timeout
      |
      v
Record success/failure → update breaker state
```

Pair with bounded retries and concurrency limits ([production components](../deployment/production-components.md), [LLM retry and fallbacks](../llm/llm-retry-fallbacks-routing.md)). For agents, **fail closed** on missing evidence rather than hallucinating when retrieval is down.

## Rollback and recovery

| Mechanism | Agent-specific use |
|-----------|-------------------|
| **Versioned prompts/tools/policies** | Roll back behavior without redeploying entire monolith |
| **Checkpoint resume** | Continue after worker crash or approval timeout |
| **Canary deploy** | Route fraction of traffic to new agent graph ([regression and canary](../observability-evaluation/regression-and-canary-releases.md)) |
| **Eval gate in CI** | Block promote when golden task success drops |
| **Feature flags** | Disable a single MCP server or tool class quickly |

Keep rollback artifacts (container image, config bundle, prompt version) aligned—mixed versions cause subtle tool schema mismatches.

## Human-in-the-loop (HITL)

Use HITL when automation risk exceeds tolerance:

| Trigger | Example |
|---------|---------|
| Destructive or financial side effect | Transfer, credit decision, account closure |
| Low model confidence or verifier fail | Second model disagrees with tool result |
| Policy gray area | Escalation queue for compliance review |
| User-requested confirmation | “Approve before send” |

Flow: pause run → persist **checkpoint** with pending action → present diff to operator → on approve, resume pre-tool execution with audit record ([secure tool execution flow](../output/output-secure-tool-execution-flow.md)). Timeouts and deny paths must be explicit.

## Scale checklist

- [ ] SLOs on p95 latency, error rate, and task success per agent profile.
- [ ] Dashboards: tokens, tool errors, breaker state, queue depth for HITL.
- [ ] Alert on loop exhaustion, breaker open, and eval regression.
- [ ] Runbooks link traces to rollback steps ([investigate failure by observability data](../observability-evaluation/investigate-failure-by-observability-data.md)).
- [ ] Periodic red-team on tool injection and exfiltration paths.

## See also

- [Deployment production flow](../deployment/production-flow.md)
- [Fintech reliable agents](../design/fintech-reliable-agents.md)
- [Agents overview](./README.md)
