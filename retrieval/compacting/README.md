# Compacting

Shrink or prioritize **retrieved context** so it fits model limits and stays useful: dedupe overlapping chunks, rank by relevance, truncate, summarize, or structure citations before the LLM call.

Compacting sits **after** vector search and **before** generation—downstream of [embedding queries](../embedding/queries/) and top-K assembly in [user query flow](../embedding/queries/embedding-user-query-flow.md).

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Selection** | Which chunks to keep when over token budget |
| **Deduping** | Overlap from chunking, multi-query, parent-child |
| **Ordering** | Relevance, recency, citation structure |
| **Summarization** | Compress long passages vs drop low-score hits |
| **Structured context** | JSON/markdown blocks for models and citations |
| **Evaluation** | Answer quality vs context size and latency |

---

## Guides

### [compact-decision-based.md](./compact-decision-based.md)

`#decision-guide` · `#storage` · `#hybrid`

Message/chat use cases: DB vs vector vs hybrid vs pgvector/Chroma for prototypes.

→ [See more in compact-decision-based.md](./compact-decision-based.md)

## Related

- [Embedding — user context compact flow](../embedding/queries/embedding-user-context-compact-flow.md) — rewrite query using chat history (before retrieve)
- [Chunking — hierarchical parent-child](../chunking/chunking-hierarchical-parent-child.md) — parent expansion after child hit
- [Ingestion observability — context relevance](../ingestion/ingestion-observability.md) · [Chunking metrics](../chunking/chunking-metrics-observability.md)
