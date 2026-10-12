# Compact decision-based

Choose **storage and retrieval shape** by use case—exact lookups vs semantic search vs hybrid—before compacting hits into LLM context ([compacting overview](./README.md)).

| Use case | Recommended approach | Why |
|----------|---------------------|-----|
| **Fetch a message by ID** | Normal database | Exact lookup is simpler and faster |
| **Filter messages by customer, user, date or status** | Normal database | Relational queries are ideal |
| **Find messages similar in meaning** | Vector storage | Semantic similarity search |
| **Retrieve past conversations for RAG** | Database + vector index | Metadata filtering plus semantic retrieval |
| **Search messages by exact keywords and meaning** | Hybrid search | Combines keyword and vector retrieval |
| **Small prototype with few messages** | PostgreSQL + `pgvector` or Chroma | Simple to build and evolve |

## RAG pipeline placement

```
  Question
      |
      +-- metadata filters (DB) ----+
      |                              v
      +-- vector / hybrid search --> candidate messages
                              |
                              v
                      [Compacting context]
                              |
                              v
                            LLM
```

- **Tenant and ACL filters** belong in the DB/metadata layer before or with vector search ([guard-rails](../../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)).
- **Compacting** applies after you have candidate rows/chunks—dedupe, rank, fit token budget ([user query flow — context assembly](../embedding/queries/embedding-user-query-flow.md)).

## See also

- [Storaging](../storaging/) — vector DB, metadata, and object storage
- [Compact architecture flow](./compact-architecture-flow.md)
- [Minimum ingestion MVP](../ingestion/minimum-ingestion-mvp.md)
- [Embedding bad practices — semantic vs keyword](../embedding/embedding-bad-practices.md)
- [Retrieval architecturing decision-based](../retrieval-architecturing-decision-based.md)
