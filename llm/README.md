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

## Related

- [Prompt relevant variables](../prompting/prompt-relevant-variables-influences.md)
- [Prompt architecturing decision-based — model configuration](../prompting/prompt-architecturing-decision-based.md)
- [Retrieval cloud tools — LLM inference](../retrieval/search/retrieval-cloud-tools.md)
- [LangGraph generate node](../contexting/context-assembly-langchain-langgraph.md)

## See also

- [Repository overview](../README.md)
