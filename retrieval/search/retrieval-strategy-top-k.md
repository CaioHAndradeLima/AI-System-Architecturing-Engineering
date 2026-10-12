# Retrieval strategy — top-K

**K** is the number of candidate results you request from the retrieval system (vector search, hybrid fusion, or post-filter pipeline).

- **K = 3:** return three candidates.
- **K = 5:** return five candidates.
- **K = 20:** return twenty candidates.

K is not the same as how many passages you send to the LLM: [compacting](../compacting/) may dedupe, rerank, or truncate after retrieval ([retrieval flow](../retrieval-flow.md)).

## Tuning (starting point)

| Lower K | Higher K |
|---------|----------|
| Less context noise and cost | Better chance relevant chunks appear (higher Recall@K) |
| Risk missing evidence | More duplicates and token pressure on the model |

Measure **Recall@K** and **Precision@K** on a golden set when you change K, chunk size, or reranking ([storage observability](../storaging/storage-observability.md)). ANN indexes may need a larger internal **efSearch** (or equivalent) so the index actually explores enough neighbors before you truncate to K ([HNSW flow](../storaging/hnsw-flow.md)).

Apply **tenant and metadata filters** as part of retrieval; do not rely on a large K and hope the LLM ignores wrong tenants ([tenant-scoped retrieval](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)).

## See also

- [Embedding user query flow](../embedding/queries/embedding-user-query-flow.md)
- [Search overview](./README.md)
