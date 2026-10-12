# Prompt categories

Four **components** that make up a typical LLM application prompt—what each owns and how often it changes per request.

| Component | Responsibility | Usually changes per request? |
|-----------|----------------|------------------------------|
| **System prompt** | Defines the application's intended behavior | Infrequently |
| **User prompt** | Expresses the user's current request | Yes |
| **Retrieved context** | Supplies external evidence | Yes |
| **Output schema or format instructions** | Specifies the expected response structure | Depends on the task |

## Where each lives in the stack

| Component | Docs |
|-----------|------|
| **System prompt** | [Reliable architecture — separate instructions from evidence](../contexting/context-reliable-architecture.md) · [Guard-rails strategy](../guard-rails/guard-rails-strategy.md) |
| **User prompt** | [Query cleaning / rewrite](../retrieval/embedding/queries/embedding-cleaning-user-query.md) |
| **Retrieved context** | [Contexting](../contexting/) · [Context info for output](../contexting/context-info-for-output.md) |
| **Output schema / format** | Version with prompts; validate outside the model when possible ([analytical question](../contexting/context-analytical-question.md)) |

Assemble **retrieved context** in contexting; bind **system**, **user**, and **format** slots in prompting templates so untrusted evidence never overwrites trusted instructions.

## See also

- [Prompt standard format](./prompt-standard-format.md) — structured system prompt sections
- [Context assembly flow](../contexting/context-assembly-flow.md)
- [Prompting overview](./README.md)
