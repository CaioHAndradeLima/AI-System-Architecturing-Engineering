# Retrieval strategy — hybrid search (vector + keyword)

**Hybrid retrieval** runs **dense vector search** and **keyword search** in parallel, then **merges or fuses** candidates before optional reranking and context assembly ([retrieval flow](../retrieval-flow.md)).

```
                    User query
                        |
              +---------+---------+
              |                   |
              v                   v
        Dense vector search   Keyword search
              |                   |
              v                   v
        Semantic matches      BM25 matches
              |                   |
              +---------+---------+
                        |
                        v
                  Merge / fuse
                   candidates
                        |
                        v
                   Optional
                   reranking
                        |
                        v
                 Final evidence
```

## When hybrid helps

| Signal | Vector search | Keyword (e.g. BM25) |
|--------|---------------|------------------------|
| Paraphrases, concepts | Strong | Weaker |
| Exact IDs, SKUs, names, acronyms | Can miss | Strong |
| Rare tokens in long docs | Depends on chunking | Often strong |

### Query types

| Query type | Why hybrid search can help |
|------------|------------------------------|
| **Natural-language questions** | Vector search captures semantic similarity |
| **Exact error codes** | Keyword search catches literal matches |
| **Product names and SKUs** | Exact terms matter |
| **Legal citations** | Specific identifiers are important |
| **Technical documentation** | Function names and parameter names need exact matching |
| **Mixed natural-language and identifiers** | Both semantic and lexical signals matter |

Use hybrid when eval shows **vector-only** misses lexical matches or **keyword-only** misses semantic paraphrases—validate on your corpus, not by default.

## Fusion (starting options)

| Approach | Idea |
|----------|------|
| **Reciprocal rank fusion (RRF)** | Combine ranked lists without calibrating scores to the same scale |
| **Weighted score fusion** | Normalize dense and sparse scores; needs tuning per index |
| **Separate top-K then union** | Simple; dedupe by chunk ID before rerank |

Apply the same **metadata filters** on both branches ([metadata filtering](./retrieval-strategy-metadata-filtering.md)). Tune per-branch K so fusion still has enough candidates after dedupe ([top-K](./retrieval-strategy-top-k.md)).

## After fusion

- **Reranking** (cross-encoder or LLM) on the merged set often pays off when lists overlap poorly.
- **Thresholds** on fused scores are harder to calibrate than single-channel search ([similarity strategy](./retrieval-strategy-similarity.md))—use golden-set regression when you change fusion weights.

## See also

- [Retrieval flow](../retrieval-flow.md)
- [Storage strategy](../storaging/storage-strategy.md)
- [Search overview](./README.md)
