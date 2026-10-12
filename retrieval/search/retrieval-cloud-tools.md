# Retrieval cloud tools

Maps **retrieval and agent-stack responsibilities** to representative services on **AWS**, **Azure**, and **Google Cloud**. Use with [retrieval architecture decision](./retrieval-architecture-decision.md) (service vs agent vs multi-agent) and [architecture evaluation](./retrieval-architecture-evaluation.md) (what to monitor per layer).

| Architectural responsibility | AWS | Azure | Google Cloud |
|------------------------------|-----|-------|--------------|
| **LLM inference** | Bedrock | Azure OpenAI / Foundry models | Gemini APIs |
| **Agent runtime** | Bedrock AgentCore or ECS | Foundry Agent Service or Container Apps | Agent Platform or Cloud Run |
| **Vector retrieval** | OpenSearch / Aurora pgvector | Azure AI Search | Vector Search / RAG Engine |
| **Document storage** | S3 | Blob Storage | Cloud Storage |
| **Event processing** | SQS / EventBridge | Service Bus / Event Grid | Pub/Sub |
| **SQL analytics** | Redshift / Athena | Fabric / Synapse | BigQuery |
| **Identity and secrets** | IAM / Secrets Manager | Entra ID / Key Vault | IAM / Secret Manager |
| **Observability** | CloudWatch / X-Ray | Azure Monitor / App Insights | Cloud Logging / Trace |

## How this fits the retrieval stack

| Responsibility | Repo guides |
|----------------|-------------|
| Vector retrieval | [Storaging](../storaging/) · [Search strategies](./retrieval-strategies-combined.md) |
| Agent runtime | [Supervisor as service](./retrieval-architecture-supervisor-as-service.md) · [Multi-agent](./retrieval-architecture-multi-agent.md) · [Agents](../../agents/) |
| Document storage + events | [Ingestion](../ingestion/) · [Multi-source ingestion](../ingestion/multi-source-ingestion.md) |
| SQL analytics branch | [Simple loop — Analytics agent](./retrieval-architecture-simple-loop.md) |
| Observability | [Retrieval metrics](./retrieval-metrics-observability.md) · [Storage observability tools](../storaging/storage-observability-tools.md) |

**Security and guard-rails** (WAF, content safety, tenant isolation) are mapped separately in [guard-rails cloud comparison](../../guard-rails/guard-rails-cloud-comparison.md). Tenant-scoped retrieval still requires **application filters** on every search ([metadata filtering](./retrieval-strategy-metadata-filtering.md)).

Vendor names and SKUs change—validate against current docs before architecture sign-off.

## See also

- [Guardrails AWS services](../../guard-rails/guardrails-aws-services.md)
- [Search overview](./README.md)
