# LLM routing flow

**Model router** sends each request to a small, strong, or specialized model based on task signals—then returns a unified result to the caller.

```
                Request
                   |
                   v
              Model Router
              /     |      \
             v      v       v
          Small   Strong   Specialized
          Model   Model     Model
             \      |       /
              \     |      /
               v    v     v
                Result
```

## Router inputs (examples)

| Signal | Route tendency |
|--------|----------------|
| Intent / task type | FAQ → small; multi-hop analysis → strong |
| Estimated context tokens | Over small-model window → strong or truncate policy |
| Tool requirements | Complex tool graphs → strong or specialized fine-tune |
| Latency SLO | Interactive UI → small when quality bar met |
| Tenant tier | Premium → strong; standard → small with fallback |

Implement routing in **application code** (rules, classifier, or lightweight model)—not only in prompt text. Log `model_id` and route reason for [observability](../prompting/prompt-architecturing-decision-based.md).

## Related patterns

| Pattern | Doc |
|---------|-----|
| Pick models with benchmarks | [Select LLM flow](./select-llm-flow.md) · [Deciding sample](./select-llm-deciding-sample.md) |
| Fallback when route target fails | [LLM questions — fallbacks](./llm-questions.md) (dedicated guide TBD) |
| Per-agent models | [Multi-agent retrieval architecture](../retrieval/search/retrieval-architecture-multi-agent.md) |
| Enterprise routing policy | [Prompt architecturing — model configuration](../prompting/prompt-architecturing-decision-based.md) |

**Specialized** may mean domain fine-tune, code model, or vision—still subject to eval on your tasks, not label alone.

## See also

- [LLM routing policy — task → model](./llm-routing-policy.md)
- [LLM flow](./llm-flow.md)
- [LLM overview](./README.md)
