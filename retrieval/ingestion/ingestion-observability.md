# Ingestion observability

**Metrics** to watch on indexing pipelines—from document processing health through index freshness, retrieval quality, and tenant isolation. Aligns with enterprise monitoring in [ingestion architecture engineering](./ingestion-architecture-engineering.md) and [multi-source ingestion](./multi-source-ingestion.md).

| Metric | What it tells you |
|--------|-------------------|
| **Ingestion success rate** | How often documents finish processing successfully |
| **Parsing failure rate** | Whether certain file formats or documents fail |
| **Ingestion latency** | How long a document takes to become searchable |
| **Embedding cost per document** | Whether processing costs are sustainable |
| **Duplicate chunk rate** | Whether retries or updates create duplicate data |
| **Index freshness** | Whether the searchable index reflects the latest source version |
| **Retrieval Recall@K** | Whether relevant evidence appears among the top K results |
| **Cross-tenant access test failures** | Whether isolation controls are working |

## Suggested alerts (starting point)

- Success rate drops below baseline for a connector or tenant
- Parsing failure spike for a MIME type (bad parser rollout)
- Freshness SLA breached (sync lag vs source)
- Any **cross-tenant access test failure** → treat as a security incident ([test use cases](../../guard-rails/guard-rails-test-use-cases.md))

Recall@K is an **evaluation** metric but belongs on ingestion dashboards when chunk/embed/index changes ship—regressions often originate in indexing, not the LLM.

Extended chunk-level metrics: [chunking metrics observability](../chunking/chunking-metrics-observability.md).

## See also

- [Ingestion procedures — Evaluation row](./ingestion-procedures.md)
- [Guard-rails robust cloud rules implementation](../../guard-rails/guard-rails-robust-cloud-rules-implementation.md)
- [Ingestion overview](./README.md)
