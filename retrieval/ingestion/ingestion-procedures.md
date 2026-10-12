# Ingestion procedures

End-to-end **retrieval pipeline components**: what each stage owns and what breaks when it is done poorly. Stages 1–5 align with [simple ingestion](./retrieval-simple-ingestion.md); retrieval, reranking, and evaluation are query-time and quality layers on top of the index.

| Component | Responsibility | What happens if it's poor? |
|-----------|----------------|----------------------------|
| **Ingestion** | Fetches source data and tracks updates/deletions | Missing or stale knowledge |
| **Parsing** | Extracts usable text and structure | Tables, sections, or important information disappear |
| **Chunking** | Divides content into retrievable units | Context is fragmented or too large |
| **Embeddings** | Represents text for semantic matching | Relevant concepts may not match well |
| **Indexing** | Makes chunks searchable | Slow or inaccurate retrieval |
| **Retrieval** | Finds candidate evidence for a question | The model receives irrelevant or incomplete context |
| **Reranking** | Improves candidate ordering | Strong evidence may be buried below weaker results |
| **Evaluation** | Measures whether the pipeline works | Regressions remain invisible |

Use this table for **on-call triage** (symptom → likely stage) and for **test planning** (each row should have at least one measurable check).

## See also

- [Retrieval simple ingestion](./retrieval-simple-ingestion.md)
- [Ingestion overview](./README.md)
- [Retrieval overview](../README.md)
- [Guard-rails — retrieval authorization](../../guard-rails/guard-rails-decision-architecturing-assistance.md)
