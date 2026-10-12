# Storage and indexing decision-based by scale

How **vector storage, indexes, metadata, and ops** evolve from startup/MVP through medium SaaS to enterprise.

Pair with [storage architecturing decision-based](./storage-architecturing-decision-based.md) (pick a starting store), [index strategies](./index-strategies.md), [storage strategy](./storage-strategy.md), and [chunking architecturing decision-based](../chunking/chunking-architecturing-decision-based.md) (ingestion-side storage rows).

| Area | Startup / MVP | Medium Scale / SaaS | Enterprise |
|------|---------------|---------------------|------------|
| **Storage choice** | FAISS, Chroma or pgvector | Managed PostgreSQL/vector service or dedicated vector database | Workload-specific database and index architecture |
| **Index strategy** | Simple default or exact search for small datasets | Tune ANN indexes based on measured workload | Tune index, memory, replication and capacity against SLOs |
| **Metadata** | Document ID, source, tenant ID | Add version, status, page, permissions and timestamps | Add lineage, lifecycle state, ACL synchronization and audit metadata |
| **Query filtering** | Basic validated metadata filters | Enforced tenant and document authorization | Defense-in-depth authorization and isolation testing |
| **Updates** | Re-index changed documents | Incremental updates and stale-record cleanup | Versioned index migrations and controlled publication |
| **Deletions** | Delete document vectors | Reliable deletion propagation | Auditable deletion workflows across indexes, caches and replicas |
| **Scaling** | One database or local service | Capacity monitoring and scaling | Workload isolation, replication, partitioning or sharding when justified |
| **Availability** | Basic backups | Managed backups and recovery testing | Defined recovery objectives, failover and disaster-recovery exercises |
| **Evaluation** | Small golden dataset | Automated retrieval regression tests | Release gates, workload-specific benchmarks and continuous evaluation |
| **Cost controls** | Track storage and query usage | Monitor tenant usage and index overhead | Capacity planning, storage optimization and per-tenant cost allocation |

## Guide links by area

| Area | Docs |
|------|------|
| Store selection | [Storage architecturing decision-based](./storage-architecturing-decision-based.md) · [Compact decision — pgvector/Chroma](../compacting/compact-decision-based.md) |
| Index / query path | [Index strategies](./index-strategies.md) · [HNSW flow](./hnsw-flow.md) · [Storage strategy — exact vs ANN](./storage-strategy.md) |
| Hybrid DB + vector | [Compact architecture flow](../compacting/compact-architecture-flow.md) |
| Embedding side of scale | [Embedding startup vs enterprise](../embedding/embedding-startup-vs-enterprise-architecture-decision-based.md) |
| Tenancy / auth / deletion | [Guard-rails data isolation](../../guard-rails/guardrails-data-isolation.md) · [Wrong architecture: shared retrieval](../../guard-rails/wrong-architecture-shared-retrieval.md) · [Robust implementation](../../guard-rails/guard-rails-robust-cloud-rules-implementation.md) |
| Metrics / migration | [Storage observability](./storage-observability.md) · [Embedding metrics](../embedding/embedding-metrics.md) · [Embedding migration](../embedding/embedding-migration-ingestion-using-another-model.md) |

## See also

- [Retrieval architecturing decision-based](../retrieval-architecturing-decision-based.md)
- [Storaging overview](./README.md)
