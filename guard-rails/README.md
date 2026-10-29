# Guard-rails

Layered validation, access control, and output policy for agent and LLM systems.

## Guard-rails types

| Type | Purpose |
|------|---------|
| **AI safety** | Control harmful, irrelevant, or unsupported model behavior. |
| **Security** | Enforce authentication, authorization, tenant isolation, and data protection. |
| **Reliability** | Validate outputs, limit resource consumption, and control failures. |

These types overlap in a real pipeline—for example, output validation touches both **AI safety** and **reliability**, and ACL spans **security** and **tool checks**. See [guardrails-strategy.md](./guardrails-strategy.md) for how layers map to a request flow.

## Enforcement layers

| Layer | What to enforce |
|-------|-----------------|
| **Identity** | Authenticate the user and establish trusted identity claims. |
| **Application** | Verify the user's membership and permissions for the requested tenant. |
| **Retrieval** | Apply tenant and document-level permission filters before returning chunks. |
| **Data stores and tools** | Enforce access restrictions on queries, object reads, and external API calls. |
| **Output and observability** | Prevent unauthorized content from being returned, cached, or exposed through logs and traces. |

See [safer-architecture-tenant-scoped-retrieval.md](./safer-architecture-tenant-scoped-retrieval.md) for a request flow that applies these layers end to end.

## What good guardrails do

| # | Goal |
|---|------|
| 1 | **Enforces a clearly defined rule.** For example, a user cannot access documents outside their tenant. |
| 2 | **Runs at the correct boundary.** Authorization runs before data access; output validation runs before the response is returned. |
| 3 | **Fails safely.** If authorization cannot be verified, access is denied. If a mandatory validation service is unavailable, the system does not silently bypass the check. |
| 4 | **Can be tested.** You can demonstrate that valid requests work and unauthorized requests fail. |

---

## Guides

### [guardrails-strategy.md](./guardrails-strategy.md)

`#pipeline` · `#layers` · `#request-flow`

A defense-in-depth pipeline for agent systems: validate and authorize before execution, constrain tool and retrieval access during the run, then validate again before anything reaches the user.

→ [See more in guardrails-strategy.md](./guardrails-strategy.md)

### [guard-rails-category.md](./guard-rails-category.md)

`#taxonomy` · `#enforcement` · `#reference`

Reference map of common guardrail categories: what each one covers, a concrete example, and where enforcement should live in the stack.

→ [See more in guard-rails-category.md](./guard-rails-category.md)

### [guardrails-cloud-architecture.md](./guardrails-cloud-architecture.md)

`#cloud` · `#architecture` · `#edge-to-output`

A full-stack request path for production agent/LLM APIs: edge protection, identity, application rules, AI safety services, scoped data access, the agent workflow, and output controls—with cloud primitives applied across the lifecycle.

→ [See more in guardrails-cloud-architecture.md](./guardrails-cloud-architecture.md)

### [guard-rails-cloud-comparison.md](./guard-rails-cloud-comparison.md)

`#cloud` · `#multi-cloud` · `#reference`

Maps common guardrail responsibilities to representative services on AWS, Google Cloud, and Azure.

Use alongside guardrails cloud architecture to pick products per layer.

→ [See more in guard-rails-cloud-comparison.md](./guard-rails-cloud-comparison.md)

### [ai-specific-controls-amazon-bedrock-guardrails.md](./ai-specific-controls-amazon-bedrock-guardrails.md)

`#aws` · `#bedrock` · `#ai-safety`

Amazon Bedrock Guardrails can evaluate prompts and model responses using configurable controls.

Use them in the AI safety service layer of guardrails cloud architecture—alongside app guardrails and output validation—not as a substitute for auth or tenant isolation.

→ [See more in ai-specific-controls-amazon-bedrock-guardrails.md](./ai-specific-controls-amazon-bedrock-guardrails.md)

### [ai-specific-controls-google-model-armor.md](./ai-specific-controls-google-model-armor.md)

`#gcp` · `#model-armor` · `#ai-safety`

Model Armor screens prompts and responses and supports configurable controls for prompt injection, jailbreaks, harmful content, and sensitive information.

It can be integrated into AI workflows on Google Cloud and other platforms.

→ [See more in ai-specific-controls-google-model-armor.md](./ai-specific-controls-google-model-armor.md)

### [ai-specific-controls-azure-content-safety-prompt-shields.md](./ai-specific-controls-azure-content-safety-prompt-shields.md)

`#azure` · `#content-safety` · `#prompt-shields`

Prompt Shields detects and helps block adversarial instructions in user prompts and documents.

Azure AI Content Safety also supports content-safety screening.

