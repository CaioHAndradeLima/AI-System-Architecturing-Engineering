# Chunking architecturing

Decision matrix for choosing a **starting chunking strategy** in a production RAG system. Validate choices on your corpus with golden questions and Recall@K ([ingestion observability](../ingestion/ingestion-observability.md)).

| Document type or requirement | Recommended starting strategy | Why |
|------------------------------|-------------------------------|-----|
| Plain text, simple FAQ | Recursive splitting | Simple, effective baseline |
| Markdown or structured documentation | Structure-aware splitting | Preserves headings and sections |
| Long PDFs with ordinary prose | Recursive splitting with page metadata | Balances context and precision |
| Tables and spreadsheets | Table-aware parsing and chunking | Preserves column and row meaning |
| Source code and API references | Language-aware or structure-aware splitting | Keeps functions and definitions together |
| Long legal or policy documents | Structure-aware parent-child chunks | Preserves clauses and broader context |
| Complex prose with weak boundaries | Experiment with semantic chunking | Can find topic transitions |
| Very large manuals | Parent-child or hierarchical retrieval | Small search units with broader context |

## Maps to guides in this folder

| Matrix row | See |
|------------|-----|
| Recursive splitting | [Chunking simpler strategy](./chunking-simpler-strategy.md) |
| Structure-aware splitting | [Chunking recursive structure-aware](./chunking-recursive-structure-aware.md) |
| Table-aware | [Structure-aware — tables section](./chunking-recursive-structure-aware.md#when-this-approach-is-insufficient) |
| Semantic chunking | [Chunking semantic](./chunking-semantic.md) |
| Parent-child / hierarchical | [Chunking hierarchical parent-child](./chunking-hierarchical-parent-child.md) |
| Maturity by system size | [Chunking architecturing decision-based](./chunking-architecturing-decision-based.md) · [Retrieval architecturing decisions](../retrieval-architecturing-decision-based.md) |

Start with the **recommended baseline**, measure, then add complexity only when evidence supports it ([guard-rails decision rules](../../guard-rails/guard-rails-decision-architecturing-assistance.md#the-rules-i-would-never-compromise-on)).

## See also

- [Chunking overview](./README.md)
- [Ingestion procedures — Chunking](../ingestion/ingestion-procedures.md)
