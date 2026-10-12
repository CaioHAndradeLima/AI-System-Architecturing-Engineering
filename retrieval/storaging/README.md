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

Exact nearest-neighbor vs approximate (ANN) search—recall, latency, and scale trade-offs.

→ [See more in storage-strategy.md](./storage-strategy.md)

### [index-strategies.md](./index-strategies.md)

`#ann` · `#hnsw` · `#ivf`

Flat exact, HNSW, IVF, and disk-oriented ANN—ideas and trade-offs.

→ [See more in index-strategies.md](./index-strategies.md)

### [hnsw-flow.md](./hnsw-flow.md)

`#hnsw` · `#query-path` · `#ann`

Graph navigation from indexed vectors to top-K neighbors at search time.

→ [See more in hnsw-flow.md](./hnsw-flow.md)

### [storage-architecturing-decision-based.md](./storage-architecturing-decision-based.md)

`#decision-guide` · `#faiss` · `#pgvector` · `#managed`

Requirement → starting store (FAISS, Chroma, pgvector, Pinecone, Qdrant, etc.) and why.

→ [See more in storage-architecturing-decision-based.md](./storage-architecturing-decision-based.md)

### [storage-indexing-decision-based.md](./storage-indexing-decision-based.md)

`#decision-guide` · `#startup` · `#enterprise` · `#slo`

Storage choice, ANN tuning, metadata, filtering, updates, deletions, scaling, availability, eval, and cost by maturity stage.

→ [See more in storage-indexing-decision-based.md](./storage-indexing-decision-based.md)

### [storage-observability.md](./storage-observability.md)

`#metrics` · `#slo` · `#ann` · `#multi-tenant`

Query latency, QPS, index size, freshness, Recall@K, filtered search, deletion propagation, and cost per tenant.

→ [See more in storage-observability.md](./storage-observability.md)

## Related

- [Compact architecture flow](../compacting/compact-architecture-flow.md) — DB + vector dual-write
- [Retrieval architecturing decision-based — Vector storage](../retrieval-architecturing-decision-based.md)
- [Embedding migration](../embedding/embedding-migration-ingestion-using-another-model.md)
- [Wrong architecture: shared retrieval](../../guard-rails/wrong-architecture-shared-retrieval.md)
