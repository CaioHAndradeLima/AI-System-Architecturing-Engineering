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

_Guides will be listed here as you add markdown files in this folder (same pattern as [observability-evaluation](../observability-evaluation/README.md))._

## Related

- [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md) · [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md)
- [LLM architecturing — gateway](../llm/llm-architecturing.md) · [LLM cloud services](../llm/llm-cloud-services.md)
- [Example Python directories](../agents/multi-agent-architecture/example-python-directories.md)
- [Guard-rails AWS services](../guard-rails/guardrails-aws-services.md) · [Guard-rails cloud comparison](../guard-rails/guard-rails-cloud-comparison.md)
- [Retrieval AWS multi-agent sample](../retrieval/search/retrieval-aws-multi-agent-sample.md)

## See also

- [Repository overview](../README.md)
