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

_Guides will be listed here as you add markdown files in this folder (same pattern as [prompting](../prompting/README.md))._

## Related

- [Prompt relevant variables](../prompting/prompt-relevant-variables-influences.md)
- [Prompt architecturing decision-based — model configuration](../prompting/prompt-architecturing-decision-based.md)
- [Retrieval cloud tools — LLM inference](../retrieval/search/retrieval-cloud-tools.md)
- [LangGraph generate node](../contexting/context-assembly-langchain-langgraph.md)

## See also

- [Repository overview](../README.md)
