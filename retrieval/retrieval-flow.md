# Retrieval flow

End-to-end **RAG retrieval path**: offline indexing, query-time search (vector + metadata + keyword), optional reranking, context assembly, and generation. Tenant and ACL filters belong on the retrieval engine branch, not only at the LLM ([tenant-scoped retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md)).

```
            DOCUMENT INGESTION
                    |
                    v
        Parse -> Chunk -> Embed
                    |
                    v
             Vector Storage
                    |
                    |
                    v
             USER ASKS QUESTION
                    |
                    v
              Query Embedding
                    |
                    v
              RETRIEVAL ENGINE
                    |
          +---------+---------+
          |         |         |
          v         v         v
       Vector    Metadata   Keyword
       search    filters    search
          |         |         |
          +---------+---------+
                    |
                    v
          Candidate passages
                    |
                    v
          Optional reranking
                    |
                    v
          Select final evidence
                    |
                    v
             Context assembly
                    |
                    v
               LLM answer
```

## Map to repo sections

| Stage | Docs |
|-------|------|
| Parse → chunk → embed (ingestion) | [Ingestion](./ingestion/) · [Chunking](./chunking/) · [Embedding](./embedding/) |
| Vector storage | [Storaging](./storaging/) |
| Query embedding | [Embedding queries](./embedding/queries/) |
| Retrieval engine (vector, filters, keyword) | [Search](./search/README.md) · [Metadata filtering](./search/retrieval-strategy-metadata-filtering.md) · [Storage strategy](./storaging/storage-strategy.md) |
| Reranking & final evidence | [Reranking](./search/retrieval-strategy-reranking.md) · [Compacting](./compacting/) |
| Context assembly → LLM | [Context assembly flow](../contexting/context-assembly-flow.md) · [Compact architecture flow](./compacting/compact-architecture-flow.md) · [Embedding user query flow](./embedding/queries/embedding-user-query-flow.md) |

**Hybrid retrieval:** vector and keyword branches merge before candidate passages—see [hybrid search (vector + keyword)](./search/retrieval-strategy-hybrid-search-vector-plus-keyword.md).

## See also

- [Retrieval architecturing decision-based](./retrieval-architecturing-decision-based.md)
- [Retrieval overview](./README.md)
