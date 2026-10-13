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

## See also

- [Output implementation strategies](./output-implementation-strategies.md)
- [Validation failure impact](./output-validation-failure-impact.md)
- [Output overview](./README.md)
