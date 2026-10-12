# Retrieval

Design and operate **retrieval** for LLM applications: indexing, query-time search, grounding, and quality—together with authorization and tenant scope ([guard-rails](../guard-rails/) retrieval notes).

## Topic areas

| Area | What we cover |
|------|----------------|
| **[Ingestion](./ingestion/)** | Fetch, parse, sync, index ops, observability |
| **[Chunking](./chunking/)** | Splitting text into retrievable units and metadata |
| **[Embedding](./embedding/)** | Document vectors, models; [queries](./embedding/queries/) for online search |
| **Search** | Dense, sparse, hybrid, filters, reranking |
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

## Guides

### [retrieval-architecturing-decision-based.md](./retrieval-architecturing-decision-based.md)

`#architecture` · `#decision-guide` · `#maturity`

Parsing through evaluation by MVP, medium, and large system—parsers, chunking, embeddings, vector store, retrieval, and eval depth.

→ [See more in retrieval-architecturing-decision-based.md](./retrieval-architecturing-decision-based.md)

_Section indexes: [ingestion](./ingestion/README.md) · [chunking](./chunking/README.md) · [embedding](./embedding/README.md) · [queries](./embedding/queries/README.md)_

## Related guard-rails

- [Safer architecture: tenant-scoped retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md)
- [Wrong architecture: shared retrieval](../guard-rails/wrong-architecture-shared-retrieval.md)
- [Retrieval authorization in decision assistance](../guard-rails/guard-rails-decision-architecturing-assistance.md)
