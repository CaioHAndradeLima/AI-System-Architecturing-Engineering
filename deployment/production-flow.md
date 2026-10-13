# Production flow

**Live production feedback loop**—telemetry and user signals become labeled cases, offline eval, and gated releases. Closes the loop in [production architecture](./production-architecture.md) (monitoring → failure dataset) and [pipeline criteria pass vs fail](./pipeline-criteria-pass-vs-fail.md).

```
                  LIVE PRODUCTION
                        |
                        v
                Collect telemetry
                        |
                        v
            Detect failure or user feedback
                        |
                        v
               Sample relevant cases
                        |
                        v
            Redact / sanitize sensitive data
                        |
                        v
            Human review and labeling
                        |
                        v
            Add approved case to dataset
                        |
                        v
             Re-run offline evaluation
                        |
                        v
             Compare candidate changes
                        |
                        v
              CI quality gate passes?
                   /          \
                 No            Yes
                  |              |
                  v              v
            Improve system   Canary release
                  |              |
                  +----<---------+
                                 |
                                 v
                         Monitor new version
```

## Step → guides

| Step | Docs |
|------|------|
| Collect telemetry | [Tracing metrics](../observability-evaluation/tracing-for-observability-metrics.md) · [Observability tools](../observability-evaluation/observability-tools.md) |
| Detect failure / feedback | [Investigate failure](../observability-evaluation/investigate-failure-by-observability-data.md) · [Tracing metrics — business metrics](../observability-evaluation/tracing-for-observability-metrics.md#c-cost-and-business-metrics) |
| Sample cases | Risk-based sampling; high-severity and novel categories first |
| Redact / sanitize | [Reliable architecture](../contexting/context-reliable-architecture.md) · [Guard-rails](../guard-rails/) |
| Human review / labeling | [LLM-as-judge vs human](../observability-evaluation/llm-as-judge-vs-human.md) |
| Add to dataset | Golden / failure set growth ([observability decision-based](../observability-evaluation/observability-decision-based.md)) |
| Offline eval + compare | [Pipeline evaluation](./pipeline-evaluation.md) · [Pipeline scoring metrics](./pipeline-scoring-metrics.md) |
| Quality gate | [Release policy (simple)](./pipeline-release-policy-simple.md) |
| Improve system (No branch) | [Poor retrieval scores](../observability-evaluation/poor-retrieval-scores.md) · loop back to dataset |
| Canary + monitor | [Regression and canary](../observability-evaluation/regression-and-canary-releases.md) · [Production feedback row in pipeline tools](./pipeline-tools-steps.md) |

The **No** path updates prompts, retrieval, or validation, then re-enters the loop at **re-run offline evaluation**—do not skip adding approved failure cases to the dataset.

## See also

- [Pipeline tools and steps](./pipeline-tools-steps.md)
- [Deployment overview](./README.md)
