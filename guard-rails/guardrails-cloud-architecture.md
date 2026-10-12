# Guardrails cloud architecture

A **full-stack request path** for production agent/LLM APIs: edge protection, identity, application rules, AI safety services, scoped data access, the agent workflow, and output controls—with cloud primitives applied across the lifecycle.

## Architecture

```
                     USER REQUEST
                         |
                         v
       +----------------------------------+
       | EDGE SECURITY                    |
       | WAF · Rate limits · API gateway |
       +----------------------------------+
                         |
                         v
       +----------------------------------+
       | IDENTITY AND ACCESS              |
       | Authentication · Authorization  |
       +----------------------------------+
                         |
                         v
       +----------------------------------+
       | APPLICATION GUARDRAILS            |
       | Schema · Tenant · Business rules |
       +----------------------------------+
                         |
                         v
       +----------------------------------+
       | AI SAFETY SERVICE                |
       | Prompt injection · Content       |
       | Sensitive data screening         |
       +----------------------------------+
                         |
                         v
       +----------------------------------+
       | DATA AND TOOL ACCESS             |
       | Tenant filters · DB policies     |
       | Least-privilege service identity |
       +----------------------------------+
                         |
                         v
       +----------------------------------+
       | LLM / AGENT WORKFLOW             |
       +----------------------------------+
                         |
                         v
       +----------------------------------+
       | OUTPUT CONTROLS                  |
       | Schema · Policy · Source checks  |
       +----------------------------------+
                         |
                         v
                   USER RESPONSE

       CROSS-CUTTING CLOUD CONTROLS
       Secrets · Encryption · Audit · Monitoring
```

## Layer responsibilities

| Layer | Role |
|-------|------|
| **Edge security** | First line against abuse: WAF rules, bot/rate limits, TLS termination, request size caps at the gateway. |
| **Identity and access** | Establish who is calling; decide what tenants, features, and APIs they may use before business logic runs. |
| **Application guardrails** | Validate payloads (schema), resolve and enforce tenant context, apply product/business rules not covered by IdP alone. |
| **AI safety service** | Dedicated screening for injection in user input and retrieved text, harmful content, and sensitive data in prompts/context. |
| **Data and tool access** | Tenant-scoped retrieval, database authorization, tool allowlists; workloads use least-privilege IAM/service identities. |
| **LLM / agent workflow** | Orchestration, agents, and tools operate only inside the envelope established above. |
| **Output controls** | Structured response validation, policy moderation, verify citations/sources match authorized data. |
| **Cross-cutting controls** | Secrets management, encryption in transit/at rest, audit logs, monitoring and alerts on all layers. |

## How this relates to other notes

- Application-layer ordering aligns with [guardrails-strategy.md](./guardrails-strategy.md) (input → ACL → agents → tools → output).
- Tenant retrieval detail: [safer-architecture-tenant-scoped-retrieval.md](./safer-architecture-tenant-scoped-retrieval.md).
- AWS-shaped controls at each tier: [guardrails-aws-services.md](./guardrails-aws-services.md).
- Multi-cloud product map: [guard-rails-cloud-comparison.md](./guard-rails-cloud-comparison.md).
- Category-to-enforcement map: [guard-rails-category.md](./guard-rails-category.md).

Cross-cutting items are not a bypass path—if secrets or monitoring fail, fail safely rather than skipping upstream checks.

## Practical checklist

- [ ] Map each box in the diagram to an **owner team** (platform vs application vs ML safety)
- [ ] Ensure **AI safety** runs on both user input and retrieved documents before they enter the agent context
- [ ] Service accounts for retrieval/tools have **narrower** permissions than the human user’s UI role where appropriate
- [ ] Output controls run **before** caching or streaming completion to the client
- [ ] Audit events cover auth decisions, tool calls, and retrieval doc IDs (redacted content where required)

## See also

- [Guard-rails overview](./README.md)
- [Guard-rails test use cases](./guard-rails-test-use-cases.md)
