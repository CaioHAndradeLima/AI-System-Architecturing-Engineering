# Pipeline scoring metrics

**Score each configuration at multiple layers** in [pipeline evaluation](./pipeline-evaluation.md)—after candidates run on the same golden set, aggregate retrieval, answer, operational, and safety signals before the quality gate.

## Layer A: Retrieval quality

**What to measure:** Recall@K, Precision@K, MRR, and nDCG@K against labeled relevant documents.

**Purpose:** Whether the retrieval configuration finds and ranks the right evidence.

→ [Evaluate retrieval independently — metrics](../observability-evaluation/evaluate-retrieval-independently-metrics.md) · [Poor retrieval scores](../observability-evaluation/poor-retrieval-scores.md)

## Layer B: Answer quality

**What to measure:** Correctness, groundedness, citation support, completeness, and abstention quality.

**Purpose:** Whether the model uses retrieved evidence well in the final response.

→ [Evaluate answer metrics](../observability-evaluation/evaluate-answer-metrics.md) · [LLM-as-judge vs human](../observability-evaluation/llm-as-judge-vs-human.md)

## Layer C: Operational performance

**What to measure:** p50/p95 latency, input and output token counts, cost per request, error rate, and retry count.

**Purpose:** Whether the configuration is practical and affordable in production.

→ [Tracing metrics — operational and cost groups](../observability-evaluation/tracing-for-observability-metrics.md) · [LLM latency](../llm/llm-latency-variables-measurement.md)

## Layer D: Safety and reliability

**What to measure:** Schema validity, citation-ID validity, permission enforcement, and prohibited-action prevention.

**Purpose:** Whether the configuration preserves required safety properties.

→ [Output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md) · [Guardrails practices](../output/output-validation-guardrails-practices.md) · [Guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md)

## Using layers in the gate

| Layer | Typical gate |
|-------|----------------|
| A | No Recall@K / nDCG regression vs baseline |
| B | Answer correctness / groundedness / abstention thresholds |
| C | p95 latency and cost per successful task caps |
| D | Zero tolerance on ACL leaks; bounded schema/citation failure rate |

A candidate can pass **A** and fail **B**—tune [context assembly](../contexting/context-assembly-flow.md) or prompt before changing retrieval again ([pipeline evaluation components](./pipeline-evaluation-components.md)).

## See also

- [Pipeline scoring quality gate — example comparison](./pipeline-scoring-quality-gate.md)
- [Pipeline evaluation YAML sample](./pipeline-evaluation-yaml-sample.md)
- [Deployment overview](./README.md)
