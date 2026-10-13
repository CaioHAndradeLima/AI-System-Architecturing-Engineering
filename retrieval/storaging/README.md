# Storaging

Where **retrieval data lives**: vector indexes, relational/metadata stores, object storage for originals, and how they stay consistent for search and RAG.

Storaging connects [ingestion](../ingestion/) outputs, [embedding](../embedding/) vectors, and query-time filters in [compacting](../compacting/) and [embedding queries](../embedding/queries/).

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Vector index** | pgvector, Chroma, managed vector DBs, filters, dimensions |
| **Relational / metadata** | Document IDs, tenant, ACL, message rows, join keys |
| **Object storage** | Original PDFs, attachments, re-parse sources |
| **Hybrid layout** | DB + vector index ([compact decision](../compacting/compact-decision-based.md)) |
| **Lifecycle** | Upsert, tombstones, blue/green indexes, replication |
| **Multi-tenant** | Shared index + filters vs dedicated indexes ([guard-rails data isolation](../../guard-rails/guardrails-data-isolation.md)) |

---

## Guides

### [storage-strategy.md](./storage-strategy.md)

`#vector-index` · `#ann` · `#exact-search`

How the vector index answers similarity search—exact scan vs approximate index—and when each fits your scale and recall targets.

→ [See more in storage-strategy.md](./storage-strategy.md)

### [index-strategies.md](./index-strategies.md)

`#ann` · `#hnsw` · `#ivf`

Vector index structures used for approximate or exact search—how each works and what you trade off.

Builds on storage strategy — exact vs ANN.

→ [See more in index-strategies.md](./index-strategies.md)

### [hnsw-flow.md](./hnsw-flow.md)

`#hnsw` · `#query-path` · `#ann`

Query-time path for HNSW (Hierarchical Navigable Small World): graph traversal to approximate nearest neighbors without scanning every vector.

→ [See more in hnsw-flow.md](./hnsw-flow.md)

### [storage-architecturing-decision-based.md](./storage-architecturing-decision-based.md)

`#decision-guide` · `#faiss` · `#pgvector` · `#managed`

Pick a vector storage starting point by requirement—not by popularity alone.

Pair with index strategies and storage strategy once you know scale and recall targets.

→ [See more in storage-architecturing-decision-based.md](./storage-architecturing-decision-based.md)

### [storage-indexing-decision-based.md](./storage-indexing-decision-based.md)

`#decision-guide` · `#startup` · `#enterprise` · `#slo`

How vector storage, indexes, metadata, and ops evolve from startup/MVP through medium SaaS to enterprise.

→ [See more in storage-indexing-decision-based.md](./storage-indexing-decision-based.md)

### [storage-observability.md](./storage-observability.md)

`#metrics` · `#slo` · `#ann` · `#multi-tenant`

Key metrics for vector storage and search—latency, capacity, freshness, quality with filters, security, and cost.

Complements ingestion observability and chunking metrics with store- and query-path signals.

→ [See more in storage-observability.md](./storage-observability.md)

### [storage-observability-tools.md](./storage-observability-tools.md)

`#tools` · `#prometheus` · `#opentelemetry` · `#langfuse`

Tooling for vector-store and search observability—metrics, dashboards, traces, and retrieval quality.

Complements storage observability (what to measure), embedding tools decision-based (embedding/RAG path), and the repo-wide observability tools reference.

→ [See more in storage-observability-tools.md](./storage-observability-tools.md)

## Related

- [Search](../search/README.md) — query-time retrieval after indexes are ready
- [Compact architecture flow](../compacting/compact-architecture-flow.md) — DB + vector dual-write
- [Retrieval architecturing decision-based — Vector storage](../retrieval-architecturing-decision-based.md)
- [Embedding migration](../embedding/embedding-migration-ingestion-using-another-model.md)
- [Wrong architecture: shared retrieval](../../guard-rails/wrong-architecture-shared-retrieval.md)
