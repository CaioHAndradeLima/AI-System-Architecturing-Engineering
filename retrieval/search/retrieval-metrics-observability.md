# Retrieval metrics observability

Metrics for **query-time retrieval and RAG quality**—ranking, rerank lift, latency, filters, context size, answers, and abstention. Complements [storage observability](../storaging/storage-observability.md) (index/store signals) and [chunking metrics](../chunking/chunking-metrics-observability.md) (ingestion-side).

| Metric | What it measures | Why it matters |
|--------|------------------|----------------|
| **Recall@K** | Fraction of relevant evidence retrieved in the top K | Detects missing evidence |
| **Precision@K** | Fraction of top-K results that are relevant | Detects noisy retrieval |
| **MRR** | Ranking position of the first relevant result | Rewards finding a useful passage early |
| **nDCG@K** | Ranking quality across results with graded relevance | Useful when some passages are more relevant than others |
| **Reranker improvement** | Difference in ranking quality before and after reranking | Shows whether reranking is worth its cost |
| **No-result rate** | Queries that retrieve no acceptable evidence | Helps identify unsupported questions or overly strict filters |
| **Retrieval latency** | Time spent searching and ranking | Measures responsiveness |
| **Filtered-search failures** | Errors or unauthorized results involving filters | Critical for correctness and tenant isolation |
| **Context token count** | Amount of retrieved content sent to the LLM | Helps control cost and irrelevant context |
| **Answer correctness** | Whether the final response is supported by retrieved evidence | Measures end-to-end RAG quality |
| **Abstention quality** | Whether the system declines to answer when evidence is insufficient | Reduces unsupported answers |

## Suggested alerts (starting point)

- **Filtered-search failures** or cross-tenant hits → incident-grade ([guard-rails test use cases](../../guard-rails/guard-rails-test-use-cases.md))
- **No-result rate** or **abstention quality** regressions after threshold, filter, or embedding changes
- **Retrieval latency** p95 breach after hybrid, rerank, or ANN tuning
- **Recall@K** drop on automated regression suite before release ([decision-based by scale](./retrieval-decision-based.md))

Run ranking metrics when you change [top-K](./retrieval-strategy-top-k.md), [similarity thresholds](./retrieval-strategy-similarity.md), [hybrid fusion](./retrieval-strategy-hybrid-search-vector-plus-keyword.md), or [reranking](./retrieval-strategy-reranking.md).

## Tooling

Dashboards, traces, and golden-set eval: [storage observability tools](../storaging/storage-observability-tools.md) · [embedding tools decision-based](../embedding/embedding-tools-decision-based.md) · [query evaluation](../embedding/queries/embedding-user-query-evaluation.md).

## See also

- [Retrieval decision-based by scale](./retrieval-decision-based.md)
- [Retrieval strategies combined](./retrieval-strategies-combined.md)
- [Search overview](./README.md)
