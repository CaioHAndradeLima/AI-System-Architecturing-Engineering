# Poor retrieval scores

When **offline retrieval metrics** look bad, decide whether the problem is still in search/ranking or downstream in context and generation ([architecture evaluation — layers](../retrieval/search/retrieval-architecture-evaluation.md)).

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

## If metrics are not acceptable

Tune the retrieval stack on a **golden qrels set** before changing prompts or models ([independent retrieval metrics](./evaluate-retrieval-independently-metrics.md)).

| Area | What to inspect |
|------|-----------------|
| **Query rewriting** | Contextual query resolution, typos, language mismatch ([context scoring — rewriting](../contexting/context-scoring-math.md)) |
| **Chunking** | Size, overlap, structure ([chunking metrics](../retrieval/chunking/chunking-metrics-observability.md) · [ingestion procedures](../retrieval/ingestion/ingestion-procedures.md)) |
| **Embeddings** | Model choice, domain fit, query vs document encoding ([embedding query evaluation](../retrieval/embedding/queries/embedding-user-query-evaluation.md)) |
| **Filters** | Over-strict metadata, tenant ACL, empty-result rate ([metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md)) |
| **Reranking** | Fusion, top-K, hybrid vs vector-only ([reranking](../retrieval/search/retrieval-strategy-reranking.md) · [top-K](../retrieval/search/retrieval-strategy-top-k.md)) |

Also check index health and **empty-result rate** ([storage observability](../retrieval/storaging/storage-observability.md)).

## If metrics are acceptable

Retrieval is finding relevant evidence; poor answers usually sit in **assembly**, **prompting**, or **generation**.

| Area | Docs |
|------|------|
| Context assembly | [Assembly flow](../contexting/context-assembly-flow.md) · [Algorithm](../contexting/context-algorithm.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| Prompting & grounding | [Standard format](../prompting/prompt-standard-format.md) · [Prompt implementation flow](../prompting/prompt-implementation-flow.md) |
| Output validation | [Output implementation flow](../output/output-implementation-flow.md) · [Citation validation](../output/output-citation-validation.md) |

Re-run end-to-end eval only after retrieval scores meet your gate ([retrieval implementation flow](../retrieval/search/retrieval-implementation-flow.md)).

## See also

- [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md)
- [Observability & evaluation overview](./README.md)
