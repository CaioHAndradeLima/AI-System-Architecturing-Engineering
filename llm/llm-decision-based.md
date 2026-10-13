# LLM decision-based by scale

How **chat/completion model and inference ops** evolve from startup/prototype through growing production to enterprise / multi-agent.

| Area | Startup / Prototype | Growing Production | Enterprise / Multi-Agent |
|------|---------------------|--------------------|---------------------------|
| **Model choice** | One capable hosted model | Benchmark several candidates | Approved model catalog and task-specific routing |
| **Configuration** | Sensible defaults | Versioned generation settings | Governed configurations by task and environment |
| **Cost control** | Limit output and unnecessary calls | Track cost per request and task | Budgets, attribution, quotas, and optimization across agents |
| **Latency** | Basic timeout | p95 monitoring and bounded concurrency | End-to-end SLOs and coordinated latency budgets |
| **Streaming / async** | Add when user experience requires it | Handle concurrency and disconnects | Backpressure, capacity management, and distributed tracing |
| **Tool calling** | A few clearly defined tools | Schema validation and bounded steps | Least privilege, audit trails, and per-agent policies |
| **Reliability** | Basic error handling | Retries, rate limits, and tested fallbacks | Multi-provider strategies and controlled degradation |
| **Evaluation** | Manual comparison | Golden datasets and CI evaluations | Continuous evaluation and governed model promotion |
| **Deployment** | Managed API | Canary releases and rollback | Model gateway, policy controls, regional requirements, and auditability |

## Guide links by area

| Area | Docs |
|------|------|
| Model choice | [Select LLM flow](./select-llm-flow.md) · [Hosted vs open-weight](./llm-hosted-vs-open-weight-models.md) · [Deciding sample](./select-llm-deciding-sample.md) |
| Configuration | [Generation parameters](./llm-generation-parameters.md) · [Prompt versioning](../prompting/prompt-versioning.md) |
| Cost / latency | [Latency variables and measurement](./llm-latency-variables-measurement.md) · [Latency sample](./llm-latency-sample.md) |
| Streaming / async | [Async vs streaming](./llm-async-vs-streaming.md) |
| Tool calling | [Routing policy](./llm-routing-policy.md) · [Architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md) |
| Reliability | [Retry, fallbacks, and routing](./llm-retry-fallbacks-routing.md) |
| Evaluation | [LLM questions](./llm-questions.md) · [Prompt architecturing decision-based](../prompting/prompt-architecturing-decision-based.md) |
| Deployment | [LLM architecturing — gateway](./llm-architecturing.md) · [Cloud services](./llm-cloud-services.md) · [Routing policy](./llm-routing-policy.md) |

## See also

- [Output decision-based by scale](../output/output-decision-based.md)
- [Prompt architecturing decision-based](../prompting/prompt-architecturing-decision-based.md)
- [Context architecturing decision-based](../contexting/context-architecturing-decision-based.md)
- [LLM overview](./README.md)
