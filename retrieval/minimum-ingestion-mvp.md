# Minimum ingestion MVP

Smallest **useful RAG loop**: index documents offline, then at query time embed the question, search the vector store, pass top-K chunks to the LLM, return an answer with citations. Add auth, reranking, and eval before calling it production-ready ([ingestion procedures](./ingestion-procedures.md)).

## Indexing path

```
             DOCUMENTS
                 |
                 v
         +---------------+
         | Parser        |
         +---------------+
                 |
                 v
         +---------------+
         | Chunker       |
         +---------------+
                 |
                 v
         +---------------+
         | Embedding API |
         +---------------+
                 |
                 v
         +---------------+
         | Vector Store  |
         +---------------+
```

## Query path

```
  Question -> Query embedding
                    |
                    v
              Vector search
                    |
                    v
              Top-K chunks
                    |
                    v
                   LLM
                    |
                    v
            Answer + citations
```

## MVP scope

| In scope | Usually deferred |
|----------|------------------|
| Single corpus or tenant | Multi-tenant ACL filters on every search |
| One embedding model for index and query | Hybrid sparse+dense, rerankers |
| Fixed chunk size / overlap | Structure-aware chunking |
| Top-K similarity search | Freshness jobs, deletion tombstones |
| Prompt with chunks + cite sources | Grounding eval suite, guardrails services |

Even an MVP should attach **source IDs** to chunks so citations are real and you can grow into [simple ingestion](./retrieval-simple-ingestion.md) tracking (updates/deletions).

## Practical checklist

- [ ] Same **embedding model** for indexing and query embedding
- [ ] Store **chunk text** alongside vectors (do not rely on vector ID alone)
- [ ] Cap **K** and total context tokens before the LLM call
- [ ] Plan the first **golden questions** before expanding the pipeline

## See also

- [Retrieval simple ingestion](./retrieval-simple-ingestion.md)
- [Ingestion procedures](./ingestion-procedures.md)
- [Safer tenant-scoped retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md)
