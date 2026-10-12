# LLM implementation flow

**LLM model selection and generation checklist**—from requirements through eval, inference, reliability, and canary deploy.

```
LLM MODEL SELECTION & GENERATION CHECKLIST
==========================================

                  START
                    |
                    v
+------------------------------------------+
| 1. Define task requirements              |
|    Quality, latency, cost, context size  |
+------------------------------------------+
                    |
                    v
+------------------------------------------+
| 2. Select candidate models               |
|    Hosted API vs. open-weight            |
+------------------------------------------+
                    |
                    v
+------------------------------------------+
| 3. Evaluate on a golden dataset          |
|    Quality, tool calls, groundedness     |
+------------------------------------------+
                    |
                    v
+------------------------------------------+
| 4. Configure generation                  |
|    Temperature, output limits, format    |
+------------------------------------------+
                    |
                    v
+------------------------------------------+
| 5. Implement inference                   |
|    Timeouts, streaming, async calls      |
+------------------------------------------+
                    |
                    v
+------------------------------------------+
| 6. Validate tool calls and outputs       |
|    Schemas, permissions, bounded steps   |
+------------------------------------------+
                    |
                    v
+------------------------------------------+
| 7. Add reliability controls              |
|    Retries, rate limits, fallback model  |
+------------------------------------------+
                    |
                    v
+------------------------------------------+
| 8. Measure quality, latency, and cost    |
+------------------------------------------+
                    |
                    v
          Meets requirements?
              /       \
            NO         YES
            |           |
            v           v
      Tune / replace  Canary release
      and re-evaluate      |
                           v
                   Monitor production
                           |
                           v
                         DEPLOY
```

## Step → guides

| Step | Docs |
|------|------|
| 1. Task requirements | [LLM flow — model selection](./llm-flow.md) · [Decision-based by scale](./llm-decision-based.md) |
| 2. Candidate models | [Hosted vs open-weight](./llm-hosted-vs-open-weight-models.md) · [Select LLM flow](./select-llm-flow.md) |
| 3. Golden dataset eval | [Select LLM flow](./select-llm-flow.md) · [Query evaluation](../retrieval/embedding/queries/embedding-user-query-evaluation.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| 4. Generation config | [Generation parameters](./llm-generation-parameters.md) · [Prompt standard format](../prompting/prompt-standard-format.md) |
| 5. Inference | [Async vs streaming](./llm-async-vs-streaming.md) · [Cloud services](./llm-cloud-services.md) |
| 6. Tools & outputs | [Routing policy — authorization row](./llm-routing-policy.md) · [Prompt injection](../prompting/prompt-injection.md) |
| 7. Reliability | [Retry, fallbacks, and routing](./llm-retry-fallbacks-routing.md) · [Architecturing — gateway](./llm-architecturing.md) |
| 8. Measure | [Latency variables and measurement](./llm-latency-variables-measurement.md) · [Deciding sample](./select-llm-deciding-sample.md) |
| Canary / deploy | [Prompt versioning](../prompting/prompt-versioning.md) |
| Full stack | [Prompt implementation flow](../prompting/prompt-implementation-flow.md) · [Retrieval implementation](../retrieval/search/retrieval-implementation-flow.md) |

## See also

- [LLM overview](./README.md)
