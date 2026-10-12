# Context evaluate assembling

Metrics and tests for **context assembly** quality—whether the prompt carries the right evidence efficiently, safely, and traceably ([context algorithm](./context-algorithm.md), [reliable architecture](./context-reliable-architecture.md)).

| Metric or test | What it tells you |
|----------------|-------------------|
| **Evidence coverage** | Whether the context contains evidence for the required parts of the question |
| **Redundancy rate** | How much context repeats the same information |
| **Context utilization** | How much of the available budget is used |
| **Relevant evidence per token** | How efficiently the context uses tokens |
| **Citation traceability** | Whether cited sources map to the evidence actually provided |
| **Context assembly latency** | How long filtering, selection, formatting, and token counting take |
| **Unauthorized-evidence tests** | Whether inaccessible content can enter the context |
| **Answer groundedness** | Whether generated claims are supported by the assembled evidence |
| **No-answer handling** | Whether the system admits when evidence is insufficient |

## Related retrieval / RAG metrics

| Overlap | See also |
|---------|----------|
| Token count, groundedness, abstention | [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) |
| Security / tenant tests | [Guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md) · [Architecture evaluation — security](../retrieval/search/retrieval-architecture-evaluation.md) |
| Per-question-type eval | [Simple document](./context-simple-document-question.md) · [Multi-hop](./context-multi-hop-question.md) · [Analytical](./context-analytical-question.md) |

Run **unauthorized-evidence tests** on every change to assembly, caching, or filter logic—not only on retrieval index changes.

## See also

- [Context info for output](./context-info-for-output.md)
- [Contexting overview](./README.md)
