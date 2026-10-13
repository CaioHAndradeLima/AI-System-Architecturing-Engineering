# Pipeline tools and steps

**When each test runs** in the delivery path—from PR through [pipeline evaluation](./pipeline-evaluation.md) to production feedback ([pipeline criteria pass vs fail](./pipeline-criteria-pass-vs-fail.md)).

| Test | Typical trigger |
|------|-----------------|
| Ruff, mypy, unit tests | Every pull request |
| Mocked model/tool integration tests | Every pull request |
| Fast golden-set regression | Every relevant pull request |
| Full model/prompt/retrieval comparison | Scheduled run or deliberate experiment |
| Staging smoke tests | After deployment to staging |
| Canary health checks | During rollout |
| Production feedback evaluation | Continuous or scheduled, according to volume and risk |

## Test → pipeline stage

| Test | Stage | Docs |
|------|-------|------|
| Ruff, mypy, unit tests | Static checks in [pipeline evaluation](./pipeline-evaluation.md) | [Example Python — `tests/`](../agents/multi-agent-architecture/example-python-directories.md) |
| Mocked integration | PR — no live LLM/provider | [Secure tool execution](../output/output-secure-tool-execution-flow.md) |
| Fast golden-set regression | PR when prompt/retrieval/output changes | [Release policy (simple)](./pipeline-release-policy-simple.md) · [Guardrails practices](../output/output-validation-guardrails-practices.md) |
| Full comparison | Offline eval matrix ([candidates](./pipeline-evaluation-components.md), [YAML manifest](./pipeline-evaluation-yaml-sample.md)) | [Pipeline scoring metrics](./pipeline-scoring-metrics.md) |
| Staging smoke | Post-image deploy | [Production architecture](./production-architecture.md) |
| Canary health checks | Steps 4–6 in [pass vs fail](./pipeline-criteria-pass-vs-fail.md) | [Regression and canary](../observability-evaluation/regression-and-canary-releases.md) |
| Production feedback | Live eval / human review | [LLM-as-judge vs human](../observability-evaluation/llm-as-judge-vs-human.md) · [Tracing metrics — business group](../observability-evaluation/tracing-for-observability-metrics.md#c-cost-and-business-metrics) |

**Relevant** PRs: touch prompts, retrieval config, models, context assembly, or output validation—skip full golden regression only when change is docs-only or unrelated paths (define in CI config).

## See also

- [Production components — CI/CD and offline evaluation](./production-components.md)
- [Observability tools](../observability-evaluation/observability-tools.md)
- [Deployment overview](./README.md)
