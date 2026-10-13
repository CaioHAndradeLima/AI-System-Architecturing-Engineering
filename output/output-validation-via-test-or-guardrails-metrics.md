# Output validation via test or guardrails metrics

Metrics and tests for **post-generation validation**—schema, citations, grounding, abstain, blocks, repair, latency, and cost ([implementation strategies](./output-implementation-strategies.md), [failure procedure flow](./output-failure-procedure-flow.md)).

| Metric or test | What it measures |
|----------------|------------------|
| **Schema-validity rate** | Percentage of outputs conforming to the required schema |
| **Citation validity rate** | Percentage of citations resolving to legitimate sources |
| **Citation support rate** | Whether cited evidence actually supports the associated claims |
| **Groundedness rate** | Whether factual claims are supported by available evidence |
| **Abstention quality** | Whether the system declines appropriately when evidence is insufficient |
| **False-block rate** | How often legitimate outputs are incorrectly blocked |
| **Unsafe-action prevention** | Whether unauthorized or prohibited tool actions are rejected |
| **Repair success rate** | How often a bounded repair corrects the original failure |
| **Validation latency** | Time added by validation and recovery |
| **Cost per successful task** | Total cost, including validation, retries, and recovery |

## Related eval docs

| Overlap | See also |
|---------|----------|
| Context / answer quality | [Evaluate answer metrics](../observability-evaluation/evaluate-answer-metrics.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| Retrieval + E2E | [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) |
| Architecture layers | [Architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md) |
| Adversarial / tenant | [Guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md) |

Scenario checklist: [validation guardrails practices](./output-validation-guardrails-practices.md). Track **false-block rate** alongside **unsafe-action prevention**—tight guardrails that block good answers harm UX. Log failure category on every [LangGraph validation route](./output-failure-guardrails-via-langchain.md) for repair and abstain dashboards.

## See also

- [Validation failure impact](./output-validation-failure-impact.md)
- [Output overview](./README.md)
