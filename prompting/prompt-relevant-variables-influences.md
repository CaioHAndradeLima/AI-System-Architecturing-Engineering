# Prompt relevant variables and influences

**Generation parameters** and model choice affect quality, cost, and reliability—version and eval them with prompts ([prompt versioning](./prompt-versioning.md)).

| Parameter | What it controls | Practical guidance |
|-----------|------------------|-------------------|
| **Temperature** | Randomness in token selection for models that support it | Start low for factual RAG; evaluate before changing |
| **Maximum output tokens** | How long the generated response can be | Set a limit that fits the task and prevents runaway output |
| **Top-p** | Sampling from a probability mass of candidate tokens | Usually tune only when needed; avoid blindly tuning it alongside temperature |
| **Stop sequences** | Conditions that stop generation | Useful for some formats and integrations, but can truncate valid output |
| **Structured output mode** | Constrains the output format where supported | Prefer schema-constrained generation when reliable structured data is required |
| **Model choice** | Capability, latency, context size, cost, and tool support | Evaluate on representative tasks instead of selecting by reputation alone |

Full parameter list including **seed** and **reasoning effort**: [LLM generation parameters](../llm/llm-generation-parameters.md).

## Related stack settings

Parameters above sit beside **input** influences documented elsewhere:

| Influence | Docs |
|-----------|------|
| Retrieved context size | [Context algorithm — token budget](../contexting/context-algorithm.md) |
| Embedding / retrieval | [Retrieval decision-based](../retrieval/search/retrieval-decision-based.md) |
| Output contract in prompt | [Standard format — OUTPUT CONTRACT](./prompt-standard-format.md) |

Record parameter values in each [prompt version](./prompt-versioning.md) record alongside template and model name.

## See also

- [LLM section](../llm/) — model hosting and inference (chat/completion)
- [Embedding hosted vs self-hosted](../retrieval/embedding/embedding-hosted-vs-self-hosted.md)
- [Prompting overview](./README.md)
