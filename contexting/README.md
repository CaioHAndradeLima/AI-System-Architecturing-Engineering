# Contexting

What happens **after retrieval** and **around the LLM call**: assemble evidence into a prompt, enforce context limits, citations, grounding, and safe fallbacks when evidence is thin.

Contexting follows [retrieval/search](../retrieval/search/) (candidate passages) and complements [retrieval/compacting](../retrieval/compacting/) (shrink/dedupe retrieved text). Guard-rails for output and tenancy still apply ([guard-rails](../guard-rails/)).

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Context assembly** | Order chunks, metadata, system vs user messages |
| **Token budget** | Window limits, truncation vs summarize |
| **Citations & grounding** | Require evidence-linked answers; cite chunk/source IDs |
| **Prompt structure** | See [prompting](../prompting/) for templates and instructions; contexting focuses on evidence slots |
| **Insufficient evidence** | Abstain, clarify, degraded answers ([search similarity](../retrieval/search/retrieval-strategy-similarity.md)) |
| **Multi-turn context** | History, compaction of chat, retrieval in threads |
| **Evaluation** | Groundedness, faithfulness, context relevance |

---

## Guides

### [context-assembly-flow.md](./context-assembly-flow.md)

`#flow` · `#rag` · `#prompt`

End-to-end RAG pipeline with context assembly as the step that merges retrieved candidates with conversation history, permissions, and token budget before the prompt reaches the LLM.

→ [See more in context-assembly-flow.md](./context-assembly-flow.md)

### [context-info-for-output.md](./context-info-for-output.md)

`#context` · `#citations` · `#history`

Five inputs that context assembly combines before the LLM—each with a distinct role in grounded, traceable answers (context assembly flow).

→ [See more in context-info-for-output.md](./context-info-for-output.md)

### [context-algorithm.md](./context-algorithm.md)

`#algorithm` · `#dedupe` · `#token-budget`

Ordered context assembly steps from retrieved candidates to the final prompt—after search returns candidates and before the LLM runs (context assembly flow).

→ [See more in context-algorithm.md](./context-algorithm.md)

### [context-scoring-math.md](./context-scoring-math.md)

`#scoring` · `#weights` · `#freshness`

Score and select evidence during context assembly (context algorithm — step 4).

Initial retrieval similarity is useful but should not be the only selection criterion.

→ [See more in context-scoring-math.md](./context-scoring-math.md)

### [context-conversation-strategies.md](./context-conversation-strategies.md)

`#history` · `#summarization` · `#token-budget`

How much conversation history to include during context assembly—trade-offs for token budget and follow-up understanding (context info — conversation history).

→ [See more in context-conversation-strategies.md](./context-conversation-strategies.md)

### [context-simple-document-question.md](./context-simple-document-question.md)

`#mvp` · `#citations` · `#policy`

Minimal context shape for single-corpus policy or doc Q&A: question plus top chunks and citation fields—no multi-agent branches or structured SQL blocks (minimum ingestion MVP).

→ [See more in context-simple-document-question.md](./context-simple-document-question.md)

### [context-multi-hop-question.md](./context-multi-hop-question.md)

`#multi-hop` · `#synthesis` · `#timeline`

Some questions need several evidence threads (metrics, errors, incidents) before the model can answer.

Context assembly gathers and organizes each hop—often with dates—then asks the LLM to synthesize (e.g.

a causal timeline).

→ [See more in context-multi-hop-question.md](./context-multi-hop-question.md)

### [context-analytical-question.md](./context-analytical-question.md)

`#sql` · `#analytics` · `#structured`

Metrics and analytics questions: context is built from validated query results, not (only) document chunks.

The LLM explains numbers that the application already computed or fetched.

→ [See more in context-analytical-question.md](./context-analytical-question.md)

### [context-assembly-langchain-langgraph.md](./context-assembly-langchain-langgraph.md)

`#langgraph` · `#langchain` · `#workflow`

Example graph nodes for RAG: retrieval, context assembly, generation, and optional validation—state passed between steps (context algorithm).

→ [See more in context-assembly-langchain-langgraph.md](./context-assembly-langchain-langgraph.md)

### [context-reliable-architecture.md](./context-reliable-architecture.md)

`#security` · `#tenancy` · `#provenance`

Rules for safe, trustworthy context assembly—what may enter the prompt and how evidence is handled before and after the LLM.

→ [See more in context-reliable-architecture.md](./context-reliable-architecture.md)

### [context-evaluate-assembling.md](./context-evaluate-assembling.md)

`#eval` · `#metrics` · `#groundedness`

Metrics and tests for context assembly quality—whether the prompt carries the right evidence efficiently, safely, and traceably (context algorithm, reliable architecture).

→ [See more in context-evaluate-assembling.md](./context-evaluate-assembling.md)

### [context-assembling-trade-offs.md](./context-assembling-trade-offs.md)

`#trade-offs` · `#anti-patterns` · `#token-budget`

Common context assembly mistakes, why they hurt, and better approaches—companion to evaluate assembling and reliable architecture.

→ [See more in context-assembling-trade-offs.md](./context-assembling-trade-offs.md)

### [context-architecturing-decision-based.md](./context-architecturing-decision-based.md)

`#decision-guide` · `#startup` · `#enterprise` · `#multi-agent`

How context assembly and prompt safety evolve from startup/prototype through growing production to enterprise / multi-agent.

→ [See more in context-architecturing-decision-based.md](./context-architecturing-decision-based.md)

## Runnable code lab

**[contexting-strategies](https://github.com/CaioHAndradeLima/contexting-strategies)** is a small Python project that implements and measures ideas from this section on a synthetic corpus. It is for learning and controlled experiments—not a production service.

| Command | What it exercises |
|---------|-------------------|
| `python -m contexting_strategies.cli evaluate` | [Context algorithm](./context-algorithm.md) steps (ACL, dedupe, \(S(d)\) scoring, budget), [assembling trade-offs](./context-assembling-trade-offs.md) baselines, [evaluate assembling](./context-evaluate-assembling.md) metrics |
| `python -m contexting_strategies.cli evaluate-scenarios` | [Multi-hop question](./context-multi-hop-question.md), [conversation strategies](./context-conversation-strategies.md), insufficient-evidence / no-answer handling |

Pair with **[reranking-strategies](https://github.com/CaioHAndradeLima/reranking-strategies)** for candidate ordering before assembly ([reranking](../retrieval/search/retrieval-strategy-reranking.md)).

## Related

- [Retrieval flow](../retrieval/retrieval-flow.md) · [Retrieval strategies combined](../retrieval/search/retrieval-strategies-combined.md)
- [Compacting](../retrieval/compacting/)
- [Embedding user context compact flow](../retrieval/embedding/queries/embedding-user-context-compact-flow.md)
- [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md)

## See also

- [Repository overview](../README.md)
