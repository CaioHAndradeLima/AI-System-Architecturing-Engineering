# LLM

**Generation models and inference**: choosing models, hosting (API vs self-hosted), request/response patterns, streaming, tool calling, routing, fallbacks, and runtime cost/latency—downstream of [prompting](../prompting/) and [contexting](../contexting/).

**Embedding models** for retrieval live under [retrieval/embedding](../retrieval/embedding/) (index-time and query-time vectors). This section focuses on **chat/completion** models that produce answers.

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Model selection** | Capability, context window, tools, multimodal, license |
| **Hosted vs self-hosted** | Bedrock, Azure OpenAI, Gemini, vLLM, TGI, Ollama |
| **Inference API** | Messages format, parameters, streaming, batch |
| **Tool / function calling** | Schemas, parallel tools, validation outside the model |
| **Routing & fallbacks** | Primary model, degraded model, escalation |
| **Cost & latency** | Tokens in/out, caching, concurrency limits |
| **Safety at inference** | Provider guardrails + [guard-rails](../guard-rails/) app controls |
| **Observability** | Traces, model/version tags, eval hooks |
| **Multi-agent** | Per-agent model choice ([agents](../agents/)) |

---

## Guides

### [llm-implementation-flow.md](./llm-implementation-flow.md)

`#checklist` · `#implementation` · `#canary`

LLM model selection and generation checklist—from requirements through eval, inference, reliability, and canary deploy.

→ [See more in llm-implementation-flow.md](./llm-implementation-flow.md)

### [llm-questions.md](./llm-questions.md)

`#index` · `#decision-guide`

Topic → key question map for this section—use as a reading order as guides are added under llm/.

→ [See more in llm-questions.md](./llm-questions.md)

### [llm-flow.md](./llm-flow.md)

`#flow` · `#model-selection` · `#rag`

End-to-end path from user question to response, with model selection as an explicit gate before inference.

→ [See more in llm-flow.md](./llm-flow.md)

### [llm-hosted-vs-open-weight-models.md](./llm-hosted-vs-open-weight-models.md)

`#hosted` · `#open-weight` · `#bedrock` · `#vllm`

Hosted (managed API) versus self-hosted open-weight inference for chat/completion models.

For embedding hosting, see embedding hosted vs self-hosted.

→ [See more in llm-hosted-vs-open-weight-models.md](./llm-hosted-vs-open-weight-models.md)

### [select-llm-flow.md](./select-llm-flow.md)

`#benchmark` · `#model-selection` · `#canary`

Benchmark-driven model selection before production—same prompts and evidence across candidates, then quality/SLA gate and canary.

→ [See more in select-llm-flow.md](./select-llm-flow.md)

### [select-llm-deciding-sample.md](./select-llm-deciding-sample.md)

`#benchmark` · `#example` · `#sla`

Illustrative benchmark after select LLM flow—same dataset, same prompts and evidence; numbers are examples only, not vendor-specific.

→ [See more in select-llm-deciding-sample.md](./select-llm-deciding-sample.md)

### [llm-routing-flow.md](./llm-routing-flow.md)

`#routing` · `#small-model` · `#sla`

Model router sends each request to a small, strong, or specialized model based on task signals—then returns a unified result to the caller.

→ [See more in llm-routing-flow.md](./llm-routing-flow.md)

### [llm-routing-policy.md](./llm-routing-policy.md)

`#routing` · `#policy` · `#rag`

Task → model choice for the router below.

Calibrate “small / medium / strong” on your benchmark, not vendor labels alone.

Router signals: LLM routing flow.

→ [See more in llm-routing-policy.md](./llm-routing-policy.md)

### [llm-generation-parameters.md](./llm-generation-parameters.md)

`#temperature` · `#top-p` · `#max-tokens` · `#reasoning`

Inference-time sampling and limits for chat/completion calls.

Version values with prompts and models (prompt versioning).

→ [See more in llm-generation-parameters.md](./llm-generation-parameters.md)

### [llm-latency-sample.md](./llm-latency-sample.md)

`#latency` · `#parallel` · `#multi-agent`

Illustrative end-to-end latency for multi-branch workflows—numbers are examples; measure on your stack (LLM flow).

→ [See more in llm-latency-sample.md](./llm-latency-sample.md)

### [llm-latency-variables-measurement.md](./llm-latency-variables-measurement.md)

`#metrics` · `#ttft` · `#p95` · `#cost`

What to measure on inference and multi-step LLM paths—complements latency sample (illustrative math) and provider dashboards.

→ [See more in llm-latency-variables-measurement.md](./llm-latency-variables-measurement.md)

### [llm-async-vs-streaming.md](./llm-async-vs-streaming.md)

`#streaming` · `#async` · `#ttft`

Two different ideas: streaming improves perceived latency for one generation; async lets the application do other work (or other requests) while I/O-bound steps run.

→ [See more in llm-async-vs-streaming.md](./llm-async-vs-streaming.md)

### [llm-retry-fallbacks-routing.md](./llm-retry-fallbacks-routing.md)

`#retry` · `#fallback` · `#429` · `#agent-loop`

How to respond when inference or agent steps fail—retries, limits, fallback models, and when not to retry.

Complements routing policy (happy path) and latency measurement (errors, retries).

→ [See more in llm-retry-fallbacks-routing.md](./llm-retry-fallbacks-routing.md)

### [llm-cloud-services.md](./llm-cloud-services.md)

`#cloud` · `#aws` · `#azure` · `#gcp`

Capability → provider map for running LLM applications—model APIs, runtime, secrets, monitoring, identity.

Deploy/runtime stack by cloud: deployment cloud tools.

Broader retrieval/agent stack: retrieval cloud tools.

→ [See more in llm-cloud-services.md](./llm-cloud-services.md)

### [llm-architecturing.md](./llm-architecturing.md)

`#gateway` · `#multi-agent` · `#langgraph`

Reference layout: agents call a shared model gateway instead of provider APIs directly—routing, limits, credentials, tracing, and fallbacks live in one place (multi-agent sample).

→ [See more in llm-architecturing.md](./llm-architecturing.md)

### [llm-decision-based.md](./llm-decision-based.md)

`#decision-guide` · `#startup` · `#enterprise` · `#gateway`

How chat/completion model and inference ops evolve from startup/prototype through growing production to enterprise / multi-agent.

→ [See more in llm-decision-based.md](./llm-decision-based.md)

## Related

- [Prompt relevant variables](../prompting/prompt-relevant-variables-influences.md)
- [Prompt architecturing decision-based — model configuration](../prompting/prompt-architecturing-decision-based.md)
- [Retrieval cloud tools — LLM inference](../retrieval/search/retrieval-cloud-tools.md)
- [LangGraph generate node](../contexting/context-assembly-langchain-langgraph.md)

## See also

- [Repository overview](../README.md)
