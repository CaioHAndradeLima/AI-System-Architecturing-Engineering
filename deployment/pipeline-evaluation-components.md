# Pipeline evaluation components

**Dimensions to vary** when running candidate configurations through the [pipeline evaluation](./pipeline-evaluation.md) golden set—change one axis at a time when possible so comparisons stay interpretable.

| Dimension | Candidate changes | What you want to discover |
|-----------|-------------------|---------------------------|
| **Model** | Model A vs. Model B | Which model produces the best quality/latency/cost trade-off? |
| **Prompt** | Prompt v3 vs. Prompt v4 | Which instructions improve correctness, groundedness, and output consistency? |
| **Retrieval** | Dense vs. hybrid, top-K, filters, reranking | Which setup finds the best evidence and improves final answers? |
| **Context assembly** | Selection strategy, token budget, ordering | Which evidence package helps the model answer correctly? |
| **Generation configuration** | Output limits, supported sampling settings | Which configuration meets quality and operational requirements? |

## Dimension → guides

| Dimension | Docs |
|-----------|------|
| Model | [Select LLM flow](../llm/select-llm-flow.md) · [LLM decision-based](../llm/llm-decision-based.md) · [Deciding sample](../llm/select-llm-deciding-sample.md) |
| Prompt | [Prompt versioning](../prompting/prompt-versioning.md) · [Standard format](../prompting/prompt-standard-format.md) |
| Retrieval | [Evaluate retrieval metrics](../observability-evaluation/evaluate-retrieval-independently-metrics.md) · [Hybrid search](../retrieval/search/retrieval-strategy-hybrid-search-vector-plus-keyword.md) · [Reranking](../retrieval/search/retrieval-strategy-reranking.md) |
| Context assembly | [Context algorithm](../contexting/context-algorithm.md) · [Conversation strategies](../contexting/context-conversation-strategies.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| Generation configuration | [Generation parameters](../llm/llm-generation-parameters.md) · [Prompt variables](../prompting/prompt-relevant-variables-influences.md) |

Score each dimension with the matching metric families in [pipeline evaluation](./pipeline-evaluation.md) (retrieval vs. answer vs. operational). If retrieval metrics improve but answer quality does not, inspect [context assembly](../contexting/context-assembly-flow.md) before promoting the retrieval candidate.

## See also

- [Production components](./production-components.md)
- [Deployment overview](./README.md)
