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

How evaluation, tracing, metrics, and release discipline evolve from startup/prototype through growing production to enterprise / multi-agent.

→ [See more in observability-decision-based.md](./observability-decision-based.md)

### [observability-implementation-flow.md](./observability-implementation-flow.md)

`#checklist` · `#implementation` · `#canary` · `#regression`

Evaluation and observability checklist—golden data through retrieval and answer quality, tracing, monitoring, failure diagnosis, regression gates, and canary promote or rollback.

→ [See more in observability-implementation-flow.md](./observability-implementation-flow.md)

### [evaluate-retrieval-independently-metrics.md](./evaluate-retrieval-independently-metrics.md)

`#retrieval` · `#metrics` · `#golden-set` · `#offline-eval`

Measure search and ranking alone on a golden dataset (query → known relevant document IDs) before blaming the LLM for bad answers.

Independent retrieval eval isolates chunking, embeddings, indexes, filters, hybrid fusion, and top-K from generation and output validation.

→ [See more in evaluate-retrieval-independently-metrics.md](./evaluate-retrieval-independently-metrics.md)

### [poor-retrieval-scores.md](./poor-retrieval-scores.md)

`#debugging` · `#retrieval` · `#recall` · `#ndcg`

Decision flow after independent retrieval metrics on a golden set (architecture evaluation — layers).

→ [See more in poor-retrieval-scores.md](./poor-retrieval-scores.md)

### [evaluate-answer-metrics.md](./evaluate-answer-metrics.md)

`#answers` · `#groundedness` · `#citations` · `#abstain`

End-to-end answer quality metrics on golden or sampled conversations—after retrieval and context assembly, including what output validation checks before delivery.

→ [See more in evaluate-answer-metrics.md](./evaluate-answer-metrics.md)

### [llm-as-judge-vs-human.md](./llm-as-judge-vs-human.md)

`#eval` · `#llm-judge` · `#human` · `#rubric`

Two ways to score answers against evidence and rubrics when deterministic checks are not enough (evaluate answer metrics, output implementation strategies — LLM-as-a-judge).

→ [See more in llm-as-judge-vs-human.md](./llm-as-judge-vs-human.md)

### [tracing-for-observability.md](./tracing-for-observability.md)

`#tracing` · `#spans` · `#multi-agent` · `#latency`

Example distributed trace for a multi-agent RAG request: one trace ID ties API, supervisor, agents, retrieval, generation, validation, and response—so latency and failures are attributable to a step (storage observability tools — tracing, observability/ package).

→ [See more in tracing-for-observability.md](./tracing-for-observability.md)

### [tracing-for-observability-metrics.md](./tracing-for-observability-metrics.md)

`#tracing` · `#attributes` · `#cost` · `#tokens`

What to record on traces and spans so you can debug latency, cost, quality regressions, and security incidents (example trace tree).

→ [See more in tracing-for-observability-metrics.md](./tracing-for-observability-metrics.md)

### [investigate-failure-by-observability-data.md](./investigate-failure-by-observability-data.md)

`#incident` · `#debugging` · `#trace` · `#regression`

Work top-down from the trace when a user report or alert does not match expectations—before guessing at prompts or models (tracing example tree, span attributes).

→ [See more in investigate-failure-by-observability-data.md](./investigate-failure-by-observability-data.md)

### [observability-tools.md](./observability-tools.md)

`#tools` · `#langsmith` · `#langfuse` · `#opentelemetry` · `#prometheus` · `#eval`

Reference tracing, metrics, and evaluation platforms for AI systems—what each tool is good at and how they complement span attributes (tracing for observability — metrics) and incident workflows (investigate failure by observability data).

→ [See more in observability-tools.md](./observability-tools.md)

### [regression-and-canary-releases.md](./regression-and-canary-releases.md)

`#canary` · `#regression` · `#deploy` · `#rollback`

Safe rollout when prompts, models, or retrieval change—automated tests and baseline comparison before traffic; canary monitoring before full promotion (prompt versioning, LLM implementation flow).

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
