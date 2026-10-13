# Output implementation strategies

How to **validate LLM outputs** against evidence and policy—pick strategies by risk, cost, and coverage ([LLM flow — output validation](../llm/llm-flow.md)).

| Strategy | How it works | Trade-off |
|----------|--------------|-----------|
| **Deterministic checks** | Validate IDs, dates, values, and explicit business rules | Reliable for known rules; limited semantic coverage |
| **Claim-to-evidence matching** | Extract claims and check each against the evidence | More detailed, but claim extraction can miss or distort claims |
| **NLI model** | Estimate whether evidence entails or contradicts a claim | Faster than some LLM checks, but can struggle with complex context |
| **LLM-as-a-judge** | Ask a model to compare the answer with the evidence | Flexible, but adds cost and can make its own mistakes |
| **Human review** | Have a person verify critical outputs | Strong for high-impact decisions, but expensive and slower |

Layer cheap deterministic checks first; add claim/NLI or judge on high-risk paths. On failure: [validation failure impact](./output-validation-failure-impact.md).

## See also

- [Citation validation](./output-citation-validation.md)
- [Evaluate assembling](../contexting/context-evaluate-assembling.md)
- [Output overview](./README.md)
