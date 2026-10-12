# Embedding

Turn text **chunks and queries** into vectors for similarity search: model choice, batching, versioning, re-embedding, and query/index alignment.

Embeddings sit after [chunking](../chunking/) and before or inside the vector index in the [ingestion](../ingestion/) pipeline. Weak embeddings show up as poor semantic match—see **Embeddings** in [ingestion procedures](../ingestion/ingestion-procedures.md).

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Models** | Hosted APIs vs local, dimensions, multilingual |
| **Index vs query** | Same model and preprocessing for both paths |
| **Batching & cost** | Throughput, rate limits, embedding cost per document |
| **Versioning** | Model upgrades, re-index jobs, metadata on vectors |
| **Quality** | Drift monitoring, benchmarks vs retrieval Recall@K |
| **Multi-tenant** | Per-tenant quotas, isolated embedding workloads |

---

## Guides

_Guide entries (tags, short description, see-more links) will appear here as markdown files are added—same style as [chunking README](../chunking/README.md)._

## Related

- [Chunking](../chunking/) — what gets embedded
- [Ingestion](../ingestion/) — pipeline context
- [Retrieval architecturing decisions](../retrieval-architecturing-decision-based.md) — Embeddings row by scale
- [Chunking metrics observability](../chunking/chunking-metrics-observability.md) — embedding latency and cost
