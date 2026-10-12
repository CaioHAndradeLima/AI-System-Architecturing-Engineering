# Retrieval implementation flow

```
          RETRIEVAL IMPLEMENTATION CHECKLIST
          ==================================

                         START
                           |
                           v
        +--------------------------------------+
        | 1. Build dense vector search         |
        |    - Embed user query                |
        |    - Retrieve top 5 chunks           |
        +--------------------------------------+
                           |
                           v
        +--------------------------------------+
        | 2. Add metadata filters              |
        |    - Tenant ID                       |
        |    - Document status                 |
        |    - User authorization               |
        +--------------------------------------+
                           |
                           v
        +--------------------------------------+
        | 3. Create a golden dataset            |
        |    - Representative questions         |
        |    - Expected relevant passages       |
        +--------------------------------------+
                           |
                           v
        +--------------------------------------+
        | 4. Evaluate retrieval quality         |
        |    - Recall@K                         |
        |    - Precision@K                      |
        +--------------------------------------+
                           |
                           v
        +--------------------------------------+
        | 5. Tune similarity thresholds         |
        |    - Reject weak matches              |
        |    - Test no-answer behavior          |
        +--------------------------------------+
                           |
                           v
        +--------------------------------------+
        | 6. Benchmark hybrid search            |
        |    - Dense vector search              |
        |    - BM25 keyword search               |
        |    - Compare retrieval results        |
        +--------------------------------------+
                           |
                           v
        +--------------------------------------+
        | 7. Evaluate reranking                  |
        |    - Reorder candidate chunks         |
        |    - Measure quality, latency, cost   |
        +--------------------------------------+
                           |
                           v
        +--------------------------------------+
        | 8. Add observability                  |
        |    - Trace retrieval stages           |
        |    - Monitor latency and failures     |
        |    - Run regression tests             |
        +--------------------------------------+
                           |
                           v
                 +-------------------+
                 | Quality improved? |
                 +-------------------+
                    |             |
                   YES            NO
                    |             |
                    v             v
              Deploy safely   Analyze failures
                    |             |
                    v             |
              Monitor in <--------+
              production

          ==================================
          SUCCESS CRITERIA
          - Relevant evidence is retrieved
          - Unauthorized data is never exposed
          - Latency and cost meet targets
          - Changes pass retrieval regression tests

```

## Step → guides

| Step | Docs |
|------|------|
| 1. Dense vector search | [Embedding user query flow](../embedding/queries/embedding-user-query-flow.md) · [Top-K](./retrieval-strategy-top-k.md) · [Minimum ingestion MVP](../ingestion/minimum-ingestion-mvp.md) |
| 2. Metadata filters | [Metadata filtering](./retrieval-strategy-metadata-filtering.md) · [Guard-rails test use cases](../../guard-rails/guard-rails-test-use-cases.md) |
| 3. Golden dataset | [Query evaluation](../embedding/queries/embedding-user-query-evaluation.md) |
| 4. Recall / Precision@K | [Retrieval metrics observability](./retrieval-metrics-observability.md) |
| 5. Similarity thresholds | [Similarity strategy](./retrieval-strategy-similarity.md) |
| 6. Hybrid benchmark | [Hybrid search](./retrieval-strategy-hybrid-search-vector-plus-keyword.md) |
| 7. Reranking | [Reranking](./retrieval-strategy-reranking.md) |
| 8. Observability | [Retrieval metrics](./retrieval-metrics-observability.md) · [Storage observability tools](../storaging/storage-observability-tools.md) |
| Maturity expectations | [Retrieval decision-based by scale](./retrieval-decision-based.md) |
| Full pipeline view | [Retrieval strategies combined](./retrieval-strategies-combined.md) |

Steps **2** (filters) should not wait until after eval in production multi-tenant systems—move filters up if users share an index ([wrong architecture: shared retrieval](../../guard-rails/wrong-architecture-shared-retrieval.md)).

## See also

- [Retrieval flow](../retrieval-flow.md)
- [Search overview](./README.md)
