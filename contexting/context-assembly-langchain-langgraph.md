# Context assembly — LangChain / LangGraph

Example **graph nodes** for RAG: retrieval, context assembly, generation, and optional validation—state passed between steps ([context algorithm](./context-algorithm.md)).

```
LangGraph workflow
       |
       v
retrieve_node(state)
       |
       v
assemble_context_node(state)
       |
       v
generate_answer_node(state)
       |
       v
validate_answer_node(state)
       |
       v
Return response
```

## Node responsibilities

| Node | Typical `state` inputs / outputs |
|------|--------------------------------|
| **retrieve_node** | In: user question, tenant identity, optional rewritten query. Out: candidate chunks, scores, errors ([search](../retrieval/search/)) |
| **assemble_context_node** | In: candidates, history, token budget, permissions. Out: rendered prompt / messages ([context info for output](./context-info-for-output.md), [algorithm steps](./context-algorithm.md)) |
| **generate_answer_node** | In: assembled messages. Out: draft answer + citation placeholders |
| **validate_answer_node** | In: draft + evidence. Out: final answer or retry/abstain ([guard-rails](../guard-rails/)); graph routing: [output failure guardrails LangGraph](../output/output-failure-guardrails-via-langchain.md) |

Keep **authorization** in retrieve and assemble nodes—do not rely on validate alone to strip leaked content.

## Layout in the repo mental model

| Concern | Where it lives |
|---------|----------------|
| Graph definition | `orchestration/graph.py` ([example Python directories](../agents/multi-agent-architecture/example-python-directories.md)) |
| Retrieval service | Callable from `retrieve_node` ([supervisor as service](../retrieval/search/retrieval-architecture-supervisor-as-service.md)) |
| AWS sample topology | [LangGraph on Fargate](../retrieval/search/retrieval-aws-multi-agent-sample.md) |

LangChain/LangGraph APIs change—treat node names as **roles**, not framework-specific requirements.

## Code lab

- [contexting-strategies](https://github.com/CaioHAndradeLima/contexting-strategies) — `workflow.py` linear retrieve → rerank → assemble → sufficiency trace (no LangGraph dependency); `evaluate-full` → `workflow`.

## See also

- [Context assembly flow](./context-assembly-flow.md)
- [Retrieval architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md)
- [Contexting overview](./README.md)
