# Prompt few-shot providing samples

**Few-shot prompting** means including a small number of input/output examples to demonstrate the behavior you want.

Use few-shot when:

- The model repeatedly mishandles a specific class of question.
- A domain has nuanced distinctions, such as confirmed versus suspected causes.
- An output style or classification rule is difficult to express with concise instructions alone.

## Practice notes

| Topic | Guidance |
|-------|----------|
| **Where examples live** | System or developer message—not mixed with untrusted retrieved text ([prompt categories](./prompt-categories.md), [reliable architecture](../contexting/context-reliable-architecture.md)) |
| **Token cost** | Each example consumes budget; prefer 2–5 tight pairs over long dialogs ([assembling trade-offs](../contexting/context-assembling-trade-offs.md)) |
| **vs instructions** | Start with [standard format](./prompt-standard-format.md) sections; add shots only for gaps eval shows |
| **Eval** | Regression tests per example class; watch for overfitting to phrasing |

Few-shot complements—not replaces—**EVIDENCE RULES** and **OUTPUT CONTRACT** in the standard format.

## See also

- [Prompting overview](./README.md)
