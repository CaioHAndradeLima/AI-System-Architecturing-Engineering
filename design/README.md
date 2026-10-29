# Design

**Reference cloud architectures** for multi-agent LangGraph apps—ASCII diagrams and component choices by maturity (AWS and GCP). Use with [deployment](../deployment/production-architecture.md), [guard-rails](../guard-rails/README.md), and [agent platform primitives](../agents/agent-platform-starter-kit-primitives.md).

## Topic areas

| Area | Focus |
|------|--------|
| **Basic** | Single Lambda, optional Bedrock Knowledge Base, minimal ops |
| **Intermediate** | ECS Fargate, split services, async workers, state, richer observability |
| **Advanced** | Edge (Route 53, WAF), multi-agent ECS/EKS, EventBridge/SQS, layered data, CI/CD to ECR |
| **Comparison** | When to move from basic compute and coupling to intermediate and advanced scale |
| **GCP** | Cloud Run/GKE microservices, Pub/Sub, Vertex, and shared agent platform boundaries |
| **Fintech** | High-stakes reliability, audit, HITL, and tenant isolation for banking and credit agents |

---

## Guides

### [aws-basic.md](./aws-basic.md)

`#aws` · `#lambda` · `#bedrock` · `#langgraph`

API Gateway → Lambda with in-process supervisor and agents, Bedrock LLM, optional knowledge base, CloudWatch logs.

→ [See more in aws-basic.md](./aws-basic.md)

### [aws-intermediate.md](./aws-intermediate.md)

`#aws` · `#ecs` · `#fargate` · `#sqs` · `#dynamodb`

ALB → ECS supervisor and specialist services, async SQS workers, DynamoDB/S3, dedicated retrieval path, metrics and alarms.

→ [See more in aws-intermediate.md](./aws-intermediate.md)

### [aws-advanced.md](./aws-advanced.md)

`#aws` · `#route53` · `#waf` · `#multi-agent` · `#eventbridge` · `#cicd`

Capability-to-approach table (volume, isolation, jobs, retrieval, cost, faults, deploys, security, quality) plus Route 53/WAF edge, multi-agent ECS/EKS, EventBridge/SQS, layered data, observability, and OIDC CI/CD to ECR.

→ [See more in aws-advanced.md](./aws-advanced.md)

### [gcp-microservices-agent-platform.md](./gcp-microservices-agent-platform.md)

`#gcp` · `#cloud-run` · `#gke` · `#pubsub` · `#vertex` · `#microservices`

Load-balanced agent API on Cloud Run or GKE, split orchestration and retrieval, Pub/Sub async jobs, checkpoint stores, and TypeScript/Python service boundaries.

→ [See more in gcp-microservices-agent-platform.md](./gcp-microservices-agent-platform.md)

### [fintech-reliable-agents.md](./fintech-reliable-agents.md)

`#fintech` · `#banking` · `#compliance` · `#audit` · `#hitl`

Reliability and security patterns for financial agents: idempotency, dual control, tenant-scoped data, explainability, and controlled autonomy under regulatory pressure.

→ [See more in fintech-reliable-agents.md](./fintech-reliable-agents.md)

## Related

- [Deployment cloud tools](../deployment/deployment-cloud-tools.md)
- [Production components](../deployment/production-components.md)
- [Agents overview](../agents/README.md)

## See also

- [Repository overview](../README.md)
