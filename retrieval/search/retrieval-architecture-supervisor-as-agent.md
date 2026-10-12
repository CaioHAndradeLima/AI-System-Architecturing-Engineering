# Retrieval architecture — supervisor with retrieval agent

The **supervisor** delegates to a **Retrieval Agent**—an LLM-driven specialist that chooses sources, rewrites queries, picks strategies, searches, judges evidence, and may **retry or broaden** search before returning results upstream.

Contrast with a fixed **retrieval tool/service** ([supervisor as service](./retrieval-architecture-supervisor-as-service.md)): same encapsulation boundary, but policy and routing inside retrieval are agentic rather than a single deterministic pipeline.

```
User
  |
  v
Supervisor
  |
  v
Retrieval Agent
  |
  +--> Decide which source to search
  +--> Rewrite the query
  +--> Choose search strategy
  +--> Search multiple sources
  +--> Evaluate evidence
  +--> Retry / broaden search
  |
  v
Evidence + sources
  |
  v
Supervisor
```

The supervisor then synthesizes the final user answer (or routes to other specialists) using **Evidence + sources**.

## When an agent helps

| Situation | Retrieval agent |
|-----------|-----------------|
| Multiple corpora (docs, tickets, wiki, code) | Source selection and per-source query variants |
| Ambiguous or multi-part questions | Rewrite, decompose, retry with broader K or hybrid |
| Uneven quality across hops | Explicit “evaluate evidence” step before returning |

## Guardrails (required)

Agentic retrieval must not weaken **authorization**:

- Pass **trusted tenant/user identity** into every search call the agent triggers—not LLM-invented filter values ([metadata filtering](./retrieval-strategy-metadata-filtering.md)).
- Cap **retries, tool calls, and tokens**; log each search for audit ([metrics observability](./retrieval-metrics-observability.md)).
- Prefer **deterministic search tools** behind the agent (embed, vector, BM25, rerank) so eval and regression stay reproducible ([combined strategies](./retrieval-strategies-combined.md)).

Query rewrite patterns: [cleaning user query](../embedding/queries/embedding-cleaning-user-query.md). Multi-source ingestion context: [multi-source ingestion](../ingestion/multi-source-ingestion.md).

## Service vs agent (same boundary, different brain)

| | [As service](./retrieval-architecture-supervisor-as-service.md) | As agent (this doc) |
|---|-----|-----|
| **Control flow** | Fixed pipeline | LLM plans steps |
| **Cost / latency** | Predictable | Higher; depends on retries |
| **Eval** | Easier to regression-test | Needs tool-call and outcome eval |
| **Best fit** | Production RAG default | Complex routing across sources |

## See also

- [Parallel agents architecture](../../agents/multi-agent-architecture/parallel-agents-architecture.md)
- [Search overview](./README.md)
