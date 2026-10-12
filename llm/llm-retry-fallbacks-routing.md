# LLM retry, fallbacks, and routing

How to respond when **inference or agent steps fail**—retries, limits, fallback models, and when not to retry. Complements [routing policy](./llm-routing-policy.md) (happy path) and [latency measurement](./llm-latency-variables-measurement.md) (errors, retries).

| Failure | Recommended response |
|---------|---------------------|
| **Temporary network error** | Retry with bounded exponential backoff and jitter |
| **HTTP 429 / rate limit** | Respect provider retry guidance; limit concurrency |
| **Provider timeout** | Apply a timeout and retry only within the request's latency budget |
| **Invalid structured output** | Use constrained output if available; otherwise validate and allow a bounded repair attempt |
| **Model unavailable** | Use a compatible fallback model if it meets the task's quality and security requirements |
| **Poor answer quality** | Investigate prompt, evidence, and model behavior; blindly retrying may reproduce the same failure |
| **Excessive agent loop** | Enforce step limits, time budgets, and explicit stop conditions |

## Fallback routing architecture

```
          Primary Model
                |
                v
          Request succeeds?
            /       \
          Yes        No
           |          |
           v          v
        Return     Classify error
                      |
                      v
             Is fallback appropriate?
                  /         \
                Yes          No
                 |            |
                 v            v
          Fallback Model   Fail safely
                 |
                 v
          Validate response
                 |
                 v
              Return
```

**Classify error** using the [failure table](#llm-retry-fallbacks-and-routing) above (429 → backoff; invalid JSON → repair; poor quality → do not blindly fallback). **Fail safely** = abstain, degraded response, or escalation—not unvalidated output. **Validate response** = schema, grounding, and [guard-rails](../guard-rails/) checks before return.

Pre-register **fallback models** in [select LLM flow](./select-llm-flow.md)—same security and tool contracts as primary. **Quality failures** are not fixed by switching models alone; check [context](../contexting/) and [retrieval](../retrieval/search/) first.

Agent loops: align with [architecture decision](../retrieval/search/retrieval-architecture-decision.md) and [supervisor as agent](../retrieval/search/retrieval-architecture-supervisor-as-agent.md) retry limits.

## See also

- [LLM questions — fallbacks and retries](./llm-questions.md)
- [Prompt versioning — rollback](../prompting/prompt-versioning.md)
- [LLM overview](./README.md)
