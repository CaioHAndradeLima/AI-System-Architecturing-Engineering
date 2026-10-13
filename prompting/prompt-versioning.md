# Prompt versioning

Ship **prompt changes** like code: golden-set eval, baseline comparison, canary, then full promotion. Unified prompt/model/retrieval gate: [regression and canary releases](../observability-evaluation/regression-and-canary-releases.md).

```
Prompt v1
   |
   v
Run golden dataset
   |
   v
Measure quality, latency, and cost
   |
   v
Compare with baseline
   |
   +---- Regression? ---- Yes ---> Reject / rollback
   |
   No
   |
   v
Canary release
   |
   v
Monitor production
   |
   v
Promote to full traffic
```

## Record per version

For each version, record:

- Prompt template and version identifier.
- Model name and configuration ([generation parameters](./prompt-relevant-variables-influences.md)).
- Retrieval configuration and relevant context settings.
- Evaluation dataset version.
- Answer quality, groundedness, latency, and token cost.
- Any observed failure categories.

## What to tie together

| Artifact | Why |
|----------|-----|
| **Prompt + model** | Quality shifts when either changes ([embedding migration](../retrieval/embedding/embedding-migration-ingestion-using-another-model.md) affects RAG too) |
| **Retrieval + context settings** | Top-K, thresholds, assembly policy ([retrieval decision-based](../retrieval/search/retrieval-decision-based.md), [context architecturing decision-based](../contexting/context-architecturing-decision-based.md)) |
| **Eval dataset version** | Comparable regressions ([query evaluation](../retrieval/embedding/queries/embedding-user-query-evaluation.md), [evaluate assembling](../contexting/context-evaluate-assembling.md)) |
| **Failure categories** | Abstain, hallucination, injection attempts, wrong tenant ([architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md)) |

Store prompt text in git or a versioned config store; tag releases with the eval run ID that gated promotion.

## See also

- [Prompt standard format](./prompt-standard-format.md)
- [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md)
- [Prompting overview](./README.md)
