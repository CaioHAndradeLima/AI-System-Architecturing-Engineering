# Production architecture

End-to-end **reference topology** for a multi-agent RAG service in production: user path, platform infrastructure, and the eval → deploy → monitor feedback loop ([example Python layout](../agents/multi-agent-architecture/example-python-directories.md), [AWS multi-agent sample](../retrieval/search/retrieval-aws-multi-agent-sample.md)).

```
                         USERS
                           |
                           v
                     API / Gateway
                           |
                           v
                Authentication / Rate Limits
                           |
                           v
                   LangGraph Application
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        Knowledge       Analytics     Engineering
          Agent           Agent          Agent
             |             |             |
             v             v             v
        Retrieval       SQL / APIs     Jira / Docs
             |
             v
        LLM Generation
             |
             v
        Output Validation
             |
             v
         Final Answer

    PRODUCTION INFRASTRUCTURE
    -------------------------
    Docker / Container Runtime
    Secrets / Identity / Networking
    Logs / Metrics / Distributed Tracing
    Model + Prompt + Retrieval Versioning

    DELIVERY AND IMPROVEMENT
    -----------------------
    GitHub Actions CI/CD
             |
             v
    Offline Evaluation Pipeline
             |
             v
    Quality Gates -> Staging -> Canary -> Production
             ^                              |
             |                              v
             +---- Failure Dataset <--- Monitoring
```

## Request path

| Layer | Role | Docs |
|-------|------|------|
| **API / Gateway** | Edge routing, TLS, optional [model gateway](../llm/llm-architecturing.md) | [LLM cloud services](../llm/llm-cloud-services.md) |
| **Authentication / rate limits** | Identity, tenant, abuse control | [Guard-rails](../guard-rails/) · [Guardrails strategy](../guard-rails/guardrails-strategy.md) |
| **LangGraph application** | Orchestration graph and state | [Context assembly LangGraph](../contexting/context-assembly-langchain-langgraph.md) · [Output validation routing](../output/output-failure-guardrails-via-langchain.md) |
| **Domain agents** | Knowledge (RAG), analytics (SQL), engineering (tools) | [Supervisor hierarchical](../agents/multi-agent-architecture/supervisor-hierarchical.md) · [Parallel agents](../agents/multi-agent-architecture/parallel-agents-architecture.md) |
| **Retrieval → LLM → validation** | Evidence, generation, safe response | [Search](../retrieval/search/) · [LLM flow](../llm/llm-flow.md) · [Output implementation flow](../output/output-implementation-flow.md) |

Knowledge-agent path matches [tracing for observability](../observability-evaluation/tracing-for-observability.md) spans (rewrite → search → rerank → assemble → generate → validate).

## Production infrastructure

| Concern | Docs |
|---------|------|
| Containers | Package `app/` per [example Python directories](../agents/multi-agent-architecture/example-python-directories.md) |
| Secrets / identity / network | [Guard-rails AWS](../guard-rails/guardrails-aws-services.md) · [Cloud comparison](../guard-rails/guard-rails-cloud-comparison.md) |
| Logs / metrics / tracing | [Tracing metrics](../observability-evaluation/tracing-for-observability-metrics.md) · [Observability tools](../observability-evaluation/observability-tools.md) |
| Versioning | [Prompt versioning](../prompting/prompt-versioning.md) · index and embedding version tags on traces |

## Delivery and improvement

| Stage | Docs |
|-------|------|
| CI/CD + offline eval | [Pipeline evaluation](./pipeline-evaluation.md) · [Observability implementation flow](../observability-evaluation/observability-implementation-flow.md) |
| Quality gates → canary → prod | [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md) |
| Monitoring → failure dataset | [Production flow](./production-flow.md) · [Investigate failure](../observability-evaluation/investigate-failure-by-observability-data.md) · [Guardrails practices](../output/output-validation-guardrails-practices.md) |

New incidents should add cases to the **failure dataset** and block promotion until [regression tests](../observability-evaluation/regression-and-canary-releases.md) pass.

## See also

- [Production components](./production-components.md)
- [Deployment overview](./README.md)
