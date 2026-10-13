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

### [aws-intermedium.md](./aws-intermedium.md)

`#aws` · `#ecs` · `#fargate` · `#sqs` · `#dynamodb`

ALB → ECS supervisor and specialist services, async SQS workers, DynamoDB/S3, dedicated retrieval path, metrics and alarms.

→ [See more in aws-intermedium.md](./aws-intermedium.md)

### [aws-advance.md](./aws-advance.md)

`#aws` · `#route53` · `#waf` · `#multi-agent` · `#eventbridge` · `#cicd`

Route 53 and CloudFront/WAF in front of authenticated API Gateway and ALB; ECS/EKS with multiple agent services, tool layer, OpenSearch and business APIs; EventBridge/SQS workers; S3, DynamoDB, Aurora; observability, SLOs, and GitHub Actions → OIDC → ECR deploy.

→ [See more in aws-advance.md](./aws-advance.md)

## Related

- [Deployment cloud tools](../deployment/deployment-cloud-tools.md)
- [Production components](../deployment/production-components.md)
- [Agents overview](../agents/README.md)

## See also

- [Repository overview](../README.md)
