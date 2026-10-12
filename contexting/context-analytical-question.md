# Context — analytical question

**Metrics and analytics** questions: context is built from **validated query results**, not (only) document chunks. The LLM explains numbers that the application already computed or fetched.

```
Question
  |
  v
Analytics Agent / SQL tool
  |
  v
Validated query result
  |
  v
Compact table + units + date range
  |
  v
LLM explains the result
```

## Context contents

| Step | Practice |
|------|----------|
| **Analytics Agent / SQL tool** | Parameterized queries; no raw user SQL in production without guardrails ([simple loop](../retrieval/search/retrieval-architecture-simple-loop.md)) |
| **Validated query result** | Row limits, schema checks, tenant scope on data warehouse |
| **Compact table + units + date range** | Structured block in the prompt ([context info — structured results](./context-info-for-output.md)) |
| **LLM explains** | Narrative only—do not let the model invent metrics not in the table |

Combine with doc RAG when the question needs **policy plus numbers** ([multi-hop question](./context-multi-hop-question.md)).

## See also

- [Context assembly flow](./context-assembly-flow.md)
- [Contexting overview](./README.md)
