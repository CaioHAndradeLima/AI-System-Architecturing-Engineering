# Pipeline criteria — pass vs fail

**Select the winner and promote it safely** after [pipeline evaluation](./pipeline-evaluation.md) candidates are scored ([pipeline scoring metrics](./pipeline-scoring-metrics.md)) and checked against [release policy (simple)](./pipeline-release-policy-simple.md) and [quality gate examples](./pipeline-scoring-quality-gate.md).

Once the experiments finish, the pipeline should generate a report with:

- The best eligible configuration.
- Its comparison against the baseline.
- Results by question category.
- Retrieval and answer-quality metrics.
- Latency, token usage, and cost.
- Failed cases and regression details.
- The exact configuration manifest required to reproduce the run.

Then:

1. Block the release if the quality gate fails.
2. Build an immutable Docker image from the tested commit.
3. Deploy to staging and run integration and smoke tests.
4. Deploy to a small canary population.
5. Monitor production quality signals and operational metrics.
6. Promote gradually or roll back if release criteria are violated.

## Report contents → docs

| Report section | Sources |
|----------------|---------|
| Best eligible config | Winner among candidates that [PASS](./pipeline-release-policy-simple.md) |
| Baseline comparison | [Quality gate table](./pipeline-scoring-quality-gate.md) |
| By question category | [Evaluate answer metrics](../observability-evaluation/evaluate-answer-metrics.md) · [Simple / multi-hop / analytical](../contexting/context-simple-document-question.md) |
| Retrieval + answer metrics | [Pipeline scoring layers A & B](./pipeline-scoring-metrics.md) |
| Latency, tokens, cost | Layer C · [Tracing metrics](../observability-evaluation/tracing-for-observability-metrics.md) |
| Failed cases / regressions | [Guardrails practices](../output/output-validation-guardrails-practices.md) · [Investigate failure](../observability-evaluation/investigate-failure-by-observability-data.md) |
| Reproduce manifest | [Pipeline evaluation YAML sample](./pipeline-evaluation-yaml-sample.md) |

**Eligible** means every [release policy](./pipeline-release-policy-simple.md) line passes; do not promote on “best of failing candidates” unless policy explicitly allows degraded mode.

## Steps 1–6 → deployment path

| Step | Action | Docs |
|------|--------|------|
| 1. Block on gate fail | Stop CI/CD; no image promote | [Regression and canary](../observability-evaluation/regression-and-canary-releases.md) |
| 2. Immutable image | Docker from **same commit** as eval | [Production components — containerization](./production-components.md) |
| 3. Staging + smoke | Integration tests, auth, tenant smoke | [Production architecture](./production-architecture.md) |
| 4. Canary population | Small traffic slice | [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md) |
| 5. Monitor | Quality + ops on canary | [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md) |
| 6. Promote or rollback | Gradual traffic or revert image/config | [Prompt versioning — rollback](../prompting/prompt-versioning.md) |

Tag the promoted release with the **manifest** from the report so production traces match the configuration that passed offline eval.

## See also

- [Pipeline evaluation components](./pipeline-evaluation-components.md)
- [Deployment overview](./README.md)
