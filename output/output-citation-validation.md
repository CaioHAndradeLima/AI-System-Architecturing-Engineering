# Citation validation

Validate **citation IDs and claim support** on the generated answer before delivery ([context info — source metadata](../contexting/context-info-for-output.md)).

```
Generated Answer
      |
      v
Extract Citation IDs
      |
      v
Do IDs exist in this request's
authorized evidence set?
      |
      +---- No ----> Reject / repair
      |
     Yes
      |
      v
Does each cited source support
the associated factual claim?
      |
      +---- No ----> Flag / repair /
      |              abstain as appropriate
      |
     Yes
      |
      v
Return validated citations
```

**Authorized evidence set** = chunks the user may see for this request ([metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md)), not IDs the model invents.

## Reference implementation

**[output-strategies](https://github.com/CaioHAndradeLima/output-strategies)** — citation ID extraction, authorization against the evidence set, and claim–support checks in `validators/citation.py` and `layered_pipeline`. Run `python -m output_strategies.cli evaluate-full` → `citation_validation`; PR gate: `evaluate-pipeline --profile ci-output-eval`. Map: [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/output-strategies/blob/main/docs/LAB_COVERAGE.md).

## See also

- [Output implementation strategies](./output-implementation-strategies.md)
- [Validation failure impact](./output-validation-failure-impact.md)
- [Output overview](./README.md)
