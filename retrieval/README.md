# Retrieval

Design and operate **retrieval** for LLM applications: indexing, query-time search, grounding, and quality—together with authorization and tenant scope ([guard-rails](../guard-rails/) retrieval notes).

## Topic areas

| Area | What we cover |
|------|----------------|
| **Pipeline** | Ingest → chunk → embed → index → query → rerank → context assembly |
| **Chunking** | Size, overlap, structure-aware splits, metadata |
| **Search** | Dense, sparse, hybrid, filters, reranking |
| **Grounding** | Citations, context limits, when retrieval fails |
| **Operations** | Freshness, reindexing, eval metrics (recall, MRR, grounded answers) |
| **Multi-tenant** | Scoped indexes, ACL sync, safe caching |

---

## Guides

### [retrieval-simple-ingestion.md](./retrieval-simple-ingestion.md)

`#ingestion` · `#indexing` · `#pipeline`

Five-stage offline path from PDFs, Confluence, DB, and APIs through parse, chunk, embed, and vector index—with metadata for tenant-safe retrieval.

→ [See more in retrieval-simple-ingestion.md](./retrieval-simple-ingestion.md)

### [ingestion-procedures.md](./ingestion-procedures.md)

`#reference` · `#pipeline` · `#quality`

Component-by-component responsibilities and failure symptoms from ingestion through evaluation—use for triage and test coverage.

→ [See more in ingestion-procedures.md](./ingestion-procedures.md)

### [minimum-ingestion-mvp.md](./minimum-ingestion-mvp.md)

`#mvp` · `#rag` · `#query-loop`

Minimal index path (parse → chunk → embed → store) and query path (embed question → top-K → LLM → citations).

→ [See more in minimum-ingestion-mvp.md](./minimum-ingestion-mvp.md)

### [retrieval-architecturing-decision-based.md](./retrieval-architecturing-decision-based.md)

`#architecture` · `#decision-guide` · `#maturity`

Parsing through evaluation by MVP, medium, and large system—parsers, chunking, embeddings, vector store, retrieval, and eval depth.

→ [See more in retrieval-architecturing-decision-based.md](./retrieval-architecturing-decision-based.md)

## Related guard-rails

- [Safer architecture: tenant-scoped retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md)
- [Wrong architecture: shared retrieval](../guard-rails/wrong-architecture-shared-retrieval.md)
- [Retrieval authorization in decision assistance](../guard-rails/guard-rails-decision-architecturing-assistance.md)
