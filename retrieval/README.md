# Retrieval

Design and operate **retrieval** for LLM applications: indexing, query-time search, grounding, and quality—together with authorization and tenant scope ([guard-rails](../guard-rails/) retrieval notes).

## Topic areas

| Area | What we cover |
|------|----------------|
| **[Ingestion](./ingestion/)** | Fetch, parse, sync, index ops, observability |
| **[Chunking](./chunking/)** | Splitting text into retrievable units and metadata |
| **[Embedding](./embedding/)** | Document vectors, models; [queries](./embedding/queries/) for online search |
| **[Compacting](./compacting/)** | Fit and prioritize retrieved context for the LLM |
| **[Storaging](./storaging/)** | Vector index, DB metadata, object storage, index lifecycle |
| **[Search](./search/)** | Dense, sparse, hybrid, filters, reranking |
| **[Contexting](../contexting/)** | Grounding, citations, prompt/context assembly ([decision by scale](../contexting/context-architecturing-decision-based.md)) |
| **Operations** | Freshness, reindexing, eval metrics (recall, MRR, grounded answers) |
| **Multi-tenant** | Scoped indexes, ACL sync, safe caching |

---

## Sections

| Section | Summary |
|---------|---------|
| [ingestion/](./ingestion/) | Offline pipeline: fetch, parse, sync, and index documents into searchable stores. MVP through multi-source flows, procedures, and observability when ingestion breaks retrieval. |
| [chunking/](./chunking/) | Split documents into retrieval units—fixed, structure-aware, and semantic strategies—with metrics and architecturing choices by scale. |
| [embedding/](./embedding/) | Document and query embedding models, hosting, migration, and index-time quality. [queries/](./embedding/queries/) covers online query vectors, rewrite, and latency. |
| [compacting/](./compacting/) | Shrink and prioritize retrieved text before the LLM: dedupe, truncation, summarization, and token budget trade-offs. |
| [storaging/](./storaging/) | Vector indexes, metadata stores, HNSW lifecycle, freshness, and storage-side observability. |
| [search/](./search/) | Query-time dense, sparse, and hybrid retrieval, metadata filters, reranking, architecture patterns, and eval metrics. |

## Guides

### [retrieval-flow.md](./retrieval-flow.md)

`#flow` · `#rag` · `#hybrid`

End-to-end RAG retrieval path: offline indexing, query-time search (vector + metadata + keyword), optional reranking, context assembly, and generation.

Tenant and ACL filters belong on the retrieval engine branch, not only at the LLM (tenant-scoped retrieval).

→ [See more in retrieval-flow.md](./retrieval-flow.md) · [Combined query-time strategies](./search/retrieval-strategies-combined.md)

### [retrieval-architecturing-decision-based.md](./retrieval-architecturing-decision-based.md)

`#architecture` · `#decision-guide` · `#maturity`

How to evolve parsing → evaluation choices as the system grows from MVP to medium to large scale.

Pair with minimum ingestion MVP and guard-rails decision assistance for security and ops maturity.

→ [See more in retrieval-architecturing-decision-based.md](./retrieval-architecturing-decision-based.md)

_Section indexes: [ingestion](./ingestion/README.md) · [chunking](./chunking/README.md) · [embedding](./embedding/README.md) · [queries](./embedding/queries/README.md) · [compacting](./compacting/README.md) · [storaging](./storaging/README.md) · [search](./search/README.md)_

## Related guard-rails

- [Safer architecture: tenant-scoped retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md)
- [Wrong architecture: shared retrieval](../guard-rails/wrong-architecture-shared-retrieval.md)
- [Retrieval authorization in decision assistance](../guard-rails/guard-rails-decision-architecturing-assistance.md)
