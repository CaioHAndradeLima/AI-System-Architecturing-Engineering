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
| **Grounding** | Citations, context limits, when retrieval fails |
| **Operations** | Freshness, reindexing, eval metrics (recall, MRR, grounded answers) |
| **Multi-tenant** | Scoped indexes, ACL sync, safe caching |

---

## Sections

| Section | Summary |
|---------|---------|
| [ingestion/](./ingestion/) | Offline pipeline docs (parse → vector index, MVP, multi-source, ops) |
| [chunking/](./chunking/) | Chunk strategies, parameters, eval, and re-index |
| [embedding/](./embedding/) | Document embedding, migration, metrics; [queries/](./embedding/queries/) for user query path |
| [compacting/](./compacting/) | Context assembly, dedupe, truncation, summarization |
| [storaging/](./storaging/) | Where chunks, vectors, and source records are stored |
| [search/](./search/) | Query-time dense/sparse/hybrid retrieval, filters, reranking |

## Guides

### [retrieval-flow.md](./retrieval-flow.md)

`#flow` · `#rag` · `#hybrid`

Offline ingest through query embedding, retrieval engine (vector, metadata, keyword), reranking, context assembly, and LLM answer.

→ [See more in retrieval-flow.md](./retrieval-flow.md)

### [retrieval-architecturing-decision-based.md](./retrieval-architecturing-decision-based.md)

`#architecture` · `#decision-guide` · `#maturity`

Parsing through evaluation by MVP, medium, and large system—parsers, chunking, embeddings, vector store, retrieval, and eval depth.

→ [See more in retrieval-architecturing-decision-based.md](./retrieval-architecturing-decision-based.md)

_Section indexes: [ingestion](./ingestion/README.md) · [chunking](./chunking/README.md) · [embedding](./embedding/README.md) · [queries](./embedding/queries/README.md) · [compacting](./compacting/README.md) · [storaging](./storaging/README.md) · [search](./search/README.md)_

## Related guard-rails

- [Safer architecture: tenant-scoped retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md)
- [Wrong architecture: shared retrieval](../guard-rails/wrong-architecture-shared-retrieval.md)
- [Retrieval authorization in decision assistance](../guard-rails/guard-rails-decision-architecturing-assistance.md)
