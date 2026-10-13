# Production retrieval regression testing

**Worked example:** production symptom → trace → golden case → retrieval candidate → gate → deploy → monitor. Extends [production flow](./production-flow.md) when the root cause is **stale or wrong-version evidence** in search results.

Suppose users report that the assistant keeps returning an outdated refund policy.

1. Tracing shows the old policy is ranked above the current version.
2. You add a sanitized test case to the golden dataset.
3. You compare current retrieval against a candidate with document-version filtering.
4. You evaluate Recall@K, current-version selection, answer correctness, and latency.
5. The quality gate verifies that the candidate improves the intended behavior without breaking other cases.
6. You deploy it to staging and then a canary population.
7. You monitor for continued stale-document failures.

## Step → practice

| Step | Action | Docs |
|------|--------|------|
| 1. Trace ranking | Inspect span for retrieved chunk IDs, scores, version metadata | [Tracing for observability](../observability-evaluation/tracing-for-observability.md) · [Context info — source metadata](../contexting/context-info-for-output.md) |
| 2. Golden case | Question + expected current doc ID; no PII in stored case | [Pipeline evaluation YAML — dataset_version](./pipeline-evaluation-yaml-sample.md) · [Guardrails practices](../output/output-validation-guardrails-practices.md) |
| 3. Candidate config | e.g. filter `document_version=current` or boost latest effective date | [Metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md) · [Pipeline evaluation components — retrieval](./pipeline-evaluation-components.md) |
| 4. Metrics | Retrieval layer + answer + ops | [Pipeline scoring metrics](./pipeline-scoring-metrics.md) · add **current-version selection** rate on labeled pairs |
| 5. Quality gate | Must fix refund cases; no regression on other categories | [Release policy (simple)](./pipeline-release-policy-simple.md) · [Quality gate example](./pipeline-scoring-quality-gate.md) |
| 6. Staging / canary | Same manifest as passing eval run | [Pipeline criteria pass vs fail](./pipeline-criteria-pass-vs-fail.md) |
| 7. Monitor | Alert on stale-doc failure category in production feedback | [Production flow](./production-flow.md) · [Investigate failure](../observability-evaluation/investigate-failure-by-observability-data.md) |

Also verify **ingestion freshness** and index version on traces—ranking fixes fail if the index still lacks the current policy ([storage observability](../retrieval/storaging/storage-observability.md), [ingestion procedures](../retrieval/ingestion/ingestion-procedures.md)).

## See also

- [Poor retrieval scores](../observability-evaluation/poor-retrieval-scores.md)
- [Deployment overview](./README.md)
