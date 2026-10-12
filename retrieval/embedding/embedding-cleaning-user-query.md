# Embedding cleaning user query

**Query preprocessing** techniques before [query embedding](./embedding-user-query-flow.md)—normalize, detect language, rewrite, expand, or decompose the user question.

| Technique | Example | When it helps |
|-----------|---------|-------------|
| **Basic normalization** | Remove accidental whitespace | Almost always safe |
| **Language detection** | Detect Portuguese vs. English | Multilingual applications |
| **Query rewriting** | "Time off" → "vacation leave policy" | Ambiguous or conversational questions |
| **Query expansion** | Add related search terms | Recall-sensitive retrieval |
| **Multi-query retrieval** | Search using several reformulations | Complex questions with multiple interpretations |
| **Query decomposition** | Split a multi-part question into subquestions | Questions requiring evidence from several documents |

## Usage notes

- **Normalization** and **language detection** are cheap defaults; route to the right index or embedding settings per language ([embedding decision-based — language support](./embedding-decision-based.md)).
- **Rewriting / expansion / multi-query** add latency and cost—measure Recall@K and precision on a golden set ([embedding metrics](./embedding-metrics.md)).
- **Decomposition** pairs well with [multi-agent retrieval](../../agents/multi-agent-architecture/parallel-agents-architecture.md) or merged top-K from sub-queries; dedupe chunks in context assembly.
- LLM-based rewrite must not bypass **authorization**—preprocessing does not replace tenant filters on search.

## See also

- [Embedding user query flow](./embedding-user-query-flow.md)
- [Embedding bad practices — encoding instructions](./embedding-bad-practices.md)
- [Embedding overview](./README.md)
