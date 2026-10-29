# Poor retrieval scores

Decision flow after [independent retrieval metrics](./evaluate-retrieval-independently-metrics.md) on a golden set ([architecture evaluation — layers](../retrieval/search/retrieval-architecture-evaluation.md)).

```
Run retrieval evaluation
          |
          v
Recall@K / nDCG@K acceptable?
          |
       +--+--+
       |     |
      No    Yes
       |     |
       v     v
Check query  Evaluate context
rewriting,   assembly and generation
chunking,
embeddings,
filters, and
reranking
```

**No** — query rewriting ([context scoring](../contexting/context-scoring-math.md)), chunking ([chunking metrics](../retrieval/chunking/chunking-metrics-observability.md)), embeddings ([query evaluation](../retrieval/embedding/queries/embedding-user-query-evaluation.md)), filters ([metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md)), reranking ([strategy](../retrieval/search/retrieval-strategy-reranking.md)), index ([storage observability](../retrieval/storaging/storage-observability.md)).

**Yes** — [evaluate answer metrics](./evaluate-answer-metrics.md), [context assembly](../contexting/context-assembly-flow.md), [evaluate assembling](../contexting/context-evaluate-assembling.md), [prompting](../prompting/prompt-implementation-flow.md), [output validation](../output/output-implementation-flow.md).


## Reference implementation

**[observability-strategies](https://github.com/CaioHAndradeLima/observability-strategies)** — `poor_retrieval.next_fix_branch` and `evaluate-scenarios` (`poor_retrieval_scores`, `scenarios.poor_retrieval`).

## See also

- [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md)
- [Observability & evaluation overview](./README.md)
