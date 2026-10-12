# Embedding decision-based

**Selection factors** and questions when choosing an embedding model for RAG. Validate answers on a **golden dataset** and Recall@K—not benchmarks alone ([chunking metrics observability](../chunking/chunking-metrics-observability.md)).

| Selection factor | Questions to ask |
|------------------|------------------|
| **Retrieval quality** | Does it retrieve the evidence needed to answer our real questions? |
| **Language support** | Does it handle Portuguese, English and the languages used by our customers? |
| **Domain fit** | Does it work well with legal, financial, medical, technical or business text relevant to our use case? |
| **Context length** | Can it handle the maximum input size required by your chunking configuration? |
| **Dimensions** | What is the output size, and can it be configured? |
| **Latency** | How long does it take to embed queries and batches of documents? |
| **Cost** | What is the cost per token or other billing unit? |
| **Deployment** | Is a hosted API acceptable, or must embeddings run in your own environment? |
| **Data governance** | Can your organization send this data to the selected provider? |
| **Operational maturity** | Are versioning, batching, limits, availability and migration options adequate? |

## How this ties to the pipeline

- **Context length** must match [chunking](../chunking/) max chunk size (tokens or chars after tokenizer mapping).
- **Same model** for index and query paths—see upcoming embedding flow docs; mismatch breaks semantic search.
- **Migration** when changing models: plan re-embed per [chunking architecturing decision-based](../chunking/chunking-architecturing-decision-based.md) (hash/version incremental embedding at scale).
- **Governance** overlaps [guard-rails](../../guard-rails/) (data protection, tenant isolation—not sending cross-tenant batches to the wrong region/account).

## See also

- [Retrieval architecturing decisions — Embeddings](../retrieval-architecturing-decision-based.md)
- [Ingestion procedures — Embeddings row](../ingestion/ingestion-procedures.md)
- [Embedding overview](./README.md)
