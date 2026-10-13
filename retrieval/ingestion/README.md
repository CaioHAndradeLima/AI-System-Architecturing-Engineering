# Ingestion

**Offline indexing**: fetch sources, parse, chunk, embed, and load the vector index. Query-time search and reranking live under the parent [retrieval](../README.md) section as it grows.

Parent overview: [retrieval topic areas](../README.md#topic-areas).

---

## Guides

### [basic-document-ingestion.md](./basic-document-ingestion.md)

`#upload` · `#pdf` · `#pipeline`

Upload-driven ingestion pipeline for PDFs: accept the file, store the original, parse and clean text, chunk, embed, and load the vector database for query-time retrieval.

→ [See more in basic-document-ingestion.md](./basic-document-ingestion.md)

### [multi-source-ingestion.md](./multi-source-ingestion.md)

`#connectors` · `#sync` · `#enterprise`

Enterprise ingestion from many systems: connectors per source, incremental sync, queued workers, extract/validate/ACL sync, then shared chunk/embed/index path—with cross-cutting reliability and lifecycle controls.

→ [See more in multi-source-ingestion.md](./multi-source-ingestion.md)

### [ingestion-architecture-engineering.md](./ingestion-architecture-engineering.md)

`#architecture` · `#mvp-vs-enterprise` · `#operations`

Basic MVP vs enterprise ingestion concerns: how triggers, processing, lifecycle, permissions, and monitoring differ as you move from upload scripts to multi-source sync (multi-source ingestion).

→ [See more in ingestion-architecture-engineering.md](./ingestion-architecture-engineering.md)

### [ingestion-observability.md](./ingestion-observability.md)

`#observability` · `#metrics` · `#sla`

Metrics to watch on indexing pipelines—from document processing health through index freshness, retrieval quality, and tenant isolation.

Aligns with enterprise monitoring in ingestion architecture engineering and multi-source ingestion.

→ [See more in ingestion-observability.md](./ingestion-observability.md)

### [retrieval-simple-ingestion.md](./retrieval-simple-ingestion.md)

`#ingestion` · `#indexing` · `#pipeline`

Offline indexing pipeline from heterogeneous sources into a vector index: ingest, parse, chunk, embed, and store chunks with metadata for later query-time retrieval.

→ [See more in retrieval-simple-ingestion.md](./retrieval-simple-ingestion.md)

### [ingestion-procedures.md](./ingestion-procedures.md)

`#reference` · `#pipeline` · `#quality`

End-to-end retrieval pipeline components: what each stage owns and what breaks when it is done poorly.

Stages 1–5 align with simple ingestion; retrieval, reranking, and evaluation are query-time and quality layers on top of the index.

→ [See more in ingestion-procedures.md](./ingestion-procedures.md)

### [minimum-ingestion-mvp.md](./minimum-ingestion-mvp.md)

`#mvp` · `#rag` · `#query-loop`

Smallest useful RAG loop: index documents offline, then at query time embed the question, search the vector store, pass top-K chunks to the LLM, return an answer with citations.

Add auth, reranking, and eval before calling it production-ready (ingestion procedures).

→ [See more in minimum-ingestion-mvp.md](./minimum-ingestion-mvp.md)

_Add new ingestion-specific markdown files in this directory; link them here._
