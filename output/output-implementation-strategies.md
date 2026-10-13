# Output implementation strategies

Post-generation checks sit **after** [model inference](../llm/llm-flow.md) and **before** the response is returned. Combine layers: cheap deterministic gates first, heavier judges only when needed ([citation validation](./output-citation-validation.md), [failure responses](./output-validation-failure-impact.md)).

| Strategy | How it works | Trade-off |
|----------|--------------|-----------|
| **Deterministic checks** | Parse structured output (JSON schema, regex, required fields); verify citation ID format; enforce length, allowlists, and PII patterns with rule engines. | Fast, cheap, and auditable; misses semantic errors and subtle unsupported claims. |
| **Claim-to-evidence** | Split the answer into atomic claims; retrieve or map each claim to cited chunks; flag claims with no linked evidence or wrong source IDs. | Strong fit for RAG with explicit citations; depends on chunk quality and segmentation heuristics. |
| **NLI (natural language inference)** | For each (claim, passage) pair, run an entailment model: supported / contradicted / neutral relative to the cited text. | Good middle ground vs pure LLM judge; weaker on numerics, tables, and long-context reasoning. |
| **LLM-as-a-judge** | Second model (or same model with a rubric prompt) scores faithfulness, citation use, safety, and format against evidence and policy. | Flexible and catches nuanced issues; higher cost/latency and can inherit judge blind spots—calibrate on eval sets ([evaluate assembling](../contexting/context-evaluate-assembling.md)). |
| **Human review** | Route low-confidence, high-risk, or policy-triggered outputs to a reviewer queue; approve, edit, or reject before delivery. | Highest trust for regulated or high-stakes content; does not scale for real-time chat without tight triage rules. |

## Practical checklist

- [ ] Run deterministic schema and citation-ID checks on every response.
- [ ] Align claim-to-evidence with [context info for output](../contexting/context-info-for-output.md) (paired chunk + source metadata).
- [ ] Log validation scores and failure class for [retry and routing](../llm/llm-retry-fallbacks-routing.md).

## See also

- [Citation validation](./output-citation-validation.md)
- [Output overview](./README.md)
- [Guard-rails strategy](../guard-rails/guardrails-strategy.md)
