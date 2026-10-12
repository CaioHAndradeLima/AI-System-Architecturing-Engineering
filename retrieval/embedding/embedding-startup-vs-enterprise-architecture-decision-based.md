# Embedding startup vs enterprise architecture decision-based

How **embedding** choices evolve from startup/MVP through medium SaaS to enterprise—model, hosting, ops, cost, eval, and security.

Use with [embedding decision-based](./embedding-decision-based.md) (selection questions), [hosted vs self-hosted](./embedding-hosted-vs-self-hosted.md), and [migration](./embedding-migration-ingestion-using-another-model.md).

| Area | Startup / MVP | Medium Scale / SaaS | Enterprise |
|------|---------------|---------------------|------------|
| **Model selection** | One general-purpose embedding model | Benchmark alternatives against real queries | Domain-specific evaluation and controlled model lifecycle |
| **Hosting** | Hosted API or small local model | Managed API or dedicated inference service | Hosted, private or self-hosted based on governance and scale |
| **Batch processing** | Small batches | Batch jobs and concurrent workers | Capacity-managed, distributed processing |
| **Caching** | Optional | Cache repeated content embeddings | Version-aware caching with tenant-safe access |
| **Storage** | Local vector store | Managed vector database | Scalable index, replication and migration strategy |
| **Dimensions** | Model default | Tune if supported and evaluation justifies it | Evaluate quality, storage and latency together |
| **Model upgrades** | Rebuild a small index | Background re-embedding | Versioned indexes, parallel evaluation and controlled cutover |
| **Cost controls** | Track usage | Batch requests, cache and avoid unnecessary re-embedding | Budgets, per-tenant accounting and capacity optimization |
| **Evaluation** | Small golden dataset | Automated retrieval regression tests | Continuous evaluation and release gates |
| **Security** | Protect API keys and enforce tenant filters | Tenant-aware authorization and audit | Fine-grained access, governance and isolated deployments where required |
| **Observability** | Logs and basic timings | Dashboards, alerts and RAG traces | SLOs, distributed tracing, incident workflows and model lifecycle controls |

## Guide links by area

| Area | Docs |
|------|------|
| Model / hosting / upgrades | [Decision-based](./embedding-decision-based.md) · [Hosted vs self-hosted](./embedding-hosted-vs-self-hosted.md) · [Migration](./embedding-migration-ingestion-using-another-model.md) |
| Metrics / observability / tools | [Embedding metrics](./embedding-metrics.md) · [Tools decision-based](./embedding-tools-decision-based.md) |
| Chunking + storage together | [Chunking architecturing decision-based](../chunking/chunking-architecturing-decision-based.md) |
| Security / tenancy | [Guard-rails data isolation](../../guard-rails/guardrails-data-isolation.md) · [Robust implementation](../../guard-rails/guard-rails-robust-cloud-rules-implementation.md) |

## See also

- [Retrieval architecturing decision-based](../retrieval-architecturing-decision-based.md)
- [Embedding overview](./README.md)
