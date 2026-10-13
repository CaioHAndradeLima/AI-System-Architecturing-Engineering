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
| **Scale & maturity** | Runtime, CI/CD, deploy, and feedback by stage |

---

## Guides

### [deployment-decision-based.md](./deployment-decision-based.md)

`#architecture` · `#scale` · `#enterprise` · `#multi-agent`

How runtime, CI/CD, evaluation pipelines, and production operations evolve from startup/prototype through growing production to enterprise / multi-agent.

→ [See more in deployment-decision-based.md](./deployment-decision-based.md)

### [deployment-checklist-flow.md](./deployment-checklist-flow.md)

`#checklist` · `#implementation` · `#cicd` · `#canary`

Production AI delivery checklist—application hardening, offline eval, CI/CD, release, and continuous improvement (deployment decision-based by scale).

→ [See more in deployment-checklist-flow.md](./deployment-checklist-flow.md)

### [production-architecture.md](./production-architecture.md)

`#topology` · `#langgraph` · `#multi-agent` · `#cicd`

End-to-end reference topology for a multi-agent RAG service in production: user path, platform infrastructure, and the eval → deploy → monitor feedback loop (example Python layout, AWS multi-agent sample).

→ [See more in production-architecture.md](./production-architecture.md)

### [production-components.md](./production-components.md)

`#stack` · `#fastapi` · `#langgraph` · `#docker` · `#cicd`

Application stack and operational controls for a production LLM service—fits production architecture and production flow (example Python directories).

→ [See more in production-components.md](./production-components.md)

### [production-flow.md](./production-flow.md)

`#production` · `#feedback` · `#dataset` · `#loop`

Live production feedback loop—telemetry and user signals become labeled cases, offline eval, and gated releases.

Closes the loop in production architecture (monitoring → failure dataset) and pipeline criteria pass vs fail.

→ [See more in production-flow.md](./production-flow.md)

### [production-retrieval-regression-testing.md](./production-retrieval-regression-testing.md)

`#regression` · `#retrieval` · `#versioning` · `#golden-set`

Worked example: production symptom → trace → golden case → retrieval candidate → gate → deploy → monitor.

Extends production flow when the root cause is stale or wrong-version evidence in search results.

→ [See more in production-retrieval-regression-testing.md](./production-retrieval-regression-testing.md)

### [pipeline-evaluation.md](./pipeline-evaluation.md)

`#cicd` · `#golden-set` · `#quality-gate` · `#canary`

CI evaluation pipeline for comparing model, prompt, and retrieval candidates on one golden set before image build and staged rollout (regression and canary releases, production components — offline evaluation).

→ [See more in pipeline-evaluation.md](./pipeline-evaluation.md)

### [pipeline-evaluation-components.md](./pipeline-evaluation-components.md)

`#ab-test` · `#model` · `#prompt` · `#retrieval` · `#context`

Dimensions to vary when running candidate configurations through the pipeline evaluation golden set—change one axis at a time when possible so comparisons stay interpretable.

→ [See more in pipeline-evaluation-components.md](./pipeline-evaluation-components.md)

### [pipeline-evaluation-yaml-sample.md](./pipeline-evaluation-yaml-sample.md)

`#config` · `#yaml` · `#experiment` · `#reproducibility`

Pinned experiment config for one candidate run in pipeline evaluation—store alongside results so baseline comparison replays the same model, prompt, retrieval, and dataset versions (pipeline evaluation components).

→ [See more in pipeline-evaluation-yaml-sample.md](./pipeline-evaluation-yaml-sample.md)

### [pipeline-scoring-metrics.md](./pipeline-scoring-metrics.md)

`#metrics` · `#retrieval` · `#answers` · `#safety` · `#sla`

Score each configuration at multiple layers in pipeline evaluation—after candidates run on the same golden set, aggregate retrieval, answer, operational, and safety signals before the quality gate.

→ [See more in pipeline-scoring-metrics.md](./pipeline-scoring-metrics.md)

### [pipeline-scoring-quality-gate.md](./pipeline-scoring-quality-gate.md)

`#quality-gate` · `#baseline` · `#regression` · `#cost`

Example baseline comparison after pipeline scoring metrics—use fixed thresholds for regressions (citation support, latency, cost) and minimum lifts on quality before canary release.

→ [See more in pipeline-scoring-quality-gate.md](./pipeline-scoring-quality-gate.md)

### [pipeline-release-policy-simple.md](./pipeline-release-policy-simple.md)

`#release` · `#quality-gate` · `#sla` · `#budget`

PASS only if all conditions hold after pipeline scoring and baseline compare (quality gate example)—use as CI/release gate before canary.

→ [See more in pipeline-release-policy-simple.md](./pipeline-release-policy-simple.md)

### [pipeline-criteria-pass-vs-fail.md](./pipeline-criteria-pass-vs-fail.md)

`#report` · `#promote` · `#canary` · `#rollback`

Select the winner and promote it safely after pipeline evaluation candidates are scored (pipeline scoring metrics) and checked against release policy (simple) and quality gate examples.

→ [See more in pipeline-criteria-pass-vs-fail.md](./pipeline-criteria-pass-vs-fail.md)

### [pipeline-tools-steps.md](./pipeline-tools-steps.md)

`#ci` · `#pr` · `#golden-set` · `#canary` · `#production`

When each test runs in the delivery path—from PR through pipeline evaluation to production feedback (pipeline criteria pass vs fail).

→ [See more in pipeline-tools-steps.md](./pipeline-tools-steps.md)

### [deployment-cloud-tools.md](./deployment-cloud-tools.md)

`#aws` · `#azure` · `#gcp` · `#containers` · `#cicd`

Deployment concern → cloud services on AWS, Azure, and Google Cloud—runtime, registry, secrets, observability, async ingestion, model APIs, and CI identity (production controls — queues and secrets, LLM cloud services).

→ [See more in deployment-cloud-tools.md](./deployment-cloud-tools.md)

## Related

- [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md) · [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md)
- [LLM architecturing — gateway](../llm/llm-architecturing.md) · [LLM cloud services](../llm/llm-cloud-services.md)
- [Example Python directories](../agents/multi-agent-architecture/example-python-directories.md)
- [Guard-rails AWS services](../guard-rails/guardrails-aws-services.md) · [Guard-rails cloud comparison](../guard-rails/guard-rails-cloud-comparison.md)
- [Retrieval AWS multi-agent sample](../retrieval/search/retrieval-aws-multi-agent-sample.md)

## See also

- [Repository overview](../README.md)
