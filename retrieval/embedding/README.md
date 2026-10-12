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

### [embedding-decision-based.md](./embedding-decision-based.md)

`#decision-guide` · `#model-selection` · `#governance`

Ten selection factors (quality, languages, domain, latency, cost, deployment, ops) with questions to ask before committing.

→ [See more in embedding-decision-based.md](./embedding-decision-based.md)

### [embedding-hosted-vs-self-hosted.md](./embedding-hosted-vs-self-hosted.md)

`#deployment` · `#hosted` · `#self-hosted`

Setup, scaling, cost, latency, governance, and customization—hosted API vs self-hosted inference.

→ [See more in embedding-hosted-vs-self-hosted.md](./embedding-hosted-vs-self-hosted.md)

### [embedding-migration-ingestion-using-another-model.md](./embedding-migration-ingestion-using-another-model.md)

`#migration` · `#re-index` · `#blue-green`

Evaluate model B, build new index, switch query+index together, retire model A after validation.

→ [See more in embedding-migration-ingestion-using-another-model.md](./embedding-migration-ingestion-using-another-model.md)

### [embedding-metrics.md](./embedding-metrics.md)

`#observability` · `#metrics` · `#recall`

Latency, throughput, cost, cache, dimension consistency, freshness, Recall@K, and answer correctness.

→ [See more in embedding-metrics.md](./embedding-metrics.md)

### [embedding-tools-decision-based.md](./embedding-tools-decision-based.md)

`#tools` · `#observability` · `#startup-vs-scale`

Logs, traces, RAG eval, LangSmith/Langfuse, and per-tenant embedding usage—starting vs scaling stack.

→ [See more in embedding-tools-decision-based.md](./embedding-tools-decision-based.md)

### [embedding-startup-vs-enterprise-architecture-decision-based.md](./embedding-startup-vs-enterprise-architecture-decision-based.md)

`#maturity` · `#architecture` · `#mvp-to-enterprise`

Eleven areas—from model selection and hosting through caching, upgrades, cost, eval, security, and observability by scale.

→ [See more in embedding-startup-vs-enterprise-architecture-decision-based.md](./embedding-startup-vs-enterprise-architecture-decision-based.md)

### [embedding-bad-practices.md](./embedding-bad-practices.md)

`#anti-patterns` · `#quality` · `#security`

Nine common embedding mistakes with fixes—dimensions, similarity scores, model mix, ACL, hybrid search, re-embed waste.

→ [See more in embedding-bad-practices.md](./embedding-bad-practices.md)

## Related

- [Chunking](../chunking/) — what gets embedded
- [Ingestion](../ingestion/) — pipeline context
- [Retrieval architecturing decisions](../retrieval-architecturing-decision-based.md) — Embeddings row by scale
- [Embedding metrics](./embedding-metrics.md) · [Chunking metrics observability](../chunking/chunking-metrics-observability.md)
