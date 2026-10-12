# Ingestion

**Offline indexing**: fetch sources, parse, chunk, embed, and load the vector index. Query-time search and reranking live under the parent [retrieval](../README.md) section as it grows.

Parent overview: [retrieval topic areas](../README.md#topic-areas).

---

## Guides

### [basic-document-ingestion.md](./basic-document-ingestion.md)

`#upload` · `#pdf` · `#pipeline`

User PDF upload through API, object storage, parse/clean, chunk, embed, and vector DB until ready for retrieval.

→ [See more in basic-document-ingestion.md](./basic-document-ingestion.md)

### [multi-source-ingestion.md](./multi-source-ingestion.md)

`#connectors` · `#sync` · `#enterprise`

Drive, Confluence, SharePoint, and APIs through connectors, CDC, queues, ACL sync, and shared chunk/embed/index with cross-cutting ops.

→ [See more in multi-source-ingestion.md](./multi-source-ingestion.md)

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

_Add new ingestion-specific markdown files in this directory; link them here._
