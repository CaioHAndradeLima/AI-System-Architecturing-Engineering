# Storage observability

Key **metrics for vector storage and search**—latency, capacity, freshness, quality with filters, security, and cost. Complements [ingestion observability](../ingestion/ingestion-observability.md) and [chunking metrics](../chunking/chunking-metrics-observability.md) with store- and query-path signals.

| Metric | What it tells you | Why it matters |
|--------|-------------------|----------------|
| **Query latency (p50/p95/p99)** | How long searches take | Reveals slow queries and tail-latency issues |
| **Queries per second** | Search throughput | Helps determine capacity requirements |
| **Index size** | Storage used by vectors and index structures | Helps with capacity and cost planning |
| **Memory utilization** | Memory used by the database and index | Especially important for memory-intensive ANN indexes |
| **Indexing throughput** | Vectors inserted or updated per second | Indicates how quickly new documents become searchable |
| **Index freshness** | Delay between source change and searchable update | Prevents stale information from being returned |
| **Search error rate** | Failed or timed-out queries | Detects availability and configuration issues |
| **Recall@K** | Whether relevant evidence appears in top-K results | Measures retrieval coverage |
| **Precision@K** | How much of the top-K result set is relevant | Measures retrieval noise |
| **Filtered-search performance** | Latency and quality with tenant/metadata filters | Ensures real production query patterns perform well |
| **Deletion propagation** | Whether deleted or revoked records remain searchable | Important for security and correctness |
| **Cost per query / tenant** | Storage and query cost allocation | Helps identify expensive workloads |

## Suggested alerts (starting point)

- p95/p99 query latency breaches SLO (especially after ANN or filter changes)
- Search error rate or timeout spike
- Index freshness lag beyond agreed SLA
- **Deletion propagation** failures or revoked content still retrievable → security review ([guard-rails test use cases](../../guard-rails/guard-rails-test-use-cases.md))
- Memory pressure on HNSW or in-memory indexes approaching limits ([HNSW flow](./hnsw-flow.md))

Recall@K and Precision@K belong on storage dashboards when index parameters, dimensions, or filters change—not only on LLM eval. Pair with [embedding query evaluation](../embedding/queries/embedding-user-query-evaluation.md) for end-to-end regressions.

## By maturity

| Stage | Focus |
|-------|--------|
| Startup / MVP | Latency logs, index size, small golden-set Recall@K |
| Medium SaaS | Percentiles, QPS, freshness, filtered-search latency, tenant cost signals |
| Enterprise | SLO-backed latency, replication health, release gates on Recall@K, auditable deletion metrics |

See [storage and indexing decision-based by scale](./storage-indexing-decision-based.md) for ops expectations per stage.

## See also

- [Storage observability tools](./storage-observability-tools.md)
- [Embedding metrics](../embedding/embedding-metrics.md)
- [Storage strategy](./storage-strategy.md) · [Index strategies](./index-strategies.md)
- [Guard-rails data isolation](../../guard-rails/guardrails-data-isolation.md)
- [Storaging overview](./README.md)
