# Multi-agent architecture

Patterns for composing multiple LLM agents: routing, pipelines, parallelism, and layered supervision.

## Choosing a pattern

| Pattern | Best fit | Main trade-off |
|---------|----------|----------------|
| Supervisor | Dynamic routing to specialists | Routing and coordination overhead |
| Sequential pipeline | Known multi-step process | Latency accumulates |
| Parallel agents | Independent tasks | Concurrent cost and aggregation complexity |
| Hierarchical supervisor | Many domains with nested responsibilities | More orchestration and debugging complexity |

## Guides

- **Sequential pipeline** — [sequencial-ai-pipeline.md](./sequencial-ai-pipeline.md)
- **Parallel agents** — [parallel-agents-architecture.md](./parallel-agents-architecture.md)
- **Hierarchical supervisor** — [supervisor-hierarchical.md](./supervisor-hierarchical.md)
- **Supervisor** — flat routing to specialists (add a dedicated note here when you have the diagram)
- **Example Python layout** — [example-python-directories.md](./example-python-directories.md)
