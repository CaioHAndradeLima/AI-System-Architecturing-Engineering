# Fintech reliable agents

High-stakes patterns for **banking, credit, and payments** agents: reliability, security, auditability, and controlled autonomy when mistakes have regulatory and customer impact.

## Prerequisites

- [Agent production guardrails at scale](../agents/agent-production-guardrails-at-scale.md)
- [Safer architecture tenant-scoped retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md)
- [Guardrails strategy](../guard-rails/guardrails-strategy.md)

## Core idea

Fintech agents are **decision support and workflow automation**, not unbounded autonomous traders. Every consequential action needs identity, authorization, evidence, validation, and an audit trail suitable for compliance review—similar to how core banking services treat transactions.

## Non-negotiables

| Principle | Agent implication |
|-----------|-------------------|
| **Strong identity** | Bind every run to authenticated customer or operator; no anonymous tool access |
| **Least privilege** | Tool allowlists per role; no “admin” tools in customer-facing agents |
| **Idempotency** | Payment and account writes use idempotency keys; safe retries |
| **Dual control** | HITL for irreversible or high-value actions |
| **Explainability** | Citations to policy docs and tool results; retain trace for disputes |
| **Data minimization** | Retrieve only entitled records; redact in logs and model context |

## Architecture emphasis

```
User / operator
      |
      v
Input guardrails + auth (fail closed)
      |
      v
Orchestrator with budgets + hooks
      |
      +--> Retrieval (tenant-scoped, audited queries)
      |
      +--> Tools via policy engine (native + MCP)
      |
      v
Output validation + optional human approval
      |
      v
Audit event (who, what, policy version, outcome)
```

Credit and banking contexts add **model risk** and **fair lending** concerns: document which decisions are fully automated vs recommend-only, and keep human ownership for adverse actions.

## Reliability patterns (interview narrative)

- **PayPal / wallet scale**: idempotent APIs, fraud and rate limits, clear error taxonomy for agents—teach the model bounded retry behavior via post-tool error shaping, not infinite loops.
- **Retail banking (Itaú-style)**: strict tenant isolation, branch/channel entitlements, long-lived customer relationships—session persistence must not leak prior user context on shared devices without re-auth.
- **Credit / lending (Banco Master-style)**: sensitive PII, regulatory retention, explainable declines—HITL and structured outputs before customer-visible messages.

Tie stories to **concrete controls** (checkpoint + approval, breaker on core banking API, eval golden set for fee disclosure accuracy)—not generic “we used AI.”

## Security and abuse

- Prompt injection attempts to exfiltrate other customers’ data → blocked by retrieval filters and tool authz, not prompt pleading alone.
- Tool argument tampering (amount, payee) → server-side validation against entitled accounts.
- Model hallucination on rates or fees → require grounded retrieval or static approved snippets for regulated copy.

## Operational readiness

| Area | Practice |
|------|----------|
| **Incidents** | Roll back prompt/tool/policy version; disable tool class via flag |
| **Testing** | Golden tasks for disclosures, limits, and refusal behavior |
| **Monitoring** | Anomaly on tool denials, approval queue depth, breaker opens on ledger APIs |
| **Third parties** | MCP and vendor LLM DPAs; region and data residency on GCP Vertex |

## Practical checklist

- [ ] Classify each tool as read / idempotent write / irreversible write.
- [ ] HITL and dual approval where policy requires it.
- [ ] Audit log immutable fields: principal, action, policy version, trace id.
- [ ] No production PII in eval sets or public traces.
- [ ] Runbooks for partial outage (retrieval down → abstain, not invent).

## See also

- [GCP microservices agent platform](./gcp-microservices-agent-platform.md)
- [Secure tool execution flow](../output/output-secure-tool-execution-flow.md)
- [Observability decision-based](../observability-evaluation/observability-decision-based.md)
