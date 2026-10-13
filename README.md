# AI System Architecturing & Engineering

Markdown guides on multi-agent systems, guard-rails, retrieval, contexting, prompting, LLM inference, output validation, observability, deployment, and related production patterns.

Each section **README** lists its guides with tags and a short (2–3 line) summary; open the linked note for diagrams, tables, and checklists.

## Contents

| Section | Description |
|---------|-------------|
| [agents](./agents/README.md) | Sequential, parallel, and hierarchical multi-agent patterns plus a reference Python package layout. Use when splitting work across specialists, supervisors, and tool-backed workers. |
| [guard-rails](./guard-rails/README.md) | Defense-in-depth validation: AI safety, security, tenant isolation, and reliability at input, retrieval, tool, and output boundaries. Includes cloud architecture maps and test scenarios. |
| [retrieval](./retrieval/README.md) | Full RAG index and query path: [ingestion](./retrieval/ingestion/README.md), [chunking](./retrieval/chunking/README.md), [embedding](./retrieval/embedding/README.md), [compacting](./retrieval/compacting/README.md), [storaging](./retrieval/storaging/README.md), [search](./retrieval/search/README.md). Decision guides by scale and flow diagrams end to end. |
| [contexting](./contexting/README.md) | Assemble retrieved evidence into prompts under token budgets, with citations, conversation history, and question-type patterns. Covers scoring, LangGraph assembly nodes, and eval metrics. |
| [prompting](./prompting/README.md) | System prompts, templates, few-shot, injection defense, versioning, and implementation checklists. Includes [decision guide](./prompting/prompt-architecturing-decision-based.md) by maturity. |
| [llm](./llm/README.md) | Chat/completion model selection, hosting, inference, streaming, routing, fallbacks, and cloud services. Includes [decision guide](./llm/llm-decision-based.md) and generation checklist. |
| [output](./output/README.md) | Post-LLM validation: schemas, citations, tool execution, failure repair, LangGraph routing, metrics, and adversarial test cases. |
| [observability-evaluation](./observability-evaluation/README.md) | Golden datasets, retrieval and answer metrics, tracing, incident investigation, canary/regression, and LLM-as-judge vs human eval. |
| [deployment](./deployment/README.md) | Production topology, CI evaluation pipeline, quality gates, cloud tooling, and continuous improvement from live feedback. [Decision guide](./deployment/deployment-decision-based.md) by scale. |

## Adding a new note

1. Add a top-level directory when you introduce a new topic area, or place files under an existing one.
2. Use **kebab-case** filenames: `how-chunking-affects-recall.md`.
3. Optional outline: [`_templates/topic.md`](./_templates/topic.md).
4. Link related notes from a **See also** section and update the section **README** (summary + tags) when you add a guide.

## Repository

https://github.com/CaioHAndradeLima/AI-System-Architecturing-Engineering
