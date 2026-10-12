# LLM questions

**Topic → key question** map for this section—use as a reading order as guides are added under [llm/](./README.md).

| Topic | Key question |
|-------|--------------|
| **Model selection** | How do I choose the right model for a specific task? |
| **Hosted vs. open-weight** | When should I use a managed API versus deploying my own model? |
| **Model trade-offs** | How do I balance quality, latency, cost, and context length? |
| **Generation parameters** | How do temperature, top-p, and output-token limits affect responses? |
| **Streaming and async** | How do I reduce perceived latency and handle concurrent requests? |
| **Tool calling** | How does an LLM decide to invoke a function or agent tool? |
| **Model routing** | When should simple questions use a smaller model and complex tasks a stronger one? |
| **Fallbacks and retries** | What happens when a model is unavailable, rate-limited, or returns invalid output? |
| **Production deployment** | How do I evaluate models and release configuration changes safely? |

## Where to look today (partial coverage)

| Topic | Existing guides |
|-------|-----------------|
| Model routing | [LLM routing flow](./llm-routing-flow.md) · [Routing policy](./llm-routing-policy.md) |
| Generation parameters | [LLM generation parameters](./llm-generation-parameters.md) · [Prompt relevant variables](../prompting/prompt-relevant-variables-influences.md) |
| Production deployment | [Prompt versioning](../prompting/prompt-versioning.md) · [Prompt architecturing decision-based](../prompting/prompt-architecturing-decision-based.md) |
| Hosted vs. open-weight | [LLM hosted vs open-weight models](./llm-hosted-vs-open-weight-models.md) |
| Hosted vs API (embeddings) | [Embedding hosted vs self-hosted](../retrieval/embedding/embedding-hosted-vs-self-hosted.md) |
| Tool calling / agents | [Retrieval architecture decision](../retrieval/search/retrieval-architecture-decision.md) · [Agents](../agents/) |
| Cloud inference products | [Retrieval cloud tools — LLM inference](../retrieval/search/retrieval-cloud-tools.md) |
| Fallback / failure (prompt side) | [Context architecturing — failure handling](../contexting/context-architecturing-decision-based.md) |

_Gaps in the table above are intentional placeholders until dedicated `llm/` guides land._

## See also

- [LLM overview](./README.md)
