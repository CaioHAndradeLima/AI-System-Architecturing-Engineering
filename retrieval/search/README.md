# Search

**Query-time retrieval**: turn a user question (and optional context) into ranked evidence from indexes and metadata—before [compacting](../compacting/) sends context to the LLM.

Search sits after [embedding queries](../embedding/queries/) (query vectors and rewrite) and [storaging](../storaging/) (indexes, filters, freshness). Authorization and tenant scope belong on every path ([guard-rails tenant-scoped retrieval](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)).

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Dense retrieval** | Vector similarity, top-K, score thresholds, dimension/index params |
| **Sparse retrieval** | BM25, keyword indexes, lexical recall |
| **Hybrid search** | Combining dense + sparse, fusion (RRF, weighted), when hybrid pays off |
| **Metadata filters** | Tenant, ACL, document type, time range—validated at query time |
| **Reranking** | Cross-encoder or LLM rerank, MMR, dedupe before compacting |
| **Query planning** | Multi-query, HyDE, step-back, routing by intent or corpus |
| **Result shaping** | Parent-child fetch, chunk expansion, max tokens per source |
| **Quality & eval** | Recall@K, MRR, nDCG, filtered-search regressions ([storage observability](../storaging/storage-observability.md)) |

---

## Guides

_Guides will be listed here as you add markdown files in this folder (same pattern as [storaging](../storaging/README.md))._

## Related

- [Embedding user query flow](../embedding/queries/embedding-user-query-flow.md)
- [Compact architecture flow](../compacting/compact-architecture-flow.md)
- [Storage strategy](../storaging/storage-strategy.md) · [HNSW flow](../storaging/hnsw-flow.md)
- [Retrieval architecturing decision-based — Retrieval row](../retrieval-architecturing-decision-based.md)
- [Wrong architecture: shared retrieval](../../guard-rails/wrong-architecture-shared-retrieval.md)

## See also

- [Retrieval overview](../README.md)
