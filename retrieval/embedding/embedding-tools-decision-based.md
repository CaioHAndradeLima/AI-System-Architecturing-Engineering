# Embedding tools decision-based

**Observability and evaluation tooling** for embedding and RAG paths—startup vs scaling. Complements [embedding metrics](./embedding-metrics.md) (what to measure) and [chunking tools decision-based](../chunking/chunking-tools-decision-based.md) (broader pipeline ops).

| Need | Starting option | Scaling option |
|------|-----------------|----------------|
| **Logs and errors** | Python structured logging | Centralized logging and alerting |
| **Latency and throughput** | Application timings | Prometheus/Grafana or cloud monitoring |
| **End-to-end traces** | Basic trace IDs | OpenTelemetry |
| **RAG evaluation** | Python scripts + golden dataset | Automated regression evaluation |
| **LLM and retrieval tracing** | LangSmith or Langfuse | Centralized tracing, cost analysis and evaluation |
| **Embedding usage** | Provider usage reporting | Per-tenant usage aggregation and budgets |

## Notes

- **Embedding usage** ties to [embedding metrics](./embedding-metrics.md) (token volume, cost per document) and [guard-rails](../guard-rails/guard-rails-decision-architecturing-assistance.md) resource controls at scale.
- **RAG evaluation** should run after [embedding migration](./embedding-migration-ingestion-using-another-model.md) or chunker changes as regression gates.
- Cloud-native monitoring options: [guard-rails cloud comparison](../../guard-rails/guard-rails-cloud-comparison.md).

## See also

- [Embedding decision-based](./embedding-decision-based.md)
- [Chunking tools decision-based](../chunking/chunking-tools-decision-based.md)
- [Embedding overview](./README.md)
