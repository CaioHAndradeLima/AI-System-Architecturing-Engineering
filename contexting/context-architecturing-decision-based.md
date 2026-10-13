# Context architecturing decision-based

How **context assembly and prompt safety** evolve from startup/prototype through growing production to enterprise / multi-agent.

| Area | Startup / Prototype | Growing Production | Enterprise / Multi-Agent |
|------|---------------------|--------------------|---------------------------|
| **Context assembly** | Simple Python function | Dedicated, reusable module | Configurable policies per task and agent |
| **Evidence selection** | Top-ranked chunks | Relevance, deduplication, and coverage | Task-specific selection, source authority, conflict resolution |
| **Token budget** | Fixed token limit | Token-aware selection and trimming | Dynamic budgets per model, task, and agent |
| **Conversation history** | Recent messages | Recent messages plus summaries | Managed conversation state and task-specific memory |
| **Source metadata** | Document title and ID | URLs, page numbers, timestamps, versions | Full provenance, lineage, audit trails |
| **Security** | Basic access checks | Document-level ACLs and tenant isolation | Defense in depth, centralized authorization, audited access |
| **Prompt injection** | Basic instructions and input handling | Untrusted-content boundaries and validation | Layered controls, least-privilege tools, security testing |
| **Citation handling** | Return source IDs | Validate citation-to-source mapping | Traceable evidence across retrieval and agent workflows |
| **Evaluation** | Manual testing | Golden dataset and regression tests | Continuous evaluation per component, agent, and end-to-end workflow |
| **Observability** | Basic logs | Context size, latency, token usage, and errors | Distributed traces, per-tenant metrics, auditability |
| **Failure handling** | Return an insufficient-evidence response | Retry, adjust retrieval, or ask for clarification | Controlled recovery, bounded retries, escalation, fallback models |
| **Cost optimization** | Limit context size | Remove redundancy and monitor cost per request | Optimize cost and quality across agents, models, and workloads |

## Guide links by area

| Area | Docs |
|------|------|
| Context assembly | [Assembly flow](./context-assembly-flow.md) · [Algorithm](./context-algorithm.md) · [LangGraph nodes](./context-assembly-langchain-langgraph.md) |
| Evidence selection | [Scoring math](./context-scoring-math.md) · [Simple / multi-hop / analytical patterns](./context-simple-document-question.md) |
| Token budget & history | [Conversation strategies](./context-conversation-strategies.md) · [Compacting](../retrieval/compacting/) |
| Metadata & citations | [Context info for output](./context-info-for-output.md) |
| Security & injection | [Reliable architecture](./context-reliable-architecture.md) · [Guard-rails](../guard-rails/) |
| Evaluation & observability | [Evaluate assembling](./context-evaluate-assembling.md) · [Trade-offs](./context-assembling-trade-offs.md) |
| Failure & cost | [Similarity abstain](../retrieval/search/retrieval-strategy-similarity.md) · [Retrieval metrics](../retrieval/search/retrieval-metrics-observability.md) |
| Multi-agent | [Architecture decision (retrieval)](../retrieval/search/retrieval-architecture-decision.md) · [Multi-agent sample](../retrieval/search/retrieval-architecture-multi-agent.md) |

## See also

- [Output decision-based by scale](../output/output-decision-based.md)
- [Retrieval architecturing decision-based](../retrieval/retrieval-architecturing-decision-based.md)
- [Contexting overview](./README.md)
