# Deployment decision-based by scale

How **runtime, CI/CD, evaluation pipelines, and production operations** evolve from startup/prototype through growing production to enterprise / multi-agent.

| Area | Startup / Prototype | Growing Production | Enterprise / Multi-Agent |
|------|---------------------|--------------------|---------------------------|
| **Application runtime** | One containerized API | Multiple replicas and managed container deployment | Multi-service architecture with controlled scaling and isolation |
| **CI/CD** | Lint, unit tests, basic integration tests | Automated evaluation gates and staging deployment | Governed release policies, approvals, auditability |
| **Evaluation pipeline** | Small golden dataset and baseline | Model/prompt/retrieval comparisons | Experiment tracking, segmented evaluations, holdout datasets |
| **Experiment cost** | Run a few candidates manually | Scheduled and targeted experiments | Budgets, concurrency controls, reproducible experiment records |
| **Observability** | Basic logs and error tracking | Distributed tracing, token usage, p95 latency | Cross-service traces, tenant-aware metrics, audit trails |
| **Failure recovery** | Timeouts and safe errors | Bounded retries, fallback, circuit breakers | Dependency-specific policies, controlled degradation |
| **Deployment** | Single deployment | Staging, canary, rollback | Progressive delivery, policy gates, regional requirements |
| **Feedback loop** | Manual issue tracking | Reviewed failures added to golden tests | Privacy-aware sampling, human labeling, governed datasets |
| **Security** | Secrets management and authentication | Least privilege, document ACLs, dependency scanning | Defense in depth, tenant isolation, audit and compliance controls |
| **Cost optimization** | Limit calls and context size | Cost per successful task and model routing | Budgets and attribution across tenants, agents, and workloads |

## Guide links by area

| Area | Docs |
|------|------|
| Application runtime | [Production architecture](./production-architecture.md) · [Production components — stack](./production-components.md) · [Deployment cloud tools](./deployment-cloud-tools.md) |
| CI/CD | [Pipeline tools and steps](./pipeline-tools-steps.md) · [Pipeline evaluation](./pipeline-evaluation.md) |
| Evaluation pipeline | [Pipeline scoring metrics](./pipeline-scoring-metrics.md) · [Pipeline evaluation YAML sample](./pipeline-evaluation-yaml-sample.md) · [Observability decision-based](../observability-evaluation/observability-decision-based.md) |
| Experiment cost | [Pipeline evaluation components](./pipeline-evaluation-components.md) · [LLM decision-based](../llm/llm-decision-based.md) |
| Observability | [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md) · [Tracing metrics](../observability-evaluation/tracing-for-observability-metrics.md) |
| Failure recovery | [Production components — controls](./production-components.md) · [LLM retry and fallbacks](../llm/llm-retry-fallbacks-routing.md) |
| Deployment | [Regression and canary](../observability-evaluation/regression-and-canary-releases.md) · [Pipeline criteria pass vs fail](./pipeline-criteria-pass-vs-fail.md) · [Release policy (simple)](./pipeline-release-policy-simple.md) |
| Feedback loop | [Production flow](./production-flow.md) · [Production retrieval regression testing](./production-retrieval-regression-testing.md) |
| Security | [Guard-rails](../guard-rails/) · [Deployment cloud tools — secrets](./deployment-cloud-tools.md) |
| Cost optimization | [Pipeline scoring — layer C](./pipeline-scoring-metrics.md) · [Output decision-based](../output/output-decision-based.md) |
| Multi-agent | [Retrieval architecture decision](../retrieval/search/retrieval-architecture-decision.md) · [Production architecture](./production-architecture.md) |

## See also

- [Deployment checklist flow](./deployment-checklist-flow.md)
- [Observability decision-based by scale](../observability-evaluation/observability-decision-based.md)
- [Deployment implementation — pipeline evaluation](./pipeline-evaluation.md)
- [Deployment overview](./README.md)
