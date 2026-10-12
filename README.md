# AI System Architecturing & Engineering

Markdown guides on multi-agent systems, guard-rails, retrieval, contexting, prompting, LLM inference, and related production patterns.

## Contents

| Directory | Topics |
|-----------|--------|
| [agents](./agents/) | Multi-agent patterns (sequential, parallel, hierarchical) and Python layout |
| [guard-rails](./guard-rails/) | Strategy, tenant isolation, AWS controls, test use cases |
| [retrieval](./retrieval/) | [ingestion](./retrieval/ingestion/), [chunking](./retrieval/chunking/), [embedding](./retrieval/embedding/), [compacting](./retrieval/compacting/), [storaging](./retrieval/storaging/), [search](./retrieval/search/) |
| [contexting](./contexting/) | Context assembly, grounding, citations, and token budget after retrieval |
| [prompting](./prompting/) | System prompts, templates, grounding ([decision guide](./prompting/prompt-architecturing-decision-based.md)) |
| [llm](./llm/) | Chat/completion models, hosting, inference ([decision guide](./llm/llm-decision-based.md)) |

## Adding a new note

1. Add a top-level directory when you introduce a new topic area, or place files under an existing one.
2. Use **kebab-case** filenames: `how-chunking-affects-recall.md`.
3. Optional outline: [`_templates/topic.md`](./_templates/topic.md).
4. Link related notes from a **See also** section and update this README when you add a new top-level folder.

## Repository

https://github.com/CaioHAndradeLima/AI-System-Architecturing-Engineering
