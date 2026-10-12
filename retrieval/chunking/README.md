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

### [chunking-recursive-structure-aware.md](./chunking-recursive-structure-aware.md)

`#structure-aware` · `#headings` · `#tables`

Recursive split at headings → paragraphs → sentences; baseline benefits and when tables/code need special handling.

→ [See more in chunking-recursive-structure-aware.md](./chunking-recursive-structure-aware.md)

### [chunking-semantic.md](./chunking-semantic.md)

`#semantic` · `#embeddings` · `#topic-boundaries`

Embed sentences, detect meaning shifts, form semantic chunks, then enforce min/max size—with advantage vs trade-off table.

→ [See more in chunking-semantic.md](./chunking-semantic.md)

### [chunking-hierarchical-parent-child.md](./chunking-hierarchical-parent-child.md)

`#hierarchical` · `#parent-child` · `#retrieval`

Search small child chunks, then expand to authorized parent sections for LLM context (e.g. API manual sections).

→ [See more in chunking-hierarchical-parent-child.md](./chunking-hierarchical-parent-child.md)

### [chunking-architecturing.md](./chunking-architecturing.md)

`#architecture` · `#decision-matrix` · `#production`

Document type → recommended starting strategy and rationale; links to specific guides in this folder.

→ [See more in chunking-architecturing.md](./chunking-architecturing.md)

### [chunking-tools.md](./chunking-tools.md)

`#tools` · `#langchain` · `#llamaindex`

LangChain splitters, LlamaIndex nodes, PyMuPDF, tokenizers, and eval scripts—roles and when to use each.

→ [See more in chunking-tools.md](./chunking-tools.md)

### [chunking-architecturing-decision-based.md](./chunking-architecturing-decision-based.md)

`#maturity` · `#mvp-to-enterprise` · `#operations`

Two tables: chunking/parsing/storage/metadata by scale, plus tenancy, failures, evaluation, and scaling triggers.

→ [See more in chunking-architecturing-decision-based.md](./chunking-architecturing-decision-based.md)

### [chunking-metrics-observability.md](./chunking-metrics-observability.md)

`#observability` · `#metrics` · `#recall`

Pipeline, chunk quality, retrieval, answer, and cross-tenant metrics—startup vs enterprise practices.

→ [See more in chunking-metrics-observability.md](./chunking-metrics-observability.md)

## Related

- [Ingestion](../ingestion/) — full index-time pipelines
- [Retrieval architecturing decisions](../retrieval-architecturing-decision-based.md) — chunking maturity by system size
- [Ingestion observability](../ingestion/ingestion-observability.md) — Recall@K and duplicate chunk rate
