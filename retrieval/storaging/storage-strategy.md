# Storage strategy

How the **vector index** answers similarity search—exact scan vs approximate index—and when each fits your scale and recall targets.

## Search strategies

| Strategy | Behavior | When to use |
|----------|----------|-------------|
| **Exact nearest-neighbor search** | Compare the query against every candidate vector | Small datasets or workloads where exact results matter |
| **Approximate nearest-neighbor (ANN) search** | Use an index to search a smaller candidate set much faster, with a possible loss of recall | Larger corpora, low-latency query paths, production RAG at scale |

## Practical notes

- **Exact** — simple with [FAISS flat / brute force](https://github.com/facebookresearch/faiss), small pgvector tables, or post-filter after metadata narrows candidates sharply. Cost grows linearly with index size.
- **ANN** — HNSW, IVF, product quantization, and managed vector DB defaults; tune build params and `ef_search` / probe counts against [Recall@K](../../embedding/queries/embedding-user-query-evaluation.md) on your golden set.
- **Metadata first** — tenant and ACL filters reduce candidate count; sometimes exact search on the filtered subset is enough ([safer tenant-scoped retrieval](../../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)).
- Pair strategy choice with [retrieval architecturing — Vector storage](../retrieval-architecturing-decision-based.md) and [compact decision-based](../compacting/compact-decision-based.md) (prototype vs managed service).

## See also

- [Storaging overview](./README.md)
- [Embedding metrics — retrieval latency](../embedding/embedding-metrics.md)
- [Chunking metrics — Recall@K](../chunking/chunking-metrics-observability.md)
