# Evaluate answer metrics

End-to-end **answer quality** metrics on golden or sampled conversations—after retrieval and context assembly, including what [output validation](../output/output-validation-via-test-or-guardrails-metrics.md) checks before delivery.

| Metric | Question it answers |
|--------|---------------------|
| **Answer correctness** | Does the answer match the expected answer or facts? |
| **Groundedness** | Are the answer's factual claims supported by the supplied evidence? |
| **Answer relevance** | Does it answer the user's actual question? |
| **Citation support** | Do cited sources support the claims associated with them? |
| **Completeness** | Does it address all important parts of the question? |
| **Abstention quality** | Does it appropriately decline when evidence is insufficient? |
| **Schema validity** | Does the output satisfy the required contract? |

## How this relates to other eval layers

| Layer | Docs |
|-------|------|
| Retrieval only | [Evaluate retrieval independently — metrics](./evaluate-retrieval-independently-metrics.md) · [Poor retrieval scores](./poor-retrieval-scores.md) |
| Context assembly | [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| Post-generation gates | [Output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md) · [Guardrails practices](../output/output-validation-guardrails-practices.md) |
| By architecture layer | [Retrieval architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md) |

If **groundedness** or **citation support** fail but retrieval Recall@K is fine, debug [context assembly](../contexting/context-assembly-flow.md) and [prompt grounding](../prompting/prompt-standard-format.md) before swapping models.

Score subjective metrics with [LLM-as-judge vs human evaluation](./llm-as-judge-vs-human.md) when labels are not purely deterministic.


## Reference implementation

**[observability-strategies](https://github.com/CaioHAndradeLima/observability-strategies)** — groundedness, abstain, and citation alignment in `answer_metrics.py`; pair with [output-strategies](https://github.com/CaioHAndradeLima/output-strategies) for delivery gates. Key: `evaluate_answer_metrics`.

## See also

- [Embedding user query evaluation](../retrieval/embedding/queries/embedding-user-query-evaluation.md)
- [Observability & evaluation overview](./README.md)
