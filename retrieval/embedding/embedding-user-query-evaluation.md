# Embedding user query evaluation

Metrics to judge whether **query encoding and retrieval** work on real questions—not just whether the embed API returns 200.

| Metric | Question it answers |
|--------|---------------------|
| **Recall@K** | Is the expected evidence among the top K retrieved chunks? |
| **MRR (Mean Reciprocal Rank)** | How high is the first relevant result? |
| **nDCG@K** | Are relevant results ranked well, including cases with different relevance grades? |
| **Latency and cost** | Does the query-encoding strategy meet your requirements? |

## How to use them together

- **Recall@K** — primary gate for “can the pipeline find the right chunk at all?” ([embedding metrics](./embedding-metrics.md), [chunking metrics](../chunking/chunking-metrics-observability.md)).
- **MRR** — sensitive to putting one strong chunk at rank 1; useful when the LLM mostly reads the first passage.
- **nDCG@K** — use when labels are graded (highly relevant vs partially relevant); needs more annotation effort.
- **Latency and cost** — compare preprocessing choices ([cleaning user query](./embedding-cleaning-user-query.md), [context rewrite](./embedding-user-context-compact-flow.md)) against SLOs ([query latency and cost](./embedding-user-query-latency-and-cost.md)).

Build a **golden dataset** of user-style questions with labeled relevant chunk IDs; re-run after embedding model, chunker, or rewrite changes ([migration guide](./embedding-migration-ingestion-using-another-model.md)).

## See also

- [Embedding tools decision-based — RAG evaluation](./embedding-tools-decision-based.md)
- [Embedding bad practices — benchmarks alone](./embedding-bad-practices.md)
- [Embedding overview](./README.md)
