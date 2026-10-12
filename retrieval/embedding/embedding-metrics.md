# Embedding metrics

Metrics for **embedding generation, index health, retrieval, and end-to-end RAG**—what to measure and why. Overlaps with [chunking metrics observability](../chunking/chunking-metrics-observability.md); this note centers on the embedding and vector-search path.

| Metric | What it measures | Why it matters |
|--------|------------------|----------------|
| **Embedding latency** | Time to generate vectors | Detects slow providers, network issues, or overloaded serving infrastructure |
| **Embedding throughput** | Chunks or tokens processed per unit of time | Helps size workers and estimate processing capacity |
| **Embedding error rate** | Failed embedding requests | Detects rate limits, malformed inputs, and provider outages |
| **Token volume** | Tokens sent for embedding | Helps estimate and control cost |
| **Cost per document** | Embedding spend per processed document | Helps compare configurations and customer usage |
| **Cache hit rate** | Percentage of requests served from a valid embedding cache | Identifies potential savings from avoiding duplicate work |
| **Vector dimension consistency** | Whether vectors match the expected dimension | Prevents indexing and query compatibility errors |
| **Index freshness** | How long updated content takes to become searchable | Detects delayed or failed ingestion |
| **Recall@K** | Whether relevant evidence appears in the top K results | Measures retrieval coverage |
| **Precision@K** | How many retrieved results are relevant | Measures retrieval noise |
| **Retrieval latency** | Time spent searching the index | Helps maintain query response-time targets |
| **Answer correctness** | Whether the final answer is correct and supported | Validates the full RAG pipeline, not just embeddings |

## Suggested groupings

| Layer | Metrics |
|-------|---------|
| **Embed API / worker** | Latency, throughput, error rate, token volume, cache hit rate |
| **Index integrity** | Dimension consistency, index freshness, cost per document |
| **Query path** | Recall@K, Precision@K, retrieval latency |
| **Product quality** | Answer correctness (requires golden set or human eval) |

Alert on **dimension mismatch** and **embedding error rate** spikes before Recall@K drifts—they often precede quality regressions after [model migration](./embedding-migration-ingestion-using-another-model.md).

## See also

- [Ingestion observability](../ingestion/ingestion-observability.md)
- [Embedding decision-based](./embedding-decision-based.md)
- [Embedding overview](./README.md)
