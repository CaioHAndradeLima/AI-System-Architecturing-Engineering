# Guard-rails cloud comparison

Maps common guardrail **responsibilities** to representative services on **AWS**, **Google Cloud**, and **Azure**. Use alongside [guardrails cloud architecture](./guardrails-cloud-architecture.md) to pick products per layer.

| Responsibility | AWS | Google Cloud | Azure |
|----------------|-----|--------------|-------|
| **Edge and web protection** | AWS WAF, API Gateway | Google Cloud Armor, API Gateway | Azure WAF, API Management |
| **Identity and permissions** | IAM, Amazon Cognito | Cloud IAM, Identity Platform | Microsoft Entra ID, Azure RBAC |
| **AI content and prompt safety** | Amazon Bedrock Guardrails | Model Armor | Azure AI Content Safety, Prompt Shields |
| **Sensitive data protection** | Bedrock sensitive-information filters; AWS data protection services | Sensitive Data Protection | Microsoft Purview and applicable data protection services |
| **Secrets** | AWS Secrets Manager | Secret Manager | Azure Key Vault |
| **Audit and monitoring** | CloudTrail, CloudWatch | Cloud Audit Logs, Cloud Monitoring | Azure Monitor, Azure Activity Log |
| **Tenant isolation** | IAM policies, data-store policies, tenant-aware application design | IAM, data-store policies, tenant-aware application design | Entra identity controls, data-store policies, tenant-aware application design |

Vendor offerings change frequently—treat this table as a **starting map**, not an exhaustive or version-pinned catalog. Tenant isolation always requires **application-level** scoping (see [data isolation](./guardrails-data-isolation.md) and [safer tenant retrieval](./safer-architecture-tenant-scoped-retrieval.md)).

## See also

- [Guardrails AWS services](./guardrails-aws-services.md) — AWS control purposes in more detail
- [Guard-rails category](./guard-rails-category.md)
- [Guard-rails overview](./README.md)
