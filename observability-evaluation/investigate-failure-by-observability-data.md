# Investigate failure by observability data

Work **top-down from the trace** when a user report or alert does not match expectations—before guessing at prompts or models ([tracing example tree](./tracing-for-observability.md), [span attributes](./tracing-for-observability-metrics.md)).

```
1. Find the request trace
          |
          v
2. Inspect the final answer
          |
          v
3. Inspect output validation
          |
          v
4. Inspect the model input and prompt version
          |
          v
5. Inspect assembled evidence
          |
          v
6. Inspect retrieved documents and ranking
          |
          v
7. Identify the failure category
          |
          +--> Missing evidence?
          +--> Stale source?
          +--> Unsupported inference?
          +--> Validation failure?
          +--> Incorrect business rule?
          |
          v
8. Reproduce the failure in evaluation
          |
          v
9. Fix the responsible component
          |
          v
10. Run regression tests and deploy safely
```

## Step → where to look

| Step | Signals | Docs |
|------|---------|------|
| 1. Request trace | Trace ID, tenant, latency breakdown | [Tracing metrics](./tracing-for-observability-metrics.md) |
| 2. Final answer | User-visible text, citations shown | [Evaluate answer metrics](./evaluate-answer-metrics.md) |
| 3. Output validation | Pass/fail, repair loops, block reason | [Failure procedure flow](../output/output-failure-procedure-flow.md) · [Failure impact](../output/output-validation-failure-impact.md) |
| 4. Model input / prompt version | Messages, token count, prompt hash | [Prompt versioning](../prompting/prompt-versioning.md) · [Context info for output](../contexting/context-info-for-output.md) |
| 5. Assembled evidence | Chunk IDs in prompt vs ACL | [Assembly flow](../contexting/context-assembly-flow.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| 6. Retrieved docs / ranking | Top-K IDs, scores, filters | [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) · [Poor retrieval scores](./poor-retrieval-scores.md) |
| 7. Failure category | See branches below | [Guardrails practices](../output/output-validation-guardrails-practices.md) |
| 8. Reproduce in eval | Golden case + same config versions | [Embedding query evaluation](../retrieval/embedding/queries/embedding-user-query-evaluation.md) |
| 9–10. Fix and deploy | Component owner + CI gate | [Prompt implementation flow](../prompting/prompt-implementation-flow.md) · [Output implementation flow](../output/output-implementation-flow.md) |

## Failure category → likely owner

| Category | Often points to |
|----------|-----------------|
| **Missing evidence** | Retrieval K, filters, chunking, index freshness ([ingestion](../retrieval/ingestion/ingestion-procedures.md)) |
| **Stale source** | Ingestion pipeline, index version on trace, document versioning |
| **Unsupported inference** | Prompt grounding, model choice, insufficient abstain ([similarity abstain](../retrieval/search/retrieval-strategy-similarity.md)) |
| **Validation failure** | Schema, citations, policy ([citation validation](../output/output-citation-validation.md)) |
| **Incorrect business rule** | Deterministic validators, tool auth, policy engine ([secure tool execution](../output/output-secure-tool-execution-flow.md)) |

Add a **regression case** for step 8 whenever step 7 finds a new category you did not test before. Step 10 aligns with [regression and canary releases](./regression-and-canary-releases.md).

## See also

- [Regression and canary releases](./regression-and-canary-releases.md)

- [LLM-as-judge vs human](./llm-as-judge-vs-human.md)
- [Observability & evaluation overview](./README.md)
