# Embedding

Turn text **chunks and queries** into vectors for similarity search: model choice, batching, versioning, re-embedding, and query/index alignment.

Embeddings sit after [chunking](../chunking/) and before or inside the vector index in the [ingestion](../ingestion/) pipeline. Weak embeddings show up as poor semantic match—see **Embeddings** in [ingestion procedures](../ingestion/ingestion-procedures.md).

## Topic areas

| Area | Focus |
|------|--------|
| **[User queries](./queries/)** | Preprocess, embed, retrieve, eval, latency/cost |
| **Models & hosting** | Selection, hosted vs self-hosted, migration |
| **Index-time** | Document embed, metrics, bad practices |
| **Operations** | Versioning, re-index, observability tooling |

---

## Sections

| Section | Summary |
|---------|---------|
| [queries/](./queries/) | Online user question → query vector → evidence |
| _(this folder)_ | Document embedding, model lifecycle, platform metrics |

## Guides

### [embedding-decision-based.md](./embedding-decision-based.md)

`#decision-guide` · `#model-selection` · `#governance`

Selection factors and questions when choosing an embedding model for RAG.

Validate answers on a golden dataset and Recall@K—not benchmarks alone (chunking metrics observability).

→ [See more in embedding-decision-based.md](./embedding-decision-based.md)

### [embedding-hosted-vs-self-hosted.md](./embedding-hosted-vs-self-hosted.md)

`#deployment` · `#hosted` · `#self-hosted`

Compare hosted embedding APIs with self-hosted models when implementing RAG indexing and query embedding.

Use with embedding decision-based (deployment and data governance rows).

→ [See more in embedding-hosted-vs-self-hosted.md](./embedding-hosted-vs-self-hosted.md)

### [embedding-migration-ingestion-using-another-model.md](./embedding-migration-ingestion-using-another-model.md)

`#migration` · `#re-index` · `#blue-green`

Safe embedding model change: build and evaluate a new index on model B before switching query embeddings and retiring model A’s index.

→ [See more in embedding-migration-ingestion-using-another-model.md](./embedding-migration-ingestion-using-another-model.md)

### [embedding-metrics.md](./embedding-metrics.md)

`#observability` · `#metrics` · `#recall`

Metrics for embedding generation, index health, retrieval, and end-to-end RAG—what to measure and why.

Overlaps with chunking metrics observability; this note centers on the embedding and vector-search path.

→ [See more in embedding-metrics.md](./embedding-metrics.md)

### [embedding-tools-decision-based.md](./embedding-tools-decision-based.md)

`#tools` · `#observability` · `#startup-vs-scale`

Observability and evaluation tooling for embedding and RAG paths—startup vs scaling.

Complements embedding metrics (what to measure) and chunking tools decision-based (broader pipeline ops).

→ [See more in embedding-tools-decision-based.md](./embedding-tools-decision-based.md)

### [embedding-startup-vs-enterprise-architecture-decision-based.md](./embedding-startup-vs-enterprise-architecture-decision-based.md)

`#maturity` · `#architecture` · `#mvp-to-enterprise`

How embedding choices evolve from startup/MVP through medium SaaS to enterprise—model, hosting, ops, cost, eval, and security.

→ [See more in embedding-startup-vs-enterprise-architecture-decision-based.md](./embedding-startup-vs-enterprise-architecture-decision-based.md)

### [embedding-bad-practices.md](./embedding-bad-practices.md)

`#anti-patterns` · `#quality` · `#security`

Common embedding and retrieval mistakes, why they hurt, and what to do instead.

→ [See more in embedding-bad-practices.md](./embedding-bad-practices.md)

_User-query guides: [queries/README.md](./queries/README.md)_

## Related

- [Chunking](../chunking/) — what gets embedded
- [Ingestion](../ingestion/) — pipeline context
- [Retrieval architecturing decisions](../retrieval-architecturing-decision-based.md)
- [Embedding metrics](./embedding-metrics.md) · [Chunking metrics observability](../chunking/chunking-metrics-observability.md)
