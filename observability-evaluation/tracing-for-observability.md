# Tracing for observability

Example **distributed trace** for a multi-agent RAG request: one trace ID ties API, supervisor, agents, retrieval, generation, validation, and response—so latency and failures are attributable to a step ([storage observability tools — tracing](../retrieval/storaging/storage-observability-tools.md), [`observability/` package](../agents/multi-agent-architecture/example-python-directories.md)).

```
Trace: request_123
|
+-- Span 1: API request
|
+-- Span 2: Supervisor
|   |
|   +-- Span 3: Knowledge Agent
|   |   |
|   |   +-- Span 4: Query rewrite
|   |   +-- Span 5: Vector search
|   |   +-- Span 6: Reranking
|   |   +-- Span 7: Context assembly
|   |   +-- Span 8: LLM generation
|   |
|   +-- Span 9: Analytics Agent
|       |
|       +-- Span 10: SQL query
|
+-- Span 11: Output validation
|
+-- Span 12: Final response
```

## Span → system concern

| Span | Typical signals | Docs |
|------|-----------------|------|
| **API request** | Auth, tenant ID, request size | [Guard-rails](../guard-rails/) |
| **Supervisor** | Routing, delegation count | [Supervisor hierarchical](../agents/multi-agent-architecture/supervisor-hierarchical.md) · [Retrieval supervisor agent](../retrieval/search/retrieval-architecture-supervisor-as-agent.md) |
| **Knowledge Agent** | Agent-level latency, retries | [RAG agent patterns](../retrieval/search/) |
| **Query rewrite** | Rewritten query text, model/tokens | [Context scoring — rewriting](../contexting/context-scoring-math.md) |
| **Vector search** | K, latency, empty hits | [Search strategies](../retrieval/search/README.md) |
| **Reranking** | Pre/post rank, rerank model latency | [Reranking strategy](../retrieval/search/retrieval-strategy-reranking.md) |
| **Context assembly** | Token count, chunk IDs | [Assembly flow](../contexting/context-assembly-flow.md) |
| **LLM generation** | Model, tokens in/out, finish reason | [LLM flow](../llm/llm-flow.md) · [Async vs streaming](../llm/llm-async-vs-streaming.md) |
| **Analytics Agent** | Tool choice, SQL duration | [Parallel agents](../agents/multi-agent-architecture/parallel-agents-architecture.md) |
| **SQL query** | Rows returned, auth on data source | [Secure tool execution](../output/output-secure-tool-execution-flow.md) |
| **Output validation** | Pass/fail category, repair loops | [Output implementation flow](../output/output-implementation-flow.md) |
| **Final response** | Time to first byte (if streaming), status | [Output overview](../output/README.md) |

Attribute checklist: [tracing for observability — metrics](./tracing-for-observability-metrics.md). Propagate **tenant ID** on every span for per-tenant dashboards ([prompt architecturing decision-based](../prompting/prompt-architecturing-decision-based.md)).

## See also

- [Tracing for observability — metrics and attributes](./tracing-for-observability-metrics.md)
- [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md)
- [Evaluate answer metrics](./evaluate-answer-metrics.md)
- [Observability & evaluation overview](./README.md)
