# Retrieval architecture evaluation

What to measure **by layer** when retrieval is exposed as a service, agent, or multi-agent workflow—not only end-to-end answer quality.

| Layer | What to measure |
|-------|-----------------|
| **Retrieval service** | Recall@K, Precision@K, nDCG@K, search latency, empty-result rate |
| **Retrieval agent** | Evidence sufficiency, unnecessary retries, source selection accuracy, tool-call count |
| **Supervisor** | Routing accuracy, task completion, unnecessary delegation, workflow failures |
| **End-to-end system** | Answer correctness, groundedness, task success, p95 latency, cost per request |
| **Security** | Unauthorized retrieval attempts blocked, tenant isolation, ACL enforcement |

## Layer → docs

| Layer | See also |
|-------|----------|
| Retrieval service | [Retrieval metrics observability](./retrieval-metrics-observability.md) · [Implementation flow](./retrieval-implementation-flow.md) |
| Retrieval agent | [Supervisor with retrieval agent](./retrieval-architecture-supervisor-as-agent.md) |
| Supervisor / multi-agent | [Architecture decision](./retrieval-architecture-decision.md) · [Simple loop](./retrieval-architecture-simple-loop.md) · [Multi-agent](./retrieval-architecture-multi-agent.md) |
| End-to-end | [Query evaluation](../embedding/queries/embedding-user-query-evaluation.md) |
| Security | [Guard-rails test use cases](../../guard-rails/guard-rails-test-use-cases.md) · [Metadata filtering](./retrieval-strategy-metadata-filtering.md) |

Eval the **retrieval service** on golden sets before blaming the supervisor for bad answers. Eval **agents and supervisors** with scenarios that require routing, skip, or merge—not only single-hop RAG.

## See also

- [Retrieval decision-based by scale](./retrieval-decision-based.md)
- [Search overview](./README.md)
