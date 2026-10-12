# Context assembly flow

End-to-end **RAG pipeline** with **context assembly** as the step that merges retrieved candidates with conversation history, permissions, and token budget before the prompt reaches the LLM.

```
                  RAG PIPELINE

  Documents
      |
      v
  Ingestion -> Chunking -> Embeddings -> Vector Index
                                          |
                                          v
  User Question ----------------------> Retrieval
                                          |
                                          v
                                  Retrieved Candidates
                                          |
                                          v
  Conversation History ------------> CONTEXT ASSEMBLY
  User Permissions ---------------->       |
  Token Budget -------------------->       |
                                          v
                                     Prompt Template
                                          |
                                          v
                                          LLM
                                          |
                                          v
                                  Answer + Citations
```

## Stage → guides

| Stage | Docs |
|-------|------|
| Ingestion → index | [Retrieval flow](../retrieval/retrieval-flow.md) · [Ingestion](../retrieval/ingestion/) |
| Retrieval | [Search](../retrieval/search/) · [Retrieval strategies combined](../retrieval/search/retrieval-strategies-combined.md) |
| Shrink/dedupe candidates (optional) | [Compacting](../retrieval/compacting/) |
| History + token budget | [Embedding user context compact flow](../retrieval/embedding/queries/embedding-user-context-compact-flow.md) |
| Permissions | [Metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md) · [Guard-rails tenant retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md) |
| Insufficient evidence | [Similarity / abstain](../retrieval/search/retrieval-strategy-similarity.md) |
| Quality metrics | [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) |

**Context assembly** should only include chunks the user is authorized to see; permissions apply when selecting and formatting evidence, not only at retrieval time. Full rule set: [reliable architecture](./context-reliable-architecture.md).

What to put in the assembled prompt: [context info for output](./context-info-for-output.md). How to build it: [context algorithm](./context-algorithm.md).

## See also

- [Prompting](../prompting/) — templates and instructions after assembly
- [Contexting overview](./README.md)
