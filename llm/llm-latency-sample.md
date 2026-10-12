# LLM latency sample

**Illustrative** end-to-end latency for multi-branch workflows—numbers are examples; measure on your stack ([LLM flow](./llm-flow.md)).

## Sequential execution

```
Supervisor -> Knowledge Agent -> Analytics Agent -> Synthesis
    0.3 s          1.2 s             1.0 s           0.8 s
```

Approximate total: **3.3 seconds** + overhead

## Parallel execution

```
                 +-> Knowledge Agent --+
Supervisor ------|                      |--> Synthesis
                 +-> Analytics Agent ---+
```

Approximate total: **0.3 + max(1.2, 1.0) + 0.8 = 2.3 seconds** + overhead

## Takeaways

| Pattern | When |
|---------|------|
| **Sequential** | Steps depend on prior agent output; simpler traces |
| **Parallel** | Independent branches (docs + SQL)—[simple loop](../retrieval/search/retrieval-architecture-simple-loop.md), [parallel agents](../agents/multi-agent-architecture/parallel-agents-architecture.md) |

Overhead includes retrieval, context assembly, and **model routing** ([routing policy](./llm-routing-policy.md)). Parallelism saves wall-clock time only when branches do not block each other and the supervisor waits for all required results before synthesis.

Track **p95** per node in traces ([architecture evaluation](../retrieval/search/retrieval-architecture-evaluation.md)). Full metric list: [latency variables and measurement](./llm-latency-variables-measurement.md).

## See also

- [LLM routing flow](./llm-routing-flow.md)
- [LLM overview](./README.md)
