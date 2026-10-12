# Storage architecturing decision-based

Pick a **vector storage** starting point by requirement—not by popularity alone. Pair with [index strategies](./index-strategies.md) and [storage strategy](./storage-strategy.md) once you know scale and recall targets.

| Requirement | Good starting option | Why |
|-------------|---------------------|-----|
| Learn embeddings and similarity search | **FAISS** | Direct access to vector search concepts |
| Build a small local RAG prototype | **Chroma or FAISS** | Low setup overhead |
| Existing application already uses PostgreSQL | **pgvector** | Reuse existing relational infrastructure |
| Need relational transactions and vector search | **PostgreSQL + pgvector** | One database can handle both |
| Dedicated managed vector-search service | **Pinecone** or a managed **Qdrant/Weaviate** offering | Less infrastructure management |
| Self-managed dedicated vector service | **Qdrant**, **Weaviate**, or **Milvus** | More control over deployment and configuration |
| Very large corpus with strict performance goals | Benchmark dedicated indexes and database options | Workload, hardware, filtering, and recall targets determine the winner |

## How this maps to the repo

| Requirement row | See also |
|-----------------|----------|
| Prototype / pgvector | [Minimum ingestion MVP](../ingestion/minimum-ingestion-mvp.md) · [Compact decision — pgvector/Chroma](../compacting/compact-decision-based.md) |
| DB + vectors (messages) | [Compact architecture flow](../compacting/compact-architecture-flow.md) |
| Maturity by scale | [Retrieval architecturing decision-based — Vector storage](../retrieval-architecturing-decision-based.md) · [Chunking architecturing — Storage row](../chunking/chunking-architecturing-decision-based.md) |
| Tenant isolation | [Guard-rails data isolation](../../guard-rails/guardrails-data-isolation.md) |
| Large corpus performance | [HNSW flow](./hnsw-flow.md) · [Embedding metrics — retrieval latency](../embedding/embedding-metrics.md) |

Vendor features change—re-benchmark on **your** filters, dimension count, and QPS before committing.

## See also

- [Storaging overview](./README.md)
- [Embedding hosted vs self-hosted](../embedding/embedding-hosted-vs-self-hosted.md)
