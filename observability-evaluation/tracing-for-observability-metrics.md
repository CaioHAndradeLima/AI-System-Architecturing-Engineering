# Tracing for observability — metrics and attributes

What to **record on traces and spans** so you can debug latency, cost, quality regressions, and security incidents ([example trace tree](./tracing-for-observability.md)).

Capture on the trace or on the relevant span:

- Trace ID and request ID.
- Model and prompt version.
- Retrieval configuration and index version.
- Duration of each stage.
- Input and output token counts.
- Tool calls, results, and errors.
- Retry counts and timeout events.
- Validation outcomes.
- Estimated or provider-reported costs.

## Where each attribute usually lives

| Attribute | Typical spans | Docs |
|-----------|---------------|------|
| Trace / request ID | Root + all children | [Guard-rails](../guard-rails/) |
| Model / prompt version | Query rewrite, LLM generation, validation | [Prompt versioning](../prompting/prompt-versioning.md) · [LLM flow](../llm/llm-flow.md) |
| Retrieval config / index version | Vector search, reranking | [Storage observability](../retrieval/storaging/storage-observability.md) · [Top-K](../retrieval/search/retrieval-strategy-top-k.md) |
| Stage duration | Every span | [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) |
| Token counts | Context assembly, LLM generation | [Context algorithm](../contexting/context-algorithm.md) · [Generation parameters](../llm/llm-generation-parameters.md) |
| Tool calls / errors | Analytics agent, SQL, secure tools | [Secure tool execution](../output/output-secure-tool-execution-flow.md) |
| Retries / timeouts | LLM, retrieval, validation | [Retry and fallbacks](../llm/llm-retry-fallbacks-routing.md) · [Failure impact](../output/output-validation-failure-impact.md) |
| Validation outcomes | Output validation | [Output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md) |
| Cost | LLM + rerank + judge spans | [LLM latency sample](../llm/llm-latency-sample.md) · [Output decision-based](../output/output-decision-based.md) |

Redact **PII and secrets** in span payloads; keep IDs and hashes needed for audit ([reliable architecture](../contexting/context-reliable-architecture.md)).

## A. Operational metrics

- Request success and error rates.
- p50, p95, and p99 end-to-end latency.
- Model and retrieval timeouts.
- Throughput and concurrent requests.
- Queue depth and ingestion freshness.
- Retry count and provider rate limits.

Dashboards and alerts: [retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) · [LLM latency](../llm/llm-latency-variables-measurement.md) · [storage observability](../retrieval/storaging/storage-observability.md).

## B. AI quality metrics

- Recall@K, Precision@K, and nDCG@K.
- Answer correctness and groundedness.
- Citation support rate.
- Empty retrieval results and abstention rate.
- Tool-call success and routing accuracy.
- Schema validation and repair rates.

These tell you whether the system is finding the right evidence and using it correctly.

Retrieval-only: [evaluate retrieval independently — metrics](./evaluate-retrieval-independently-metrics.md). Answers: [evaluate answer metrics](./evaluate-answer-metrics.md). Validation gates: [output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md). Architecture layers: [retrieval architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md).

## C. Cost and business metrics

- Input/output tokens per request.
- Model and infrastructure cost per successful task.
- Task completion and user adoption.
- User feedback and escalation rate.
- Resolution time or other domain-specific outcomes.

These tell you whether the system provides enough value to justify its operating cost.

Cost attribution on traces: span-level tokens and provider cost fields above. Scale policies: [output decision-based](../output/output-decision-based.md) · [LLM decision-based](../llm/llm-decision-based.md).


## Reference implementation

**[observability-strategies](https://github.com/CaioHAndradeLima/observability-strategies)** — latency, token, and cost rollups in `tracing_metrics.py`. Key: `tracing_metrics`.

## See also

- [Tracing for observability — example tree](./tracing-for-observability.md)
- [Storage observability tools](../retrieval/storaging/storage-observability-tools.md)
- [Observability & evaluation overview](./README.md)
