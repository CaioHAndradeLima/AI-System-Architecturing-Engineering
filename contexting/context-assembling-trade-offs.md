# Context assembling trade-offs

Common **context assembly mistakes**, why they hurt, and better approaches—companion to [evaluate assembling](./context-evaluate-assembling.md) and [reliable architecture](./context-reliable-architecture.md).

| Mistake | Why it hurts | Better approach |
|---------|--------------|-----------------|
| **Include every retrieved chunk** | Wastes tokens and adds noise | Rank, deduplicate, and budget |
| **Always send the last 20 messages** | History can overwhelm evidence | Use relevant history, recent messages, and summaries |
| **Truncate context arbitrarily** | Can remove exceptions or critical evidence | Select and trim at meaningful boundaries |
| **Assume the highest similarity score is sufficient** | Similarity is not proof of correctness | Evaluate evidence quality and sufficiency |
| **Summarize everything automatically** | Summaries can lose details and citations | Summarize selectively and preserve provenance |
| **Trust source text as instructions** | Exposes the model to prompt injection | Treat retrieved content as untrusted data |
| **Give every agent all context** | Increases cost and data exposure | Provide task-specific context |
| **Assume a larger context window solves everything** | More tokens can mean more noise and higher cost | Benchmark context quality and length |

## Guide links by row

| Better approach | Docs |
|-----------------|------|
| Rank, dedupe, budget | [Context algorithm](./context-algorithm.md) · [Scoring math](./context-scoring-math.md) |
| History strategy | [Conversation strategies](./context-conversation-strategies.md) |
| Meaningful boundaries | [Chunking](../retrieval/chunking/) · parent-child fetch in search |
| Quality / sufficiency | [Similarity / abstain](../retrieval/search/retrieval-strategy-similarity.md) · [Evaluate assembling](./context-evaluate-assembling.md) |
| Selective summarize + provenance | [Context info — source metadata](./context-info-for-output.md) |
| Untrusted data | [Reliable architecture](./context-reliable-architecture.md) |
| Task-specific context | [Multi-agent sample](../retrieval/search/retrieval-aws-multi-agent-sample.md) · [LangGraph nodes](./context-assembly-langchain-langgraph.md) |
| Benchmark quality vs length | [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) |

## See also

- [Contexting overview](./README.md)
