# Context info for output

Five **inputs** that context assembly combines before the LLM—each with a distinct role in grounded, traceable answers ([context assembly flow](./context-assembly-flow.md)).

| Type | What it is | Role / practice |
|------|------------|-----------------|
| **Retrieved evidence** | Relevant document chunks from vector search, keyword search, databases, or APIs | Primary factual source for RAG answers |
| **Conversation history** | Earlier user and assistant messages | Interprets follow-ups; pick a strategy ([conversation strategies](./context-conversation-strategies.md)) · [user context compact flow](../retrieval/embedding/queries/embedding-user-context-compact-flow.md) |
| **Request and application context** | Current question, locale, output format, app state | Permissions enforced in **application logic**, not by trusting prompt text ([metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md)) |
| **Structured results** | SQL rows, API payloads, calculations, other agent outputs | Preserve **schema and units** so the model does not misread values ([simple loop](../retrieval/search/retrieval-architecture-simple-loop.md)) |
| **Source metadata** | Document IDs, titles, URLs, page, timestamps, version | Citations, freshness checks, traceability in **Answer + Citations** |

## Assembly order (starting point)

1. System / policy instructions (grounding rules, citation format)
2. Retrieved evidence + source metadata (paired per chunk)
3. Structured results (labeled blocks)
4. Relevant conversation history
5. Current user request and application context

Trim by **token budget** after ranking; drop low-score retrieval before dropping citation metadata on kept chunks.

## See also

- [Retrieval metrics observability — context token count](../retrieval/search/retrieval-metrics-observability.md)
- [Contexting overview](./README.md)
