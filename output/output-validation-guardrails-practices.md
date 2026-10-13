# Output validation guardrails practices

**Test and review scenarios** for post-generation validation—cover in golden sets, CI eval, and adversarial suites ([metrics](./output-validation-via-test-or-guardrails-metrics.md), [guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md)).

Exercise the pipeline with cases like:

- Correct answers with valid citations.
- Correct-looking answers with fabricated citations.
- Unsupported causal claims.
- Missing or contradictory evidence.
- Malformed JSON.
- Prompt injection inside retrieved documents.
- Attempts to access another tenant's data.
- Tool calls with invalid or unauthorized arguments.
- Legitimate answers that should not be blocked.

## What each scenario checks

| Scenario | Primary signal |
|----------|----------------|
| Valid citations | Citation validity + support rate |
| Fabricated citations | Citation validity; hallucinated IDs |
| Unsupported causal claims | Groundedness; claim-to-evidence |
| Missing / contradictory evidence | Abstention quality; failure procedure ([insufficient / conflict](./output-validation-failure-impact.md)) |
| Malformed JSON | Schema-validity rate; one repair attempt |
| Injection in retrieved docs | Untrusted content boundaries ([prompt injection](../prompting/prompt-injection.md)) |
| Cross-tenant access | Unsafe-action prevention; metadata filters |
| Bad tool calls | [Secure tool execution flow](./output-secure-tool-execution-flow.md) |
| Legitimate not blocked | False-block rate |

Include **negative controls** (legitimate answers) whenever tightening validators—regressions often show up as false blocks before unsafe leaks.

## See also

- [Failure procedure flow](./output-failure-procedure-flow.md)
- [Citation validation](./output-citation-validation.md)
- [Output overview](./README.md)
