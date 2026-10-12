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
| Retrieval engine (vector, filters, keyword) | [Search](./search/README.md) · [Storage strategy](./storaging/storage-strategy.md) |
| Reranking & final evidence | _Search docs (as added)_ · [Compacting](./compacting/) |
| Context assembly → LLM | [Compact architecture flow](./compacting/compact-architecture-flow.md) · [Embedding user query flow](./embedding/queries/embedding-user-query-flow.md) |

**Hybrid retrieval:** vector and keyword branches often merge before candidate passages (RRF or weighted fusion)—details live under [search](./search/README.md) as you add them.

## See also

- [Retrieval architecturing decision-based](./retrieval-architecturing-decision-based.md)
- [Retrieval overview](./README.md)
