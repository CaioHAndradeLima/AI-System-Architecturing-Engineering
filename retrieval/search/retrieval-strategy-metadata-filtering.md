# Retrieval strategy — metadata filtering

**Metadata filters** restrict search to vectors the caller is allowed to see—before or during vector/keyword retrieval, not after the LLM assembles context. Example query: *“What is our vacation policy?”*

```
Query: "What is our vacation policy?"
                |
                v
      Trusted tenant identity
                |
                v
      Apply access restrictions
                |
                v
      Search eligible vectors
                |
                v
      Return relevant authorized chunks
```

## What to filter on

| Metadata | Role |
|----------|------|
| **Tenant ID** | Scope results to the customer or org ([tenant-scoped retrieval](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)) |
| **Document / ACL** | User or role may read only a subset of indexed documents |
| **Source, type, status** | Exclude drafts, deleted docs, or wrong corpora |
| **Time / version** | Prefer current policy versions when multiple exist |

**Trusted tenant identity** must come from auth/session/service identity—not from unvalidated client fields in the query body.

## Store and query patterns

- **Pre-filter:** index supports filter predicates before ANN search (common in managed vector DBs).
- **Post-filter:** retrieve top-K then drop unauthorized hits—simple but can return **fewer than K** or empty sets if many neighbors are out of scope; may need higher internal K.
- **Hybrid:** relational ACL join + vector search ([compact architecture flow](../compacting/compact-architecture-flow.md)).

Validate filters in application code; test with [guard-rails test use cases](../../guard-rails/guard-rails-test-use-cases.md) and [wrong architecture: shared retrieval](../../guard-rails/wrong-architecture-shared-retrieval.md).

Pair with [retrieval strategy top-K](./retrieval-strategy-top-k.md) and [similarity thresholds](./retrieval-strategy-similarity.md)—filters change effective recall; measure **filtered-search performance** ([storage observability](../storaging/storage-observability.md)).

## See also

- [Retrieval flow](../retrieval-flow.md)
- [Guard-rails data isolation](../../guard-rails/guardrails-data-isolation.md)
- [Storage and indexing decision-based — Query filtering](../storaging/storage-indexing-decision-based.md)
- [Search overview](./README.md)
