# Deployment

**Shipping and operating** AI systems in production: environments, release gates, runtime topology, scaling, secrets, and rollback—downstream of [observability-evaluation](../observability-evaluation/) (what to measure before and after promote) and upstream of live [guard-rails](../guard-rails/) enforcement.

Deployment closes the loop from [LLM](../llm/) inference and [output](../output/) validation to user-facing services and [multi-agent](../agents/) orchestration.

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Environments** | Dev, staging, production; config and data separation |
| **Release strategy** | CI gates, canary, blue/green, feature flags |
| **Runtime topology** | API, workers, model gateway, vector stores |
| **Scaling & capacity** | Concurrency, queues, GPU/CPU, regional deployment |
| **Secrets & config** | API keys, tenant credentials, prompt/model routing |
| **Infrastructure as code** | Reproducible stacks and drift control |
| **Rollback & incidents** | Safe revert when quality or SLOs break |
| **Compliance & residency** | Data location, audit, retention |

---

## Guides

### [production-architecture.md](./production-architecture.md)

`#topology` · `#langgraph` · `#multi-agent` · `#cicd`

Users through gateway, agents, RAG path, infra, and eval → canary → production loop.

→ [See more in production-architecture.md](./production-architecture.md)

### [production-components.md](./production-components.md)

`#stack` · `#fastapi` · `#langgraph` · `#docker` · `#cicd`

Eleven production components with responsibilities and typical implementations.

→ [See more in production-components.md](./production-components.md)

### [pipeline-evaluation.md](./pipeline-evaluation.md)

`#cicd` · `#golden-set` · `#quality-gate` · `#canary`

PR checks → candidate matrix → score → baseline gate → staging → production.

→ [See more in pipeline-evaluation.md](./pipeline-evaluation.md)

### [pipeline-evaluation-components.md](./pipeline-evaluation-components.md)

`#ab-test` · `#model` · `#prompt` · `#retrieval` · `#context`

Five evaluation dimensions, candidate changes, and discovery goals.

→ [See more in pipeline-evaluation-components.md](./pipeline-evaluation-components.md)

### [pipeline-evaluation-yaml-sample.md](./pipeline-evaluation-yaml-sample.md)

`#config` · `#yaml` · `#experiment` · `#reproducibility`

Pinned model, prompt, retrieval, context, and golden dataset version for one eval run.

→ [See more in pipeline-evaluation-yaml-sample.md](./pipeline-evaluation-yaml-sample.md)

### [pipeline-scoring-metrics.md](./pipeline-scoring-metrics.md)

`#metrics` · `#retrieval` · `#answers` · `#safety` · `#sla`

Four scoring layers: retrieval, answer, operational, and safety/reliability.

→ [See more in pipeline-scoring-metrics.md](./pipeline-scoring-metrics.md)

### [pipeline-scoring-quality-gate.md](./pipeline-scoring-quality-gate.md)

`#quality-gate` · `#baseline` · `#regression` · `#cost`

Example baseline vs candidates B/C on recall, answers, citations, latency, cost.

→ [See more in pipeline-scoring-quality-gate.md](./pipeline-scoring-quality-gate.md)

### [pipeline-release-policy-simple.md](./pipeline-release-policy-simple.md)

`#release` · `#quality-gate` · `#sla` · `#budget`

PASS criteria: correctness, citations, schema, auth, latency, cost, critical regressions.

→ [See more in pipeline-release-policy-simple.md](./pipeline-release-policy-simple.md)

### [pipeline-criteria-pass-vs-fail.md](./pipeline-criteria-pass-vs-fail.md)

`#report` · `#promote` · `#canary` · `#rollback`

Eval report contents and six steps from gate block to gradual promote or rollback.

→ [See more in pipeline-criteria-pass-vs-fail.md](./pipeline-criteria-pass-vs-fail.md)

### [pipeline-tools-steps.md](./pipeline-tools-steps.md)

`#ci` · `#pr` · `#golden-set` · `#canary` · `#production`

Seven test types and when they run from PR through production feedback.

→ [See more in pipeline-tools-steps.md](./pipeline-tools-steps.md)

## Related

- [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md) · [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md)
- [LLM architecturing — gateway](../llm/llm-architecturing.md) · [LLM cloud services](../llm/llm-cloud-services.md)
- [Example Python directories](../agents/multi-agent-architecture/example-python-directories.md)
- [Guard-rails AWS services](../guard-rails/guardrails-aws-services.md) · [Guard-rails cloud comparison](../guard-rails/guard-rails-cloud-comparison.md)
- [Retrieval AWS multi-agent sample](../retrieval/search/retrieval-aws-multi-agent-sample.md)

## See also

- [Repository overview](../README.md)
