# User query embedding

**Online path**: preprocess the question, embed the query, search, assemble context—aligned with the same model as document vectors ([parent embedding](../README.md)).

---

## Guides

### [embedding-user-query-flow.md](./embedding-user-query-flow.md)

`#flow` · `#offline-online` · `#rag`

Document ingest embed path vs query embed, search, context assembly, and LLM—same model both sides.

→ [See more in embedding-user-query-flow.md](./embedding-user-query-flow.md)

### [embedding-cleaning-user-query.md](./embedding-cleaning-user-query.md)

`#query` · `#preprocessing` · `#retrieval`

Normalization, language detection, rewriting, expansion, multi-query, and decomposition before embedding.

→ [See more in embedding-cleaning-user-query.md](./embedding-cleaning-user-query.md)

### [embedding-user-context-compact-flow.md](./embedding-user-context-compact-flow.md)

`#conversation` · `#query-rewrite` · `#context`

Standalone vs context-dependent messages; authorized history, rewrite, then embed and retrieve.

→ [See more in embedding-user-context-compact-flow.md](./embedding-user-context-compact-flow.md)

### [embedding-user-query-latency-and-cost.md](./embedding-user-query-latency-and-cost.md)

`#latency` · `#cost` · `#production`

Query embed, p95 latency, tenant cost, safe caching, retries, rewriting, and tracing—startup vs enterprise.

→ [See more in embedding-user-query-latency-and-cost.md](./embedding-user-query-latency-and-cost.md)

### [embedding-user-query-evaluation.md](./embedding-user-query-evaluation.md)

`#evaluation` · `#recall` · `#ndcg`

Recall@K, MRR, nDCG@K, and latency/cost for judging query encoding and retrieval.

→ [See more in embedding-user-query-evaluation.md](./embedding-user-query-evaluation.md)
