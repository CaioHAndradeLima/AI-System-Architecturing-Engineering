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

## Guides

| Note | Summary |
|------|---------|
| [guard-rails-category.md](./guard-rails-category.md) | Categories, examples, and preferred enforcement (Pydantic, IdP, IAM, etc.) |
| [guardrails-aws-services.md](./guardrails-aws-services.md) | API gateway/WAF, IAM, secrets, encryption, audit logs, monitoring |
| [guardrails-data-isolation.md](./guardrails-data-isolation.md) | Tenant isolation: shared DB, separate DBs/schemas, dedicated envs |
| [guard-rails-test-use-cases.md](./guard-rails-test-use-cases.md) | Multi-tenant and guardrail scenarios with expected outcomes |
| [guardrails-strategy.md](./guardrails-strategy.md) | Input → ACL → agents → tool checks → output pipeline |
| [wrong-architecture-shared-retrieval.md](./wrong-architecture-shared-retrieval.md) | Anti-pattern: one shared vector index for all tenants |
| [safer-architecture-tenant-scoped-retrieval.md](./safer-architecture-tenant-scoped-retrieval.md) | IdP → backend tenant → ACL → scoped retrieval → validate |

_Add more markdown files here as you expand this section._
