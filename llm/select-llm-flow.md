# Select LLM flow

**Benchmark-driven model selection** before production—same prompts and evidence across candidates, then quality/SLA gate and canary.

```
Define application requirements
          |
          v
Create representative test dataset
          |
          v
Select 2-4 candidate models
          |
          v
Run the same prompts and evidence
          |
          v
Measure quality, latency, and cost
          |
          v
Check tool calls, structured output,
security, and failure behavior
          |
          v
Choose the model that meets
the required quality and SLA
          |
          v
Canary release and monitor
```

## Step notes

| Step | Guides |
|------|--------|
| Requirements | Task complexity, context window, tools ([LLM flow — model selection](./llm-flow.md)) |
| Test dataset | Golden questions + expected behavior ([query evaluation](../retrieval/embedding/queries/embedding-user-query-evaluation.md), [evaluate assembling](../contexting/context-evaluate-assembling.md)) |
| Candidates | [Hosted vs open-weight](./llm-hosted-vs-open-weight-models.md) · [Cloud tools](../retrieval/search/retrieval-cloud-tools.md) |
| Same prompts & evidence | Fix [prompt version](../prompting/prompt-versioning.md) and retrieval config while comparing models |
| Quality, latency, cost | [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) · [Prompt variables](../prompting/prompt-relevant-variables-influences.md) |
| Tools, structured output, security | [Architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md) · [Prompt injection](../prompting/prompt-injection.md) |
| Canary / monitor | [Prompt versioning — rollout](./prompt-versioning.md) |

Do not change retrieval, context assembly, and prompt templates mid-benchmark unless you are explicitly testing that variable.

## See also

- [Deciding sample — example benchmark table](./select-llm-deciding-sample.md)
- [LLM questions — model selection](./llm-questions.md)
- [LLM overview](./README.md)
