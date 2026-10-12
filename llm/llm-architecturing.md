# LLM architecturing

Reference layout: **agents** call a shared **model gateway** instead of provider APIs directly—routing, limits, credentials, tracing, and fallbacks live in one place ([multi-agent sample](../retrieval/search/retrieval-aws-multi-agent-sample.md)).

```
              LangGraph Supervisor
                       |
          +------------+------------+
          |            |            |
          v            v            v
      Knowledge     Analytics    Engineering
        Agent         Agent        Agent
          \            |            /
           +-----------+-----------+
                       |
                       v
                 Model Gateway
                       |
          +------------+------------+
          |            |            |
          v            v            v
       Routing      Rate limits   Telemetry
          |
          v
   +------+------+------+
   |             |      |
   v             v      v
 Model A       Model B  Fallback
   |             |      |
   +-------------+------+
                 |
                 v
          Validated response
```

## Model gateway responsibilities

- **Model routing** based on task, latency, and cost requirements.
- **Standardized timeouts and retries.**
- **Provider credentials and access policies.**
- **Rate limiting and concurrency control.**
- **Request tracing and cost attribution.**
- **Model version management and fallback policies.**

## Guide links

| Responsibility | Docs |
|----------------|------|
| Routing | [Routing policy](./llm-routing-policy.md) · [Routing flow](./llm-routing-flow.md) |
| Timeouts / retries / fallback | [Retry, fallbacks, and routing](./llm-retry-fallbacks-routing.md) |
| Credentials / identity | [Cloud services — secrets & identity](./llm-cloud-services.md) · [Guard-rails](../guard-rails/) |
| Rate limits / concurrency | [Retry guide — 429](./llm-retry-fallbacks-routing.md) · [Async vs streaming](./llm-async-vs-streaming.md) |
| Tracing / cost | [Latency variables and measurement](./llm-latency-variables-measurement.md) |
| Version / fallback policy | [Select LLM flow](./select-llm-flow.md) · [Prompt versioning](../prompting/prompt-versioning.md) |
| Validated response | [LLM flow — output validation](./llm-flow.md) · [Context reliable architecture](../contexting/context-reliable-architecture.md) |

Agents stay thin: retrieval and tools behind domain agents; **all** chat/completion calls go through the gateway for consistent policy.

## See also

- [Retrieval architecture — multi-agent](../retrieval/search/retrieval-architecture-multi-agent.md)
- [LLM overview](./README.md)
