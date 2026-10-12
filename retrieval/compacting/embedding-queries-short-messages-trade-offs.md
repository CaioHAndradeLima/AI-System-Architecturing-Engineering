# Embedding queries short messages trade-offs

Which **messages** are worth embedding for semantic search—and when to skip, enrich, or summarize—especially for chat/support corpora in [compact architecture flow](./compact-architecture-flow.md).

| Message type | Suggested approach |
|--------------|-------------------|
| **Thanks!** | Usually don't embed; little retrieval value |
| **Payment failed** | Embed if searching for similar incidents; add context if available |
| **Payment failed after updating my card** | Usually useful to embed directly |
| **Multi-message support conversation** | Consider embedding a conversation summary or meaningful message groups, while preserving individual messages |
| **Thousands of messages from one conversation** | Avoid treating every tiny message as an independent knowledge document without evaluation |

## Practical rules

- **Skip or filter** low-signal utterances (acknowledgments, “ok”, emoji-only) before embed jobs to save cost and reduce retrieval noise ([embedding metrics](../embedding/embedding-metrics.md)).
- **Short but substantive** lines often embed well; **short but vague** lines need surrounding context (previous turn, ticket metadata, product area).
- **Long threads** — index at multiple granularities: message-level for precise hits, **summary-level** for theme search; link summaries to message IDs for authorized fetch from DB.
- Evaluate on real support questions: Recall@K with and without skip rules ([user query evaluation](../embedding/queries/embedding-user-query-evaluation.md)).

## See also

- [Compact decision-based](./compact-decision-based.md)
- [Chunking semantic](../chunking/chunking-semantic.md) — topic boundaries in long prose
- [Compacting overview](./README.md)
