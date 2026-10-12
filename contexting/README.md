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

### [context-assembly-flow.md](./context-assembly-flow.md)

`#flow` · `#rag` · `#prompt`

Full RAG path highlighting context assembly: retrieval + history + permissions + token budget → prompt → LLM → citations.

→ [See more in context-assembly-flow.md](./context-assembly-flow.md)

### [context-info-for-output.md](./context-info-for-output.md)

`#context` · `#citations` · `#history`

Evidence, history, request context, structured results, and source metadata for the prompt.

→ [See more in context-info-for-output.md](./context-info-for-output.md)

### [context-algorithm.md](./context-algorithm.md)

`#algorithm` · `#dedupe` · `#token-budget`

Eight-step assembly from candidates through render → prompt template → LLM.

→ [See more in context-algorithm.md](./context-algorithm.md)

### [context-scoring-math.md](./context-scoring-math.md)

`#scoring` · `#weights` · `#freshness`

Multi-signal evidence score: relevance, freshness, authority, task fit.

→ [See more in context-scoring-math.md](./context-scoring-math.md)

### [context-conversation-strategies.md](./context-conversation-strategies.md)

`#history` · `#summarization` · `#token-budget`

Full thread vs last-N vs summary + recent messages for context assembly.

→ [See more in context-conversation-strategies.md](./context-conversation-strategies.md)

### [context-simple-document-question.md](./context-simple-document-question.md)

`#mvp` · `#citations` · `#policy`

Question + top chunks + source IDs → LLM answer.

→ [See more in context-simple-document-question.md](./context-simple-document-question.md)

### [context-multi-hop-question.md](./context-multi-hop-question.md)

`#multi-hop` · `#synthesis` · `#timeline`

Multiple evidence threads, dated organization, LLM causal synthesis.

→ [See more in context-multi-hop-question.md](./context-multi-hop-question.md)

### [context-analytical-question.md](./context-analytical-question.md)

`#sql` · `#analytics` · `#structured`

SQL/tool result as compact table with units and dates → LLM explanation.

→ [See more in context-analytical-question.md](./context-analytical-question.md)

### [context-assembly-langchain-langgraph.md](./context-assembly-langchain-langgraph.md)

`#langgraph` · `#langchain` · `#workflow`

retrieve → assemble_context → generate → validate → response.

→ [See more in context-assembly-langchain-langgraph.md](./context-assembly-langchain-langgraph.md)

### [context-reliable-architecture.md](./context-reliable-architecture.md)

`#security` · `#tenancy` · `#provenance`

Seven rules for permissions, untrusted evidence, secrets, tools, tenant isolation, and traceability.

→ [See more in context-reliable-architecture.md](./context-reliable-architecture.md)

### [context-evaluate-assembling.md](./context-evaluate-assembling.md)

`#eval` · `#metrics` · `#groundedness`

Coverage, redundancy, tokens, citations, latency, security tests, abstain.

→ [See more in context-evaluate-assembling.md](./context-evaluate-assembling.md)

### [context-assembling-trade-offs.md](./context-assembling-trade-offs.md)

`#trade-offs` · `#anti-patterns` · `#token-budget`

Eight assembly mistakes, impact, and better approaches.

→ [See more in context-assembling-trade-offs.md](./context-assembling-trade-offs.md)

## Related

- [Retrieval flow](../retrieval/retrieval-flow.md) · [Retrieval strategies combined](../retrieval/search/retrieval-strategies-combined.md)
- [Compacting](../retrieval/compacting/)
- [Embedding user context compact flow](../retrieval/embedding/queries/embedding-user-context-compact-flow.md)
- [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md)

## See also

- [Repository overview](../README.md)
