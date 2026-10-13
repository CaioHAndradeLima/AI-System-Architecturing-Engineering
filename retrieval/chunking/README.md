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

A fixed-size window with overlap: split long text into passages small enough for precise retrieval, with shared boundary tokens so facts split across cuts still appear whole in at least one chunk.

→ [See more in chunking-simpler-strategy.md](./chunking-simpler-strategy.md)

### [chunking-recursive-structure-aware.md](./chunking-recursive-structure-aware.md)

`#structure-aware` · `#headings` · `#tables`

Split on document structure first (headings, sections), then fall back to paragraphs and sentences only when a section exceeds the size limit.

Contrast with pure fixed windows in chunking simpler strategy.

→ [See more in chunking-recursive-structure-aware.md](./chunking-recursive-structure-aware.md)

### [chunking-semantic.md](./chunking-semantic.md)

`#semantic` · `#embeddings` · `#topic-boundaries`

Split text at topic boundaries instead of fixed token windows: embed sentence-level (or passage-level) units, compare neighbors, cut where meaning shifts, then clamp to min/max chunk sizes.

→ [See more in chunking-semantic.md](./chunking-semantic.md)

### [chunking-hierarchical-parent-child.md](./chunking-hierarchical-parent-child.md)

`#hierarchical` · `#parent-child` · `#retrieval`

Two-level index: small child chunks for precise vector search; larger parent sections for context passed to the LLM after a relevant child hit.

→ [See more in chunking-hierarchical-parent-child.md](./chunking-hierarchical-parent-child.md)

### [chunking-architecturing.md](./chunking-architecturing.md)

`#architecture` · `#decision-matrix` · `#production`

Decision matrix for choosing a starting chunking strategy in a production RAG system.

Validate choices on your corpus with golden questions and Recall@K (ingestion observability).

→ [See more in chunking-architecturing.md](./chunking-architecturing.md)

### [chunking-tools.md](./chunking-tools.md)

`#tools` · `#langchain` · `#llamaindex`

Reference tools for splitting, parsing, token counting, and evaluating chunk configs—not a mandatory stack; pick per chunking architecturing strategy.

→ [See more in chunking-tools.md](./chunking-tools.md)

### [chunking-architecturing-decision-based.md](./chunking-architecturing-decision-based.md)

`#maturity` · `#mvp-to-enterprise` · `#operations`

How chunking and indexing choices evolve from startup/MVP through medium SaaS to enterprise—plus multi-tenancy, failures, evaluation, and scaling triggers.

→ [See more in chunking-architecturing-decision-based.md](./chunking-architecturing-decision-based.md)

### [chunking-metrics-observability.md](./chunking-metrics-observability.md)

`#observability` · `#metrics` · `#recall`

Metrics for chunking, embedding, indexing, retrieval, and answers—what to measure at startup vs enterprise.

Complements ingestion observability with chunk-specific signals.

→ [See more in chunking-metrics-observability.md](./chunking-metrics-observability.md)

### [chunking-tools-decision-based.md](./chunking-tools-decision-based.md)

`#tools` · `#observability` · `#startup-vs-scale`

Observability and orchestration choices for chunking and RAG pipelines at startup vs scale.

Pairs with chunking tools (splitters/parsers) and chunking metrics observability (what to measure).

→ [See more in chunking-tools-decision-based.md](./chunking-tools-decision-based.md)

## Related

- [Ingestion](../ingestion/) — full index-time pipelines
- [Retrieval architecturing decisions](../retrieval-architecturing-decision-based.md) — chunking maturity by system size
- [Ingestion observability](../ingestion/ingestion-observability.md) — Recall@K and duplicate chunk rate
