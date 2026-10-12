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

### [prompt-categories.md](./prompt-categories.md)

`#taxonomy` · `#system` · `#rag`

System, user, retrieved context, and output format—responsibility and change frequency.

→ [See more in prompt-categories.md](./prompt-categories.md)

### [prompt-standard-format.md](./prompt-standard-format.md)

`#system-prompt` · `#rag` · `#abstain`

Seven-part template: role, objective, evidence, decisions, security, output, failure.

→ [See more in prompt-standard-format.md](./prompt-standard-format.md)

### [prompt-few-shot-providing-samples.md](./prompt-few-shot-providing-samples.md)

`#few-shot` · `#examples`

When to add input/output samples; domain nuance and repeated failure modes.

→ [See more in prompt-few-shot-providing-samples.md](./prompt-few-shot-providing-samples.md)

### [prompt-injection.md](./prompt-injection.md)

`#security` · `#injection` · `#rag`

Untrusted input flow, delimiters, tool validation, output checks, adversarial testing.

→ [See more in prompt-injection.md](./prompt-injection.md)

### [prompt-versioning.md](./prompt-versioning.md)

`#versioning` · `#canary` · `#eval`

Golden dataset, regression gate, canary, promotion; per-version audit fields.

→ [See more in prompt-versioning.md](./prompt-versioning.md)

### [prompt-relevant-variables-influences.md](./prompt-relevant-variables-influences.md)

`#temperature` · `#model` · `#structured-output`

Temperature, max tokens, top-p, stop sequences, schema mode, model choice.

→ [See more in prompt-relevant-variables-influences.md](./prompt-relevant-variables-influences.md)

### [prompt-architecturing-decision-based.md](./prompt-architecturing-decision-based.md)

`#decision-guide` · `#startup` · `#enterprise` · `#multi-agent`

Prompt design, few-shot, grounding, schemas, injection, versioning, eval, and ops by maturity.

→ [See more in prompt-architecturing-decision-based.md](./prompt-architecturing-decision-based.md)

## Related

- [Context algorithm — render final context](../contexting/context-algorithm.md)
- [Context architecturing decision-based](../contexting/context-architecturing-decision-based.md)
- [LangGraph — generate / validate nodes](../contexting/context-assembly-langchain-langgraph.md)
- [Guard-rails strategy](../guard-rails/guard-rails-strategy.md)

## See also

- [Repository overview](../README.md)
