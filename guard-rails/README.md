# Guard-rails

Layered validation, access control, and output policy for agent and LLM systems.

## Guard-rails types

| Type | Purpose |
|------|---------|
| **AI safety** | Control harmful, irrelevant, or unsupported model behavior. |
| **Security** | Enforce authentication, authorization, tenant isolation, and data protection. |
| **Reliability** | Validate outputs, limit resource consumption, and control failures. |

These types overlap in a real pipeline—for example, output validation touches both **AI safety** and **reliability**, and ACL spans **security** and **tool checks**. See [guardrails-strategy.md](./guardrails-strategy.md) for how layers map to a request flow.

## Enforcement layers

| Layer | What to enforce |
|-------|-----------------|
| **Identity** | Authenticate the user and establish trusted identity claims. |
| **Application** | Verify the user's membership and permissions for the requested tenant. |
| **Retrieval** | Apply tenant and document-level permission filters before returning chunks. |
| **Data stores and tools** | Enforce access restrictions on queries, object reads, and external API calls. |
| **Output and observability** | Prevent unauthorized content from being returned, cached, or exposed through logs and traces. |

See [safer-architecture-tenant-scoped-retrieval.md](./safer-architecture-tenant-scoped-retrieval.md) for a request flow that applies these layers end to end.

## What good guardrails do

| # | Goal |
|---|------|
| 1 | **Enforces a clearly defined rule.** For example, a user cannot access documents outside their tenant. |
| 2 | **Runs at the correct boundary.** Authorization runs before data access; output validation runs before the response is returned. |
| 3 | **Fails safely.** If authorization cannot be verified, access is denied. If a mandatory validation service is unavailable, the system does not silently bypass the check. |
| 4 | **Can be tested.** You can demonstrate that valid requests work and unauthorized requests fail. |

---

## Guides

### [guardrails-strategy.md](./guardrails-strategy.md)

`#pipeline` · `#layers` · `#request-flow`

End-to-end guardrail order from user input through ACL, agent execution, tool/retrieval checks, and output validation. Use this as the default mental model for where each control runs.

→ [See more in guardrails-strategy.md](./guardrails-strategy.md)

### [guard-rails-category.md](./guard-rails-category.md)

`#taxonomy` · `#enforcement` · `#reference`

Maps guardrail categories (input, auth, tenant isolation, tools, output, privacy, etc.) to examples and preferred enforcement points—application code, IdP, IAM, classifiers.

→ [See more in guard-rails-category.md](./guard-rails-category.md)

### [guardrails-cloud-architecture.md](./guardrails-cloud-architecture.md)

`#cloud` · `#architecture` · `#edge-to-output`

Full production stack from WAF/API gateway through identity, app guardrails, AI safety screening, tenant-scoped data/tools, agent workflow, and output controls—plus cross-cutting secrets, encryption, audit, and monitoring.

→ [See more in guardrails-cloud-architecture.md](./guardrails-cloud-architecture.md)

### [guard-rails-cloud-comparison.md](./guard-rails-cloud-comparison.md)

`#cloud` · `#multi-cloud` · `#reference`

Side-by-side AWS, Google Cloud, and Azure services for edge protection, identity, AI safety, DLP, secrets, audit/monitoring, and tenant isolation.

→ [See more in guard-rails-cloud-comparison.md](./guard-rails-cloud-comparison.md)

### [ai-specific-controls-amazon-bedrock-guardrails.md](./ai-specific-controls-amazon-bedrock-guardrails.md)

`#aws` · `#bedrock` · `#ai-safety`

Bedrock Guardrails capabilities (content, injection, topics, PII, grounding, reasoning checks) plus related WAF, API Gateway, IAM, secrets, and audit services.

→ [See more in ai-specific-controls-amazon-bedrock-guardrails.md](./ai-specific-controls-amazon-bedrock-guardrails.md)

### [ai-specific-controls-google-model-armor.md](./ai-specific-controls-google-model-armor.md)

`#gcp` · `#model-armor` · `#ai-safety`

Model Armor prompt/document/response screening, Sensitive Data Protection integration, templates—and related Armor, API Gateway, IAM, Secret Manager, audit, and monitoring.

→ [See more in ai-specific-controls-google-model-armor.md](./ai-specific-controls-google-model-armor.md)

### [ai-specific-controls-azure-content-safety-prompt-shields.md](./ai-specific-controls-azure-content-safety-prompt-shields.md)

`#azure` · `#content-safety` · `#prompt-shields`

Prompt Shields and Content Safety screening, app-side validation, Purview integration—and related WAF, API Management, Entra ID, Key Vault, and Monitor.

→ [See more in ai-specific-controls-azure-content-safety-prompt-shields.md](./ai-specific-controls-azure-content-safety-prompt-shields.md)

### [wrong-architecture-shared-retrieval.md](./wrong-architecture-shared-retrieval.md)

`#anti-pattern` · `#multi-tenant` · `#rag`

Shows why one shared vector index for all customers leaks data across tenants. Documents failure modes when retrieval is not scoped before the LLM sees chunks.

→ [See more in wrong-architecture-shared-retrieval.md](./wrong-architecture-shared-retrieval.md)

### [safer-architecture-tenant-scoped-retrieval.md](./safer-architecture-tenant-scoped-retrieval.md)

`#architecture` · `#multi-tenant` · `#rag` · `#identity`

IdP verification, backend tenant resolution, membership checks, and mandatory `tenant_id` filters on retrieval—with response validation before reply.

→ [See more in safer-architecture-tenant-scoped-retrieval.md](./safer-architecture-tenant-scoped-retrieval.md)

### [guardrails-data-isolation.md](./guardrails-data-isolation.md)

`#data-isolation` · `#tenancy` · `#storage`

Compares three storage patterns: shared DB with `tenant_id`, separate schemas/databases, and dedicated infrastructure per tenant—including trade-offs and guardrail checklists.

→ [See more in guardrails-data-isolation.md](./guardrails-data-isolation.md)

### [guardrails-aws-services.md](./guardrails-aws-services.md)

`#aws` · `#infrastructure` · `#security`

Platform controls that complement app guardrails: API gateway/WAF, IAM, secrets, DB auth, network, encryption, audit logs, and monitoring.

→ [See more in guardrails-aws-services.md](./guardrails-aws-services.md)

### [guard-rails-test-use-cases.md](./guard-rails-test-use-cases.md)

`#testing` · `#multi-tenant` · `#checklist`

Integration-style scenarios (cross-tenant doc access, forged `tenant_id`, cache isolation, tool abuse, injection in chunks) with expected deny or safe outcomes.

→ [See more in guard-rails-test-use-cases.md](./guard-rails-test-use-cases.md)

### [guard-rails-robust-cloud-rules-implementation.md](./guard-rails-robust-cloud-rules-implementation.md)

`#checklist` · `#multi-tenant` · `#production`

Seven requirements for trusted tenant resolution, pre-access authorization, DB policies, scoped retrieval, isolated cache/memory/jobs, least-privilege tools, and cross-tenant tests.

→ [See more in guard-rails-robust-cloud-rules-implementation.md](./guard-rails-robust-cloud-rules-implementation.md)
