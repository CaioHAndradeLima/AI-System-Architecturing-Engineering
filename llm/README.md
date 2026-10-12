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

### [llm-questions.md](./llm-questions.md)

`#index` · `#decision-guide`

Nine topics and key questions—model choice through safe production deployment.

→ [See more in llm-questions.md](./llm-questions.md)

### [llm-flow.md](./llm-flow.md)

`#flow` · `#model-selection` · `#rag`

Retrieval through prompt, model selection box, inference, validation, response.

→ [See more in llm-flow.md](./llm-flow.md)

### [llm-hosted-vs-open-weight-models.md](./llm-hosted-vs-open-weight-models.md)

`#hosted` · `#open-weight` · `#bedrock` · `#vllm`

Managed APIs vs self-hosted weights—advantages, trade-offs, and flows.

→ [See more in llm-hosted-vs-open-weight-models.md](./llm-hosted-vs-open-weight-models.md)

### [select-llm-flow.md](./select-llm-flow.md)

`#benchmark` · `#model-selection` · `#canary`

Requirements → dataset → candidates → measure → choose → canary.

→ [See more in select-llm-flow.md](./select-llm-flow.md)

### [select-llm-deciding-sample.md](./select-llm-deciding-sample.md)

`#benchmark` · `#example` · `#sla`

Sample Model A/B/C comparison—quality, latency, cost, tool success.

→ [See more in select-llm-deciding-sample.md](./select-llm-deciding-sample.md)

### [llm-routing-flow.md](./llm-routing-flow.md)

`#routing` · `#small-model` · `#sla`

Router to small, strong, or specialized model; merge result.

→ [See more in llm-routing-flow.md](./llm-routing-flow.md)

### [llm-routing-policy.md](./llm-routing-policy.md)

`#routing` · `#policy` · `#rag`

Task-based model choices—rewrite, RAG, synthesis, schema, supervisor, auth.

→ [See more in llm-routing-policy.md](./llm-routing-policy.md)

### [llm-generation-parameters.md](./llm-generation-parameters.md)

`#temperature` · `#top-p` · `#max-tokens` · `#reasoning`

Sampling, output limits, stop sequences, seed, reasoning effort.

→ [See more in llm-generation-parameters.md](./llm-generation-parameters.md)

### [llm-latency-sample.md](./llm-latency-sample.md)

`#latency` · `#parallel` · `#multi-agent`

Sequential vs parallel agent timing example (~3.3s vs ~2.3s).

→ [See more in llm-latency-sample.md](./llm-latency-sample.md)

### [llm-latency-variables-measurement.md](./llm-latency-variables-measurement.md)

`#metrics` · `#ttft` · `#p95` · `#cost`

TTFT, percentiles, tokens/s, errors, cost, calls and retries.

→ [See more in llm-latency-variables-measurement.md](./llm-latency-variables-measurement.md)

### [llm-async-vs-streaming.md](./llm-async-vs-streaming.md)

`#streaming` · `#async` · `#ttft`

Token streaming UX vs concurrent awaits for agents and requests.

→ [See more in llm-async-vs-streaming.md](./llm-async-vs-streaming.md)

## Related

- [Prompt relevant variables](../prompting/prompt-relevant-variables-influences.md)
- [Prompt architecturing decision-based — model configuration](../prompting/prompt-architecturing-decision-based.md)
- [Retrieval cloud tools — LLM inference](../retrieval/search/retrieval-cloud-tools.md)
- [LangGraph generate node](../contexting/context-assembly-langchain-langgraph.md)

## See also

- [Repository overview](../README.md)
