# LLM generation parameters

Inference-time **sampling and limits** for chat/completion calls. Version values with prompts and models ([prompt versioning](../prompting/prompt-versioning.md)).

| Parameter | Purpose | Practical guidance |
|-----------|---------|-------------------|
| **`temperature`** | Controls sampling variability | Start low for factual answers |
| **`top_p`** | Restricts sampling to a probability mass of candidate tokens | Usually leave at the provider default initially |
| **`max_output_tokens`** | Limits generated output length | Set based on expected answer size |
| **Stop sequences** | Stops generation at configured sequences | Use carefully to avoid truncating valid output |
| **`seed`** | Requests more reproducible sampling where supported | Not a guarantee of identical outputs across systems or versions |
| **Reasoning effort** | Controls reasoning computation for models that expose this setting | Increase only when the task benefits enough to justify the cost and latency |

## RAG and agents

| Use case | Starting bias |
|----------|----------------|
| Factual RAG answers | Low `temperature`; cap `max_output_tokens` to citation-friendly length |
| Structured JSON / tools | Prefer provider **structured output** where available ([prompt variables](../prompting/prompt-relevant-variables-influences.md)) |
| Supervisor / routing classifiers | Low variability; eval with `seed` only for regression harnesses, not prod diversity |
| Long reasoning tasks | Raise reasoning effort only after [select LLM flow](./select-llm-flow.md) shows lift vs latency/cost |

Avoid tuning **`temperature`** and **`top_p`** together without measurement—change one variable per experiment.

## See also

- [Prompt relevant variables and influences](../prompting/prompt-relevant-variables-influences.md)
- [LLM questions — generation parameters](./llm-questions.md)
- [LLM overview](./README.md)
