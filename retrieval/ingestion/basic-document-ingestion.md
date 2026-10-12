# Basic document ingestion

**Upload-driven ingestion pipeline** for PDFs: accept the file, store the original, parse and clean text, chunk, embed, and load the vector database for query-time retrieval.

## Pipeline

```
                  INGESTION PIPELINE
                  ==================

 User uploads PDF
       |
       v
  [API / Upload]
       |
       v
  [File Storage] ------> Original PDF
       |
       v
  [Document Parser]
       |
       v
  [Text Cleaning + Validation]
       |
       v
  [Chunking]
       |
       v
  [Embedding Model]
       |
       v
  [Vector Database]
       |
       v
  Ready for retrieval
```

## Stage notes

| Stage | Role |
|-------|------|
| **API / Upload** | Authenticate caller, validate file type/size, assign document ID and tenant metadata. |
| **File Storage** | Keep the **original PDF** for re-parse, audit, and citation links—not only derived text. |
| **Document Parser** | Extract text and layout signals (pages, headings) from PDF. |
| **Text Cleaning + Validation** | Strip noise, detect empty/garbled parses, fail or quarantine bad uploads. |
| **Chunking** | Split into retrieval units; attach page numbers and document ID to each chunk. |
| **Embedding Model** | Vectorize chunks; record model version on the batch. |
| **Vector Database** | Upsert vectors with chunk text and filters (`tenant_id`, `document_id`, ACL). |

## Relation to other ingestion docs

- Broader sources (Confluence, DB, APIs): [retrieval simple ingestion](./retrieval-simple-ingestion.md)
- End-to-end component failures: [ingestion procedures](./ingestion-procedures.md)
- Smallest query loop after index is ready: [minimum ingestion MVP](./minimum-ingestion-mvp.md)

## Practical checklist

- [ ] Virus scan or sandbox if uploads are user-supplied
- [ ] Async job for parse → embed so the upload API returns quickly with a **processing status**
- [ ] Re-index path when parser or embedding model changes
- [ ] Tenant-scoped object keys in file storage and vector metadata ([guard-rails](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md))

## See also

- [Ingestion overview](./README.md)
- [Retrieval overview](../README.md)
