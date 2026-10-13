# Validation failure impact

When post-generation checks fail, the system should **fail safely**: repair, retry with constraints, abstain, or escalate—not silently ship bad output ([implementation strategies](./output-implementation-strategies.md), [citation validation](./output-citation-validation.md), [secure tool execution](./output-secure-tool-execution-flow.md)).

| Failure | Recommended response |
|---------|----------------------|
| **Invalid JSON** | Reject for user-facing APIs; one structured **repair** pass (fix-schema prompt or constrained decoder); if still invalid, return safe error and log trace. Route repeated failures via [retry fallbacks and routing](../llm/llm-retry-fallbacks-routing.md). |
| **Unknown citation ID** | Block publish; strip or replace invalid IDs; **regenerate** with explicit allowed ID list from context assembly; if persistent, abstain with “insufficient verified sources.” |
| **Unsupported factual claim** | Flag claim; **repair** answer to remove or soften unsupported sentences; require entailment or judge pass; otherwise abstain ([similarity abstain](../retrieval/search/retrieval-strategy-similarity.md)). |
| **Insufficient retrieval evidence** | Do not invent facts; **abstain**, ask a clarifying question, or offer to search again—same policy as prompt grounding rules. |
| **Conflicting sources** | Surface conflict in answer or abstain; optionally retrieve tie-breakers; never pick one source silently without disclosure. |
| **Unauthorized tool request** | **Block** call; log security event; return policy-safe message to model/user; never execute with elevated credentials ([secure tool flow](./output-secure-tool-execution-flow.md)). |
| **Unsafe output** | Block response; run provider or app safety classifier; return generic refusal; alert if repeated or adversarial ([prompt injection](../prompting/prompt-injection.md)). |
| **Provider timeout** | Retry with backoff; switch model/route per [retry fallbacks and routing](../llm/llm-retry-fallbacks-routing.md); degrade to cached or partial answer only if pre-validated. |
| **Repeated validation failures** | Stop repair loops; **abstain** or hand off to human review; circuit-break high-failure routes; alert on-call with failure taxonomy. |

## See also

- [Output implementation strategies](./output-implementation-strategies.md)
- [Citation validation](./output-citation-validation.md)
- [Secure tool execution flow](./output-secure-tool-execution-flow.md)
- [Retry fallbacks and routing](../llm/llm-retry-fallbacks-routing.md)
- [Similarity / abstain](../retrieval/search/retrieval-strategy-similarity.md)
- [Output overview](./README.md)
