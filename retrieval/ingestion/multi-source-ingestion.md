# Multi-source ingestion

**Enterprise ingestion** from many systems: connectors per source, incremental sync, queued workers, extract/validate/ACL sync, then shared chunk/embed/index path—with cross-cutting reliability and lifecycle controls.

## Architecture

```
                 EXTERNAL DATA SOURCES
       +------------+-----------+-------------+
       |            |           |             |
    Drive       Confluence   SharePoint    Internal API
       |            |           |             |
       +------------+-----------+-------------+
                              |
                              v
                    [Source Connectors]
                              |
                              v
                   [Incremental Sync / CDC]
                              |
                              v
                      [Queue / Jobs]
                              |
                              v
                    [Ingestion Workers]
                              |
                 +------------+------------+
                 |            |            |
                 v            v            v
              Extract      Validate     ACL Sync
                 |            |            |
                 +------------+------------+
                              |
                              v
                     [Chunk + Embed]
                              |
                              v
                      [Vector Index]
                              |
                              v
                    [Index / Version State]

   Cross-cutting: retries, idempotency, monitoring,
   dead-letter handling, deletion and re-indexing
```

## Stage responsibilities

| Stage | Role |
|-------|------|
| **Source connectors** | Authenticate to each system; normalize source IDs, URLs, and modification timestamps. |
| **Incremental sync / CDC** | Fetch only creates/updates/deletes since last cursor; avoid full re-crawl unless required. |
| **Queue / jobs** | Decouple sync discovery from heavy processing; scale workers horizontally. |
| **Ingestion workers** | Orchestrate per-document pipeline with bounded concurrency per tenant/source. |
| **Extract** | Pull raw content (and attachments) into a canonical internal representation. |
| **Validate** | Reject or quarantine empty parses, oversize blobs, or schema violations. |
| **ACL sync** | Copy permission metadata from source into index filters—must stay in step with [tenant-scoped retrieval](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md). |
| **Chunk + embed** | Same indexing core as [simple ingestion](./retrieval-simple-ingestion.md) and [basic document upload](./basic-document-ingestion.md). |
| **Vector index** | Upsert with tombstones for deleted source objects. |
| **Index / version state** | Track embedding model, chunk config, and last successful sync per source/tenant for re-index jobs. |

## Cross-cutting controls

| Control | Purpose |
|---------|---------|
| **Retries** | Transient API/rate-limit failures without duplicating indexed rows when idempotent keys are set. |
| **Idempotency** | Stable document keys `(source, external_id, content_version)` for upserts. |
| **Monitoring** | Lag, error rate, queue depth, docs/hour per connector. |
| **Dead-letter handling** | Inspect poison messages without blocking the whole queue. |
| **Deletion and re-indexing** | Remove vectors when source deletes; batch re-embed when models or chunkers change. |

## Compare to simpler paths

| Pattern | When |
|---------|------|
| [Minimum ingestion MVP](./minimum-ingestion-mvp.md) | Single corpus, manual or batch load |
| [Basic document ingestion](./basic-document-ingestion.md) | User upload PDF/DOCX |
| **Multi-source ingestion (this note)** | Ongoing sync from SaaS + internal APIs with ACLs |

## See also

- [Ingestion architecture engineering — MVP vs enterprise](./ingestion-architecture-engineering.md)
- [Ingestion procedures](./ingestion-procedures.md)
- [Retrieval architecturing decisions](../retrieval-architecturing-decision-based.md)
- [Guard-rails robust implementation](../../guard-rails/guard-rails-robust-cloud-rules-implementation.md)
