# Embedding hosted vs self-hosted

Compare **hosted embedding APIs** with **self-hosted models** when implementing RAG indexing and query embedding. Use with [embedding decision-based](./embedding-decision-based.md) (deployment and data governance rows).

| Dimension | Hosted API | Self-hosted model |
|-----------|------------|-------------------|
| **Initial setup** | Usually simpler | Requires serving infrastructure |
| **Scaling** | Provider handles much of the serving infrastructure | Your team manages capacity and deployment |
| **Cost structure** | Often usage-based | Compute, hosting, and operations |
| **Latency** | Includes network and provider latency | Can be low with local serving, but depends on hardware and load |
| **Data governance** | Requires reviewing provider terms and controls | More direct control over where inference runs |
| **Model customization** | Depends on provider | Greater deployment flexibility, depending on the model and license |

## Practical guidance

- **Hosted** fits most MVPs and many SaaS products when contracts allow sending chunk text to the provider ([basic document ingestion](../ingestion/basic-document-ingestion.md) embedding step).
- **Self-hosted** when data must stay in a VPC, air-gapped region, or specific jurisdiction—or when embedding volume makes usage-based cost dominate ([chunking metrics — embedding cost](../chunking/chunking-metrics-observability.md)).
- Either path: record **`embedding_model_id`** and **`embedding_model_version`** on every vector batch for re-index and debugging.

## See also

- [Embedding decision-based](./embedding-decision-based.md)
- [Chunking architecturing decision-based — Embedding strategy](../chunking/chunking-architecturing-decision-based.md)
- [Embedding overview](./README.md)
