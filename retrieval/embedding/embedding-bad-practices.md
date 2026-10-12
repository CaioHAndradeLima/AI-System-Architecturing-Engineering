# Embedding bad practices

Common **embedding and retrieval mistakes**, why they hurt, and what to do instead.

| Mistake | Why it is a problem | Better approach |
|---------|----------------------|-----------------|
| **Assuming more dimensions mean better quality** | Higher dimensionality can increase cost without improving results | Benchmark quality and storage together |
| **Treating cosine similarity as a probability** | Similarity scores are not calibrated answer-confidence scores | Calibrate thresholds on labeled data |
| **Mixing vectors from incompatible models** | Similarity comparisons may become meaningless | Keep model and index versions compatible |
| **Ignoring query/document encoding instructions** | Retrieval quality can degrade even when code runs | Follow the model's retrieval documentation |
| **Using one embedding model for every language without testing** | Multilingual performance varies | Evaluate actual queries in every supported language |
| **Assuming semantic search replaces keyword search** | Exact IDs and rare terms can be difficult to retrieve semantically | Benchmark hybrid search |
| **Re-embedding all documents for every run** | Wastes tokens, time, and money | Use versioning, hashes, and incremental processing |
| **Assuming the embedding model prevents data leakage** | Embeddings do not enforce authorization | Enforce tenant and document access in the retrieval system |
| **Selecting a model from benchmark rankings alone** | Public benchmarks may not reflect your data | Build a representative golden dataset |

## Related guides

| Mistake theme | See |
|---------------|-----|
| Model / index compatibility | [Migration using another model](./embedding-migration-ingestion-using-another-model.md) |
| Dimensions, cost, eval | [Decision-based](./embedding-decision-based.md) · [Metrics](./embedding-metrics.md) |
| Authorization | [Safer tenant-scoped retrieval](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md) · [Wrong shared retrieval](../../guard-rails/wrong-architecture-shared-retrieval.md) |
| Incremental embed | [Multi-source ingestion](../ingestion/multi-source-ingestion.md) · [Startup vs enterprise table](./embedding-startup-vs-enterprise-architecture-decision-based.md) |

## See also

- [Embedding overview](./README.md)
- [Guard-rails — rules I would never compromise on](../../guard-rails/guard-rails-decision-architecturing-assistance.md#the-rules-i-would-never-compromise-on)
