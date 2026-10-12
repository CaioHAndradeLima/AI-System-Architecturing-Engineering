# Guardrails AWS services

Infrastructure and platform controls that complement application-level guardrails on AWS (and similar clouds).

| Control | Purpose |
|---------|---------|
| **API gateway and WAF** | Reject abusive traffic, enforce request limits, and reduce exposure to common web attacks |
| **IAM and service identities** | Restrict which cloud resources each workload can access |
| **Secrets manager** | Protect API keys and credentials |
| **Database authorization** | Restrict access at the data layer, not just in the API |
| **Network controls** | Reduce unnecessary public exposure and constrain service-to-service connectivity |
| **Encryption** | Protect data in transit and at rest |
| **Audit logs** | Record security-relevant actions and access decisions |
| **Monitoring and alerts** | Detect unusual access patterns, failures, and potential abuse |

Pair these with [guard-rails category](./guard-rails-category.md) enforcement in application code (tenant isolation, tool safety, output validation).

## See also

- [Safer architecture: tenant-scoped retrieval](./safer-architecture-tenant-scoped-retrieval.md)
- [Guard-rails overview](./README.md)
