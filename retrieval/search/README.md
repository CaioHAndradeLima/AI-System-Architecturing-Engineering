# Search

**Query-time retrieval**: turn a user question (and optional context) into ranked evidence from indexes and metadata—before [compacting](../compacting/) sends context to the LLM.

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

Full query-time stack: rewrite, embed, auth, dense/hybrid, merge, rerank, evidence rules, context, LLM.

→ [See more in retrieval-strategies-combined.md](./retrieval-strategies-combined.md)

### [../retrieval-flow.md](../retrieval-flow.md)

`#flow` · `#rag` · `#hybrid`

Full pipeline diagram: ingestion → storage → query embed → retrieval engine → rerank → context → LLM.

→ [See more in retrieval-flow.md](../retrieval-flow.md)

### [retrieval-strategy-top-k.md](./retrieval-strategy-top-k.md)

`#dense` · `#top-k` · `#recall`

What K means, example values, and how K relates to context assembly and eval.

→ [See more in retrieval-strategy-top-k.md](./retrieval-strategy-top-k.md)

### [retrieval-strategy-similarity.md](./retrieval-strategy-similarity.md)

`#dense` · `#threshold` · `#abstain`

Top-K vs threshold vs both; score filter flow and when to abstain or clarify.

→ [See more in retrieval-strategy-similarity.md](./retrieval-strategy-similarity.md)

### [retrieval-strategy-metadata-filtering.md](./retrieval-strategy-metadata-filtering.md)

`#metadata` · `#multi-tenant` · `#acl`

Trusted tenant identity → access restrictions → search eligible vectors only.

→ [See more in retrieval-strategy-metadata-filtering.md](./retrieval-strategy-metadata-filtering.md)

### [retrieval-strategy-hybrid-search-vector-plus-keyword.md](./retrieval-strategy-hybrid-search-vector-plus-keyword.md)

`#hybrid` · `#bm25` · `#dense` · `#rrf`

Parallel vector and keyword paths, merge/fuse, optional rerank to final evidence.

→ [See more in retrieval-strategy-hybrid-search-vector-plus-keyword.md](./retrieval-strategy-hybrid-search-vector-plus-keyword.md)

### [retrieval-strategy-reranking.md](./retrieval-strategy-reranking.md)

`#rerank` · `#cross-encoder` · `#latency`

Wide initial retrieval, query+passage rerank, narrow final evidence for the LLM.

→ [See more in retrieval-strategy-reranking.md](./retrieval-strategy-reranking.md)

### [retrieval-decision-based.md](./retrieval-decision-based.md)

`#decision-guide` · `#startup` · `#enterprise` · `#slo`

Retrieval method, K, thresholds, filters, rerank, hybrid, index, fallback, eval, and scaling by maturity.

→ [See more in retrieval-decision-based.md](./retrieval-decision-based.md)

### [retrieval-metrics-observability.md](./retrieval-metrics-observability.md)

`#metrics` · `#recall` · `#rerank` · `#abstain`

Recall@K, MRR, nDCG, rerank lift, no-result rate, filter failures, context tokens, answer correctness.

→ [See more in retrieval-metrics-observability.md](./retrieval-metrics-observability.md)

### [retrieval-implementation-flow.md](./retrieval-implementation-flow.md)

`#checklist` · `#implementation` · `#eval`

Eight-step rollout from dense search through hybrid, rerank, observability, and deploy loop.

→ [See more in retrieval-implementation-flow.md](./retrieval-implementation-flow.md)

### [retrieval-architecture-supervisor-as-service.md](./retrieval-architecture-supervisor-as-service.md)

`#agents` · `#supervisor` · `#tool`

Supervisor calls retrieval tool (embed, search, filters, rerank) then main agent answers.

→ [See more in retrieval-architecture-supervisor-as-service.md](./retrieval-architecture-supervisor-as-service.md)

### [retrieval-architecture-supervisor-as-agent.md](./retrieval-architecture-supervisor-as-agent.md)

`#agents` · `#supervisor` · `#retrieval-agent`

Retrieval agent selects sources, rewrites, strategizes, evaluates, retries; returns evidence to supervisor.

→ [See more in retrieval-architecture-supervisor-as-agent.md](./retrieval-architecture-supervisor-as-agent.md)

### [retrieval-architecture-multi-agent.md](./retrieval-architecture-multi-agent.md)

`#agents` · `#supervisor` · `#parallel`

Supervisor → Knowledge / Data / Engineering agents → tools → merge → final answer.

→ [See more in retrieval-architecture-multi-agent.md](./retrieval-architecture-multi-agent.md)

### [retrieval-architecture-decision.md](./retrieval-architecture-decision.md)

`#decision-guide` · `#agents` · `#tool`

Requirement → service, multi-backend tool, routing, retrieval agent, or multi-agent.

→ [See more in retrieval-architecture-decision.md](./retrieval-architecture-decision.md)

### [retrieval-architecture-simple-loop.md](./retrieval-architecture-simple-loop.md)

`#agents` · `#router` · `#rag` · `#sql`

Two-branch supervisor loop: analytics + knowledge tools, merge, evidence sufficiency, response.

→ [See more in retrieval-architecture-simple-loop.md](./retrieval-architecture-simple-loop.md)

## Related

- [Embedding user query flow](../embedding/queries/embedding-user-query-flow.md)
- [Compact architecture flow](../compacting/compact-architecture-flow.md)
- [Storage strategy](../storaging/storage-strategy.md) · [HNSW flow](../storaging/hnsw-flow.md)
- [Retrieval architecturing decision-based — Retrieval row](../retrieval-architecturing-decision-based.md)
- [Wrong architecture: shared retrieval](../../guard-rails/wrong-architecture-shared-retrieval.md)

## See also

- [Retrieval overview](../README.md)
