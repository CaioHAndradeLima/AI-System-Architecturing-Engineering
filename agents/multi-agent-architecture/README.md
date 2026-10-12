# Multi-agent architecture

Patterns for composing multiple LLM agents: routing, pipelines, parallelism, and layered supervision.

Overview and pattern comparison: [agents README](../README.md).

## Choosing a pattern

| Pattern | Best fit | Main trade-off |
|---------|----------|----------------|
| Supervisor | Dynamic routing to specialists | Routing and coordination overhead |
| Sequential pipeline | Known multi-step process | Latency accumulates |
| Parallel agents | Independent tasks | Concurrent cost and aggregation complexity |
| Hierarchical supervisor | Many domains with nested responsibilities | More orchestration and debugging complexity |

---

## Guides

### [sequencial-ai-pipeline.md](./sequencial-ai-pipeline.md)

`#sequential` · `#pipeline` · `#rag`

Fixed-order workflow: planner → retrieval → specialist → reviewer → final response. Best when steps depend on each other and you want a simple, auditable trace.

→ [See more in sequencial-ai-pipeline.md](./sequencial-ai-pipeline.md)

### [parallel-agents-architecture.md](./parallel-agents-architecture.md)

`#parallel` · `#coordinator` · `#aggregator`

Coordinator fans out to independent agents (e.g. docs, Jira, metrics), then an aggregator merges results. Best when subtasks are I/O-bound and do not need strict ordering.

→ [See more in parallel-agents-architecture.md](./parallel-agents-architecture.md)

### [supervisor-hierarchical.md](./supervisor-hierarchical.md)

`#hierarchical` · `#supervisor` · `#domains`

Main supervisor delegates to domain supervisors; each manages worker agents, then results roll up for the final answer. Best for many domains with nested ownership.

→ [See more in supervisor-hierarchical.md](./supervisor-hierarchical.md)

### [example-python-directories.md](./example-python-directories.md)

`#python` · `#project-layout` · `#implementation`

Reference `app/` tree: API, orchestration graph, agents, services, tools, guardrails, adapters, observability, evaluation, and tests—with import direction and pattern mapping.

→ [See more in example-python-directories.md](./example-python-directories.md)
