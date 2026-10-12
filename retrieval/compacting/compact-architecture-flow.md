# Compact architecture flow

**Dual-write message storage**: keep authoritative text in a **normal database**, embed into a **vector index** for semantic recall—then at question time search with **tenant filters**, fetch authorized rows, and run RAG.

Implements the “Database + vector index” pattern from [compact decision-based](./compact-decision-based.md).

## Architecture

```
          Incoming message
                 |
                 v
          [Application API]
                 |
          +------+------+
          |             |
          v             v
   Normal database   Embedding model
   (original text)        |
          |               v
          |          Message vector
          |               |
          |               v
          |          Vector index
          |               |
          +-------+-------+
                  |
           User asks a question
                  |
                  v
          Embed the query
                  |
                  v
        Search relevant messages
         with tenant filters
                  |
                  v
         Fetch authorized records
                  |
                  v
              RAG / LLM
```

## Stage responsibilities

| Stage | Role |
|-------|------|
| **Application API** | Authenticate sender; attach `tenant_id`, user, message ID, timestamps |
| **Normal database** | Source of truth for message body and relational filters (customer, date, status) |
| **Embedding model** | Same model family as query embedding; version stored on index rows |
| **Vector index** | Semantic search over messages; metadata for filter + join back to DB primary key |
| **Embed the query** | [User query path](../embedding/queries/embedding-user-query-flow.md) |
| **Search with tenant filters** | Mandatory scope before returning IDs or text ([guard-rails](../../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)) |
| **Fetch authorized records** | Load full message text from DB by ID—do not trust vector payload alone if ACL can change |
| **RAG / LLM** | [Compacting](./README.md) optional: trim, dedupe, order messages before generation |

## Design notes

- Vector hits should return **stable message IDs**; hydrate text from the database after ACL check.
- Re-embed on edit; tombstone or delete vectors when messages are removed ([embedding migration — change table](../embedding/embedding-migration-ingestion-using-another-model.md)).
- Conversation RAG may also use [user context compact flow](../embedding/queries/embedding-user-context-compact-flow.md) before embed.

## See also

- [Compact decision-based](./compact-decision-based.md)
- [Safer tenant-scoped retrieval](../../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)
- [Compacting overview](./README.md)
