# Output failure procedure flow

After **generation**, classify validation failures and apply the matching branch—pairs with the [failure impact table](./output-validation-failure-impact.md).

```
Generate
   |
   v
Validate output
   |
   +---- Valid ----> Return response
   |
 Invalid
   |
   v
Classify failure
   |
   +--> Schema error
   |       |
   |       v
   |   One repair attempt
   |
   +--> Missing evidence
   |       |
   |       v
   |   Retrieve more / abstain
   |
   +--> Authorization failure
   |       |
   |       v
   |   Deny; do not retry action
   |
   +--> Repeated failure
           |
           v
      Safe fallback / escalation
```

## Branch → impact table

| Branch | See [validation failure impact](./output-validation-failure-impact.md) |
|--------|------------------------------------------------------------------------|
| Schema error | Invalid JSON or missing fields |
| Missing evidence | Insufficient retrieval evidence; unsupported factual claim |
| Authorization failure | Unauthorized tool request |
| Repeated failure | Repeated validation failures |

**Retrieve more** only within latency budget and ACL scope ([search](../retrieval/search/), [metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md)). **One repair attempt** aligns with constrained output ([generation parameters](../llm/llm-generation-parameters.md)).

## Reference implementation

**[output-strategies](https://github.com/CaioHAndradeLima/output-strategies)** — branch mapping (repair, retrieve-more, deny, escalate) in `failure_routing.py`; scenario metrics in `evaluate-scenarios` → `failure_routing`. Map: [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/output-strategies/blob/main/docs/LAB_COVERAGE.md).

## See also

- [Output implementation strategies](./output-implementation-strategies.md)
- [Secure tool execution flow](./output-secure-tool-execution-flow.md)
- [LLM retry and fallbacks](../llm/llm-retry-fallbacks-routing.md)
- [Output overview](./README.md)
