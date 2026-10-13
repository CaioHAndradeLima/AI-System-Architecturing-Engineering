# Observability & evaluation

**Traces, metrics, golden datasets, and continuous evaluation** span the path from [retrieval](../retrieval/) and [contexting](../contexting/) through [prompting](../prompting/), [LLM](../llm/) inference, and [output](../output/) validation—so you can debug production behavior, audit decisions, and catch regressions before users do.

## Topic areas

| Area | Focus |
|------|--------|
| Tracing | End-to-end spans across retrieval, tools, agents, and model calls |
| Metrics | Latency, cost, quality, and throughput dashboards |
| Logging & audit | Structured logs, PII handling, and compliance trails |
| Golden datasets | Curated inputs and expected behaviors for offline benchmarks |
| Regression & CI | Eval gates on pull requests and before deploy |
| Continuous evaluation | Sampling and scoring live traffic over time |
| Multi-agent | Attribution, per-step metrics, and eval when several agents collaborate |
| Scale & maturity | Golden sets, CI/canary, tracing, and cost by stage |

---

## Guides

### [observability-decision-based.md](./observability-decision-based.md)

`#architecture` · `#scale` · `#enterprise` · `#multi-agent`

Golden data, retrieval/answer eval, tracing, CI/CD, feedback, and cost by maturity.

→ [See more in observability-decision-based.md](./observability-decision-based.md)

### [evaluate-retrieval-independently-metrics.md](./evaluate-retrieval-independently-metrics.md)

`#retrieval` · `#metrics` · `#golden-set` · `#offline-eval`

Recall@K, Precision@K, MRR, nDCG@K, and empty-result rate—when each helps for retrieval-only benchmarks.

→ [See more in evaluate-retrieval-independently-metrics.md](./evaluate-retrieval-independently-metrics.md)

### [poor-retrieval-scores.md](./poor-retrieval-scores.md)

`#debugging` · `#retrieval` · `#recall` · `#ndcg`

If Recall@K / nDCG@K fail, fix retrieval; if they pass, eval context assembly and generation.

→ [See more in poor-retrieval-scores.md](./poor-retrieval-scores.md)

### [evaluate-answer-metrics.md](./evaluate-answer-metrics.md)

`#answers` · `#groundedness` · `#citations` · `#abstain`

Seven end-to-end answer metrics—correctness, relevance, completeness, schema, and abstention.

→ [See more in evaluate-answer-metrics.md](./evaluate-answer-metrics.md)

### [llm-as-judge-vs-human.md](./llm-as-judge-vs-human.md)

`#eval` · `#llm-judge` · `#human` · `#rubric`

Automated rubric scoring vs expert review—advantages, limits, and when to combine.

→ [See more in llm-as-judge-vs-human.md](./llm-as-judge-vs-human.md)

### [tracing-for-observability.md](./tracing-for-observability.md)

`#tracing` · `#spans` · `#multi-agent` · `#latency`

Example trace tree: API → supervisor → agents → validation → response.

→ [See more in tracing-for-observability.md](./tracing-for-observability.md)

### [tracing-for-observability-metrics.md](./tracing-for-observability-metrics.md)

`#tracing` · `#attributes` · `#cost` · `#tokens`

Span attributes plus operational, AI quality, and cost/business metric groups.

→ [See more in tracing-for-observability-metrics.md](./tracing-for-observability-metrics.md)

### [investigate-failure-by-observability-data.md](./investigate-failure-by-observability-data.md)

`#incident` · `#debugging` · `#trace` · `#regression`

Ten-step flow from trace to failure category, repro, fix, and safe deploy.

→ [See more in investigate-failure-by-observability-data.md](./investigate-failure-by-observability-data.md)

### [observability-tools.md](./observability-tools.md)

`#tools` · `#langsmith` · `#langfuse` · `#opentelemetry` · `#prometheus` · `#eval`

Cross-stack tracing, metrics, cloud monitoring, and custom evaluation tooling for AI systems.

→ [See more in observability-tools.md](./observability-tools.md)

### [regression-and-canary-releases.md](./regression-and-canary-releases.md)

`#canary` · `#regression` · `#deploy` · `#rollback`

Test → baseline → reject or canary → monitor → rollback or promote.

→ [See more in regression-and-canary-releases.md](./regression-and-canary-releases.md)

## Related links

- [Output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md)
- [Evaluate assembling](../contexting/context-evaluate-assembling.md)
- [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md)
- [Retrieval architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md)
- [Guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md)
- [Example Python directories — `observability/`](../agents/multi-agent-architecture/example-python-directories.md)

## See also

- [Repository overview](../README.md)
