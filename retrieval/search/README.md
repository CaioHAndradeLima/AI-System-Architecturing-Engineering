# Search

**Query-time retrieval**: turn a user question (and optional context) into ranked evidence from indexes and metadata—before [compacting](../compacting/) and [contexting](../../contexting/) shape what the LLM sees.

Search sits after [embedding queries](../embedding/queries/) (query vectors and rewrite) and [storaging](../storaging/) (indexes, filters, freshness). Authorization and tenant scope belong on every path ([guard-rails tenant-scoped retrieval](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)).

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Dense retrieval** | Vector similarity, top-K, score thresholds, dimension/index params |
| **Sparse retrieval** | BM25, keyword indexes, lexical recall |
| **Hybrid search** | Combining dense + sparse, fusion (RRF, weighted), when hybrid pays off |
| **Metadata filters** | Tenant, ACL, document type, time range—validated at query time |
| **Reranking** | Cross-encoder or LLM rerank, MMR, dedupe before compacting |
| **Query planning** | Multi-query, HyDE, step-back, routing by intent or corpus |
| **Result shaping** | Parent-child fetch, chunk expansion, max tokens per source |
| **Quality & eval** | Recall@K, MRR, nDCG, filtered-search regressions ([storage observability](../storaging/storage-observability.md)) |

---

## Guides

### [retrieval-strategies-combined.md](./retrieval-strategies-combined.md)

`#flow` · `#rag` · `#pipeline`

Single query-time pipeline that stitches together optional rewrite, embedding, auth filters, dense and/or keyword retrieval, merge, rerank, evidence rules, and context for the LLM.

Each optional stage has a dedicated guide when you need depth.

→ [See more in retrieval-strategies-combined.md](./retrieval-strategies-combined.md)

### [../retrieval-flow.md](../retrieval-flow.md)

`#flow` · `#rag` · `#hybrid`

End-to-end RAG retrieval path: offline indexing, query-time search (vector + metadata + keyword), optional reranking, context assembly, and generation.

Tenant and ACL filters belong on the retrieval engine branch, not only at the LLM (tenant-scoped retrieval).

→ [See more in retrieval-flow.md](../retrieval-flow.md)

### [retrieval-strategy-top-k.md](./retrieval-strategy-top-k.md)

`#dense` · `#top-k` · `#recall`

K is the number of candidate results you request from the retrieval system (vector search, hybrid fusion, or post-filter pipeline).

→ [See more in retrieval-strategy-top-k.md](./retrieval-strategy-top-k.md)

### [retrieval-strategy-similarity.md](./retrieval-strategy-similarity.md)

`#dense` · `#threshold` · `#abstain`

How similarity scores from vector (or hybrid) search combine with top-K and thresholds to decide what counts as evidence—and when to abstain instead of hallucinating.

→ [See more in retrieval-strategy-similarity.md](./retrieval-strategy-similarity.md)

### [retrieval-strategy-metadata-filtering.md](./retrieval-strategy-metadata-filtering.md)

`#metadata` · `#multi-tenant` · `#acl`

Metadata filters restrict search to vectors the caller is allowed to see—before or during vector/keyword retrieval, not after the LLM assembles context.

Example query: *“What is our vacation policy?”*

→ [See more in retrieval-strategy-metadata-filtering.md](./retrieval-strategy-metadata-filtering.md)

### [retrieval-strategy-hybrid-search-vector-plus-keyword.md](./retrieval-strategy-hybrid-search-vector-plus-keyword.md)

`#hybrid` · `#bm25` · `#dense` · `#rrf`

Hybrid retrieval runs dense vector search and keyword search in parallel, then merges or fuses candidates before optional reranking and context assembly (retrieval flow).

→ [See more in retrieval-strategy-hybrid-search-vector-plus-keyword.md](./retrieval-strategy-hybrid-search-vector-plus-keyword.md)

### [retrieval-strategy-reranking.md](./retrieval-strategy-reranking.md)

`#rerank` · `#cross-encoder` · `#latency`

A vector database (or hybrid index) can quickly find a set of candidate passages.

A reranker then examines the query and each candidate together to estimate how relevant each passage is to that specific query—before compacting and the LLM (retrieval flow).

→ [See more in retrieval-strategy-reranking.md](./retrieval-strategy-reranking.md)

### [retrieval-reranker-evaluation-and-fine-tuning.md](./retrieval-reranker-evaluation-and-fine-tuning.md)

`#cross-encoder` · `#golden-set` · `#hard-negatives` · `#latency`

Build query-document relevance labels, compare a pretrained cross-encoder against the retrieval baseline, fine-tune with hard negatives when needed, and gate on ranking quality, latency, and cost.

→ [See more in retrieval-reranker-evaluation-and-fine-tuning.md](./retrieval-reranker-evaluation-and-fine-tuning.md)

### [retrieval-decision-based.md](./retrieval-decision-based.md)

`#decision-guide` · `#startup` · `#enterprise` · `#slo`

How query-time retrieval choices evolve from startup/MVP through medium SaaS to enterprise—method, K, thresholds, filters, rerank, hybrid, index tuning, fallback, eval, and scaling.

→ [See more in retrieval-decision-based.md](./retrieval-decision-based.md)

