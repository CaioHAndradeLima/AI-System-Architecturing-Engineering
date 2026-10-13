# AWS advanced reference architecture

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