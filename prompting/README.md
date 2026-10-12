# Prompting

**Instructions and templates** that tell the model how to behave: system prompts, roles, output formats, grounding rules, few-shot examples, and tool-use wording—distinct from **what evidence** is included ([contexting](../contexting/)).

Typical RAG order: [retrieval](../retrieval/) → [context assembly](../contexting/context-assembly-flow.md) → **prompting** (policy + template) → LLM → validation ([guard-rails](../guard-rails/)).

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **System vs user messages** | Trusted instructions separated from untrusted evidence |
| **RAG prompt templates** | Slots for question, evidence, citation format |
| **Grounding instructions** | Answer only from context; abstain when insufficient |
| **Output structure** | JSON, markdown, citations, tone, locale |
| **Few-shot & examples** | When they help vs add token noise |
| **Multi-agent prompts** | Per-agent role prompts and handoff text |
| **Prompt injection defense** | Boundaries with retrieved content ([reliable architecture](../contexting/context-reliable-architecture.md)) |
| **Evaluation & iteration** | Prompt regression, A/B, versioned prompts |

---

## Guides

_Guides will be listed here as you add markdown files in this folder (same pattern as [contexting](../contexting/README.md))._

## Related

- [Context algorithm — render final context](../contexting/context-algorithm.md)
- [Context architecturing decision-based](../contexting/context-architecturing-decision-based.md)
- [LangGraph — generate / validate nodes](../contexting/context-assembly-langchain-langgraph.md)
- [Guard-rails strategy](../guard-rails/guard-rails-strategy.md)

## See also

- [Repository overview](../README.md)
