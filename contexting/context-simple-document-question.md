# Context — simple document question

Minimal **context shape** for single-corpus policy or doc Q&A: question plus top chunks and citation fields—no multi-agent branches or structured SQL blocks ([minimum ingestion MVP](../retrieval/ingestion/minimum-ingestion-mvp.md)).

```
Question
  +
Top relevant policy chunks
  +
Source IDs / citations
  |
  v
LLM answer
```

## What to include

| Piece | Notes |
|-------|--------|
| **Question** | User text; optionally a **resolved** query if the thread is ambiguous ([contextual query resolution](./context-scoring-math.md#contextual-query-resolution-before-retrieval)) |
| **Top relevant chunks** | From dense (or hybrid) search after tenant filters ([metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md), [top-K](../retrieval/search/retrieval-strategy-top-k.md)) |
| **Source IDs / citations** | Doc ID, title, page/section—paired with each chunk ([context info — source metadata](./context-info-for-output.md)) |

Skip conversation history when turns are independent; add [conversation strategies](./context-conversation-strategies.md) when users ask follow-ups.

For scoring, dedupe, and token limits before this minimal prompt, use the full [context algorithm](./context-algorithm.md) or a subset (validate → select → render).

## See also

- [Context assembly flow](./context-assembly-flow.md)
- [Contexting overview](./README.md)
