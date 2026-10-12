# Index strategies

**Vector index structures** used for approximate or exact search—how each works and what you trade off. Builds on [storage strategy — exact vs ANN](./storage-strategy.md).

| Index / approach | General idea | Trade-off |
|------------------|--------------|-----------|
| **Flat / exact search** | Compare against all vectors | Exact results, but potentially expensive at scale |
| **HNSW** (Hierarchical Navigable Small World) | Graph-based navigation between nearby vectors ([query flow](./hnsw-flow.md)) | Often fast, but uses additional memory and indexing resources |
| **IVF** (Inverted File Index) | Partition vectors into clusters and search selected clusters | Can reduce search work, but requires tuning and may miss candidates |
| **Disk-oriented ANN approaches** | Storage-efficient structures to search large datasets | May trade latency and complexity for lower memory requirements |

## Choosing among ANN options

| If you need… | Often start with… |
|--------------|-------------------|
| Low query latency, RAM available | **HNSW** (many managed DB defaults) |
| Very large corpus, batch-heavy ingest | **IVF** (+ probe count tuning) |
| Memory-constrained or huge static indexes | **Disk-oriented ANN** (evaluate latency SLOs) |
| Small filtered candidate set | **Flat / exact** on the subset |

Always validate with **Recall@K** on your data after index build or parameter changes ([user query evaluation](../embedding/queries/embedding-user-query-evaluation.md)).

## See also

- [Storage strategy](./storage-strategy.md)
- [Storaging overview](./README.md)
- [Retrieval architecturing decision-based](../retrieval-architecturing-decision-based.md)
