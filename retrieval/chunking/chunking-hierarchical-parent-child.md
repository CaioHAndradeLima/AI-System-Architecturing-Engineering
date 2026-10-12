# Chunking hierarchical parent-child

**Two-level index**: small **child** chunks for precise vector search; larger **parent** sections for context passed to the LLM after a relevant child hit.

## Document structure (example)

```
  API Manual
      |
      +--- Parent: Authentication
      |        |
      |        +--- Child 1: Access-token lifetime
      |        +--- Child 2: Refresh-token lifetime
      |        +--- Child 3: Expiration behavior
      |
      +--- Parent: Billing
               |
               +--- Child 1: Subscription plans
               +--- Child 2: Payment retries
```

Parents map to logical sections (headings); children are narrow passages within that section—often aligned with [recursive structure-aware](./chunking-recursive-structure-aware.md) splits at subsection granularity.

## Retrieval flow

```
  RETRIEVAL
      |
      v
  Search small child chunks
      |
      v
  Find relevant child
      |
      v
  Retrieve its authorized parent section
      |
      v
  Give the useful context to the LLM
```

1. **Embed and search children** — better precision for specific facts (e.g. “refresh token lifetime”).
2. **Resolve parent ID** from the winning child’s metadata (`parent_id`, section path).
3. **Load parent text** (full section) subject to **authorization**—same tenant and document ACL as the child ([guard-rails](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)).
4. **Prompt assembly** — include parent context (and optionally cite child offset); cap total tokens.

## Design notes

| Aspect | Guidance |
|--------|----------|
| **Child size** | Small enough for sharp retrieval; not so tiny that embeddings are noisy |
| **Parent size** | Fits in context window with room for question + answer; may truncate with summary if huge |
| **Storage** | Child vectors in index; parent text in object store, DB, or same index with different `chunk_type` |
| **Metadata** | `document_id`, `parent_id`, `section_title`, `child_index`, `tenant_id` on every child |
| **Duplicates** | Parent text is not re-embedded for every child unless you also search parents |

## Compare to other strategies

| Strategy | Search unit | Context passed to LLM |
|----------|-------------|-------------------------|
| [Fixed overlap](./chunking-simpler-strategy.md) | Same chunk | Same chunk |
| [Structure-aware](./chunking-recursive-structure-aware.md) | Section or sub-section | Usually same unit |
| **Parent-child (this note)** | Child | Parent (broader section) |

## Practical checklist

- [ ] Verify ACL on **parent fetch**, not only on child search hits
- [ ] Handle child hit whose parent was updated (version or `content_hash` on parent)
- [ ] Eval: child Recall@K **and** answer quality with parent context ([Recall@K](../ingestion/ingestion-observability.md))

## See also

- [Chunking semantic](./chunking-semantic.md)
- [Ingestion procedures — Chunking / Retrieval rows](../ingestion/ingestion-procedures.md)
- [Chunking overview](./README.md)
