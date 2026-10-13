# Production components

**Application stack** and **operational controls** for a production LLM service—fits [production architecture](./production-architecture.md) and [production flow](./production-flow.md) ([example Python directories](../agents/multi-agent-architecture/example-python-directories.md)).

## Application stack

| Component | Responsibility | Typical implementation |
|-----------|----------------|------------------------|
| **API layer** | Accept requests, validate input, authenticate users | FastAPI |
| **Agent orchestration** | Coordinate tools and agents | LangGraph |
| **Retrieval service** | Search authorized evidence | Vector DB, BM25, hybrid search |
| **Model integration** | Invoke the selected LLM | LangChain model integration |
| **Output validation** | Validate schemas, citations, and business rules | Pydantic + application code |
| **Containerization** | Package reproducible application environments | Docker |
| **CI/CD** | Test, evaluate, package, and deploy | GitHub Actions |
| **Offline evaluation** | Compare model, prompt, and retrieval variants | Python + pytest + evaluation harness |
| **LLM observability** | Inspect traces, prompts, tool calls, and model behavior | LangSmith or Langfuse |
| **Infrastructure monitoring** | Monitor service health and resource usage | Cloud monitoring + OpenTelemetry |
| **Deployment strategy** | Roll out and reverse releases safely | Staging, canary, rollback |

## Component → guides

| Component | Docs |
|-----------|------|
| API layer | [Guard-rails](../guard-rails/) · [Example Python — `api/`](../agents/multi-agent-architecture/example-python-directories.md) |
| Agent orchestration | [Context assembly LangGraph](../contexting/context-assembly-langchain-langgraph.md) · [Supervisor hierarchical](../agents/multi-agent-architecture/supervisor-hierarchical.md) |
| Retrieval service | [Search overview](../retrieval/search/README.md) · [Hybrid search](../retrieval/search/retrieval-strategy-hybrid-search-vector-plus-keyword.md) · [Metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md) |
| Model integration | [LLM flow](../llm/llm-flow.md) · [LLM architecturing — gateway](../llm/llm-architecturing.md) |
| Output validation | [Output implementation flow](../output/output-implementation-flow.md) · [Citation validation](../output/output-citation-validation.md) |
| Offline evaluation | [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md) · [Evaluate answer metrics](../observability-evaluation/evaluate-answer-metrics.md) |
| LLM observability | [Observability tools](../observability-evaluation/observability-tools.md) · [Tracing for observability](../observability-evaluation/tracing-for-observability.md) |
| Infrastructure monitoring | [Tracing metrics](../observability-evaluation/tracing-for-observability-metrics.md) · [Storage observability tools](../retrieval/storaging/storage-observability-tools.md) |
| Deployment strategy | [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md) |

Keep **retrieval authorization** and **output validation** in application code even when using LangChain/LangGraph abstractions—do not rely on the framework alone for tenant boundaries ([reliable architecture](../contexting/context-reliable-architecture.md)).

## Production controls

| Control | Purpose | Example implementation |
|---------|---------|------------------------|
| **Docker** | Reproducible application packaging | Dockerfile with pinned dependencies |
| **Health checks** | Detect unhealthy service instances | Liveness and readiness endpoints |
| **Timeouts** | Bound slow operations | Per-call and end-to-end deadlines |
| **Retries** | Recover from transient failures | Exponential backoff with jitter |
| **Rate limiting** | Prevent overload and control spend | Gateway limits and provider quotas |
| **Concurrency limits** | Protect model and database capacity | Bounded async workers |
| **Circuit breaker** | Stop repeatedly calling a failing dependency | Temporarily reject or route around failures |
| **Queue and worker** | Handle long-running ingestion and batch tasks | SQS, Azure Service Bus, Pub/Sub, or equivalent |
| **Secrets management** | Protect API keys and credentials | Cloud secret manager |
| **Canary release** | Limit exposure to a new version | Gradual traffic rollout |
| **Rollback** | Restore a known-good release | Versioned image and configuration |

## Control → guides

| Control | Docs |
|---------|------|
| Docker / health | [Pipeline criteria pass vs fail — immutable image](./pipeline-criteria-pass-vs-fail.md) |
| Timeouts / retries / circuit breaker | [LLM retry and fallbacks](../llm/llm-retry-fallbacks-routing.md) · [Output failure impact](../output/output-validation-failure-impact.md) |
| Rate limiting / concurrency | [LLM architecturing — gateway](../llm/llm-architecturing.md) · [Async vs streaming](../llm/llm-async-vs-streaming.md) |
| Queue and worker | [Ingestion procedures](../retrieval/ingestion/ingestion-procedures.md) |
| Secrets | [Guard-rails AWS services](../guard-rails/guardrails-aws-services.md) |
| Canary / rollback | [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md) · [Prompt versioning](../prompting/prompt-versioning.md) |

## See also

- [Pipeline tools and steps](./pipeline-tools-steps.md)
- [Deployment overview](./README.md)
