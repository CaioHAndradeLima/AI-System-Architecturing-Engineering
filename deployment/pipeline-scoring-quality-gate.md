# Pipeline scoring quality gate

**Example baseline comparison** after [pipeline scoring metrics](./pipeline-scoring-metrics.md)—use fixed thresholds for regressions (citation support, latency, cost) and minimum lifts on quality before [canary release](../observability-evaluation/regression-and-canary-releases.md).

| Metric | Baseline | Candidate B | Candidate C |
|--------|----------|-------------|-------------|
| **Recall@5** | 0.78 | 0.86 | 0.90 |
| **Answer correctness** | 84% | 89% | 90% |
| **Citation support** | 95% | 96% | 91% |
| **p95 latency** | 2.0 s | 2.4 s | 4.1 s |
| **Cost per 1,000 requests** | $8 | $10 | $18 |

## Reading this sample

| Candidate | Summary |
|-----------|---------|
| **B** | Better retrieval and answer quality, slightly higher latency and cost, **citation support holds or improves**—typical **pass** if p95 and cost stay within SLO/budget caps. |
| **C** | Best Recall@5 and answer correctness, but **citation support drops** vs baseline and latency/cost jump—likely **fail** or require human review unless product explicitly trades safety for recall. |

Gate rules should be **explicit** (e.g. no drop in citation support; p95 ≤ baseline + 20%; cost per 1k ≤ baseline + 25%) and recorded in CI config next to [pipeline evaluation YAML](./pipeline-evaluation-yaml-sample.md).

## Metric → scoring layer

| Metric | Layer |
|--------|--------|
| Recall@5 | A — Retrieval ([evaluate retrieval metrics](../observability-evaluation/evaluate-retrieval-independently-metrics.md)) |
| Answer correctness | B — Answer ([evaluate answer metrics](../observability-evaluation/evaluate-answer-metrics.md)) |
| Citation support | B + D — Answer and safety ([citation validation](../output/output-citation-validation.md)) |
| p95 latency, cost | C — Operational ([tracing metrics](../observability-evaluation/tracing-for-observability-metrics.md)) |

On **FAIL**, block merge/release and add failing cases to the failure dataset ([investigate failure](../observability-evaluation/investigate-failure-by-observability-data.md)). On **PASS**, proceed to package → staging → canary in [pipeline evaluation](./pipeline-evaluation.md).

## See also

- [Pipeline evaluation components](./pipeline-evaluation-components.md)
- [Deployment overview](./README.md)
