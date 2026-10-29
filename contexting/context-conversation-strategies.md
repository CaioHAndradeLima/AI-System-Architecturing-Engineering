# Context conversation strategies

How much **conversation history** to include during [context assembly](./context-assembly-flow.md)—trade-offs for token budget and follow-up understanding ([context info — conversation history](./context-info-for-output.md)).

| Strategy | Advantages | Risks |
|----------|------------|-------|
| **Send the full conversation** | Simple; preserves detail | Token growth, irrelevant messages |
| **Send only the last N messages** | Cheap and predictable | May lose important earlier context |
| **Maintain a summary plus recent messages** | Better long-conversation scalability | Summaries can omit or distort details |

## Choosing a strategy

| Stage | Starting point |
|-------|----------------|
| **MVP / short threads** | Last **N** messages (fixed N from model window and retrieval budget) |
| **Long support or copilot sessions** | **Summary + recent**; refresh summary on a schedule or when N exceeds threshold |
| **Debug / low volume** | Full history only if total tokens stay under a hard cap |

Pair with **contextual query resolution** so retrieval uses a standalone query even when the prompt keeps only recent turns ([context scoring math — query resolution](./context-scoring-math.md), [cleaning user query](../retrieval/embedding/queries/embedding-cleaning-user-query.md)).

Message compaction and DB+vector chat patterns: [compacting](../retrieval/compacting/) · [user context compact flow](../retrieval/embedding/queries/embedding-user-context-compact-flow.md).

## Code lab

- [contexting-strategies — `evaluate-scenarios`](https://github.com/CaioHAndradeLima/contexting-strategies) — `full_history`, `last_n`, and `summary_plus_recent` with split history/evidence budgets (`threads.json`); `evaluate-full` → `query_resolution` for resolved vs ambiguous follow-ups.

## See also
- [Context algorithm — token budget](./context-algorithm.md)
- [Contexting overview](./README.md)
