# Retrieval strategy — reranking

A **vector database** (or hybrid index) can quickly find a set of **candidate passages**. A **reranker** then examines the query and each candidate together to estimate how relevant each passage is to that specific query—before [compacting](../compacting/) and the LLM ([retrieval flow](../retrieval-flow.md)).

Typical pattern: retrieve a **larger K** (e.g. 20), rerank, then keep **3–5** for context.

```
  Query
    |
    v
  Initial retrieval: Top 20 candidates
    |
    v
  Reranker evaluates query + each passage
    |
    v
  Reorder candidates by relevance
    |
    v
  Select final 3–5 passages
    |
    v
  Send context to the LLM
```

## Approach comparison

| Approach | Advantages | Trade-offs |
|----------|------------|------------|
| **Vector ranking only** | Simple and usually fast | May rank related but non-answering passages highly |
| **Vector retrieval + reranker** | Can improve relevance and evidence selection | Adds compute, latency and sometimes API cost |
| **Hybrid retrieval + reranker** | Can combine exact matches and semantic relevance | More components to tune and monitor |

## Practice notes

- Rerank **after** [metadata filtering](./retrieval-strategy-metadata-filtering.md)—do not rerank passages the user must not see.
- Initial K and final count link to [top-K](./retrieval-strategy-top-k.md) and token limits in [embedding user query flow](../embedding/queries/embedding-user-query-flow.md).
- **Hybrid + reranker** follows [hybrid search (vector + keyword)](./retrieval-strategy-hybrid-search-vector-plus-keyword.md) fusion, then rerank the merged list.
- Measure latency p95 and **Precision@K** / answer quality when enabling reranking ([storage observability](../storaging/storage-observability.md), [query evaluation](../embedding/queries/embedding-user-query-evaluation.md)).

Common reranker types: cross-encoder models (query+passage joint scoring), lightweight LLM judges, or provider rerank APIs—pick based on latency budget and eval lift.

## See also

- [reranking-strategies](https://github.com/CaioHAndradeLima/reranking-strategies) — hybrid retrieval and reranker comparison lab (`rerank-lab evaluate`)
- [Retrieval strategy — similarity scores](./retrieval-strategy-similarity.md)
- [Search overview](./README.md)
