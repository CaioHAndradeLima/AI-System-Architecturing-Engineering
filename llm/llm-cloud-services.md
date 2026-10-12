# LLM cloud services

**Capability → provider** map for running LLM applications—model APIs, runtime, secrets, monitoring, identity. Broader retrieval/agent stack: [retrieval cloud tools](../retrieval/search/retrieval-cloud-tools.md). Security layers: [guard-rails cloud comparison](../guard-rails/guard-rails-cloud-comparison.md).

| Capability | AWS | Azure | Google Cloud |
|------------|-----|-------|--------------|
| **Managed model access** | Amazon Bedrock | Azure OpenAI / Microsoft Foundry | Gemini APIs / Google Cloud's managed AI platform |
| **Application runtime** | ECS/Fargate, EKS, Lambda where suitable | Container Apps, AKS, Functions where suitable | Cloud Run, GKE, Functions where suitable |
| **Secrets** | Secrets Manager | Key Vault | Secret Manager |
| **Monitoring** | CloudWatch, X-Ray | Azure Monitor, Application Insights | Cloud Logging, Cloud Trace |
| **Identity** | IAM | Microsoft Entra ID | Cloud IAM |

## Wiring to LLM docs

| Capability | See also |
|------------|----------|
| Managed model access | [Hosted vs open-weight](./llm-hosted-vs-open-weight-models.md) |
| Application runtime | [AWS multi-agent sample](../retrieval/search/retrieval-aws-multi-agent-sample.md) · [LangGraph nodes](../contexting/context-assembly-langchain-langgraph.md) |
| Monitoring | [Latency variables and measurement](./llm-latency-variables-measurement.md) · [Storage observability tools](../retrieval/storaging/storage-observability-tools.md) |
| Identity / secrets | [Reliable architecture](../contexting/context-reliable-architecture.md) · [Guardrails AWS services](../guard-rails/guardrails-aws-services.md) |

Vendor names change—validate regions, model IDs, and data-processing terms before production sign-off.

## See also

- [LLM overview](./README.md)
