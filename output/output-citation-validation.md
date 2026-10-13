# Citation validation

Answers that cite [retrieved evidence](../contexting/context-info-for-output.md) should only reference **authorized** chunks and only attach claims those chunks support. Validation runs on the draft answer before return ([implementation strategies](./output-implementation-strategies.md)).

```
Generated Answer
       |
       v
Extract Citation IDs
       |
       v
Do IDs exist in authorized evidence set?
       |
   No--+--> Reject / repair
       |
      Yes
       |
       v
Does each cited source support claim?
       |
   No--+--> Flag / repair / abstain
       |
      Yes
       |
       v
Return validated citations
```

**Authorized evidence set** = chunks (and metadata) passed into context assembly after [metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md) and tenant permission checks—not every ID the model might hallucinate.

When support checks fail, prefer **repair** (regenerate with stricter grounding), **abstain** ([similarity / insufficient evidence](../retrieval/search/retrieval-strategy-similarity.md)), or a degraded answer without unsupported citations.

## See also

- [Context info for output](../contexting/context-info-for-output.md)
- [Metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md)
- [Evaluate assembling](../contexting/context-evaluate-assembling.md)
- [Validation failure impact](./output-validation-failure-impact.md)
- [Output overview](./README.md)
