# LLM latency variables and measurement

What to **measure** on inference and multi-step LLM paths—complements [latency sample](./llm-latency-sample.md) (illustrative math) and provider dashboards.

| Metric | What it tells you |
|--------|-------------------|
| **Time to first token (TTFT)** | Perceived responsiveness for streaming UIs |
| **Total response latency** | End-to-end wait until the answer is complete |
| **p50, p95, and p99 latency** | Typical vs tail behavior under load |
| **Tokens per second** | Throughput of generation (where the provider exposes it) |
| **Error and timeout rates** | Availability, limits, and misconfigured timeouts |
| **Cost per request and successful task** | Unit economics; include failed retries in denominators carefully |
| **Number of model calls and retries** | Multi-agent and routing overhead; retry storms |

## Where to slice

| Slice | Why |
|-------|-----|
| **Model ID / route** | Compare [routing policy](./llm-routing-policy.md) paths |
| **Prompt version** | Regressions after [prompt versioning](../prompting/prompt-versioning.md) |
| **Tenant** | Fairness and noisy-neighbor detection ([guard-rails data isolation](../guard-rails/guardrails-data-isolation.md)) |
| **Stage** (retrieve, assemble, generate) | [Architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md) |

Pair **TTFT** with streaming design; pair **total latency** with non-streaming and batch jobs. Retrieval and assembly time often dominate RAG—see [storage observability](../retrieval/storaging/storage-observability.md) and [context evaluate assembling](../contexting/context-evaluate-assembling.md).

## See also

- [LLM generation parameters](./llm-generation-parameters.md)
- [Select LLM flow — measure quality, latency, cost](./select-llm-flow.md)
- [LLM overview](./README.md)
