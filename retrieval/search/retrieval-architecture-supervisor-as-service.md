# Retrieval architecture — supervisor with retrieval as a service

The **main or supervisor agent** does not embed vector search inline—it calls a **retrieval tool** (or service) that runs the full query-time pipeline and returns **relevant evidence** for answer generation.

```
User
  |
  v
Supervisor / Main Agent
  |
  v
Retrieval Tool
  |
  +--> Query embedding
  +--> Vector search
  +--> Keyword search
  +--> Metadata / ACL filters
  +--> Reranking
  |
  v
Relevant evidence
  |
  v
Main Agent generates answer
```

## Why encapsulate retrieval

| Benefit | Detail |
|---------|--------|
| **Single policy surface** | Tenant filters, thresholds, and abstain rules live in one place ([metadata filtering](./retrieval-strategy-metadata-filtering.md)) |
| **Reuse** | Same tool from supervisor, sequential pipeline, or parallel workers |
| **Testability** | Golden-set and regression tests target the tool contract, not every agent prompt |
| **Observability** | Trace retrieval stages once ([metrics observability](./retrieval-metrics-observability.md)) |

The tool may skip keyword or rerank when config says so—match [retrieval strategies combined](./retrieval-strategies-combined.md) optional stages.

## Agent layout

| Layer | Role |
|-------|------|
| **Supervisor / main agent** | Intent, routing, when to retrieve, final synthesis |
| **Retrieval tool** | Deterministic (or workflow-backed) search pipeline; returns passages + metadata/citations |
| **Other tools** | APIs, calculators, etc.—retrieval is not mixed into general tool handlers |

Python layout sketch: `tools/retrieval.py` or `services/retrieval/` called from `orchestration/supervisor.py` ([example Python directories](../../agents/multi-agent-architecture/example-python-directories.md)).

Related patterns: [sequential AI pipeline](../../agents/multi-agent-architecture/sequencial-ai-pipeline.md) (retrieval as an explicit step), [parallel agents](../../agents/multi-agent-architecture/parallel-agents-architecture.md) (multiple retrieval calls merged upstream).

## Contract (starting point)

- **Input:** user question, trusted tenant/user identity, optional corpus scope
- **Output:** ranked chunks (or abstain / insufficient evidence), citation fields, latency-safe size for context
- **Never:** return chunks the caller is not authorized to see ([guard-rails test use cases](../../guard-rails/guard-rails-test-use-cases.md))

## See also

- [Retrieval architecture decision](./retrieval-architecture-decision.md)
- [Supervisor with retrieval **agent**](./retrieval-architecture-supervisor-as-agent.md) — LLM-driven source choice, rewrite, and retry
- [Retrieval implementation flow](./retrieval-implementation-flow.md)
- [Search overview](./README.md)
- [Agents overview](../../agents/README.md)
