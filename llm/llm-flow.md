# LLM flow

End-to-end path from user question to response, with **model selection** as an explicit gate before inference.

```
User question
     |
     v
Retrieval
     |
     v
Context assembly
     |
     v
Prompt construction
     |
     v
+--------------------------------+
|       MODEL SELECTION           |
|                                |
|  Task complexity                |
|  Quality requirements           |
|  Latency budget                 |
|  Cost budget                    |
|  Context / tool support         |
+--------------------------------+
     |
     v
Model inference / generation
     |
     v
Output validation
     |
     v
Response to user
```

## Stage → guides

| Stage | Docs |
|-------|------|
| Retrieval | [Retrieval flow](../retrieval/retrieval-flow.md) · [Search](../retrieval/search/) |
| Context assembly | [Context assembly flow](../contexting/context-assembly-flow.md) |
| Prompt construction | [Prompt categories](../prompting/prompt-categories.md) · [Standard format](../prompting/prompt-standard-format.md) |
| Model selection | [LLM questions](./llm-questions.md) · [Prompt variables — model choice](../prompting/prompt-relevant-variables-influences.md) · [Architecturing decision-based](../prompting/prompt-architecturing-decision-based.md) |
| Inference / generation | [Cloud tools — LLM inference](../retrieval/search/retrieval-cloud-tools.md) · [LangGraph generate node](../contexting/context-assembly-langchain-langgraph.md) |
| Output validation | [Guard-rails](../guard-rails/) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) · [Prompt injection](../prompting/prompt-injection.md) |

Selection inputs (complexity, quality, latency, cost, context/tools) should be **explicit in code or config**, not only implied by the prompt.

## See also

- [LLM overview](./README.md)
