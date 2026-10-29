# Observability tools

Reference **tracing, metrics, and evaluation platforms** for AI systems—what each tool is good at and how they complement span attributes ([tracing for observability — metrics](./tracing-for-observability-metrics.md)) and incident workflows ([investigate failure by observability data](./investigate-failure-by-observability-data.md)).

| Tool | Typical role |
|------|----------------|
| **LangSmith** | LangChain/LangGraph tracing, debugging, datasets, and evaluations |
| **Langfuse** | LLM tracing, observability, prompt management, and evaluation workflows |
| **OpenTelemetry** | Vendor-neutral instrumentation and trace propagation |
| **Prometheus + Grafana** | Metrics collection and dashboards |
| **Cloud-native monitoring** | Infrastructure metrics, logs, alerts, and distributed tracing |
| **Custom Python evaluation suite** | Reproducible tests for retrieval, correctness, schemas, and domain rules |

## Stack layering

| Layer | Docs |
|-------|------|
| Trace tree and spans | [Tracing for observability](./tracing-for-observability.md) · [Tracing metrics](./tracing-for-observability-metrics.md) |
| Retrieval and index signals | [Storage observability](../retrieval/storaging/storage-observability.md) · [Storage observability tools](../retrieval/storaging/storage-observability-tools.md) · [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) |
| Offline and CI evaluation | [Evaluate retrieval independently — metrics](./evaluate-retrieval-independently-metrics.md) · [Evaluate answer metrics](./evaluate-answer-metrics.md) · [LLM-as-judge vs human](./llm-as-judge-vs-human.md) |
| Post-generation validation | [Output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md) · [Guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md) |
| Incident response | [Investigate failure by observability data](./investigate-failure-by-observability-data.md) · [Poor retrieval scores](./poor-retrieval-scores.md) |
| Cloud monitoring patterns | [Guard-rails cloud comparison](../guard-rails/guard-rails-cloud-comparison.md) · [Retrieval cloud tools](../retrieval/search/retrieval-cloud-tools.md) |

## Custom evaluation beyond traces

LangSmith, Langfuse, and cloud dashboards rarely encode **tenant ACL boundaries**, **citation-to-source rules**, or **domain-specific business logic** on their own. Keep a **custom Python evaluation suite** (golden datasets plus deterministic checks) for filtered-search isolation, citation support, schema contracts, and policy outcomes—aligned with [guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md) and [output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md).


## Reference implementation

**[observability-strategies](https://github.com/CaioHAndradeLima/observability-strategies)** — platform capability matrix in `observability_tools.py` (no vendor SDK deploy). Key: `observability_tools`.

## See also

- [Observability & evaluation overview](./README.md)
- [Chunking tools decision-based](../retrieval/chunking/chunking-tools-decision-based.md)
- [Embedding tools decision-based](../retrieval/embedding/embedding-tools-decision-based.md)
- [Example Python directories — `observability/`](../agents/multi-agent-architecture/example-python-directories.md)
