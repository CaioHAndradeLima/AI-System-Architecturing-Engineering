# Guard-rails decision architecturing assistance

When to adopt common guardrails by **product stage** (small/MVP → medium → large/mature), plus a **cloud service map** for AWS, Google Cloud, and Azure. Use with [guard-rails category](./guard-rails-category.md), [cloud comparison](./guard-rails-cloud-comparison.md), and [robust implementation](./guard-rails-robust-cloud-rules-implementation.md).

## Foundation and platform controls

| Guardrail / tool | Relevance | Cost | Small / MVP | Medium | Large / mature |
|------------------|-----------|------|-------------|--------|----------------|
| **Input/output validation** — Pydantic, JSON Schema | Prevents malformed requests, tool arguments, and responses | Low | Required | Required | Required |
| **Authentication** — OIDC/OAuth, managed identity | Establishes who the user is | Low–Medium | Required for user-facing products | Required | Required |
| **Authorization** — application policies, OPA/OpenFGA | Determines which actions and resources users can access | Low–Medium | Required | Centralize policies as complexity grows | Formal policy governance |
| **Tenant isolation** — tenant-scoped queries, database policies | Prevents customers from accessing one another's data | Low–High depending on isolation model | Required for multi-tenant products | Automated isolation tests | Dedicated resources for high-risk tenants |
| **API protection** — API Gateway, WAF, rate limits | Reduces abuse and common web attacks | Low–Medium | Basic gateway and quotas | WAF and tuned policies | Advanced edge protection |
| **Secrets** — Secrets Manager, Secret Manager, Key Vault | Protects credentials and API keys | Low–Medium | Required | Rotation and alerts | Automated rotation and audited access |
| **Least privilege** — IAM, service identities | Limits what workloads and tools can access | Low | Required | Separate identities by workload | Stronger workload and tenant boundaries |

## AI safety and agent controls

| Guardrail / tool | Relevance | Cost | Small / MVP | Medium | Large / mature |
|------------------|-----------|------|-------------|--------|----------------|
| **Prompt-injection detection** — Bedrock Guardrails, Model Armor, Prompt Shields | Helps identify malicious instructions | Low–Medium | Based on threat model | Add monitoring and adversarial tests | Layered defenses and formal red-team testing |
| **Content moderation** — cloud safety services | Detects configured harmful or prohibited content | Low–Medium | Based on product risk | Tune thresholds and policies | Governance and specialized controls |
| **PII/DLP** — Presidio, cloud DLP services | Detects or masks sensitive data | Low–Medium | Minimize sensitive data and logs | Add screening at relevant boundaries | Classification and retention governance |
| **Retrieval authorization** — tenant filters, ACLs, database policies | Prevents unauthorized documents reaching the LLM | Low–Medium | Required for private RAG | ACL synchronization and regression tests | Stronger index/database separation if needed |
| **Tool guardrails** — typed tools, allowlists, authorization | Prevents agents performing unauthorized actions | Low | Required if tools access data or change state | Per-tool permissions and audit events | Approval workflows and separation of duties |
| **Human approval** | Controls high-impact or destructive actions | Low–Medium | Required for high-risk actions | Workflow-based approvals | Role-based approvals and dual control |
| **Output checks** — schema and citation validation | Rejects malformed output and invalid references | Low | Required where structured output is expected | Add semantic checks | Versioned contracts and independent validation |

## Reliability, evaluation, and state isolation

| Guardrail / tool | Relevance | Cost | Small / MVP | Medium | Large / mature |
|------------------|-----------|------|-------------|--------|----------------|
| **Grounding/evaluation** — golden datasets, retrieval metrics | Measures whether answers are supported and correct | Low–Medium | Golden dataset and manual reviews | Automated regression suite | Continuous risk-based evaluation |
| **Rate limits and cost budgets** | Prevents abuse, runaway loops, and unexpected spend | Low | Basic quotas and token limits | Per-tenant quotas and alerts | Budgets and anomaly detection |
| **Timeouts/retries/idempotency** | Prevents hung calls and duplicate actions | Low | Required for external calls | Standard resilience policies | Durable workflows and replay controls |
| **Observability** — CloudWatch, Cloud Monitoring, Azure Monitor, LangSmith/Langfuse | Investigates failures and traces AI execution | Low–Medium | Basic logs, metrics, audit events | Distributed traces and alerts | SIEM integration and formal incident workflows |
| **Privacy-safe logging** | Prevents logs and traces becoming another data-leak path | Low–Medium | Minimize sensitive logging | Automated redaction | Retention governance and audited access |
| **Cache isolation** | Prevents cached results leaking between users or tenants | Low | Required if private data is cached | Automated cache-isolation tests | Separate namespaces/caches when justified |
| **Conversation memory isolation** | Prevents cross-user or cross-tenant history leakage | Low–Medium | Required if memory persists | Scoped storage and deletion jobs | Stronger state separation |

