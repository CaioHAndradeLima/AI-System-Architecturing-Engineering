# User query embedding latency and cost

**Online query path** maturity: embedding API usage, latency SLOs, caching, reliability, rewriting, and observability—startup vs production/enterprise.

Complements [user query flow](./embedding-user-query-flow.md), [startup vs enterprise architecture](./embedding-startup-vs-enterprise-architecture-decision-based.md), and [embedding metrics](./embedding-metrics.md).

| Concern | Startup | Production / Enterprise |
|---------|---------|-------------------------|
| **Query embedding** | One API call per question | Batching only when the workflow naturally supports it; optimize request overhead |
| **Latency** | Measure simple end-to-end response time | Track percentile-based latency: p50, p95, and p99 |
| **Cost** | Estimate embedding cost per query | Track usage by model and tenant |
| **Caching** | Usually skipped initially | Cache repeated equivalent queries when safe (tenant-scoped keys) |
| **Reliability** | Basic retries and error handling | Bounded retries, timeouts, provider failover if justified |
| **Query rewriting** | Skip initially to reduce complexity | Add selectively based on evaluation ([cleaning user query](./embedding-cleaning-user-query.md), [context compact flow](./embedding-user-context-compact-flow.md)) |
| **Observability** | Log latency and errors | Trace rewriting, embedding, retrieval, and generation ([tools decision-based](./embedding-tools-decision-based.md)) |

## Cache safety

Cache **query embeddings** or retrieval results only with keys that include **tenant_id** (and user/session if data is not tenant-wide public)—see [guard-rails test use cases](../../guard-rails/guard-rails-test-use-cases.md) (cached answer isolation).

## See also

- [Embedding bad practices — cosine as probability](./embedding-bad-practices.md)
- [Embedding overview](./README.md)
