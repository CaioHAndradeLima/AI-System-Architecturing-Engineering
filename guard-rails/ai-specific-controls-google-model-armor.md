# AI-specific controls — Google Cloud Model Armor

[Model Armor](https://cloud.google.com/security-command-center/docs/model-armor-overview) screens prompts and responses and supports configurable controls for prompt injection, jailbreaks, harmful content, and sensitive information. It can be integrated into AI workflows on Google Cloud and other platforms.

Place it in the **AI safety service** layer of [guardrails cloud architecture](./guardrails-cloud-architecture.md), together with application guardrails and tenant-scoped retrieval—not instead of them.

## Model Armor capabilities

| Capability | Responsibility |
|------------|----------------|
| **Prompt screening** | Inspect user prompts before model processing. |
| **Document screening** | Help identify malicious instructions embedded in supported documents. |
| **Response screening** | Inspect model-generated content before returning it. |
| **Sensitive-data protection** | Integrate with Sensitive Data Protection for supported detection and redaction workflows. |
| **Configurable templates** | Define reusable screening policies and confidence thresholds. |

Document screening is especially relevant for RAG: retrieved files may carry injection text that must be treated as untrusted even after vector search.

**Important:** Model Armor can reduce AI-specific risks, but it does **not** establish whether a user is authorized to read a particular document. Enforce authorization and tenant filters before retrieval ([safer tenant-scoped retrieval](./safer-architecture-tenant-scoped-retrieval.md)).

## Related Google Cloud security controls

| Service | Role |
|---------|------|
| **Google Cloud Armor** | Helps protect supported applications from web attacks and unwanted traffic. |
| **API Gateway** | Provides a managed API entry point. |
| **Cloud IAM** | Controls access to cloud resources. |
| **Secret Manager** | Stores credentials and other secrets. |
| **Cloud Audit Logs** | Records supported administrative and data-access activities. |
| **Cloud Monitoring** | Supports metrics, dashboards, and alerts. |

Multi-cloud mapping: [guard-rails-cloud-comparison.md](./guard-rails-cloud-comparison.md). AWS counterpart: [Amazon Bedrock Guardrails](./ai-specific-controls-amazon-bedrock-guardrails.md).

## Practical checklist

- [ ] Screen **prompts, ingested documents, and responses** where the product allows separate hooks
- [ ] Version **templates** and thresholds per environment; regression-test policy changes
- [ ] On block/redact, return a safe user-facing message and log the event without leaking blocked content
- [ ] Pair Model Armor with **IAM + tenant-aware retrieval**, not prompt screening alone

## See also

- [AI-specific controls — Azure Content Safety and Prompt Shields](./ai-specific-controls-azure-content-safety-prompt-shields.md)
- [Guard-rails category](./guard-rails-category.md)
- [Guard-rails test use cases](./guard-rails-test-use-cases.md)
- [Guard-rails overview](./README.md)
