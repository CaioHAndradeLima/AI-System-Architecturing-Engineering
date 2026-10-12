# Retrieval simple ingestion

Offline **indexing pipeline** from heterogeneous sources into a vector index: ingest, parse, chunk, embed, and store chunks with metadata for later query-time retrieval.

## Sources

```
PDFs / Confluence / DB / APIs
```

Connectors differ per system; the pipeline stages stay the same. Track **source identity**, **version**, and **permissions metadata** at ingestion so query-time filters can enforce tenant and document ACLs ([guard-rails](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)).

## Pipeline

```
PDFs / Confluence / DB / APIs
                |
                v
       +--------------------+
       | 1. Ingestion       |
       | Fetch and track    |
       | source documents   |
       +--------------------+
                |
                v
       +--------------------+
       | 2. Parsing         |
       | Extract text and   |
       | document structure |
       +--------------------+
                |
                v
       +--------------------+
       | 3. Chunking        |
       | Split into useful  |
       | sections           |
       +--------------------+
                |
                v
       +--------------------+
       | 4. Embeddings      |
       | Text -> vectors    |
       +--------------------+
                |
                v
       +--------------------+
       | 5. Indexing        |
       | Store vectors,     |
       | chunks, metadata   |
       +--------------------+
                |
                v
           VECTOR INDEX
```

## Stage responsibilities

| Stage | Role |
|-------|------|
| **1. Ingestion** | Pull or receive documents; dedupe by source ID; record crawl/sync state and deletion signals. |
| **2. Parsing** | Extract clean text, headings, tables where possible; preserve structure hints for chunk boundaries. |
| **3. Chunking** | Split into retrieval-sized units with overlap and metadata (page, section, URL, `tenant_id`, ACL). |
| **4. Embeddings** | Map chunk text to vectors with a chosen model; version the embedding model in metadata. |
| **5. Indexing** | Upsert vectors + chunk text + filters into the vector store; support updates and tombstones for removed docs. |

## Practical checklist

- [ ] Idempotent ingestion (re-run safe) with clear **document IDs** and **content hashes**
- [ ] Store **embedding model ID** and **chunking config** on each index batch for reproducibility
- [ ] Apply **tenant and permission metadata** before indexing, not only at query time
- [ ] Monitor lag between source change and index refresh

## See also

- [Ingestion procedures — component failures](./ingestion-procedures.md)
- [Ingestion overview](./README.md)
- [Retrieval overview](../README.md)
- [Sequential pipeline — retrieval agent](../../agents/multi-agent-architecture/sequencial-ai-pipeline.md)
