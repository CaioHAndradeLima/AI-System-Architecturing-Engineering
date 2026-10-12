# Retrieval architecture — simple loop

A **lightweight multi-branch loop**: supervisor routes to a small set of specialists (here **Analytics** and **Knowledge**), each uses one primary tool, then the supervisor **merges findings** and checks **evidence sufficiency** before the final response.

```
User question
     |
     v
Supervisor / Router
     |
     +--------------------+
     |                    |
     v                    v
Analytics Agent      Knowledge Agent
     |                    |
     v                    v
SQL tool              RAG tool
     |                    |
     v                    v
Conversion metrics    Jira + Confluence
     |                    |
     +---------+----------+
               |
               v
        Supervisor combines
        findings and checks
        whether evidence is sufficient
               |
               v
          Final response
```

## Compared to other patterns

| Pattern | This loop | [Multi-agent](./retrieval-architecture-multi-agent.md) | [Retrieval service](./retrieval-architecture-supervisor-as-service.md) |
|---------|-----------|--------------------------------------------------------|------------------------------------------------------------------------|
| **Branches** | Few (often 2) | Several domain agents | Single retrieval path |
| **Merge** | Supervisor + sufficiency check | Supervisor rollup | N/A (one evidence bundle) |
| **Best fit** | One question needs **structured data + docs** | Many domains / tool types | Docs-only Q&A |

Example sources (Jira, Confluence, SQL metrics) are placeholders—wire branches to your real systems and ACLs.

## Implementation notes

- **Router:** activate only branches the question needs; avoid always calling both ([architecture decision](./retrieval-architecture-decision.md)).
- **Knowledge path:** RAG tool should enforce tenant filters and thresholds ([metadata filtering](./retrieval-strategy-metadata-filtering.md), [similarity strategy](./retrieval-strategy-similarity.md)).
- **Sufficiency check:** if combined evidence is weak, abstain or ask clarification—same policy as retrieval-only abstain paths.
- **Tracing:** log branch latency and outputs ([metrics observability](./retrieval-metrics-observability.md)).

Related agent pattern: [parallel agents architecture](../../agents/multi-agent-architecture/parallel-agents-architecture.md).

## See also

- [Retrieval architecture decision](./retrieval-architecture-decision.md)
- [Search overview](./README.md)
