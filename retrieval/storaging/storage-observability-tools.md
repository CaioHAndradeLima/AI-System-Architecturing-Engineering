# Storage observability tools

**Tooling** for vector-store and search observability—metrics, dashboards, traces, and retrieval quality. Complements [storage observability](./storage-observability.md) (what to measure) and [embedding tools decision-based](../embedding/embedding-tools-decision-based.md) (embedding/RAG path).

| Need | Possible tools |
|------|----------------|
| **Database and query metrics** | PostgreSQL monitoring, cloud database monitoring, or the vector provider's metrics |
| **Dashboards and alerts** | Grafana/Prometheus or cloud-native monitoring |
| **Distributed tracing** | OpenTelemetry |
| **RAG retrieval tracing** | LangSmith or Langfuse |
| **Retrieval quality** | Golden dataset and custom evaluation scripts |

## Mapping to metrics

| Need | Metrics to wire first |
|------|------------------------|
| Database and query metrics | Query latency (p50/p95/p99), QPS, search error rate, index size, memory utilization ([storage observability](./storage-observability.md)) |
| Dashboards and alerts | Freshness, indexing throughput, filtered-search latency |
| Distributed tracing | End-to-end query path including filter construction and vector search |
| RAG retrieval tracing | Recall@K regressions tied to traces; cost per query / tenant |
| Retrieval quality | Recall@K, Precision@K, deletion propagation checks |

Provider-native metrics (Pinecone, Qdrant Cloud, etc.) often cover index size and query latency; you still own **tenant filters**, **freshness**, and **quality** gates in application code or eval pipelines.

Cloud monitoring patterns: [guard-rails cloud comparison](../../guard-rails/guard-rails-cloud-comparison.md) · [AWS services](../../guard-rails/guardrails-aws-services.md).

## See also

- [Storage and indexing decision-based by scale](./storage-indexing-decision-based.md)
- [Embedding query evaluation](../embedding/queries/embedding-user-query-evaluation.md)
- [Storaging overview](./README.md)
