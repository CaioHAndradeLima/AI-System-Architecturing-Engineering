# Chunking recursive structure-aware

Split on **document structure first** (headings, sections), then fall back to paragraphs and sentences only when a section exceeds the size limit. Contrast with pure fixed windows in [chunking simpler strategy](./chunking-simpler-strategy.md).

## Flow

```
  Whole document
       |
       v
  Split at headings
       |
       +---- Section 1
       |        |
       |        v
       |    Fits limit? ---- yes ---> Keep section
       |        |
       |        no
       |        v
       |    Split paragraphs
       |
       +---- Section 2
                |
                v
           Fits limit? ---- yes ---> Keep section
                |
                no
                v
           Split sentences / smaller units
```

**Fits limit?** — chunk stays under your token or character budget for embedding and retrieval context.

## Why this is usually a better baseline

- **Context preservation** — Less likely to separate a heading from its explanation.
- **Structural integrity** — Respects natural document boundaries where possible.
- **Efficiency** — Relatively inexpensive compared with semantic splitting.
- **Versatility** — Works well for many PDFs, Markdown files, knowledge-base articles, and internal documentation.

## When this approach is insufficient

Tables, code examples, legal clauses, and complex nested sections may need **specialized handling**. A common failure: splitting a table on arbitrary row boundaries so **column headers are no longer attached** to the data rows.

### Example: pricing table split gone wrong

Source table:

```
| Plan  | Monthly cost | User limit |
|-------|--------------|------------|
| Basic | $10          | 5          |
| Pro   | $50          | 50         |
```

| Bad chunk (row only) | What the model sees | Problem |
|----------------------|---------------------|---------|
| `Pro \| $50 \| 50` | Three numbers with no column names | Cannot reliably answer “What is Pro’s user limit?” |

| Better chunk (header + row as text) | What the model sees |
|-------------------------------------|---------------------|
| Structured line | `Plan: Pro, Monthly cost: $50, User limit: 50` |

**Fixes:** keep headers on every row chunk, or **normalize tables to structured text** (Markdown, JSON, or one sentence per row) **before** recursive splitting.

```
TABLE: Plan pricing
  Row: Plan=Basic,  Monthly cost=$10,  User limit=5
  Row: Plan=Pro,    Monthly cost=$50,  User limit=50
        |
        v
  Each row (with labels) -> chunk or embed as a unit
```

## Practical checklist

- [ ] Prefer heading-aware splitters (Markdown `#`, HTML `h1–h6`, PDF outline when available)
- [ ] Detect table blocks in parse output and route to a **table handler**, not the default text splitter
- [ ] Store **section title** in chunk metadata for citations
- [ ] Re-evaluate Recall@K after changing split hierarchy ([ingestion observability](../ingestion/ingestion-observability.md))

## See also

- [Chunking semantic](./chunking-semantic.md)
- [Chunking simpler strategy](./chunking-simpler-strategy.md)
- [Retrieval architecturing decisions — Chunking](../retrieval-architecturing-decision-based.md)
- [Chunking overview](./README.md)
