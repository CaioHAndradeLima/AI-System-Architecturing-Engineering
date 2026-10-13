# Prompt architecturing decision-based

How **prompting** practices evolve from startup/prototype through growing production to enterprise / multi-agent.

| Area | Startup / Prototype | Growing Production | Enterprise / Multi-Agent |
|------|---------------------|--------------------|---------------------------|
| **Prompt design** | One clear system prompt and a user template | Reusable templates by task | Versioned prompt policies by task, agent, and tenant where justified |
| **Few-shot examples** | Add only for obvious failure cases | Evaluate examples against a golden dataset | Curated, versioned examples and regression coverage |
| **Grounding** | Ask the model to use supplied evidence | Require source IDs and explicit uncertainty | Validate citations and evidence provenance across agent workflows |
| **Structured output** | Parse and validate simple JSON | Pydantic schemas and controlled retries | Versioned schemas, compatibility tests, strict tool contracts |
| **Prompt injection** | Basic handling for untrusted content | Adversarial tests and independent tool authorization | Defense in depth, least privilege, audit trails, tenant isolation |
| **Prompt management** | Store prompts in source control | Version prompts and CI evaluations | Controlled promotion, canary, rollbacks, clear ownership |
| **Model configuration** | One suitable model with sensible defaults | Tune limits and compare alternative models | Routing and fallback policies; quality, latency, and cost constraints |
| **Evaluation** | Manual examples | Golden datasets and automated regression | Continuous evaluation per task, model, prompt, and agent |
| **Observability** | Basic errors and token counts | Trace prompt/model versions, latency, and cost | Distributed tracing, privacy controls, per-tenant monitoring, auditability |
| **Optimization** | Keep prompts simple and short | Reduce unnecessary tokens and retries | Optimize end-to-end quality and cost across the agent workflow |

## Guide links by area

| Area | Docs |
|------|------|
| Prompt design | [Standard format](./prompt-standard-format.md) · [Categories](./prompt-categories.md) |
| Few-shot | [Few-shot providing samples](./prompt-few-shot-providing-samples.md) |
| Grounding | [Context info for output](../contexting/context-info-for-output.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| Structured output | [Variables — structured output mode](./prompt-relevant-variables-influences.md) |
| Prompt injection | [Prompt injection](./prompt-injection.md) · [Reliable architecture](../contexting/context-reliable-architecture.md) |
| Prompt management | [Prompt versioning](./prompt-versioning.md) |
| Model configuration | [Variables and influences](./prompt-relevant-variables-influences.md) · [Embedding hosted vs self-hosted](../retrieval/embedding/embedding-hosted-vs-self-hosted.md) |
| Evaluation & observability | [Architecture evaluation (retrieval)](../retrieval/search/retrieval-architecture-evaluation.md) · [Context architecturing decision-based](../contexting/context-architecturing-decision-based.md) |
| Multi-agent | [Retrieval architecture decision](../retrieval/search/retrieval-architecture-decision.md) |

## See also

- [Observability decision-based by scale](../observability-evaluation/observability-decision-based.md)
- [Output decision-based by scale](../output/output-decision-based.md)
- [Context architecturing decision-based](../contexting/context-architecturing-decision-based.md)
- [Retrieval architecturing decision-based](../retrieval/retrieval-architecturing-decision-based.md)
- [Prompting overview](./README.md)
