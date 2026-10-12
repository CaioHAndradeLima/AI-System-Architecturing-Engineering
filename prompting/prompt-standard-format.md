# Prompt standard format

A **system-prompt skeleton** for production assistants—especially RAG. Keep sections explicit and versioned; pair with [prompt categories](./prompt-categories.md) (system vs user vs context vs output).

```
1. ROLE
   Who is the assistant?

2. OBJECTIVE
   What should it accomplish?

3. EVIDENCE RULES
   Which sources can support factual claims?

4. DECISION RULES
   What should it do when evidence is missing or conflicting?

5. SECURITY RULES
   What must it never disclose or execute?

6. OUTPUT CONTRACT
   What response format is expected?

7. FAILURE BEHAVIOR
   When should it abstain, ask a question, or escalate?
```

## Section → implementation

| Section | Pointers |
|---------|----------|
| **ROLE / OBJECTIVE** | Product tone and scope; avoid contradicting retrieval corpora |
| **EVIDENCE RULES** | Only provided context + named tools; cite [source metadata](../contexting/context-info-for-output.md) |
| **DECISION RULES** | Missing vs conflicting evidence ([similarity abstain](../retrieval/search/retrieval-strategy-similarity.md), [multi-hop synthesis](../contexting/context-multi-hop-question.md)) |
| **SECURITY RULES** | [Reliable architecture](../contexting/context-reliable-architecture.md) · [Guard-rails](../guard-rails/) |
| **OUTPUT CONTRACT** | JSON/markdown/citations; validate parse in app code |
| **FAILURE BEHAVIOR** | Insufficient-evidence response, clarification, human escalation ([architecturing decision — failure row](../contexting/context-architecturing-decision-based.md)) |

**Retrieved evidence** belongs in context slots—not inside ROLE or SECURITY as copy-paste from documents ([untrusted content boundaries](../contexting/context-reliable-architecture.md)).

## See also

- [Evaluate context assembling](../contexting/context-evaluate-assembling.md) — groundedness, no-answer handling
- [Prompting overview](./README.md)
