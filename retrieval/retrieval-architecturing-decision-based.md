# Retrieval architecturing decision-based

How to evolve **parsing → evaluation** choices as the system grows from MVP to medium to large scale. Pair with [minimum ingestion MVP](./ingestion/minimum-ingestion-mvp.md) and [guard-rails decision assistance](../guard-rails/guard-rails-decision-architecturing-assistance.md) for security and ops maturity.

| Decision | MVP | Medium system | Large system |
|----------|-----|---------------|--------------|
| **Parsing** | Lightweight parser for supported formats | Format-specific parsers and OCR where needed | Managed/document-processing pipelines |
| **Chunking** | Structure-aware splitter | Document-specific strategies and evaluation | Multiple strategies with versioned experiments |
| **Embeddings** | One suitable hosted or local model | Benchmark alternatives and monitor drift | Model governance, throughput optimization, migration plans |
| **Vector storage** | Existing DB with vector support or lightweight index | Managed vector/search service | Scale, availability, isolation, and operational requirements drive selection |
| **Retrieval** | Vector similarity + metadata filters | Hybrid search if evidence supports it | Tuned retrieval, reranking, partitioning, and advanced filtering |

Detail by maturity stage: [search retrieval decision-based](./search/retrieval-decision-based.md).
| **Evaluation** | Golden dataset + manual review | Automated regression tests | Continuous, risk-based evaluation and monitoring |

## How to use this table

- **MVP:** Ship [minimum ingestion MVP](./ingestion/minimum-ingestion-mvp.md); do not skip metadata filters if the product is multi-tenant.
- **Medium:** Invest when manual review catches repeated retrieval failures or embedding drift hurts quality.
- **Large:** Treat chunking/embedding/retrieval configs as **versioned experiments** with rollback; align index isolation with [data isolation](../guard-rails/guardrails-data-isolation.md).

## See also

- [Search section](./search/README.md)
- [Ingestion section](./ingestion/README.md)
- [Ingestion procedures](./ingestion/ingestion-procedures.md)
- [Retrieval simple ingestion](./ingestion/retrieval-simple-ingestion.md)
- [Retrieval overview](./README.md)
