# Contexting

What happens **after retrieval** and **around the LLM call**: assemble evidence into a prompt, enforce context limits, citations, grounding, and safe fallbacks when evidence is thin.

Contexting follows [retrieval/search](../retrieval/search/) (candidate passages) and complements [retrieval/compacting](../retrieval/compacting/) (shrink/dedupe retrieved text). Guard-rails for output and tenancy still apply ([guard-rails](../guard-rails/)).

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Context assembly** | Order chunks, metadata, system vs user messages |
| **Token budget** | Window limits, truncation vs summarize |
| **Citations & grounding** | Require evidence-linked answers; cite chunk/source IDs |
| **Prompt structure** | Instructions, few-shot, tool results in context |
| **Insufficient evidence** | Abstain, clarify, degraded answers ([search similarity](../retrieval/search/retrieval-strategy-similarity.md)) |
| **Multi-turn context** | History, compaction of chat, retrieval in threads |
| **Evaluation** | Groundedness, faithfulness, context relevance |

---

## Guides

_Guides will be listed here as you add markdown files in this folder (same pattern as [retrieval/search](../retrieval/search/README.md))._

## Related

- [Retrieval flow](../retrieval/retrieval-flow.md) · [Retrieval strategies combined](../retrieval/search/retrieval-strategies-combined.md)
- [Compacting](../retrieval/compacting/)
- [Embedding user context compact flow](../retrieval/embedding/queries/embedding-user-context-compact-flow.md)
- [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md)

## See also

- [Repository overview](../README.md)
