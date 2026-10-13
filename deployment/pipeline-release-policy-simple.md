# Pipeline release policy (simple)

**PASS only if** all conditions hold after [pipeline scoring](./pipeline-scoring-metrics.md) and baseline compare ([quality gate example](./pipeline-scoring-quality-gate.md))—use as CI/release gate before [canary](../observability-evaluation/regression-and-canary-releases.md).

PASS only if:

- Answer correctness >= 88%
- Citation support >= 95%
- Schema validity >= 99.5%
- No critical authorization failures
- p95 latency <= 3 seconds
- Cost per successful task <= budget
- No unacceptable regression on critical test categories

## Mapping to metrics layers

| Policy line | Layer | Docs |
|-------------|-------|------|
| Answer correctness | B | [Evaluate answer metrics](../observability-evaluation/evaluate-answer-metrics.md) |
| Citation support | B + D | [Citation validation](../output/output-citation-validation.md) |
| Schema validity | D | [Output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md) |
| Authorization failures | D | [Guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md) · [Secure tool execution](../output/output-secure-tool-execution-flow.md) |
| p95 latency | C | [Tracing metrics — operational](../observability-evaluation/tracing-for-observability-metrics.md) |
| Cost per successful task | C | [LLM decision-based — cost](../llm/llm-decision-based.md) |
| Critical test categories | Golden / adversarial | [Guardrails practices](../output/output-validation-guardrails-practices.md) |

Tune thresholds per product risk; document **budget** and **critical categories** in repo config next to [pipeline evaluation YAML](./pipeline-evaluation-yaml-sample.md). Any **FAIL** blocks promote in [pipeline evaluation](./pipeline-evaluation.md) until fixed and re-run.

## See also

- [Deployment overview](./README.md)
