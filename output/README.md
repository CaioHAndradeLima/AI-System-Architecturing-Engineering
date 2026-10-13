# Output

What happens **after model generation** and **before the user sees a response**: schema and policy checks, citation grounding, tool execution boundaries, and safe handling when validation fails.

Output validation sits at the end of [LLM flow](../llm/llm-flow.md) (after inference) and consumes the same evidence and metadata that [context assembly](../contexting/context-assembly-flow.md) prepared upstream.

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Implementation strategies** | Deterministic checks through human review for grounded answers |
| **Citation validation** | Authorized source IDs and claim–evidence alignment |
| **Tool execution** | Policy gates, sandboxing, scoped credentials |
| **Failure handling** | Repair, retry, abstain, and escalation by failure type |

---

## Guides

### [output-implementation-strategies.md](./output-implementation-strategies.md)

`#validation` · `#groundedness` · `#quality`

Five common post-generation validation strategies—from cheap deterministic gates to LLM-as-a-judge and human review—and when each fits your latency and risk budget.

→ [See more in output-implementation-strategies.md](./output-implementation-strategies.md)

### [output-citation-validation.md](./output-citation-validation.md)

`#citations` · `#grounding` · `#rag`

Confirm cited IDs exist in the authorized evidence set and that each source supports the claims attached to it before returning Answer + Citations.

→ [See more in output-citation-validation.md](./output-citation-validation.md)

### [output-secure-tool-execution-flow.md](./output-secure-tool-execution-flow.md)

`#tools` · `#security` · `#sandbox`

Run LLM-proposed tool calls only after guardrail checks, with sandboxed execution and bounded results returned to the model.

→ [See more in output-secure-tool-execution-flow.md](./output-secure-tool-execution-flow.md)

### [output-validation-failure-impact.md](./output-validation-failure-impact.md)

`#failures` · `#abstain` · `#operations`

Nine validation failure modes mapped to recommended responses—repair prompts, reroute, block, or escalate—so delivery stays reliable under edge cases.

→ [See more in output-validation-failure-impact.md](./output-validation-failure-impact.md)

### [output-failure-procedure-flow.md](./output-failure-procedure-flow.md)

`#flow` · `#repair` · `#abstain` · `#escalation`

Validate → classify → schema repair, retrieve/abstain, deny, or fallback.

→ [See more in output-failure-procedure-flow.md](./output-failure-procedure-flow.md)

### [output-failure-guardrails-via-langchain.md](./output-failure-guardrails-via-langchain.md)

`#langgraph` · `#routing` · `#repair` · `#safe-exit`

retrieve → generate → validate → route: END, repair, retrieve_more, safe_exit.

→ [See more in output-failure-guardrails-via-langchain.md](./output-failure-guardrails-via-langchain.md)

## Related

- [LLM flow](../llm/llm-flow.md) · [LangGraph validate node](../contexting/context-assembly-langchain-langgraph.md)
- [Evaluate assembling](../contexting/context-evaluate-assembling.md)
- [Prompt injection](../prompting/prompt-injection.md) · [Retry fallbacks and routing](../llm/llm-retry-fallbacks-routing.md)

## See also

- [Repository overview](../README.md)
