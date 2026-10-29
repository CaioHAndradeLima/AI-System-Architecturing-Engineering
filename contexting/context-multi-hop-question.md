# Context — multi-hop question

Some questions need **several evidence threads** (metrics, errors, incidents) before the model can answer. Context assembly **gathers and organizes** each hop—often with dates—then asks the LLM to synthesize (e.g. a causal timeline).

```
Multi-hop Question
  |
  +--> Evidence about conversion
  |
  +--> Evidence about API errors
  |
  +--> Evidence about incident resolution
  |
  v
Organized evidence with dates
  |
  v
LLM synthesizes causal timeline
```

## Implementation patterns

| Approach | When |
|----------|------|
| **Multiple retrieval calls** | One query (or sub-query) per facet; label each block in the prompt ([cleaning user query — decomposition](../retrieval/embedding/queries/embedding-cleaning-user-query.md)) |
| **Multi-agent branches** | Analytics + knowledge paths merge structured + doc evidence ([simple loop](../retrieval/search/retrieval-architecture-simple-loop.md)) |
| **Retrieval agent** | Dynamic source choice and retries ([supervisor as agent](../retrieval/search/retrieval-architecture-supervisor-as-agent.md)) |

Organize evidence with **timestamps, source IDs, and section headers** so the model can order events ([context info — structured results & metadata](./context-info-for-output.md)). Use [context scoring math](./context-scoring-math.md) to rank within each hop; use **diversity/coverage** (algorithm step 5) so one hop does not crowd out others in the token budget.

Eval: answer correctness and groundedness on questions that require more than one corpus ([retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md)).

## See also

- [contexting-strategies — `evaluate-scenarios`](https://github.com/CaioHAndradeLima/contexting-strategies) — per-hop retrieval and hop-coverage metrics (`multihop_golden.json`)
- [Simple document question](./context-simple-document-question.md) — single-hop contrast
- [Context assembly flow](./context-assembly-flow.md)
- [Contexting overview](./README.md)
