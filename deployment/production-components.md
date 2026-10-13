# Production components

**Component map** for a production LLM application—what each layer owns and common implementations. Fits the [production architecture](./production-architecture.md) diagram ([example Python directories](../agents/multi-agent-architecture/example-python-directories.md)).

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

## See also

- [Deployment overview](./README.md)
