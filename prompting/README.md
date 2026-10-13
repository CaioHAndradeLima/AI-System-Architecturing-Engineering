# Prompting

**Instructions and templates** that tell the model how to behave: system prompts, roles, output formats, grounding rules, few-shot examples, and tool-use wording—distinct from **what evidence** is included ([contexting](../contexting/)).

Typical RAG order: [retrieval](../retrieval/) → [context assembly](../contexting/context-assembly-flow.md) → **prompting** (policy + template) → [LLM flow](../llm/llm-flow.md) → validation ([guard-rails](../guard-rails/)).

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

### [prompt-implementation-flow.md](./prompt-implementation-flow.md)

`#checklist` · `#implementation` · `#eval`

Prompt engineering implementation checklist—from separation of trusted instructions through rollout, regression gate, and production monitoring.

→ [See more in prompt-implementation-flow.md](./prompt-implementation-flow.md)

### [prompt-categories.md](./prompt-categories.md)

`#taxonomy` · `#system` · `#rag`

Four components that make up a typical LLM application prompt—what each owns and how often it changes per request.

→ [See more in prompt-categories.md](./prompt-categories.md)

### [prompt-standard-format.md](./prompt-standard-format.md)

`#system-prompt` · `#rag` · `#abstain`

A system-prompt skeleton for production assistants—especially RAG.

Keep sections explicit and versioned; pair with prompt categories (system vs user vs context vs output).

→ [See more in prompt-standard-format.md](./prompt-standard-format.md)

### [prompt-few-shot-providing-samples.md](./prompt-few-shot-providing-samples.md)

`#few-shot` · `#examples`

Few-shot prompting means including a small number of input/output examples to demonstrate the behavior you want.

→ [See more in prompt-few-shot-providing-samples.md](./prompt-few-shot-providing-samples.md)

### [prompt-injection.md](./prompt-injection.md)

`#security` · `#injection` · `#rag`

Defense-in-depth for untrusted user input and retrieved documents—from auth through delimiters, instructions, tools, and output checks.

→ [See more in prompt-injection.md](./prompt-injection.md)

### [prompt-versioning.md](./prompt-versioning.md)

`#versioning` · `#canary` · `#eval`

Ship prompt changes like code: golden-set eval, baseline comparison, canary, then full promotion.

Unified prompt/model/retrieval gate: regression and canary releases.

→ [See more in prompt-versioning.md](./prompt-versioning.md)

### [prompt-relevant-variables-influences.md](./prompt-relevant-variables-influences.md)

`#temperature` · `#model` · `#structured-output`

Generation parameters and model choice affect quality, cost, and reliability—version and eval them with prompts (prompt versioning).

→ [See more in prompt-relevant-variables-influences.md](./prompt-relevant-variables-influences.md)

### [prompt-architecturing-decision-based.md](./prompt-architecturing-decision-based.md)

`#decision-guide` · `#startup` · `#enterprise` · `#multi-agent`

How prompting practices evolve from startup/prototype through growing production to enterprise / multi-agent.

→ [See more in prompt-architecturing-decision-based.md](./prompt-architecturing-decision-based.md)

## Related

- [Context algorithm — render final context](../contexting/context-algorithm.md)
- [Context architecturing decision-based](../contexting/context-architecturing-decision-based.md)
- [LangGraph — generate / validate nodes](../contexting/context-assembly-langchain-langgraph.md)
- [Guard-rails strategy](../guard-rails/guard-rails-strategy.md)

## See also

- [Repository overview](../README.md)
