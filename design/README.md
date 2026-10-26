# Design

**Reference AWS architectures** for multi-agent LangGraph apps—ASCII diagrams and component choices by maturity. Use with [deployment](../deployment/production-architecture.md), [guard-rails AWS](../guard-rails/guardrails-aws-services.md), and [retrieval AWS sample](../retrieval/search/retrieval-aws-multi-agent-sample.md).

## Topic areas

| Area | Focus |
|------|--------|
| **Basic** | Single Lambda, optional Bedrock Knowledge Base, minimal ops |
| **Intermediate** | ECS Fargate, split services, async workers, state, richer observability |
| **Advanced** | Edge (Route 53, WAF), multi-agent ECS/EKS, EventBridge/SQS, layered data, CI/CD to ECR |
| **Comparison** | When to move from basic compute and coupling to intermediate and advanced scale |

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

## Related

- [Deployment cloud tools](../deployment/deployment-cloud-tools.md)
- [Production components](../deployment/production-components.md)
- [Agents overview](../agents/README.md)

## See also

- [Repository overview](../README.md)
