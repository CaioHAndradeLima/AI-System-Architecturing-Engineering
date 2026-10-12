# Chunking semantic

Split text at **topic boundaries** instead of fixed token windows: embed sentence-level (or passage-level) units, compare neighbors, cut where meaning shifts, then clamp to min/max chunk sizes.

## Flow

```
  Sentences
      |
      v
  Embed candidate passages
      |
      v
  Compare neighboring meanings
      |
      v
  Detect topic changes
      |
      v
  Create semantic boundaries
      |
      v
  Enforce minimum / maximum chunk sizes
```

Typical implementation: sliding groups of sentences (or small windows), cosine similarity between consecutive embeddings drops below a **threshold** → start a new chunk. Min/max size prevents tiny fragments or oversized blobs.

## Advantages and trade-offs

| Advantage | Trade-off |
|-----------|-----------|
| Can preserve coherent topics | More processing and implementation complexity |
| May improve retrieval on some datasets | Does not automatically outperform simpler splitting |
| Can help with irregular prose | Similarity thresholds require tuning |
| Less dependent on fixed section sizes | Usually requires additional embeddings or similarity calculations |

Benchmark against [recursive structure-aware](./chunking-recursive-structure-aware.md) or [fixed overlap](./chunking-simpler-strategy.md) on **your** golden set ([ingestion observability — Recall@K](../ingestion/ingestion-observability.md)) before committing in production.

## When to consider it

- Long, uneven prose without reliable headings (transcripts, support threads)
- Structure-aware splitting still produces mixed-topic chunks
- You can afford **extra embedding calls at index time** and ongoing threshold tuning

When documents are well-structured (Markdown, KB articles), structure-aware chunking is often the better **baseline** first.

## Practical checklist

- [ ] Version **embedding model** used for boundary detection (may differ from index embeddings)
- [ ] Log chosen **threshold**, min/max sizes, and chunk count per document for replay
- [ ] Fall back to paragraph or character split if semantic pipeline fails on a document
- [ ] Re-run eval when threshold or embedding model changes

## See also

- [Chunking recursive structure-aware](./chunking-recursive-structure-aware.md)
- [Retrieval architecturing decisions — Chunking](../retrieval-architecturing-decision-based.md)
- [Chunking overview](./README.md)