Use both in the AI safety service layer of guardrails cloud architecture, alongside app validation and tenant-scoped data access.

→ [See more in ai-specific-controls-azure-content-safety-prompt-shields.md](./ai-specific-controls-azure-content-safety-prompt-shields.md)

### [wrong-architecture-shared-retrieval.md](./wrong-architecture-shared-retrieval.md)

`#anti-pattern` · `#multi-tenant` · `#rag`

An anti-pattern for multi-tenant RAG: every customer’s documents sit in one vector index, and user questions hit that shared search before the LLM answers—with no strong tenant boundary in the retrieval path.

→ [See more in wrong-architecture-shared-retrieval.md](./wrong-architecture-shared-retrieval.md)

### [safer-architecture-tenant-scoped-retrieval.md](./safer-architecture-tenant-scoped-retrieval.md)

`#architecture` · `#multi-tenant` · `#rag` · `#identity`

A multi-tenant RAG pattern where identity and authorization are resolved in a trusted backend before any search, retrieval is filtered by tenant_id, and the response is validated before it reaches the user.

→ [See more in safer-architecture-tenant-scoped-retrieval.md](./safer-architecture-tenant-scoped-retrieval.md)

### [guardrails-data-isolation.md](./guardrails-data-isolation.md)

`#data-isolation` · `#tenancy` · `#storage`

Strategies for keeping each tenant’s data separate in storage and retrieval.

Pick based on compliance needs, operational cost, and blast radius if a filter bug slips through.

→ [See more in guardrails-data-isolation.md](./guardrails-data-isolation.md)

### [guardrails-aws-services.md](./guardrails-aws-services.md)

`#aws` · `#infrastructure` · `#security`

Infrastructure and platform controls that complement application-level guardrails on AWS (and similar clouds).

→ [See more in guardrails-aws-services.md](./guardrails-aws-services.md)

### [guard-rails-test-use-cases.md](./guard-rails-test-use-cases.md)

`#testing` · `#multi-tenant` · `#checklist`

Scenarios to prove tenant isolation, tool safety, and content handling behave as intended.

Use as a checklist for integration tests and release gates.

→ [See more in guard-rails-test-use-cases.md](./guard-rails-test-use-cases.md)

### [guard-rails-robust-cloud-rules-implementation.md](./guard-rails-robust-cloud-rules-implementation.md)

`#checklist` · `#multi-tenant` · `#production`

Checklist for a production-grade multi-tenant agent or RAG stack on cloud: rules must be enforced in identity, data, retrieval, async work, and tests—not only in prompts or AI safety APIs.

→ [See more in guard-rails-robust-cloud-rules-implementation.md](./guard-rails-robust-cloud-rules-implementation.md)

### [guard-rails-decision-architecturing-assistance.md](./guard-rails-decision-architecturing-assistance.md)

`#architecture` · `#decision-guide` · `#maturity`

When to adopt common guardrails by product stage (small/MVP → medium → large/mature), plus a cloud service map for AWS, Google Cloud, and Azure.

Use with guard-rails category, cloud comparison, and robust implementation.

→ [See more in guard-rails-decision-architecturing-assistance.md](./guard-rails-decision-architecturing-assistance.md)

---

## Reference implementation

**[guardrails-strategies](https://github.com/CaioHAndradeLima/guardrails-strategies)** — layered policy orchestration (identity → ACL → retrieval → tools → output), multi-tenant golden attacks, and CI measure gates on bundled fixtures.

| Command | Guides exercised |
| --- | --- |
| `python -m guardrails_strategies.cli evaluate-pipeline --profile ci-guardrails-eval` | Core policy metrics + [test use cases](./guard-rails-test-use-cases.md) + tenant-scoped vs shared retrieval |
| `python -m guardrails_strategies.cli evaluate-scenarios` | All rows in [guard-rails-test-use-cases.md](./guard-rails-test-use-cases.md) |
| `python -m guardrails_strategies.cli evaluate-full` | **100% guard-rails guide coverage** — [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/guardrails-strategies/blob/main/docs/LAB_COVERAGE.md) (14/14) |
| Docker + `check-measure` | Profiles in [measure_profiles.json](https://github.com/CaioHAndradeLima/guardrails-strategies/blob/main/config/measure_profiles.json); **`ci-guardrails-eval`** uses `evaluate-pipeline`. GitHub Actions `measure-gate`. |

Pair with **[contexting-strategies](https://github.com/CaioHAndradeLima/contexting-strategies)** (tenant-scoped evidence), **[output-strategies](https://github.com/CaioHAndradeLima/output-strategies)** (post-LLM validation), and **[observability-strategies](https://github.com/CaioHAndradeLima/observability-strategies)** (incident/canary regression).
