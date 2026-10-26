# Example Python directories

Reference layout for a **multi-agent application**: API entrypoints, orchestration graph, agents, shared services, tools, guardrails, adapters, observability, and evaluation live in separate packages so you can grow each area without tangling imports.

## Layout

```
app/
|
+-- api/
|   +-- routes.py
|
+-- orchestration/
|   +-- graph.py
|   +-- state.py
|
+-- agents/
|   +-- supervisor.py
|   +-- rag_agent.py
|   +-- analytics_agent.py
|
+-- services/
|   +-- retrieval.py
|   +-- embeddings.py
|   +-- reranking.py
|   +-- llm.py
|
+-- tools/
|   +-- jira_tools.py
|   +-- analytics_tools.py
|
+-- guardrails/
|   +-- input_validation.py
|   +-- access_control.py
|   +-- output_validation.py
|
+-- adapters/
|   +-- vector_store.py
|   +-- llm_provider.py
|   +-- jira_client.py
|
+-- observability/
|   +-- tracing.py
|   +-- metrics.py
|
+-- evaluation/
|   +-- golden_dataset.py
|   +-- evaluate.py
|
+-- tests/
    +-- test_retrieval.py
    +-- test_agents.py
    +-- test_guardrails.py
    +-- test_workflows.py
```

## Package roles

| Path | Responsibility |
|------|----------------|
| **`api/`** | HTTP/WebSocket handlers; parse requests, call orchestration, return responses. No business logic. |
| **`orchestration/`** | Workflow graph (sequential, parallel, or hierarchical); shared **state** schema passed between steps. |
| **`agents/`** | One module per agent role: prompts, tool bindings, and “what this agent returns.” |
| **`services/`** | Domain-agnostic capabilities reused by agents (RAG pipeline pieces, LLM wrapper). |
| **`tools/`** | Functions exposed to the model (Jira search, metrics queries); thin wrappers over adapters. |
| **`guardrails/`** | Pre/post checks: PII, authz, injection patterns, schema validation on outputs. |
| **`adapters/`** | External systems (vector DB, LLM vendor, Jira API); swap implementations in one place. |
| **`observability/`** | Traces, spans per agent step, latency/cost metrics. |
| **`evaluation/`** | Golden sets and offline runs against orchestration + agents. |
| **`tests/`** | Unit tests per layer; workflow tests for end-to-end paths. |

## Dependency direction

Keep imports flowing **inward**:

```
api → orchestration → agents → tools / services
                              ↓
                         adapters
guardrails & observability hook at api + orchestration boundaries
```

- **Agents** should call **services** and **tools**, not **adapters** directly (tools use adapters).
- **Orchestration** imports agents and state; it should not import FastAPI/Flask types.
- **Evaluation** may call orchestration the same way **api** does, without going through HTTP.

## Mapping to architecture patterns

| Pattern | Where it lives |
|---------|----------------|
| [Sequential pipeline](./sequential-ai-pipeline.md) | `graph.py` defines ordered nodes; `state.py` accumulates plan → evidence → draft → review |
| [Parallel agents](./parallel-agents-architecture.md) | `graph.py` fan-out/fan-in; coordinator/aggregator nodes or supervisor routing |
| [Hierarchical supervisor](./supervisor-hierarchical.md) | `supervisor.py` + nested subgraphs or delegated agent modules |

Add agents under `agents/` and tools under `tools/` as you add domains; extend `graph.py` rather than growing monolithic route handlers.

## See also

- [Multi-agent architecture README](./README.md)
- [Guardrails strategy](../../guard-rails/guardrails-strategy.md)
- [Guard-rails test use cases](../../guard-rails/guard-rails-test-use-cases.md)
