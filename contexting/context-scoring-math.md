# Context scoring math

**Score and select evidence** during context assembly ([context algorithm — step 4](./context-algorithm.md)). Initial retrieval similarity is useful but should not be the only selection criterion.

A candidate may have:

- High semantic similarity but little factual relevance.
- Lower similarity but contain a critical exact identifier.
- The same information as several other candidates.
- Strong relevance but outdated content.

Combine several signals:

\[
S(d) = w_r R(d) + w_f F(d) + w_a A(d) + w_t T(d)
\]

Where:

- \(R(d)\) = relevance score.
- \(F(d)\) = freshness score.
- \(A(d)\) = source authority or reliability score.
- \(T(d)\) = task-specific relevance, such as containing the requested entity or date.
- \(w_r, w_f, w_a, w_t\) = weights calibrated to the application.

## Mapping signals to practice

| Signal | Typical inputs |
|--------|----------------|
| \(R(d)\) | Vector/BM25/reranker score, normalized per query ([similarity strategy](../retrieval/search/retrieval-strategy-similarity.md)) |
| \(F(d)\) | `updated_at`, index freshness, document version metadata ([storage observability — index freshness](../retrieval/storaging/storage-observability.md)) |
| \(A(d)\) | Source tier (policy wiki vs draft), trust labels, corpus priority |
| \(T(d)\) | Regex/entity match on SKU, error code, date range; hybrid lexical hits ([hybrid search](../retrieval/search/retrieval-strategy-hybrid-search-vector-plus-keyword.md)) |

Calibrate weights on a **golden set**—do not copy defaults from another product. After scoring, apply **diversity and token budget** in steps 5–6 of the [context algorithm](./context-algorithm.md).

Duplicate candidates often share high \(R(d)\) but should lose after dedupe (step 2) or diversity rules (step 5).

## Contextual query resolution (before retrieval)

The second question is ambiguous without history. A retrieval system may not know what “it” refers to.

The application can use **conversation history** to resolve the reference and create a standalone retrieval query:

**Original question:**

"Did we fix it?"

**Resolved retrieval query:**

"Was the checkout API incident that caused the 12% conversion drop resolved? What mitigation was applied and when?"

This is often called **query rewriting** or **contextual query resolution**. It usually happens **before** retrieval, although the relevant conversation history is also useful during [context assembly](./context-assembly-flow.md) ([context info — conversation history](./context-info-for-output.md)).

Deeper patterns: [embedding — cleaning user query](../retrieval/embedding/queries/embedding-cleaning-user-query.md).

## See also

- [Context info for output](./context-info-for-output.md)
- [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md)
- [Contexting overview](./README.md)
