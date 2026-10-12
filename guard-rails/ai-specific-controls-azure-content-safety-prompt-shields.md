# AI-specific controls — Azure AI Content Safety and Prompt Shields

**Prompt Shields** detects and helps block adversarial instructions in user prompts and documents. **Azure AI Content Safety** also supports content-safety screening. Use both in the **AI safety service** layer of [guardrails cloud architecture](./guardrails-cloud-architecture.md), alongside app validation and tenant-scoped data access.

## Azure AI safety capabilities

| Capability | Responsibility |
|------------|----------------|
| **Prompt Shields** | Detect potential user-prompt attacks and document-based prompt injection. |
| **Content safety** | Screen supported content against configured safety categories. |
| **Application-side validation** | Validate schemas, permissions, business rules, and allowed operations. |
| **Data protection integration** | Apply appropriate Microsoft data-protection capabilities where configured. |

Application-side validation remains your responsibility: Azure AI services do not replace schema checks, RBAC, or business rules in the app tier ([guard-rails category](./guard-rails-category.md)).

**Important:** Prompt Shields is **not** a tenant-authorization engine. Even if it detects a malicious prompt, the application must still prevent unauthorized data retrieval ([safer tenant-scoped retrieval](./safer-architecture-tenant-scoped-retrieval.md), [test use cases](./guard-rails-test-use-cases.md)).

## Related Azure cloud security controls

| Service | Role |
|---------|------|
| **Azure Web Application Firewall (WAF)** | Helps protect supported web applications from common web exploits. |
| **Azure API Management** | Manages API exposure, policies, authentication integrations, and traffic controls. |
| **Microsoft Entra ID** | Provides identity and access capabilities (formerly Azure AD). |
| **Azure RBAC** | Controls access to Azure resources. |
| **Azure Key Vault** | Stores secrets, keys, and certificates. |
| **Azure Monitor** | Provides monitoring and diagnostic capabilities. |
| **Microsoft Purview** | Supports data governance and applicable data-protection workflows. |

Multi-cloud map: [guard-rails-cloud-comparison.md](./guard-rails-cloud-comparison.md).

## Tenant isolation on Azure

Use **trusted identity claims**, **server-side membership checks**, and **tenant-scoped data access**. For higher isolation requirements, consider dedicated databases or resources rather than relying exclusively on application filters ([guardrails data isolation](./guardrails-data-isolation.md)).

## Practical checklist

- [ ] Run Prompt Shields on **user input and document content** used in RAG where supported
- [ ] Combine Content Safety on **model output** with schema/policy validation before response
- [ ] Wire Purview or other DLP where sensitive categories require governance beyond AI safety APIs
- [ ] Test unauthorized retrieval failures **without** assuming Prompt Shields blocks data exfiltration

## See also

- [AI-specific controls — Amazon Bedrock Guardrails](./ai-specific-controls-amazon-bedrock-guardrails.md)
- [AI-specific controls — Google Cloud Model Armor](./ai-specific-controls-google-model-armor.md)
- [Guard-rails overview](./README.md)
