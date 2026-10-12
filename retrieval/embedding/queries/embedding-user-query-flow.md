# Embedding user query flow

How **document vectors** (offline) and **query vectors** (online) meet at similarity search—the core RAG embedding path. Index and query must use the **same embedding model and encoding rules** ([migration guide](../embedding-migration-ingestion-using-another-model.md), [bad practices — model mix](../embedding-bad-practices.md)).

## Offline: document ingestion

```
             OFFLINE: DOCUMENT INGESTION
             ===========================

  Document
     |
     v
  Chunking
     |
     v
  Document embedding model
     |
     v
  Stored document vectors
```

Chunks and metadata come from [chunking](../../chunking/) and [ingestion](../../ingestion/); store `embedding_model_id` on every vector batch.

## Online: user query

```
             ONLINE: USER QUERY
             ==================

  User asks:
  "How many days in advance must I
   request vacation?"
     |
     v
  [Query preprocessing]
     |
     v
  [Query embedding model]
     |
     v
  Query vector
     |
     v
  [Vector similarity search]
     |
     v
  Top-K relevant document chunks
     |
     v
  [Context assembly]
     |
     v
  [LLM generates answer]
```

## Stage notes

| Stage | Role |
|-------|------|
| **Query preprocessing** | Normalize text; apply model-specific prefixes (e.g. query vs document) per provider docs — see [cleaning user query](./embedding-cleaning-user-query.md) |
| **Query embedding model** | Must match **document embedding model** used for stored vectors |
| **Vector similarity search** | Apply **tenant and ACL filters** before or during search—not after the LLM ([guard-rails](../../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)) |
| **Top-K** | Tune K and max context tokens; watch duplicate overlap ([chunking metrics](../../chunking/chunking-metrics-observability.md)) |
| **Context assembly** | Order chunks, dedupe, attach citation metadata |
| **LLM** | Answer from context; validate output if required |

## End-to-end picture

```
  OFFLINE                          ONLINE
  -------                          ------

  Doc -> chunk -> embed_doc  |  Question -> embed_query
            |                |            |
            v                |            v
     stored vectors  <-------+---- similarity search -> top-K -> LLM
```

## See also

- [Retrieval flow (full pipeline)](../../retrieval-flow.md)
- [User query latency and cost](./embedding-user-query-latency-and-cost.md)
- [Minimum ingestion MVP](../../ingestion/minimum-ingestion-mvp.md)
- [Embedding metrics](../embedding-metrics.md)
- [Queries overview](./README.md) · [Embedding overview](../README.md)
