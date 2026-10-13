# User query embedding

**Online path**: preprocess the question, embed the query, search, assemble context—aligned with the same model as document vectors ([parent embedding](../README.md)).

---

## Guides

### [embedding-user-query-flow.md](./embedding-user-query-flow.md)

`#flow` · `#offline-online` · `#rag`

How document vectors (offline) and query vectors (online) meet at similarity search—the core RAG embedding path.

Index and query must use the same embedding model and encoding rules (migration guide, bad practices — model mix).

→ [See more in embedding-user-query-flow.md](./embedding-user-query-flow.md)

### [embedding-cleaning-user-query.md](./embedding-cleaning-user-query.md)

`#query` · `#preprocessing` · `#retrieval`

Query preprocessing techniques before query embedding—normalize, detect language, rewrite, expand, or decompose the user question.

→ [See more in embedding-cleaning-user-query.md](./embedding-cleaning-user-query.md)

### [embedding-user-context-compact-flow.md](./embedding-user-context-compact-flow.md)

`#conversation` · `#query-rewrite` · `#context`

When the latest user message is ambiguous alone, use authorized conversation history to rewrite the question before embed and retrieve—without leaking other users’ or tenants’ context.

→ [See more in embedding-user-context-compact-flow.md](./embedding-user-context-compact-flow.md)

### [embedding-user-query-latency-and-cost.md](./embedding-user-query-latency-and-cost.md)

`#latency` · `#cost` · `#production`

Online query path maturity: embedding API usage, latency SLOs, caching, reliability, rewriting, and observability—startup vs production/enterprise.

→ [See more in embedding-user-query-latency-and-cost.md](./embedding-user-query-latency-and-cost.md)

### [embedding-user-query-evaluation.md](./embedding-user-query-evaluation.md)

`#evaluation` · `#recall` · `#ndcg`

Metrics to judge whether query encoding and retrieval work on real questions—not just whether the embed API returns 200.

→ [See more in embedding-user-query-evaluation.md](./embedding-user-query-evaluation.md)
