# Deployment cloud tools

**Deployment concern → cloud services** on AWS, Azure, and Google Cloud—runtime, registry, secrets, observability, async ingestion, model APIs, and CI identity ([production controls — queues and secrets](./production-components.md), [LLM cloud services](../llm/llm-cloud-services.md)).

| Deployment concern | AWS | Azure | Google Cloud |
|--------------------|-----|-------|--------------|
| **Container runtime** | ECS/Fargate or EKS | Container Apps or AKS | Cloud Run or GKE |
| **Container registry** | ECR | Azure Container Registry | Artifact Registry |
| **Secrets** | Secrets Manager | Key Vault | Secret Manager |
| **Logs and monitoring** | CloudWatch | Azure Monitor | Cloud Logging |
| **Queue-based ingestion** | SQS / EventBridge | Service Bus / Event Grid | Pub/Sub |
| **Model API** | Amazon Bedrock or external API | Azure OpenAI / Foundry models or external API | Gemini APIs or external API |
| **CI/CD integration** | GitHub Actions with AWS identity | GitHub Actions with Azure identity | GitHub Actions with Google Cloud identity |

## Concern → docs

| Concern | See also |
|---------|----------|
| Container runtime / registry | [Production components — Docker](./production-components.md) · [Pipeline criteria — immutable image](./pipeline-criteria-pass-vs-fail.md) |
| Secrets | [Guard-rails AWS services](../guard-rails/guardrails-aws-services.md) |
| Logs and monitoring | [Tracing metrics](../observability-evaluation/tracing-for-observability-metrics.md) · [Observability tools](../observability-evaluation/observability-tools.md) |
| Queue-based ingestion | [Ingestion procedures](../retrieval/ingestion/ingestion-procedures.md) · [Retrieval cloud tools](../retrieval/search/retrieval-cloud-tools.md) |
| Model API | [Hosted vs open-weight](../llm/llm-hosted-vs-open-weight-models.md) · [AI-specific controls — Bedrock guardrails](../guard-rails/ai-specific-controls-amazon-bedrock-guardrails.md) |
| CI/CD | [Pipeline evaluation](./pipeline-evaluation.md) · [Pipeline tools and steps](./pipeline-tools-steps.md) |

**Security and guard-rails** (WAF, tenant isolation, content safety) are not fully covered by this table—see [guard-rails cloud comparison](../guard-rails/guard-rails-cloud-comparison.md). Pick one primary cloud per environment where possible so secrets, logs, and deploy identity stay consistent.

## See also

- [Retrieval AWS multi-agent sample](../retrieval/search/retrieval-aws-multi-agent-sample.md)
- [Deployment overview](./README.md)
