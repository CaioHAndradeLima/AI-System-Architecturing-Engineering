# Guard-rails robust cloud rules implementation

Checklist for a **production-grade** multi-tenant agent or RAG stack on cloud: rules must be enforced in identity, data, retrieval, async work, and tests—not only in prompts or AI safety APIs.

## A robust implementation should have

| Requirement | What it means |
|-------------|----------------|
| **Trusted tenant resolution from authenticated identity** | Map the verified principal to tenant context in the backend; never trust client-supplied tenant IDs alone. |
| **Authorization checks before retrieving or modifying data** | Membership and resource permissions are evaluated before vector search, SQL, or tool side effects. |
| **Database policies or equivalent enforcement where supported** | Row-level security, IAM-scoped data access, or store-native policies as a backstop to application filters. |
| **Tenant-scoped vector retrieval and document permissions** | Every chunk query and document read is filtered to the active tenant and user entitlements. |
| **Isolated caches, agent memory, and background-job state** | Keys and queues include tenant (and user where needed) so one customer cannot read another’s cached answers or job payloads. |
| **Restricted service identities and tool permissions** | Workloads and tools run with least privilege; broad admin roles are not attached to the agent runtime. |
| **Automated tests that attempt cross-tenant access** | CI proves forbidden reads, searches, cache hits, and tool calls fail—see [test use cases](./guard-rails-test-use-cases.md). |

## Where this fits in the stack

- End-to-end flow: [guardrails cloud architecture](./guardrails-cloud-architecture.md)
- Retrieval pattern: [safer architecture — tenant-scoped retrieval](./safer-architecture-tenant-scoped-retrieval.md)
- Storage tiers: [guardrails data isolation](./guardrails-data-isolation.md)
- AI safety alone is insufficient: [Azure Prompt Shields note](./ai-specific-controls-azure-content-safety-prompt-shields.md), [Model Armor](./ai-specific-controls-google-model-armor.md), [Bedrock Guardrails](./ai-specific-controls-amazon-bedrock-guardrails.md)

## Reference implementation

**[guardrails-strategies](https://github.com/CaioHAndradeLima/guardrails-strategies)** — Checklist coverage in `implementation_flow.py`. Keys: `guard_rails_robust_implementation`, `implementation_checklist`.

Recommended gate: `ci-guardrails-eval` (`evaluate-pipeline` + `check-measure`). Coverage: [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/guardrails-strategies/blob/main/docs/LAB_COVERAGE.md) (14/14).

## See also

- [What good guardrails do](./README.md#what-good-guardrails-do)
- [Enforcement layers](./README.md#enforcement-layers)
- [Guard-rails overview](./README.md)
