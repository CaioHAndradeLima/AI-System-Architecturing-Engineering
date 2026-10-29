# AI-specific controls — Amazon Bedrock Guardrails

[Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) can evaluate **prompts and model responses** using configurable controls. Use them in the **AI safety service** layer of [guardrails cloud architecture](./guardrails-cloud-architecture.md)—alongside app guardrails and output validation—not as a substitute for auth or tenant isolation.

## Bedrock Guardrails capabilities

| Capability | Responsibility |
|------------|----------------|
| **Content filters** | Detect configured categories of harmful content. |
| **Prompt-attack detection** | Help detect prompt injection and jailbreak attempts. |
| **Denied topics** | Block configured topics. |
| **Sensitive-information filters** | Detect, block, or mask supported sensitive information. |
| **Contextual grounding checks** | Assess whether responses are grounded in supplied source information. |
| **Automated reasoning checks** | Evaluate certain logical rules and policies. |

Apply guardrails on **both** user/tool-assembled prompts and model outputs where your integration supports it. Grounding checks pair well with RAG when source chunks are passed explicitly to the model or to the guardrail API.

## Related AWS cloud security controls

These sit outside Bedrock but support the same end-to-end stack (edge → identity → audit):

| Service | Role |
|---------|------|
| **AWS WAF** | Helps protect supported web endpoints against common web exploits and unwanted traffic. |
| **Amazon API Gateway** | Provides API entry-point capabilities such as authentication integration, throttling, and request handling. |
| **AWS IAM** | Controls which users and workloads may access AWS resources. |
| **AWS Secrets Manager** | Stores and manages application secrets. |
| **AWS CloudTrail** | Records AWS API activity for auditing. |
| **Amazon CloudWatch** | Collects metrics, logs, and alarms. |

More control-to-purpose mapping: [guardrails-aws-services.md](./guardrails-aws-services.md) and [guard-rails-cloud-comparison.md](./guard-rails-cloud-comparison.md).

## Tenant isolation on AWS

AWS documents several isolation models, including **shared-resource isolation**, **dedicated resources**, and **hybrid** approaches. Choose according to the required security boundary, cost, and operational complexity.

Guardrails do not enforce tenancy—combine Bedrock controls with [guardrails data isolation](./guardrails-data-isolation.md) and [tenant-scoped retrieval](./safer-architecture-tenant-scoped-retrieval.md).

## Practical checklist

- [ ] Version and test guardrail **configs** like application code; track drift across environments
- [ ] Define behavior when a guardrail **blocks** (user message, fallback model, human review)
- [ ] Log guardrail interventions without storing full PII in plain text
- [ ] Validate cross-tenant scenarios still fail at **retrieval/IAM**, not only at content filters

## Reference implementation

**[guardrails-strategies](https://github.com/CaioHAndradeLima/guardrails-strategies)** — AWS control slot + offline stub in `cloud_adapters.py`. Keys: `amazon_bedrock_guardrails`.

Recommended gate: `ci-guardrails-eval` (`evaluate-pipeline` + `check-measure`). Coverage: [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/guardrails-strategies/blob/main/docs/LAB_COVERAGE.md) (14/14).

## See also

- [AI-specific controls — Google Cloud Model Armor](./ai-specific-controls-google-model-armor.md)
- [AI-specific controls — Azure Content Safety and Prompt Shields](./ai-specific-controls-azure-content-safety-prompt-shields.md)
- [Guard-rails category — Content safety / Privacy](./guard-rails-category.md)
- [Guard-rails test use cases](./guard-rails-test-use-cases.md)
- [Guard-rails overview](./README.md)
