# Retrieval reranker evaluation and fine-tuning

Evaluate a reranker on labeled query-document pairs before deciding whether to fine-tune a pretrained cross-encoder. The goal is to improve ordering of the candidate set while keeping latency and serving cost within budget.

## Build a golden dataset

Create representative queries and candidate documents from the real corpus. Label each query-document pair for relevance; graded labels (for example, 0 = irrelevant, 1 = partial, 2 = useful, 3 = directly answers) preserve more signal than a binary label. Record the annotation rubric and resolve disagreements on important examples.

Split by query, and where possible by source or time, so near-duplicate passages do not leak between training and evaluation. Keep a fixed held-out set for comparisons.

## Establish a baseline

For each query, save the initial BM25, vector, or hybrid candidate list and evaluate it before reranking. Then run the same candidate list through the pretrained reranker. Compare ranking quality using:

| Metric | What it tells you |
|--------|-------------------|
| **Recall@K** | Whether a relevant document entered the candidate set at all; reranking cannot recover missing candidates. |
| **MRR@K** | How early the first relevant result appears. |
| **nDCG@K** | Whether graded-relevance documents are ordered well across the top K. |

Also record p50/p95 latency, throughput at target concurrency, memory or accelerator use, and cost per query. Measure the full request path and the reranker stage separately.

## Fine-tune with hard negatives

If the pretrained model misses important cases, build training examples from labeled positives and hard negatives: plausible candidates retrieved by BM25, vector search, or the current hybrid pipeline but judged irrelevant or less relevant. Random negatives alone are usually too easy to teach fine distinctions.

Fine-tune a pretrained cross-encoder on query-document pairs with binary or graded relevance targets, using a ranking or classification loss supported by the training setup. Keep query groups intact when batching/listwise training requires comparisons among candidates. Mine negatives from the current retrieval stack, then refresh them as that stack changes.

## Compare and ship

| Check | Decision |
|-------|----------|
| Held-out ranking metrics improve | Confirm lift on important query slices, not only the aggregate. |
| Candidate recall is adequate | Fix retrieval/fusion if relevant documents are absent before tuning the reranker. |
| Latency and cost fit the SLO | Test realistic candidate counts and concurrency; cap reranking K if needed. |
| Baseline remains reproducible | Version data, labels, candidate generation, model, and evaluation configuration. |

Promote only when quality gains justify added latency and cost. Keep the previous model available for rollback, and monitor online latency and sampled relevance after rollout.

## See also

- [Retrieval strategy — reranking](./retrieval-strategy-reranking.md)
- [Hybrid search (vector + keyword)](./retrieval-strategy-hybrid-search-vector-plus-keyword.md)
- [Evaluate retrieval independently](../../observability-evaluation/evaluate-retrieval-independently-metrics.md)
- [Pipeline scoring metrics](../../deployment/pipeline-scoring-metrics.md)
