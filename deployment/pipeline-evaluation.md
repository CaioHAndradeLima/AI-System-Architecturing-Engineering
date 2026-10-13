# Pipeline evaluation

**CI evaluation pipeline** for comparing model, prompt, and retrieval candidates on one golden set before image build and staged rollout ([regression and canary releases](../observability-evaluation/regression-and-canary-releases.md), [production components — offline evaluation](./production-components.md)).

```
                    GIT COMMIT / PR
                           |
                           v
                  Static Code Checks
               Ruff / mypy / pytest
                           |
                           v
                  Build Test Dataset
                           |
                           v
                 GOLDEN EVALUATION SET
                           |
                           v
             +-------------+-------------+
             |             |             |
             v             v             v
        Candidate A    Candidate B    Candidate C
        Model A        Model B        Model A
        Prompt v3      Prompt v3      Prompt v4
        Dense Top-5    Dense Top-5    Hybrid Top-5
             |             |             |
             v             v             v
        Run retrieval + generation for each
        configuration on the same test cases
             |             |             |
             +-------------+-------------+
                           |
                           v
                    Score each run
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        Retrieval      Answer         Operational
        metrics        quality        metrics
             |             |             |
             +-------------+-------------+
                           |
                           v
                  Compare to baseline
                           |
                           v
                   QUALITY GATE
                    /         \
                  FAIL        PASS
                   |            |
                   v            v
             Block release   Package image
                                |
                                v
                              Staging
                                |
                                v
                              Canary
                                |
                                v
                             Production
```

## Phase → guides

| Phase | Docs |
|-------|------|
| Static checks | Unit tests for retrieval, agents, guardrails ([example Python — `tests/`](../agents/multi-agent-architecture/example-python-directories.md)) |
| Golden set | [Observability decision-based — golden dataset](../observability-evaluation/observability-decision-based.md) · [Guardrails practices](../output/output-validation-guardrails-practices.md) |
| Candidate matrix | [Select LLM flow](../llm/select-llm-flow.md) · [Prompt versioning](../prompting/prompt-versioning.md) · [Top-K / hybrid](../retrieval/search/retrieval-strategy-top-k.md) |
| Retrieval scores | [Evaluate retrieval independently — metrics](../observability-evaluation/evaluate-retrieval-independently-metrics.md) |
| Answer scores | [Evaluate answer metrics](../observability-evaluation/evaluate-answer-metrics.md) · [LLM-as-judge vs human](../observability-evaluation/llm-as-judge-vs-human.md) |
| Operational scores | [Tracing metrics](../observability-evaluation/tracing-for-observability-metrics.md) |
| Baseline / quality gate | [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md) |
| Staging → production | [Production architecture](./production-architecture.md) · [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md) |

Run every candidate on the **same frozen golden set** with tagged **model, prompt, and retrieval config** on each run record so baseline comparison is fair. Which axes to vary: [pipeline evaluation components](./pipeline-evaluation-components.md).

## See also

- [Pipeline evaluation components](./pipeline-evaluation-components.md)
- [Production components — CI/CD and offline evaluation](./production-components.md)
- [Deployment overview](./README.md)
