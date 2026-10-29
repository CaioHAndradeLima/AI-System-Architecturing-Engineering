# Observability implementation flow

**Evaluation and observability checklist**—golden data through retrieval and answer quality, tracing, monitoring, failure diagnosis, regression gates, and canary promote or rollback.

```
EVALUATION & OBSERVABILITY CHECKLIST
====================================

                 START
                   |
                   v
+------------------------------------------+
| 1. Create a golden evaluation dataset    |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
| 2. Measure retrieval quality             |
|    Recall@K, Precision@K, nDCG@K         |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
| 3. Measure answer quality                |
|    Correctness, groundedness, citations  |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
| 4. Instrument execution traces           |
|    Retrieval, agents, tools, model calls |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
| 5. Monitor latency, errors, tokens,      |
|    cost, and task success                |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
| 6. Diagnose and categorize failures      |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
| 7. Add regression tests and thresholds   |
+------------------------------------------+
                   |
                   v
+------------------------------------------+
| 8. Canary release and monitor            |
+------------------------------------------+
                   |
                   v
          Regression detected?
              /        \
            YES         NO
             |           |
             v           v
          Rollback    Promote release
             |           |
             v           v
       Fix and retest  Continue monitoring
```

## Step → guides

| Step | Docs |
|------|------|
| 1. Golden dataset | [Observability decision-based](./observability-decision-based.md) · [Guardrails practices](../output/output-validation-guardrails-practices.md) · [Query evaluation](../retrieval/embedding/queries/embedding-user-query-evaluation.md) |
| 2. Retrieval quality | [Evaluate retrieval independently — metrics](./evaluate-retrieval-independently-metrics.md) · [Poor retrieval scores](./poor-retrieval-scores.md) |
| 3. Answer quality | [Evaluate answer metrics](./evaluate-answer-metrics.md) · [LLM-as-judge vs human](./llm-as-judge-vs-human.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| 4. Execution traces | [Tracing for observability](./tracing-for-observability.md) · [Tracing metrics — attributes](./tracing-for-observability-metrics.md) · [Observability tools](./observability-tools.md) |
| 5. Latency, cost, success | [Tracing metrics — operational & business groups](./tracing-for-observability-metrics.md) · [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) |
| 6. Diagnose failures | [Investigate failure by observability data](./investigate-failure-by-observability-data.md) |
| 7. Regression tests / thresholds | [Output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md) · [Retrieval architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md) |
| 8. Canary and monitor | [Regression and canary releases](./regression-and-canary-releases.md) · [Prompt versioning](../prompting/prompt-versioning.md) |
| Gate: regression | Rollback, fix, retest — same flow as [regression and canary releases](./regression-and-canary-releases.md) |
| Full stack | [Deployment checklist flow](../deployment/deployment-checklist-flow.md) · [Retrieval implementation flow](../retrieval/search/retrieval-implementation-flow.md) · [Prompt implementation flow](../prompting/prompt-implementation-flow.md) · [LLM implementation flow](../llm/llm-implementation-flow.md) · [Output implementation flow](../output/output-implementation-flow.md) |


## Reference implementation

**[observability-strategies](https://github.com/CaioHAndradeLima/observability-strategies)** — checklist coverage in `implementation_flow.py` and `evaluate_implementation_checklist`. Keys: `implementation_flow`, `implementation_checklist`.

## See also

- [Observability & evaluation overview](./README.md)
