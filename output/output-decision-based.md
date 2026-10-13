# Output decision-based by scale

How **post-generation validation, delivery, and guardrails** evolve from startup/prototype through growing production to enterprise / multi-agent.

| Area | Startup / Prototype | Growing Production | Enterprise / Multi-Agent |
|------|---------------------|--------------------|---------------------------|
| **Schema validation** | Basic JSON parsing and Pydantic | Versioned schemas and bounded repair | Strict contracts between agents, compatibility testing |
| **Groundedness** | Prompt instructions and manual checks | Automated claim checks and golden datasets | Risk-based verification and domain-specific policies |
| **Citations** | Check source IDs | Verify source mapping and support | Full provenance, auditability, source-access controls |
| **Security** | Basic authentication and access checks | Document-level ACLs and tool authorization | Defense in depth, tenant isolation, least privilege |
| **Prompt injection** | Basic untrusted-content handling | Adversarial testing and validated tool inputs | Threat modeling, isolation, monitoring, and incident response |
| **Business rules** | Validate critical fields | Centralized deterministic rules | Governed policy services and approval workflows |
| **Failure handling** | Return safe errors | Bounded retries, repair, and abstention | Controlled recovery, escalation, and failure budgets |
| **Evaluation** | Manual tests | Golden dataset and CI regression tests | Continuous evaluation by model, agent, tenant, and risk |
| **Observability** | Basic logs | Validation failures, latency, and retry metrics | Distributed traces, audit trails, privacy controls |
| **Cost control** | Limit retries | Track validation cost and repair success | Budgets and execution limits across the agent graph |

## Guide links by area

| Area | Docs |
|------|------|
| Schema validation | [Implementation strategies](./output-implementation-strategies.md) · [Failure procedure flow](./output-failure-procedure-flow.md) |
| Groundedness | [Implementation strategies](./output-implementation-strategies.md) · [Validation guardrails practices](./output-validation-guardrails-practices.md) |
| Citations | [Citation validation](./output-citation-validation.md) · [Context info for output](../contexting/context-info-for-output.md) |
| Security & tools | [Secure tool execution flow](./output-secure-tool-execution-flow.md) · [Guard-rails](../guard-rails/) · [Reliable architecture](../contexting/context-reliable-architecture.md) |
| Prompt injection | [Prompt injection](../prompting/prompt-injection.md) · [Guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md) |
| Business rules | [Implementation strategies — deterministic checks](./output-implementation-strategies.md) · [Secure tool execution flow](./output-secure-tool-execution-flow.md) |
| Failure handling | [Validation failure impact](./output-validation-failure-impact.md) · [Failure procedure flow](./output-failure-procedure-flow.md) · [LangGraph routing](./output-failure-guardrails-via-langchain.md) |
| Evaluation | [Validation metrics](./output-validation-via-test-or-guardrails-metrics.md) · [Guardrails practices](./output-validation-guardrails-practices.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| Observability | [Observability decision-based](../observability-evaluation/observability-decision-based.md) · [Validation metrics](./output-validation-via-test-or-guardrails-metrics.md) |
| Cost control | [Validation metrics — cost per successful task](./output-validation-via-test-or-guardrails-metrics.md) · [LLM retry and fallbacks](../llm/llm-retry-fallbacks-routing.md) |
| Multi-agent | [Failure guardrails LangGraph](./output-failure-guardrails-via-langchain.md) · [Retrieval architecture decision](../retrieval/search/retrieval-architecture-decision.md) |

## See also

- [Output implementation flow](./output-implementation-flow.md)
- [Prompt architecturing decision-based](../prompting/prompt-architecturing-decision-based.md)
- [Context architecturing decision-based](../contexting/context-architecturing-decision-based.md)
- [LLM decision-based by scale](../llm/llm-decision-based.md)
- [Output overview](./README.md)
