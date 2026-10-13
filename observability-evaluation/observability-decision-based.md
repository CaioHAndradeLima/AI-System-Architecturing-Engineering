# Observability decision-based by scale

How **evaluation, tracing, metrics, and release discipline** evolve from startup/prototype through growing production to enterprise / multi-agent.

| Area | Startup / Prototype | Growing Production | Enterprise / Multi-Agent |
|------|---------------------|--------------------|---------------------------|
| **Golden dataset** | Small, manually reviewed set | Expanded test suite by query category | Versioned datasets, holdout sets, domain-specific coverage |
| **Retrieval evaluation** | Recall@K and manual review | Recall@K, nDCG@K, reranking comparisons | Continuous regression tests by corpus, tenant, and task |
| **Answer evaluation** | Manual correctness checks | Automated correctness and groundedness tests | Risk-based evaluation and calibrated human review |
| **Observability** | Basic logs and errors | Traces, spans, tokens, cost, and latency | Distributed tracing across agents and services |
| **Metrics** | Success rate and basic quality | p95 latency, quality, failures, and unit economics | SLOs, segmented quality, governance, and auditability |
| **Failure diagnosis** | Reproduce manually | Trace-driven investigation | Correlated traces, evaluation records, and incident workflows |
| **CI/CD** | Run tests before merging | Automated regression tests and canary releases | Governed promotion, approval gates, and rollback policies |
| **Feedback** | Collect direct user feedback | Categorize feedback and add failures to tests | Privacy-aware feedback pipelines and domain-expert review |
| **Cost control** | Track approximate usage | Cost per request and successful task | Budgets, attribution, model routing, and optimization across agents |

## Guide links by area

| Area | Docs |
|------|------|
| Golden dataset | [Evaluate retrieval metrics](./evaluate-retrieval-independently-metrics.md) · [Evaluate answer metrics](./evaluate-answer-metrics.md) · [Guardrails practices](../output/output-validation-guardrails-practices.md) |
| Retrieval evaluation | [Evaluate retrieval independently](./evaluate-retrieval-independently-metrics.md) · [Poor retrieval scores](./poor-retrieval-scores.md) · [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) |
| Answer evaluation | [Evaluate answer metrics](./evaluate-answer-metrics.md) · [LLM-as-judge vs human](./llm-as-judge-vs-human.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| Observability | [Tracing for observability](./tracing-for-observability.md) · [Tracing metrics](./tracing-for-observability-metrics.md) · [Observability tools](./observability-tools.md) |
| Metrics | [Tracing metrics — A/B/C groups](./tracing-for-observability-metrics.md) · [Output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md) |
| Failure diagnosis | [Investigate failure by observability data](./investigate-failure-by-observability-data.md) |
| CI/CD | [Regression and canary releases](./regression-and-canary-releases.md) · [Prompt versioning](../prompting/prompt-versioning.md) · [LLM implementation flow](../llm/llm-implementation-flow.md) |
| Feedback | [Tracing metrics — cost and business](./tracing-for-observability-metrics.md#c-cost-and-business-metrics) |
| Cost control | [LLM decision-based](../llm/llm-decision-based.md) · [Output decision-based](../output/output-decision-based.md) |
| Multi-agent | [Tracing example tree](./tracing-for-observability.md) · [Retrieval architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md) |

## See also

- [Deployment decision-based by scale](../deployment/deployment-decision-based.md)
- [Observability implementation flow](./observability-implementation-flow.md)
- [Output decision-based by scale](../output/output-decision-based.md)
- [Prompt architecturing decision-based](../prompting/prompt-architecturing-decision-based.md)
- [Context architecturing decision-based](../contexting/context-architecturing-decision-based.md)
- [LLM decision-based by scale](../llm/llm-decision-based.md)
- [Observability & evaluation overview](./README.md)
