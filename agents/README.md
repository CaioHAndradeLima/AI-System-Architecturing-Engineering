# Agents

Tool use, planning loops, memory, and orchestrating multi-step AI workflows.

## Choosing a multi-agent pattern

| Pattern | Best fit | Main trade-off |
|---------|----------|----------------|
| Supervisor | Dynamic routing to specialists | Routing and coordination overhead |
| Sequential pipeline | Known multi-step process | Latency accumulates |
| Parallel agents | Independent tasks | Concurrent cost and aggregation complexity |
| Hierarchical supervisor | Many domains with nested responsibilities | More orchestration and debugging complexity |

Flat **supervisor** routing (single coordinator → specialists) is listed above; a dedicated diagram note can be added when documented.

---

## Guides

### [sequencial-ai-pipeline.md](./multi-agent-architecture/sequencial-ai-pipeline.md)

`#sequential` · `#pipeline` · `#rag`

Fixed-order workflow: planner → retrieval → specialist → reviewer → final response. Best when steps depend on each other and you want a simple, auditable trace.

→ [See more in sequencial-ai-pipeline.md](./multi-agent-architecture/sequencial-ai-pipeline.md)

### [parallel-agents-architecture.md](./multi-agent-architecture/parallel-agents-architecture.md)

`#parallel` · `#coordinator` · `#aggregator`

Coordinator fans out to independent agents (e.g. docs, Jira, metrics), then an aggregator merges results. Best when subtasks are I/O-bound and do not need strict ordering.

→ [See more in parallel-agents-architecture.md](./multi-agent-architecture/parallel-agents-architecture.md)

### [supervisor-hierarchical.md](./multi-agent-architecture/supervisor-hierarchical.md)

`#hierarchical` · `#supervisor` · `#domains`

Main supervisor delegates to domain supervisors; each manages worker agents, then results roll up for the final answer. Best for many domains with nested ownership.

→ [See more in supervisor-hierarchical.md](./multi-agent-architecture/supervisor-hierarchical.md)

### [example-python-directories.md](./multi-agent-architecture/example-python-directories.md)

`#python` · `#project-layout` · `#implementation`

Reference `app/` tree: API, orchestration graph, agents, services, tools, guardrails, adapters, observability, evaluation, and tests—with import direction and pattern mapping.

→ [See more in example-python-directories.md](./multi-agent-architecture/example-python-directories.md)
