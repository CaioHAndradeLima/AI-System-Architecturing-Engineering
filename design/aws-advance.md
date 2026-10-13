# AWS advanced reference architecture

**Production-scale** multi-agent layout: edge protection, authenticated ingress, dedicated agent services, event-driven workers, layered data, full observability, and gated CI/CD. Evolve from [AWS intermediate](./aws-intermedium.md) when you need isolation, durable workflows, and safe release at higher volume.

## Capability approach

| Capability | Approach |
|------------|----------|
| **High request volume** | Autoscaling, load balancing, rate limits, and capacity testing |
| **Independent agent workloads** | Dedicated services with independent scaling policies |
| **Long-running jobs** | SQS, event-driven workers, and durable workflow orchestration |
| **Large knowledge collections** | Managed vector search, metadata filtering, and optimized indexing |
| **Expensive LLM calls** | Model routing, caching, prompt optimization, and budgets |
| **Fault isolation** | Timeouts, circuit breakers, bounded retries, and queue isolation |
| **Safe deployments** | Canary or blue/green deployments with alarms and rollback |
| **Security** | IAM least privilege, private networking where appropriate, KMS, and Secrets Manager |
| **Quality control** | Golden datasets, offline evaluations, production feedback, and regression testing |

## Architecture diagram

```
                           USERS
                             |
                             v
                    +------------------+
                    | Route 53         |
                    +------------------+
                             |
                             v
                    +------------------+
                    | CloudFront / WAF |
                    +------------------+
                             |
                             v
                    +------------------+
                    | API Gateway      |
                    | Authentication  |
                    +------------------+
                             |
                             v
                    +------------------+
                    | ALB              |
                    +------------------+
                             |
                             v
             +--------------------------------+
             | ECS Fargate / EKS              |
             |                                |
             | +----------------------------+ |
             | | Supervisor / Router        | |
             | | LangGraph                  | |
             | +----------------------------+ |
             +--------------------------------+
                             |
             +---------------+----------------+
             |               |                |
             v               v                v
    +----------------+ +----------------+ +----------------+
    | Research Agent | | Action Agent   | | Analytics Agent|
    | Service        | | Service        | | Service        |
    +----------------+ +----------------+ +----------------+
             |               |                |
             +---------------+----------------+
                             |
                             v
                 +------------------------+
                 | Agent Tool / API Layer |
                 | Timeouts, Retries,     |
                 | Permissions, Schemas   |
                 +------------------------+
                             |
           +-----------------+------------------+
           |                 |                  |
           v                 v                  v
    +-------------+  +---------------+  +----------------+
    | Bedrock     |  | Vector Search  |  | Business APIs  |
    | Model APIs  |  | OpenSearch     |  | / Databases    |
    +-------------+  +---------------+  +----------------+


             DISTRIBUTED WORKFLOWS

    +-------------------+       +-------------------+
    | EventBridge       |------>| Amazon SQS        |
    | Event Routing     |       | Queues            |
    +-------------------+       +-------------------+
                                        |
                        +---------------+--------------+
                        |               |              |
                        v               v              v
                  +-----------+  +-----------+  +-----------+
                  | Worker A  |  | Worker B  |  | Worker C  |
                  +-----------+  +-----------+  +-----------+


             DATA AND STATE

    +----------------+  +----------------+  +----------------+
    | Amazon S3      |  | DynamoDB       |  | Aurora         |
    | Documents      |  | State / Cache  |  | Relational     |
    +----------------+  +----------------+  +----------------+
             |
             v
    +----------------+
    | Ingestion      |
    | / Embeddings   |
    +----------------+


             OBSERVABILITY AND GOVERNANCE

    +-------------------------------------------------------+
    | CloudWatch / X-Ray / OpenTelemetry / Langfuse         |
    | Traces, Logs, Metrics, Cost, Quality, Agent Execution |
    +-------------------------------------------------------+
                             |
                             v
    +-------------------------------------------------------+
    | Alarms / SLOs / Canary Rollback / Incident Response    |
    +-------------------------------------------------------+


             CI/CD AND SECURITY

    GitHub Actions
          |
          v
    OIDC + IAM
          |
          v
    Build / Test / Evaluate / Scan
          |
          v
    Amazon ECR
          |
          v
    CodeDeploy / Controlled Deployment

    Secrets Manager / KMS / IAM Least Privilege
```

## See also

- [Pipeline scoring and quality gates](../deployment/pipeline-scoring-quality-gate.md)
- [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md)
- [Design overview](./README.md)
