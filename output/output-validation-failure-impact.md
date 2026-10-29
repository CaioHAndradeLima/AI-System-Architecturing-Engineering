# Validation failure impact

When post-generation or tool validation fails, respond in a **bounded, safe** way—repair, abstain, deny, or retry only where policy allows.

| Failure | Recommended response |
|---------|---------------------|
| **Invalid JSON or missing fields** | Retry with constrained output or perform one bounded repair attempt |
| **Unknown citation ID** | Reject the citation and regenerate or abstain |
| **Unsupported factual claim** | Remove or qualify the claim, or regenerate using verified evidence |
| **Insufficient retrieval evidence** | Retrieve more evidence, ask a clarifying question, or abstain |
| **Conflicting sources** | Apply an explicit source-precedence policy or report the conflict |
| **Unauthorized tool request** | Deny the request; do not retry the same action automatically |
| **Unsafe output** | Block or transform according to policy; escalate when necessary |
| **Provider timeout** | Apply a bounded retry if the deadline permits |
| **Repeated validation failures** | Stop, return a safe failure response, and log the failure category |

## Reference implementation

**[output-strategies](https://github.com/CaioHAndradeLima/output-strategies)** — failure categories and safe routes in `failure_classifier.py` / `failure_routing.py`. Run `evaluate-full` → `failure_impact`. Map: [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/output-strategies/blob/main/docs/LAB_COVERAGE.md).

## See also

- [Failure procedure flow](./output-failure-procedure-flow.md)
- [Output implementation strategies](./output-implementation-strategies.md)
- [Citation validation](./output-citation-validation.md)
- [Secure tool execution flow](./output-secure-tool-execution-flow.md)
- [Retry, fallbacks, and routing](../llm/llm-retry-fallbacks-routing.md)
- [Similarity / abstain](../retrieval/search/retrieval-strategy-similarity.md)
- [Output overview](./README.md)
