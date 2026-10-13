# Output failure guardrails via LangGraph

**Validation routing** in a LangGraph-style RAG loop: validate after generate, branch to repair, retrieve-more, or safe exit—implements [failure procedure flow](./output-failure-procedure-flow.md) as graph edges.

```
retrieve_node
      |
      v
generate_node
      |
      v
validate_node
      |
      v
route_by_validation
      |
      +---- Valid ------> END
      |
      +---- Repairable -> repair_node
      |                       |
      |                       v
      |                  validate_node
      |
      +---- Insufficient -> retrieve_more
      |                          |
      |                          v
      |                     generate_node
      |
      +---- Unsafe / denied --> safe_exit
```

## Node roles

| Node | Role |
|------|------|
| **retrieve_node** | Fetch evidence ([search](../retrieval/search/)) |
| **generate_node** | LLM answer from assembled context |
| **validate_node** | Schema, citations, policy ([implementation strategies](./output-implementation-strategies.md)) |
| **route_by_validation** | Map result to Valid / Repairable / Insufficient / Unsafe |
| **repair_node** | One bounded fix (format or grounding)—loop back to **validate_node** |
| **retrieve_more** | Widen K or rewrite query; cap loops ([failure impact — repeated failures](./output-validation-failure-impact.md)) |
| **safe_exit** | Abstain, denial message, or escalation—no further auto-retries on **Unsafe / denied** |

Baseline graph layout: [context assembly LangGraph](../contexting/context-assembly-langchain-langgraph.md). Enforce **authorization** before **retrieve_more** and **repair_node** so loops cannot widen tenant scope.

## See also

- [Failure procedure flow](./output-failure-procedure-flow.md)
- [Secure tool execution flow](./output-secure-tool-execution-flow.md)
- [Output overview](./README.md)
