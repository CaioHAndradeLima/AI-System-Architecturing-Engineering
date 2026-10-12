# LLM hosted vs open-weight models

**Hosted (managed API)** versus **self-hosted open-weight** inference for chat/completion models. For **embedding** hosting, see [embedding hosted vs self-hosted](../retrieval/embedding/embedding-hosted-vs-self-hosted.md).

## Hosted examples

OpenAI API, Amazon Bedrock, Azure OpenAI, Gemini APIs.

### Advantages

- Fast to integrate and launch.
- No need to operate GPU infrastructure.
- Provider manages model serving and much of the scaling.
- Easier to experiment with multiple models.

### Trade-offs

- Usage-based cost and possible rate limits.
- Dependence on provider availability and API behavior.
- Less control over model internals.
- Data handling and regional requirements need review.

### Flow

```
Your Application
       |
       v
Provider API
       |
       v
Managed Model
       |
       v
Generated Response
```

## Self-hosted open-weight model

### Advantages

- More control over model versions and serving configuration.
- Can support specialized privacy, networking, or deployment requirements.
- Potential cost advantages at sustained high utilization.
- More flexibility for model adaptation and fine-tuning, subject to the model license.

### Trade-offs

- You own deployment, scaling, capacity planning, and performance tuning.
- GPU infrastructure can be expensive when underutilized.
- Reliability, security patching, and model-serving operations become your responsibility.
- A smaller open-weight model may perform worse on difficult reasoning or tool-use tasks.

### Flow

```
Your Application
       |
       v
Inference Server
       |
       v
GPU / CPU Infrastructure
       |
       v
Model Weights
       |
       v
Generated Response
```

## Choosing (starting point)

| Signal | Lean hosted | Lean self-hosted |
|--------|-------------|------------------|
| Time to market, small team | ✓ | |
| Strict data residency / air-gap | Review provider; may need | ✓ |
| Steady high QPS on one model | Cost model dependent | Often ✓ |
| Rapid model A/B | ✓ | |
| Heavy tool-use / reasoning quality bar | Strong hosted tiers | Match with eval, not assumptions |

Map products to [LLM cloud services](./llm-cloud-services.md) and [retrieval cloud tools](../retrieval/search/retrieval-cloud-tools.md). Align with [LLM flow — model selection](./llm-flow.md) and [guard-rails cloud comparison](../guard-rails/guard-rails-cloud-comparison.md) for data handling.

## See also

- [LLM questions — hosted vs open-weight](./llm-questions.md)
- [LLM overview](./README.md)
