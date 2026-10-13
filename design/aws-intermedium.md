# AWS intermediate architecture

**ECS Fargate** multi-service layout: supervisor and specialists as separate services, async jobs, durable state, and stronger observability. Compare to [AWS basic](./aws-basic.md) before adopting cost and ops complexity.

## Basic vs intermediate

| Component | Basic | Intermediate |
|-----------|-------|----------------|
| **Compute** | Lambda | ECS Fargate |
| **Application structure** | One deployment | Separate supervisor and specialist services |
| **Scaling** | Lambda concurrency | ECS service autoscaling |
| **Background jobs** | Usually synchronous | SQS + workers |
| **State** | Minimal or external | DynamoDB or a suitable persistent store |
| **Retrieval** | Optional knowledge base | Dedicated retrieval service or managed knowledge base |
| **Monitoring** | Basic logs | Metrics, dashboards, alarms, distributed tracing |

## Architecture diagram

```
                         USERS
                           |
                           v
                   +---------------+
                   | API Gateway   |
                   +---------------+
                           |
                           v
                   +---------------+
                   | ALB           |
                   +---------------+
                           |
                           v
              +-------------------------+
              | ECS Fargate             |
              |                         |
              | +---------------------+ |
              | | Supervisor Service  | |
              | | LangGraph            | |
              | +---------------------+ |
              +-------------------------+
                           |
               +-----------+-----------+
               |                       |
               v                       v
     +-------------------+   +-------------------+
     | Research Service  |   | Action Service    |
     | ECS Fargate       |   | ECS Fargate       |
     +-------------------+   +-------------------+
               |                       |
               v                       v
     +-------------------+   +-------------------+
     | Vector Retrieval  |   | External Business |
     | / Knowledge Base  |   | APIs               |
     +-------------------+   +-------------------+
               |
               v
     +-------------------+
     | Amazon Bedrock    |
     +-------------------+


      ASYNC TASK PROCESSING

     +-------------------+
     | Supervisor / API   |
     +-------------------+
               |
               v
     +-------------------+
     | Amazon SQS        |
     | Work Queue        |
     +-------------------+
               |
               v
     +-------------------+
     | ECS Worker        |
     | Background Jobs   |
     +-------------------+


      STATE AND KNOWLEDGE

     +-------------------+     +-------------------+
     | Amazon DynamoDB   |     | Amazon S3         |
     | Workflow State    |     | Documents         |
     +-------------------+     +-------------------+


      OBSERVABILITY

     ECS + ALB + Bedrock
               |
               v
     +-------------------+
     | CloudWatch        |
     | Metrics / Logs    |
     +-------------------+
               |
               v
     +-------------------+
     | Alarms / Alerts   |
     +-------------------+
```

## See also

- [Deployment cloud tools — AWS row](../deployment/deployment-cloud-tools.md)
- [Tracing for observability](../observability-evaluation/tracing-for-observability.md)
- [Design overview](./README.md)
