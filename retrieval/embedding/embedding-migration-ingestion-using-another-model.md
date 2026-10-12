# Embedding migration — ingestion using another model

Safe **embedding model change**: build and evaluate a new index on model B before switching query embeddings and retiring model A’s index.

## Flow

```
  Existing document corpus
          |
          v
  Index using model A
          |
          v
  Evaluate model B on golden dataset
          |
          v
  Create new index using model B
          |
          v
  Evaluate retrieval quality and cost
          |
          v
  Switch query embedding + index together
          |
          v
  Retire old index after validation
```

## Stage notes

| Stage | Role |
|-------|------|
| **Index using model A** | Current production baseline; tag all vectors with `embedding_model_id=A`. |
| **Evaluate model B on golden dataset** | Offline embed sample chunks or queries with B; compare Recall@K / answer quality—not provider marketing benchmarks alone. |
| **Create new index using model B** | Full or incremental re-embed of corpus into a **separate** index or namespace (blue/green). |
| **Evaluate retrieval quality and cost** | Same golden set against B index; measure latency and [embedding cost](../chunking/chunking-metrics-observability.md). |
| **Switch query embedding + index together** | **Never** query with model B against index A (or vice versa)—vectors must share the same model and preprocessing. |
| **Retire old index after validation** | Drop or archive A after soak period; keep rollback path until metrics stable. |

## When to re-embed vs update metadata

| Change | Typical action |
|--------|----------------|
| **Document text changes** | Re-embed affected chunks |
| **Chunk boundaries change** | Re-embed the newly created chunks |
| **Embedding model changes** | Re-embed the corpus into a compatible index |
| **Supported output dimension changes** | Build a compatible new index and re-embed |
| **Only metadata changes** | Update metadata where supported; re-embedding may not be necessary |
| **Document is deleted** | Remove its vectors and related searchable records |
| **Document access is revoked** | Ensure retrieval can no longer expose its content; update permissions and remove or invalidate stale indexed data as appropriate |

Access revocation is an **authorization** change—fix filters and index state even when vectors are unchanged ([guard-rails test use cases](../../guard-rails/guard-rails-test-use-cases.md)).

## Checklist

- [ ] Version metadata on chunks: `embedding_model_id`, `chunker_version`, `indexed_at`
- [ ] Dual-write or read from B in shadow mode before cutover
- [ ] Tenant filters unchanged on both indexes ([guard-rails](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md))
- [ ] Document rollback: flip routing back to index A if Recall@K or errors regress

## See also

- [Embedding decision-based](./embedding-decision-based.md)
- [Embedding hosted vs self-hosted](./embedding-hosted-vs-self-hosted.md)
- [Chunking architecturing decision-based — Embedding strategy](../chunking/chunking-architecturing-decision-based.md)
- [Multi-source ingestion — index version state](../ingestion/multi-source-ingestion.md)
