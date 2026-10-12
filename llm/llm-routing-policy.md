# LLM routing policy

**Task → model choice** for the router below. Calibrate “small / medium / strong” on your [benchmark](./select-llm-flow.md), not vendor labels alone. Router signals: [LLM routing flow](./llm-routing-flow.md).

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

## Task → model choice

| Task | Potential model choice |
|------|------------------------|
| **Intent classification** | Small, fast model—or deterministic code |
| **Query rewriting** | Small or medium model |
| **Straightforward RAG answer** | Cost-efficient model that meets the quality bar |
| **Complex evidence synthesis** | Stronger reasoning-capable model |
| **Structured extraction** | Model with reliable schema-constrained output |
| **Supervisor routing** | Small model or explicit routing rules |
| **Sensitive action or authorization** | Deterministic policy and permission checks, not model judgment alone |

## Task → stack guides

| Task | Docs |
|------|------|
| Query rewriting | [Cleaning user query](../retrieval/embedding/queries/embedding-cleaning-user-query.md) |
| Straightforward RAG | [Simple document question](../contexting/context-simple-document-question.md) · [Deciding sample](./select-llm-deciding-sample.md) |
| Complex synthesis | [Multi-hop question](../contexting/context-multi-hop-question.md) |
| Structured extraction | [Prompt variables — structured output](../prompting/prompt-relevant-variables-influences.md) |
| Supervisor routing | [Architecture decision](../retrieval/search/retrieval-architecture-decision.md) |
| Authorization | [Metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md) · [Reliable architecture](../contexting/context-reliable-architecture.md) |

Never route **permission decisions** to the strongest model—enforce ACLs in code before any LLM call.

## See also

- [LLM routing flow](./llm-routing-flow.md)
- [LLM overview](./README.md)
