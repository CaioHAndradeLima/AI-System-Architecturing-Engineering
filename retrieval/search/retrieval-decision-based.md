# Retrieval decision-based by scale

How **query-time retrieval** choices evolve from startup/MVP through medium SaaS to enterprise—method, K, thresholds, filters, rerank, hybrid, index tuning, fallback, eval, and scaling.

Pair with [retrieval strategies combined](./retrieval-strategies-combined.md) (full pipeline) and [retrieval architecturing decision-based — Retrieval row](../retrieval-architecturing-decision-based.md).

| Area | Startup / MVP | Medium Scale / SaaS | Enterprise |
|------|---------------|---------------------|------------|
| **Retrieval method** | Dense vector search | Vector + metadata filters; test hybrid search | Hybrid or multi-stage retrieval tuned by query type |
| **Top-K** | Start with 5 | Tune candidate count using evaluation | Tune candidate generation and final context size separately |
| **Similarity threshold** | Optional; establish baseline first | Calibrate using labeled queries | Versioned thresholds and evidence sufficiency rules |
| **Metadata filtering** | Tenant and document identifiers | Tenant, document ACLs, status and relevant business fields | Fine-grained authorization, synchronized ACLs and auditable policy enforcement |
| **Reranking** | Usually skip initially | Add if it measurably improves results | Rerank large candidate sets when quality and latency targets justify it |
| **Query rewriting** | Original query first | Add for ambiguous or conversational queries | Route query types to specialized retrieval strategies |
| **Hybrid search** | Add when keyword misses are observed | Benchmark BM25 + vector retrieval | Multiple retrieval channels with controlled fusion and evaluation |
| **Index configuration** | Default settings | Tune ANN parameters using real workloads | Tune recall, latency, memory and filtered-search performance |
| **Fallback behavior** | Return no-answer when evidence is insufficient | Retry or ask for clarification where useful | Policy-driven fallback, degraded-mode handling and clear abstention behavior |
| **Evaluation** | Small golden dataset | Automated regression suite | Release gates, segment-level evaluation and continuous monitoring |
| **Scaling** | One service or database | Background indexing and monitored capacity | Workload isolation, replication and partitioning when justified |

## Guide links by area

| Area | Docs |
|------|------|
| Retrieval method / hybrid | [Hybrid search](./retrieval-strategy-hybrid-search-vector-plus-keyword.md) · [Combined pipeline](./retrieval-strategies-combined.md) |
| Top-K / threshold / fallback | [Top-K](./retrieval-strategy-top-k.md) · [Similarity scores](./retrieval-strategy-similarity.md) |
| Metadata filtering | [Metadata filtering](./retrieval-strategy-metadata-filtering.md) · [Guard-rails data isolation](../../guard-rails/guardrails-data-isolation.md) |
| Reranking | [Reranking](./retrieval-strategy-reranking.md) |
| Query rewriting | [Cleaning user query](../embedding/queries/embedding-cleaning-user-query.md) |
| Index configuration | [Index strategies](../storaging/index-strategies.md) · [HNSW flow](../storaging/hnsw-flow.md) · [Storage indexing by scale](../storaging/storage-indexing-decision-based.md) |
| Evaluation / observability | [Retrieval metrics observability](./retrieval-metrics-observability.md) · [Query evaluation](../embedding/queries/embedding-user-query-evaluation.md) · [Storage observability](../storaging/storage-observability.md) |
| Scaling | [Storage and indexing by scale](../storaging/storage-indexing-decision-based.md) |

## See also

- [Retrieval flow](../retrieval-flow.md)
- [Search overview](./README.md)
