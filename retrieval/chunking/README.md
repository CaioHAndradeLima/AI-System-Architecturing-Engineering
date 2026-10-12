# Chunking

Split source documents into **retrieval units**: size, overlap, structure-aware boundaries, and metadata that survives into the vector index and citations.

Chunking sits after parsing and before embedding in the [ingestion](../ingestion/) pipeline. Poor chunking shows up as fragmented or oversized context—see the **Chunking** row in [ingestion procedures](../ingestion/ingestion-procedures.md).

## What we document here

| Topic | Focus |
|-------|--------|
| **Strategy** | Fixed size, semantic, document-structure (headings, pages) |
| **Parameters** | Chunk size, overlap, min/max length |
| **Metadata** | Section titles, page numbers, source IDs for filters and cites |
| **Evaluation** | Compare chunk configs against Recall@K and answer quality |
| **Versioning** | Re-chunk jobs when strategy changes |

---

## Guides

### [chunking-simpler-strategy.md](./chunking-simpler-strategy.md)

`#fixed-size` · `#overlap` · `#langchain`

200-token / 40-token overlap example, trade-off table, and `RecursiveCharacterTextSplitter` with character vs token notes.

→ [See more in chunking-simpler-strategy.md](./chunking-simpler-strategy.md)

## Related

- [Ingestion](../ingestion/) — full index-time pipelines
- [Retrieval architecturing decisions](../retrieval-architecturing-decision-based.md) — chunking maturity by system size
- [Ingestion observability](../ingestion/ingestion-observability.md) — Recall@K and duplicate chunk rate
