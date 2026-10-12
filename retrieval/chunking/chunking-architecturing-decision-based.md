# Chunking architecturing decision-based

How **chunking and indexing** choices evolve from startup/MVP through medium SaaS to enterprise—plus multi-tenancy, failures, evaluation, and scaling triggers.

Pair with [chunking architecturing — document-type matrix](./chunking-architecturing.md) (what strategy to pick) and [ingestion architecture engineering](../ingestion/ingestion-architecture-engineering.md) (MVP vs enterprise ops).

## Pipeline and chunking by scale

| Area | Startup / MVP | Medium Scale / SaaS | Enterprise |
|------|---------------|---------------------|------------|
| **Chunking strategy** | Recursive splitting | Structure-aware, configurable per document type | Hierarchical, semantic or specialized chunking where evaluation justifies it |
| **Chunk size** | Start with 300–800 tokens for experiments | Tune per content type using evaluation | Versioned configurations tuned against domain-specific datasets |
| **Overlap** | Start with 10–15% | Tune based on boundary errors and redundancy | Use only where beneficial; measure duplicate retrieval |
| **Document parsing** | PyMuPDF, basic DOCX/HTML parsers | Multiple parsers and format-specific handling | Specialized parsers, OCR, tables, code and complex layouts |
| **Execution** | Synchronous Python pipeline | Background jobs and workers | Queue-driven, horizontally scalable workers |
| **Storage** | Local files + FAISS/Chroma | Object storage + managed vector database | Scalable object storage, vector index and possibly separate metadata/document stores |
| **Embedding strategy** | Embed each chunk once | Hash/version-based incremental embedding | Incremental processing, batching, deduplication and controlled re-embedding |
| **Metadata** | Document ID, chunk index, source | Add tenant, version, page, section and access metadata | Add lineage, source version, parser/chunker version, ACL state and processing status |
| **Document updates** | Reprocess the document | Reprocess changed documents and retire stale chunks | Versioned indexing, controlled index publication and reliable deletion propagation |

## Operations, tenancy, and quality by scale

| Area | Startup / MVP | Medium Scale / SaaS | Enterprise |
|------|---------------|---------------------|------------|
| **Multi-tenancy** | Add tenant identity before multi-user launch | Shared infrastructure with enforced tenant and document isolation | Configurable isolation boundaries; dedicated resources for customers when required |
| **Failure handling** | Log errors and retry manually | Bounded retries, job status and alerts | Idempotent jobs, dead-letter handling, recovery workflows and service-level objectives |
| **Evaluation** | Manual review of a small question set | Automated golden-dataset regression tests | Versioned evaluations, domain-specific suites, release gates and ongoing production analysis |
| **Scaling trigger** | Optimize only when problems appear | Scale workers when ingestion backlog or latency requires it | Partition workloads, tune concurrency and isolate noisy tenants when justified |

## Guide links by row

| Topic | Docs |
|-------|------|
| Chunking strategies | [Simpler](./chunking-simpler-strategy.md) · [Structure-aware](./chunking-recursive-structure-aware.md) · [Semantic](./chunking-semantic.md) · [Parent-child](./chunking-hierarchical-parent-child.md) |
| Tools & eval | [Chunking tools](./chunking-tools.md) · [Ingestion observability](../ingestion/ingestion-observability.md) |
| Ingestion ops | [Multi-source ingestion](../ingestion/multi-source-ingestion.md) · [MVP vs enterprise](../ingestion/ingestion-architecture-engineering.md) |
| Tenancy | [Guard-rails data isolation](../../guard-rails/guardrails-data-isolation.md) · [Robust implementation](../../guard-rails/guard-rails-robust-cloud-rules-implementation.md) |

## See also

- [Retrieval architecturing decision-based](../retrieval-architecturing-decision-based.md)
- [Chunking overview](./README.md)