## Infrastructure, testing, and release

| Guardrail / tool | Relevance | Cost | Small / MVP | Medium | Large / mature |
|------------------|-----------|------|-------------|--------|----------------|
| **Background-job isolation** | Keeps queued work bound to the correct tenant | Low–Medium | Required if async jobs exist | Worker identities and replay tests | Isolated workers/queues where justified |
| **Encryption** | Protects data in transit and at rest | Low–Medium | Required baseline | Key policies and rotation | Customer-managed keys when required |
| **Network controls** | Reduces exposure and restricts service communication | Medium | Managed defaults; assess risk | Private endpoints where appropriate | Network segmentation and controlled egress |
| **Security tests** | Tests authorization, isolation, and attack scenarios | Low–Medium | Required baseline | Automated CI and adversarial tests | Continuous testing and independent assessment |
| **Release controls** — feature flags, canaries, rollback | Limits the impact of unsafe releases | Low–Medium | Basic rollback | Canary releases and runbooks | Mature incident/change management |
| **Dedicated tenant infrastructure** | Provides stronger customer separation | High | Usually unnecessary unless required | For selected enterprise customers | For high-risk or contractually isolated tenants |

## Cloud service mapping

| Responsibility | AWS | Google Cloud | Azure |
|----------------|-----|--------------|-------|
| **AI safety** | Amazon Bedrock Guardrails | Model Armor | Azure AI Content Safety |
| **Identity and access** | IAM, Cognito | Cloud IAM, Identity Platform | Microsoft Entra ID, Azure RBAC |
| **API and edge** | API Gateway, AWS WAF | API Gateway, Cloud Armor | API Management, Azure WAF |
| **Secrets** | Secrets Manager, KMS | Secret Manager, Cloud KMS | Key Vault |
| **Audit** | CloudTrail | Cloud Audit Logs | Azure Activity Log |
| **Monitoring** | CloudWatch | Cloud Monitoring | Azure Monitor |
| **Data protection** | AWS data protection services | Sensitive Data Protection | Microsoft Purview and applicable data protection services |
| **Custom policy engine** | OPA/OpenFGA or application policies | OPA/OpenFGA or application policies | OPA/OpenFGA or application policies |

Deep dives: [Bedrock Guardrails](./ai-specific-controls-amazon-bedrock-guardrails.md) · [Model Armor](./ai-specific-controls-google-model-armor.md) · [Azure Content Safety / Prompt Shields](./ai-specific-controls-azure-content-safety-prompt-shields.md) · [Cloud architecture](./guardrails-cloud-architecture.md)

## The rules I would never compromise on

| # | Rule |
|---|------|
| 1 | **Never use the LLM as the authorization boundary.** |
| 2 | **Never rely on a prompt to enforce tenant isolation.** |
| 3 | **Apply access control before data reaches the model.** |
| 4 | **Re-authorize every tool or action at execution time.** |
| 5 | **Isolate caches, conversation memory, background jobs, logs, and traces—not just the database.** |
| 6 | **Fail closed when a mandatory authorization check cannot be completed.** |
| 7 | **Test cross-tenant access continuously.** |
| 8 | **Treat AI safety filters as risk reduction, not proof of security or correctness.** |
| 9 | **Log enough to investigate incidents, but avoid logging sensitive payloads by default.** |
| 10 | **Add complexity when risk, evidence, or requirements justify it.** |

## Reference implementation

**[guardrails-strategies](https://github.com/CaioHAndradeLima/guardrails-strategies)** — Maturity snapshot in `maturity.py`. Keys: `guard_rails_decision_assistance`, `maturity`.

Recommended gate: `ci-guardrails-eval` (`evaluate-pipeline` + `check-measure`). Coverage: [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/guardrails-strategies/blob/main/docs/LAB_COVERAGE.md) (14/14).

## See also

- [Guard-rails test use cases](./guard-rails-test-use-cases.md)
- [Guardrails data isolation](./guardrails-data-isolation.md)
- [Guard-rails overview](./README.md)
