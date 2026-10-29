# LLM-as-judge vs human evaluation

Two ways to score **answers against evidence and rubrics** when deterministic checks are not enough ([evaluate answer metrics](./evaluate-answer-metrics.md), [output implementation strategies — LLM-as-a-judge](../output/output-implementation-strategies.md)).

## LLM-as-a-judge

An **evaluator model** scores the response against a rubric and the available evidence.

**Example rubric questions:**

- Are the claims supported?
- Are any required facts missing?
- Are citations appropriate?
- Does the response acknowledge uncertainty?

| | |
|--|--|
| **Advantages** | Scalable; relatively fast to automate; useful for regression comparisons |
| **Limitations** | Evaluator bias; inconsistent judgments; sensitivity to prompt wording; possible agreement with the same errors made by the answer model |

Use a **different model or prompt** than the generator when you can; log rubric version and evaluator model on every score. Pair with golden-set **human spot checks** before trusting a judge for release gates.

## Human evaluation

**Domain experts or trained reviewers** score answers against explicit criteria.

| | |
|--|--|
| **Advantages** | Useful for ambiguous cases; ensures business correctness; identifies subtle reasoning failures; used for calibrating automated judges |
| **Limitations** | Expensive; slower; potentially inconsistent across different reviewers |

Define a **shared rubric** and calibration set so reviewers align; use human labels to tune when LLM-as-judge disagrees with [guardrails practices](../output/output-validation-guardrails-practices.md) expectations.

## When to use which

| Situation | Prefer |
|-----------|--------|
| CI regression on hundreds of cases | LLM-as-judge (fixed rubric) |
| High-risk or regulated decisions | Human review on a sample or full gate |
| New product or domain | Human labels first, then distill rubric for judge |
| Judge drift or false passes | Re-calibrate with human evaluation |


## Reference implementation

**[observability-strategies](https://github.com/CaioHAndradeLima/observability-strategies)** — offline rubric struct in `llm_judge.py`; optional live judge when API keys are set (CI skips). Key: `llm_judge_vs_human`.

## See also

- [Output decision-based by scale](../output/output-decision-based.md)
- [Output validation metrics](../output/output-validation-via-test-or-guardrails-metrics.md)
- [Observability & evaluation overview](./README.md)
