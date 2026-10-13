# Deployment checklist flow

**Production AI delivery checklist**—application hardening, offline eval, CI/CD, release, and continuous improvement ([deployment decision-based by scale](./deployment-decision-based.md)).

```
PRODUCTION AI DELIVERY CHECKLIST
================================

A. APPLICATION
   [ ] Package the API and agents in Docker
   [ ] Configure secrets, identity, and networking
   [ ] Add health checks, timeouts, and rate limits
   [ ] Bound retries, concurrency, and agent steps

B. OFFLINE EVALUATION
   [ ] Create versioned golden and holdout datasets
   [ ] Establish a baseline configuration
   [ ] Compare model, prompt, retrieval, and context settings
   [ ] Measure retrieval, answer quality, latency, and cost
   [ ] Add security and regression tests
   [ ] Implement quality gates

C. CI/CD
   [ ] Run Ruff, mypy, pytest, and integration tests
   [ ] Run the required offline evaluations
   [ ] Save reproducible evaluation reports
   [ ] Build and version the tested container image
   [ ] Deploy to staging and run smoke tests

D. PRODUCTION RELEASE
   [ ] Canary the new application/configuration
   [ ] Monitor latency, errors, cost, and quality signals
   [ ] Define rollback thresholds
   [ ] Roll back automatically or manually when required

E. CONTINUOUS IMPROVEMENT
   [ ] Trace model, prompt, retrieval, and tool execution
   [ ] Sample meaningful production failures
   [ ] Sanitize sensitive data and review labels
   [ ] Add approved failures to the golden dataset
   [ ] Re-run experiments before releasing fixes
```

## Section → guides

| Section | Docs |
|---------|------|
| **A. Application** | [Production components — stack & controls](./production-components.md) · [Deployment cloud tools](./deployment-cloud-tools.md) · [Example Python directories](../agents/multi-agent-architecture/example-python-directories.md) |
| **B. Offline evaluation** | [Pipeline evaluation](./pipeline-evaluation.md) · [Pipeline scoring metrics](./pipeline-scoring-metrics.md) · [Release policy (simple)](./pipeline-release-policy-simple.md) · [Pipeline evaluation YAML sample](./pipeline-evaluation-yaml-sample.md) |
| **C. CI/CD** | [Pipeline tools and steps](./pipeline-tools-steps.md) · [Pipeline criteria pass vs fail](./pipeline-criteria-pass-vs-fail.md) |
| **D. Production release** | [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md) · [Production architecture](./production-architecture.md) |
| **E. Continuous improvement** | [Production flow](./production-flow.md) · [Investigate failure](../observability-evaluation/investigate-failure-by-observability-data.md) · [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md) |

Full stack checklists: [prompt implementation flow](../prompting/prompt-implementation-flow.md) · [LLM implementation flow](../llm/llm-implementation-flow.md) · [output implementation flow](../output/output-implementation-flow.md) · [observability implementation flow](../observability-evaluation/observability-implementation-flow.md).

## See also

- [Deployment overview](./README.md)
