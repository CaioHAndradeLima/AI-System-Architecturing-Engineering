# Guard-rails category

Reference map of common guardrail categories: what each one covers, a concrete example, and where enforcement should live in the stack.

| Guardrail category | Example | Preferred enforcement |
|--------------------|---------|------------------------|
| **Input validation** | Reject malformed requests and oversized payloads | Application code, Pydantic |
| **Authentication** | Establish the user's identity | Identity provider, OAuth/OIDC |
| **Authorization** | Check which resources a user may access | Policy engine and backend |
| **Tenant isolation** | Prevent cross-customer data access | Database policies, tenant-scoped retrieval, IAM |
| **Prompt-injection defense** | Detect malicious instructions in prompts or documents | Input screening plus constrained architecture |
| **Tool safety** | Prevent unauthorized API calls or destructive actions | Typed tools, permission checks, allowlists |
| **Output validation** | Ensure a result matches the expected schema | Pydantic, JSON Schema, deterministic checks |
| **Content safety** | Detect prohibited or harmful content | Cloud content-safety services or dedicated classifiers |
| **Privacy** | Detect or redact sensitive information when required | DLP/PII detection and data-handling policies |
| **Resource controls** | Limit tokens, requests, execution time, and cost | API gateway, application quotas, provider limits |

## See also

- [Enforcement layers](./README.md#enforcement-layers)
- [What good guardrails do](./README.md#what-good-guardrails-do)
- [Guardrails strategy](./guardrails-strategy.md)
