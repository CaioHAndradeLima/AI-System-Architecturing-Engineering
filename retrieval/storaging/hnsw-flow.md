# HNSW flow

**Query-time path** for [HNSW](./index-strategies.md) (Hierarchical Navigable Small World): graph traversal to approximate nearest neighbors without scanning every vector.

## Flow

```
        All stored vectors
                |
                v
       Navigate vector graph
                |
                v
       Explore promising neighbors
                |
                v
       Collect nearest candidates
                |
                v
       Return top-K results
```

## Stage notes

| Stage | Role |
|-------|------|
| **All stored vectors** | Indexed at ingest with an HNSW graph structure (layers, links between neighbors)—built offline, not at query time |
| **Navigate vector graph** | Start from an entry point; greedy move toward the query vector in upper layers |
| **Explore promising neighbors** | Expand local neighborhoods (`efConstruction` at build, `efSearch` at query)—wider search explores more nodes |
| **Collect nearest candidates** | Maintain a priority queue of best distances seen so far |
| **Return top-K results** | Truncate to K; apply **metadata filters** (tenant, ACL) per your store’s pre/post-filter model |

## Tuning and validation

- Higher **`efSearch`** → better recall, more latency ([storage strategy](./storage-strategy.md) ANN trade-off).
- Rebuild or reindex when **embedding model or dimensions** change—graph is tied to vector geometry ([embedding migration](../embedding/embedding-migration-ingestion-using-another-model.md)).
- Compare Recall@K vs flat search on a sample before trusting defaults ([user query evaluation](../embedding/queries/embedding-user-query-evaluation.md)).

## See also

- [Index strategies](./index-strategies.md)
- [Storaging overview](./README.md)
