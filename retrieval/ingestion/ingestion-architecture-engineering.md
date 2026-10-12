# Ingestion architecture engineering

**Basic MVP vs enterprise** ingestion concerns: how triggers, processing, lifecycle, permissions, and monitoring differ as you move from upload scripts to multi-source sync ([multi-source ingestion](./multi-source-ingestion.md)).

| Concern | Basic MVP | Enterprise |
|---------|-----------|------------|
| **Ingestion trigger** | User uploads a file | Uploads, schedules, webhooks or change feeds |
| **Processing** | One Python process | Background workers and a queue |
| **Reprocessing** | Re-run the pipeline | Reprocess only affected documents |
| **Duplicate handling** | Basic document IDs | Idempotent jobs and stable content hashes |
| **Failures** | Log and retry manually | Bounded retries, dead-letter queue, alerts |
| **Document updates** | Rebuild manually | Version tracking and incremental indexing |
| **Deletions** | Delete manually | Propagate deletions to all relevant indexes |
| **Permissions** | Simple access metadata | Synchronize source permissions and enforce them at retrieval |
| **Monitoring** | Logs | Metrics, traces, freshness and error alerts |

## Mapping to docs in this folder

| Concern row | See |
|-------------|-----|
| Upload trigger, single process | [Basic document ingestion](./basic-document-ingestion.md), [Minimum ingestion MVP](./minimum-ingestion-mvp.md) |
| Change feeds, queue, ACL sync | [Multi-source ingestion](./multi-source-ingestion.md) |
| Permission + retrieval enforcement | [Guard-rails — tenant-scoped retrieval](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md) |
| Scale decisions (parsing → eval) | [Retrieval architecturing decision-based](../retrieval-architecturing-decision-based.md) |

## See also

- [Ingestion procedures](./ingestion-procedures.md)
- [Ingestion overview](./README.md)
