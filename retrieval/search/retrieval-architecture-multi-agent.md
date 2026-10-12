# Retrieval architecture — multi-agent

A **supervisor** fans out to **domain agents** (each with its own tools), then **aggregates** branch results before the final user answer. Retrieval (RAG / search) is one branch—not the only path to evidence.

```
                    Supervisor
                   /    |     \
                  v     v      v
             Knowledge  Data   Engineering
               Agent    Agent    Agent
                  |       |        |
                  v       v        v
              RAG tools  SQL     Jira tools
              / Search   tools   / Docs
                  \       |       /
                   \      |      /
                    v     v     v
                    Supervisor
                         |
                         v
                    Final answer
```

## Branch roles (example)

| Agent | Typical tools | Evidence type |
|-------|---------------|---------------|
| **Knowledge** | RAG, search indexes | Policy/docs chunks ([combined retrieval](./retrieval-strategies-combined.md)) |
| **Data** | SQL, warehouses, metrics APIs | Structured query results |
| **Engineering** | Jira, code search, runbooks | Tickets, links, technical docs |

Names and tools are illustrative—split branches by **who owns the data** and **authorization boundary**, not by LLM persona alone.

## Design notes

- **Supervisor (first pass):** decide which branches to activate (zero, one, or many); pass trusted identity into each branch.
- **Domain agents:** narrow prompts + tool allowlists; Knowledge branch should use [retrieval as service](./retrieval-architecture-supervisor-as-service.md) or [retrieval agent](./retrieval-architecture-supervisor-as-agent.md) behind RAG tools.
- **Supervisor (second pass):** merge, dedupe, resolve conflicts, abstain if branches disagree or evidence is thin.

Pattern alignment: [parallel agents architecture](../../agents/multi-agent-architecture/parallel-agents-architecture.md), [hierarchical supervisor](../../agents/multi-agent-architecture/supervisor-hierarchical.md) when domains nest further.

## Operations

| Concern | Practice |
|---------|----------|
| **Latency** | Parallel branch calls; timeouts per agent |
| **Cost** | Skip inactive branches; cap tool rounds per branch |
| **Security** | Per-branch ACLs; no cross-tenant merge ([data isolation](../../guard-rails/guardrails-data-isolation.md)) |
| **Quality** | Trace each branch; eval end-to-end and per-source ([metrics observability](./retrieval-metrics-observability.md)) |

## See also

- [Retrieval flow](../retrieval-flow.md)
- [Agents overview](../../agents/README.md)
- [Search overview](./README.md)
