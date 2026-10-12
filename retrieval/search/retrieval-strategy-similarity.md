# Retrieval strategy — similarity scores

How **similarity scores** from vector (or hybrid) search combine with **top-K** and **thresholds** to decide what counts as evidence—and when to abstain instead of hallucinating.

Pair with [retrieval strategy top-K](./retrieval-strategy-top-k.md). Score scales differ by model and index (cosine, inner product, distance); calibrate thresholds on **your** embeddings, not a generic constant.

## Strategy comparison

| Strategy | What it controls | Risk |
|----------|------------------|------|
| **Top-K only** | Number of returned candidates | Can return irrelevant results |
| **Threshold only** | Minimum score for acceptance | May return too many or too few results |
| **Top-K + threshold** | Maximum candidate count and minimum relevance | Requires evaluation and calibration |

## Top-K + threshold flow

```
  User query
      |
      v
  Retrieve top-K candidates
      |
      v
  Compare relevance scores
      |
      +---- Above threshold ----> Keep candidate
      |
      +---- Below threshold ----> Reject candidate
                                      |
                                      v
                               No useful evidence
                                      |
                                      v
                            Abstain / ask clarification
```

After filtering, remaining passages may still go through **reranking** and [compacting](../compacting/) before the LLM ([retrieval flow](../retrieval-flow.md)).

## Notes

- **Abstain / ask clarification** is preferable to forcing the model to answer with weak or empty context—align with product policy and [guard-rails](../../guard-rails/) output controls where needed.
- If every candidate is below threshold, check query rewrite, corpus coverage, and embedding model mismatch ([embedding bad practices](../embedding/embedding-bad-practices.md)) before lowering the threshold blindly.
- Track how often the “no useful evidence” branch fires; spikes often mean index freshness, filter bugs, or eval drift ([storage observability](../storaging/storage-observability.md)).

## See also

- [Retrieval strategy top-K](./retrieval-strategy-top-k.md)
- [Embedding user query evaluation](../embedding/queries/embedding-user-query-evaluation.md)
- [Search overview](./README.md)
