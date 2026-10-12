# Context algorithm

Ordered **context assembly** steps from retrieved candidates to the final prompt—after [search](../retrieval/search/) returns candidates and before the LLM runs ([context assembly flow](./context-assembly-flow.md)).

```
Retrieved Candidates
       |
       v
1. Validate access and provenance
       |
       v
2. Remove invalid / stale / duplicate chunks
       |
       v
3. Merge or organize related chunks
       |
       v
4. Score and select evidence
       |
       v
5. Apply diversity and coverage rules
       |
       v
6. Allocate the token budget
       |
       v
7. Order evidence and attach source IDs
       |
       v
8. Render final context
       |
       v
Prompt Template -> LLM
```

## Step notes

| Step | Pointers |
|------|----------|
| **1. Validate access and provenance** | Trusted identity + ACL; chunk IDs match index metadata ([metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md)) |
| **2. Remove invalid / stale / duplicate** | Tombstones, version flags, hash dedupe ([chunking metrics — duplicate retrieval](../retrieval/chunking/chunking-metrics-observability.md)) |
| **3. Merge or organize related** | Parent-child chunks, same document sections ([hierarchical chunking](../retrieval/chunking/chunking-hierarchical-parent-child.md)) |
| **4. Score and select evidence** | Rerank scores, similarity thresholds ([reranking](../retrieval/search/retrieval-strategy-reranking.md), [similarity strategy](../retrieval/search/retrieval-strategy-similarity.md)) |
| **5. Diversity and coverage** | Avoid redundant overlap; span multiple sources when the question requires it |
| **6. Token budget** | Truncate vs summarize; reserve space for history and instructions ([context info for output](./context-info-for-output.md)) |
| **7. Order + source IDs** | Stable citation keys (doc ID, page, URL) for **Answer + Citations** |
| **8. Render final context** | Prompt template slots; structured blocks for SQL/API results |

Steps **1–2** are safety and correctness; skipping them cannot be fixed by prompt instructions alone.

## See also

- [Compacting](../retrieval/compacting/) — overlap with dedupe and budget before or inside this pipeline
- [Contexting overview](./README.md)
