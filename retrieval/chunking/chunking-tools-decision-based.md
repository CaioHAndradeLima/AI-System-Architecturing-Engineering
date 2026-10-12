# Chunking tools decision-based

**Observability and orchestration** choices for chunking and RAG pipelines at startup vs scale. Pairs with [chunking tools](./chunking-tools.md) (splitters/parsers) and [chunking metrics observability](./chunking-metrics-observability.md) (what to measure).

| Need | Startup option | Scaling option |
|------|----------------|----------------|
| **Application logs** | Python logging | Centralized structured logging |
| **Pipeline metrics** | Basic counters and timings | Prometheus + Grafana or cloud monitoring |
| **Tracing** | OpenTelemetry instrumentation | OpenTelemetry collector and distributed tracing backend |
| **RAG evaluation** | Python scripts + golden dataset | Automated evaluation pipeline and release gates |
| **LLM / RAG observability** | LangSmith or Langfuse | Centralized traces, evaluation results and cost analytics |
| **Job orchestration** | Python script or background task | Queue + workers; Airflow for scheduled or dependency-driven workflows |
| **Error reporting** | Logs and alerts | Error tracking, alert routing and incident workflows |

## Mapping to ingestion/chunking docs

| Need | See also |
|------|----------|
| Job orchestration | [Multi-source ingestion](../ingestion/multi-source-ingestion.md) · [Ingestion architecture engineering](../ingestion/ingestion-architecture-engineering.md) |
| RAG evaluation / metrics | [Chunking metrics observability](./chunking-metrics-observability.md) · [Embedding metrics](../embedding/embedding-metrics.md) · [Embedding tools decision-based](../embedding/embedding-tools-decision-based.md) |
| Pipeline maturity | [Chunking architecturing decision-based](./chunking-architecturing-decision-based.md) |
| Cloud monitoring | [Guard-rails AWS services](../../guard-rails/guardrails-aws-services.md) · [Cloud comparison](../../guard-rails/guard-rails-cloud-comparison.md) |

## See also

- [Chunking tools](./chunking-tools.md)
- [Chunking overview](./README.md)
