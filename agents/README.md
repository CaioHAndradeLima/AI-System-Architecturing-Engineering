# Agents

Tool use, planning loops, memory, and orchestrating multi-step AI workflows.

## Choosing a multi-agent pattern

| Pattern                 | Best fit                                  | Main trade-off                              |
|-------------------------|-------------------------------------------|---------------------------------------------|
| Supervisor              | Dynamic routing to specialists            | Routing and coordination overhead           |
| Sequential pipeline     | Known multi-step process                  | Latency accumulates                         |
| Parallel agents         | Independent tasks                         | Concurrent cost and aggregation complexity  |
| Hierarchical supervisor | Many domains with nested responsibilities | More orchestration and debugging complexity |

Guide files live under [`multi-agent-architecture/`](./multi-agent-architecture/) (no separate index there—this README is the section index).

---

## Guides

### [agentic-ai-evaluation-and-improvement.md](./agentic-ai-evaluation-and-improvement.md)

`#evaluation` · `#verification` · `#test-time-compute` · `#langgraph`

Evaluate task success, tool use, safety, and efficiency; control test-time scaling and use reviewed evaluation gates for self-improvement.

→ [See more in agentic-ai-evaluation-and-improvement.md](./agentic-ai-evaluation-and-improvement.md)

### [sequential-ai-pipeline.md](./multi-agent-architecture/sequential-ai-pipeline.md)

`#sequential` · `#pipeline` · `#rag`

A linear multi-agent workflow: each stage receives the output of the previous stage, transforms it, and passes control
forward until a final user-facing response is produced.

→ [See more in sequential-ai-pipeline.md](./multi-agent-architecture/sequential-ai-pipeline.md)

### [parallel-agents-architecture.md](./multi-agent-architecture/parallel-agents-architecture.md)

`#parallel` · `#coordinator` · `#aggregator`

A fan-out / fan-in multi-agent workflow: a coordinator decomposes the user request, independent agents work on disjoint
subtasks at the same time, and an aggregator merges their outputs into one final response.

→ [See more in parallel-agents-architecture.md](./multi-agent-architecture/parallel-agents-architecture.md)

### [supervisor-hierarchical.md](./multi-agent-architecture/supervisor-hierarchical.md)

`#hierarchical` · `#supervisor` · `#domains`

A tree of supervisors: a main supervisor delegates to domain supervisors, each domain supervisor manages specialist
worker agents, and results roll back up the hierarchy for synthesis and the final user response.

→ [See more in supervisor-hierarchical.md](./multi-agent-architecture/supervisor-hierarchical.md)

### [example-python-directories.md](./multi-agent-architecture/example-python-directories.md)

`#python` · `#project-layout` · `#implementation`

Reference layout for a multi-agent application: API entrypoints, orchestration graph, agents, shared services, tools,
guardrails, adapters, observability, and evaluation live in separate packages so you can grow each area without tangling
imports.

→ [See more in example-python-directories.md](./multi-agent-architecture/example-python-directories.md)
