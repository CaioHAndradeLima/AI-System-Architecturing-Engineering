# Storaging

Where **retrieval data lives**: vector indexes, relational/metadata stores, object storage for originals, and how they stay consistent for search and RAG.

Storaging connects [ingestion](../ingestion/) outputs, [embedding](../embedding/) vectors, and query-time filters in [compacting](../compacting/) and [embedding queries](../embedding/queries/).

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Vector index** | pgvector, Chroma, managed vector DBs, filters, dimensions |
| **Relational / metadata** | Document IDs, tenant, ACL, message rows, join keys |
| **Object storage** | Original PDFs, attachments, re-parse sources |
| **Hybrid layout** | DB + vector index ([compact decision](../compacting/compact-decision-based.md)) |
| **Lifecycle** | Upsert, tombstones, blue/green indexes, replication |
| **Multi-tenant** | Shared index + filters vs dedicated indexes ([guard-rails data isolation](../../guard-rails/guardrails-data-isolation.md)) |

---

## Guides

_Guide entries (tags, short description, see-more links) will appear here as markdown files are added—same style as [compacting README](../compacting/README.md)._

## Related

- [Compact architecture flow](../compacting/compact-architecture-flow.md) — DB + vector dual-write
- [Retrieval architecturing decision-based — Vector storage](../retrieval-architecturing-decision-based.md)
- [Embedding migration](../embedding/embedding-migration-ingestion-using-another-model.md)
- [Wrong architecture: shared retrieval](../../guard-rails/wrong-architecture-shared-retrieval.md)
