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

## Weak vs better (by design choice)

| Design choice | Weak approach | Better approach | Maps to |
|---------------|---------------|-----------------|---------|
| **Role** | "You are a helpful AI." | Define the domain and responsibility | §1 ROLE · §2 OBJECTIVE |
| **Evidence** | "Use the documents." | Require factual claims to be supported by supplied evidence | §3 EVIDENCE RULES |
| **Missing information** | Leave behavior unspecified | Explicitly require uncertainty or abstention | §4 DECISION RULES · §7 FAILURE BEHAVIOR |
| **Conflicting documents** | Let the model decide silently | Define source precedence or require disclosure of the conflict | §4 DECISION RULES |
| **Output** | "Answer clearly." | Define sections or a schema when downstream code needs consistency | §6 OUTPUT CONTRACT |
| **Security** | "Never do anything bad." | Enforce permissions and tool restrictions outside the model; treat document content as untrusted | §5 SECURITY RULES · [prompt injection](./prompt-injection.md) |

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
