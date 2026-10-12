# Select LLM deciding sample

**Illustrative benchmark** after [select LLM flow](./select-llm-flow.md)—same dataset, same prompts and evidence; numbers are examples only, not vendor-specific.

| Metric | Model A | Model B | Model C |
|--------|---------|---------|---------|
| **Answer quality score** | 92/100 | 89/100 | 82/100 |
| **p95 response latency** | 2.8 s | 1.4 s | 0.8 s |
| **Cost per 1,000 requests** | $12 | $5 | $2 |
| **Tool-call success rate** | 98% | 97% | 90% |

## How to decide (not “pick the highest score”)

| Priority | Favor | Example row |
|----------|--------|-------------|
| **Quality / tool reliability first** (support, compliance Q&A) | Highest quality and tool-call rate within latency SLA | Model A if p95 ≤ SLA; else Model B |
| **Balanced production default** | Quality within ~3 points of best, lower latency and cost | Model B |
| **High volume, simple tasks** | Cost and latency; accept quality floor | Model C if 82/100 and 90% tools meet bar |

Set **minimum bars** before comparing (e.g. tool-call ≥ 95%, quality ≥ 85, p95 ≤ 2 s)—then optimize cost among survivors. Re-run when prompts, retrieval, or [generation parameters](../prompting/prompt-relevant-variables-influences.md) change.

Record results in [prompt / model versioning](../prompting/prompt-versioning.md).

## See also

- [LLM hosted vs open-weight models](./llm-hosted-vs-open-weight-models.md)
- [LLM overview](./README.md)
