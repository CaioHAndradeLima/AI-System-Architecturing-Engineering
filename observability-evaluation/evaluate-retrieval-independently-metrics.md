# Evaluate retrieval independently — metrics

Measure **search and ranking alone** on a golden dataset (query → known relevant document IDs) before blaming the LLM for bad answers. Independent retrieval eval isolates chunking, embeddings, indexes, filters, hybrid fusion, and top-K from generation and [output validation](../output/output-validation-via-test-or-guardrails-metrics.md).

| Metric | What it measures | When it helps |
|--------|------------------|---------------|
| **Recall@K** | Fraction of known relevant items found in the top K | When missing relevant evidence is costly |
| **Precision@K** | Fraction of the top K results that are relevant | When irrelevant context creates noise |
| **MRR (Mean Reciprocal Rank)** | How highly the first relevant result is ranked | When one strong result is often sufficient |
| **nDCG@K (normalized Discounted Cumulative Gain)** | Ranking quality, including graded relevance | When some documents are more relevant than others |
| **Empty-result rate** | How often retrieval returns no results | Detecting indexing, filtering, or query issues |

## How this fits the stack

| Scope | Docs |
|-------|------|
| Retrieval-only (this table) | Golden qrels, no model call |
| Retrieval + rerank / filters | [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) |
| By architecture layer | [Retrieval architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md) |
| End-to-end RAG | [Embedding user query evaluation](../retrieval/embedding/queries/embedding-user-query-evaluation.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |

Run **Recall@K** and **empty-result rate** when you change [metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md), [top-K](../retrieval/search/retrieval-strategy-top-k.md), or [storage / index](../retrieval/storaging/storage-observability.md) settings. Use **MRR** or **nDCG@K** when order within K drives which chunk the model sees first.

## See also

- [Poor retrieval scores — debug flow](./poor-retrieval-scores.md)
- [Retrieval implementation flow](../retrieval/search/retrieval-implementation-flow.md)
- [Observability & evaluation overview](./README.md)
