# Retrieval strategies — combined

Single **query-time pipeline** that stitches together optional rewrite, embedding, auth filters, dense and/or keyword retrieval, merge, rerank, evidence rules, and context for the LLM. Each optional stage has a dedicated guide when you need depth.

```
  User question
       |
       v
  Query normalization / rewriting (optional)
       |
       v
  Query embedding
       |
       v
  Apply tenant + authorization constraints
       |
       v
  Retrieve candidate passages
       |
       +---- Dense vector search
       |
       +---- BM25 keyword search (optional)
       |
       v
  Merge candidates (optional)
       |
       v
  Rerank (optional)
       |
       v
  Apply relevance / evidence rules
       |
       v
  Select final context
       |
       v
  LLM generates answer
```

## Stage → guide

| Stage | Doc |
|-------|-----|
| Query normalization / rewriting | [Embedding — cleaning user query](../embedding/queries/embedding-cleaning-user-query.md) |
| Query embedding | [Embedding user query flow](../embedding/queries/embedding-user-query-flow.md) |
| Tenant + authorization | [Metadata filtering](./retrieval-strategy-metadata-filtering.md) |
| Dense vector search | [Top-K](./retrieval-strategy-top-k.md) · [Similarity scores / threshold](./retrieval-strategy-similarity.md) |
| BM25 + merge | [Hybrid search (vector + keyword)](./retrieval-strategy-hybrid-search-vector-plus-keyword.md) |
| Rerank | [Reranking](./retrieval-strategy-reranking.md) |
| Relevance / evidence rules | [Similarity — abstain path](./retrieval-strategy-similarity.md) |
| Select final context | [Compacting](../compacting/) · [Compact architecture flow](../compacting/compact-architecture-flow.md) |
| End-to-end picture | [Retrieval flow](../retrieval-flow.md) |

## Minimal vs full stack

| Profile | Typical path |
|---------|----------------|
| **MVP** | Embed → tenant filter → dense top-K → context → LLM ([minimum ingestion MVP](../ingestion/minimum-ingestion-mvp.md)) |
| **SaaS** | + rewrite as needed, hybrid when eval shows lexical gaps, rerank when precision@K is weak |
| **Enterprise** | All enforced filters, hybrid + rerank where justified, evidence thresholds, eval gates ([retrieval architecturing decision-based](../retrieval-architecturing-decision-based.md)) |

Skip optional branches until metrics or golden-set eval justify the latency and ops cost ([storage observability](../storaging/storage-observability.md)).

## See also

- [Search overview](./README.md)
