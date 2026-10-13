# Retrieval AWS multi-agent sample

Reference **AWS layout** for a supervisor-style app: authenticated API → LangGraph on ECS/Fargate → domain agents → retrieval service and data tools, with an **S3-driven ingestion** path into Bedrock embeddings and OpenSearch. Pair with [retrieval cloud tools](./retrieval-cloud-tools.md) and [multi-agent retrieval architecture](./retrieval-architecture-multi-agent.md).

```
                          USERS
                           |
                           v
                 API Gateway / ALB
                           |
                           v
              Authentication (IAM / Cognito)
                           |
                           v
                 LangGraph Application
                  ECS / Fargate
                           |
              +------------+------------+
              |            |            |
              v            v            v
        Knowledge Agent  Analytics   Engineering
              |           Agent        Agent
              v            |            |
       Retrieval Service   v            v
              |        Athena/SQL    Jira API
       +------+------+
       |             |
       v             v
   Bedrock       OpenSearch
   Embeddings    Vector Search
       ^             ^
       |             |
       +------ S3 ---+
          Documents
              |
              v
       Ingestion Pipeline
       S3 Events / SQS
              |
              v
       Parse -> Chunk -> Embed
              |
              v
       Update Search Index

 Shared services:
 IAM | KMS | Secrets Manager
 CloudWatch | X-Ray | Evaluation
```

## Component notes

| Piece | Role |
|-------|------|
| **LangGraph on Fargate** | Node split: retrieve → assemble context → generate ([context assembly LangGraph](../../contexting/context-assembly-langchain-langgraph.md)) |
| **Model gateway** | Central routing, limits, telemetry ([LLM architecturing](../../llm/llm-architecturing.md)) |
| **Knowledge Agent + Retrieval Service** | Deterministic RAG path ([supervisor as service](./retrieval-architecture-supervisor-as-service.md)); agent chooses when to call service |
| **Analytics / Engineering agents** | Branch tools ([simple loop](./retrieval-architecture-simple-loop.md), [multi-agent](./retrieval-architecture-multi-agent.md)) |
| **Bedrock embeddings + OpenSearch** | Same-model index and query embed ([embedding user query flow](../embedding/queries/embedding-user-query-flow.md)) |
| **S3 → SQS ingestion** | Async index freshness ([multi-source ingestion](../ingestion/multi-source-ingestion.md)) |
| **Shared IAM / KMS / Secrets** | No tenant IDs from clients alone—enforce filters in retrieval service ([metadata filtering](./retrieval-strategy-metadata-filtering.md)) |
| **CloudWatch / X-Ray / Evaluation** | Layered metrics ([architecture evaluation](./retrieval-architecture-evaluation.md)) |

This is a **sample topology**, not a mandatory bill of materials—swap OpenSearch for Aurora pgvector, or AgentCore, per [retrieval cloud tools](./retrieval-cloud-tools.md) and your SLOs.

## See also

- [Production architecture](../../deployment/production-architecture.md)

- [Guardrails AWS services](../../guard-rails/guardrails-aws-services.md)
- [Example Python directories](../../agents/multi-agent-architecture/example-python-directories.md)
- [Search overview](./README.md)