### [retrieval-metrics-observability.md](./retrieval-metrics-observability.md)

`#metrics` · `#recall` · `#rerank` · `#abstain`

Metrics for query-time retrieval and RAG quality—ranking, rerank lift, latency, filters, context size, answers, and abstention.

Complements storage observability (index/store signals) and chunking metrics (ingestion-side).

For retrieval-only golden-set metrics and when to use each, see evaluate retrieval independently — metrics.

→ [See more in retrieval-metrics-observability.md](./retrieval-metrics-observability.md)

### [retrieval-implementation-flow.md](./retrieval-implementation-flow.md)

`#checklist` · `#implementation` · `#eval`

Eight-step rollout from dense search through hybrid, rerank, observability, and deploy loop.

→ [See more in retrieval-implementation-flow.md](./retrieval-implementation-flow.md)

### [retrieval-architecture-supervisor-as-service.md](./retrieval-architecture-supervisor-as-service.md)

`#agents` · `#supervisor` · `#tool`

The main or supervisor agent does not embed vector search inline—it calls a retrieval tool (or service) that runs the full query-time pipeline and returns relevant evidence for answer generation.

→ [See more in retrieval-architecture-supervisor-as-service.md](./retrieval-architecture-supervisor-as-service.md)

### [retrieval-architecture-supervisor-as-agent.md](./retrieval-architecture-supervisor-as-agent.md)

`#agents` · `#supervisor` · `#retrieval-agent`

The supervisor delegates to a Retrieval Agent—an LLM-driven specialist that chooses sources, rewrites queries, picks strategies, searches, judges evidence, and may retry or broaden search before returning results upstream.

→ [See more in retrieval-architecture-supervisor-as-agent.md](./retrieval-architecture-supervisor-as-agent.md)

### [retrieval-architecture-multi-agent.md](./retrieval-architecture-multi-agent.md)

`#agents` · `#supervisor` · `#parallel`

A supervisor fans out to domain agents (each with its own tools), then aggregates branch results before the final user answer.

Retrieval (RAG / search) is one branch—not the only path to evidence.

→ [See more in retrieval-architecture-multi-agent.md](./retrieval-architecture-multi-agent.md)

### [retrieval-architecture-decision.md](./retrieval-architecture-decision.md)

`#decision-guide` · `#agents` · `#tool`

Pick how retrieval is wired into agents by requirement—not by defaulting to an LLM for every search.

→ [See more in retrieval-architecture-decision.md](./retrieval-architecture-decision.md)

### [retrieval-architecture-simple-loop.md](./retrieval-architecture-simple-loop.md)

`#agents` · `#router` · `#rag` · `#sql`

A lightweight multi-branch loop: supervisor routes to a small set of specialists (here Analytics and Knowledge), each uses one primary tool, then the supervisor merges findings and checks evidence sufficiency before the final response.

→ [See more in retrieval-architecture-simple-loop.md](./retrieval-architecture-simple-loop.md)

### [retrieval-architecture-evaluation.md](./retrieval-architecture-evaluation.md)

`#eval` · `#agents` · `#security`

What to measure by layer when retrieval is exposed as a service, agent, or multi-agent workflow—not only end-to-end answer quality.

→ [See more in retrieval-architecture-evaluation.md](./retrieval-architecture-evaluation.md)

### [retrieval-cloud-tools.md](./retrieval-cloud-tools.md)

`#cloud` · `#aws` · `#azure` · `#gcp`

Maps retrieval and agent-stack responsibilities to representative services on AWS, Azure, and Google Cloud.

Use with retrieval architecture decision (service vs agent vs multi-agent) and architecture evaluation (what to monitor per layer).

→ [See more in retrieval-cloud-tools.md](./retrieval-cloud-tools.md)

### [retrieval-aws-multi-agent-sample.md](./retrieval-aws-multi-agent-sample.md)

`#aws` · `#sample` · `#langgraph` · `#opensearch`

Reference AWS layout for a supervisor-style app: authenticated API → LangGraph on ECS/Fargate → domain agents → retrieval service and data tools, with an S3-driven ingestion path into Bedrock embeddings and OpenSearch.

Pair with retrieval cloud tools and multi-agent retrieval architecture.

→ [See more in retrieval-aws-multi-agent-sample.md](./retrieval-aws-multi-agent-sample.md)

## Runnable code lab

**[reranking-strategies](https://github.com/CaioHAndradeLima/reranking-strategies)** measures BM25, dense/hybrid, and reranking pipelines on a demo corpus. After reranking, see **[contexting-strategies](https://github.com/CaioHAndradeLima/contexting-strategies)** for prompt assembly under token budgets ([contexting](../../contexting/README.md)).

## Related

- [Embedding user query flow](../embedding/queries/embedding-user-query-flow.md)
- [Compact architecture flow](../compacting/compact-architecture-flow.md)
- [Storage strategy](../storaging/storage-strategy.md) · [HNSW flow](../storaging/hnsw-flow.md)
- [Retrieval architecturing decision-based — Retrieval row](../retrieval-architecturing-decision-based.md)
- [Wrong architecture: shared retrieval](../../guard-rails/wrong-architecture-shared-retrieval.md)

## See also

- [Retrieval overview](../README.md)
