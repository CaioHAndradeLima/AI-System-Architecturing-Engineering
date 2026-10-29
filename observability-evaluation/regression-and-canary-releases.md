# Regression and canary releases

Safe rollout when **prompts**, **models**, or **retrieval** change—automated tests and baseline comparison before traffic; canary monitoring before full promotion ([prompt versioning](../prompting/prompt-versioning.md), [LLM implementation flow](../llm/llm-implementation-flow.md)).

```
Prompt / Model / Retrieval Change
               |
               v
       Run Automated Tests
               |
               v
       Compare Against Baseline
               |
               v
       Critical Regression?
          /          \
        Yes           No
         |             |
         v             v
    Reject Change   Canary Release
                       |
                       v
                 Monitor Quality
                 and Operations
                       |
                       v
                 Meets Thresholds?
                    /      \
                   No       Yes
                   |         |
                   v         v
                Rollback   Promote
```

## What to run and watch

| Phase | Tests / signals | Docs |
|-------|-----------------|------|
| Automated tests | Retrieval golden set, answer eval, schema/guardrail cases | [Pipeline evaluation](../deployment/pipeline-evaluation.md) · [Evaluate retrieval metrics](./evaluate-retrieval-independently-metrics.md) · [Evaluate answer metrics](./evaluate-answer-metrics.md) |
| Baseline compare | Same dataset, frozen config versions on both sides | [Prompt versioning](../prompting/prompt-versioning.md) · [Tracing metrics — quality & ops](./tracing-for-observability-metrics.md) |
| Critical regression | Pre-defined gates: Recall@K drop, false-block spike, p95 latency, error rate | [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) · [Output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md) |
| Canary monitor | Operational + AI quality + cost ([metrics groups B & C](./tracing-for-observability-metrics.md)) | [Observability tools](./observability-tools.md) |
| Rollback / promote | Revert prompt hash, model route, or index version tagged on traces | [Investigate failure](./investigate-failure-by-observability-data.md) |

Tag every change with **prompt version**, **model ID**, and **retrieval/index version** on traces so canary cohorts compare apples to apples.


## Reference implementation

**[observability-strategies](https://github.com/CaioHAndradeLima/observability-strategies)** — baseline vs candidate bundles in `regression_canary.py` / `data/canary_baselines.json`. Keys: `regression_and_canary`, `scenarios.canary`.

## See also

- [Deployment overview](../deployment/README.md)
- [Observability implementation flow](./observability-implementation-flow.md)
- [Select LLM flow — canary](../llm/select-llm-flow.md)
- [Retrieval implementation flow](../retrieval/search/retrieval-implementation-flow.md)
- [Observability & evaluation overview](./README.md)
