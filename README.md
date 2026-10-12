# AI Engineering Notes

A growing collection of markdown guides on building and operating AI systems (LLMs, agents, RAG, evaluation, deployment, and related topics).

## Layout

| Directory | What goes here |
|-----------|----------------|
| [fundamentals](./fundamentals/) | Core concepts: tokens, embeddings, transformers, training vs inference |
| [llms](./llms/) | Model APIs, context windows, streaming, tool calling at the model layer |
| [prompting](./prompting/) | System prompts, few-shot, structured output, prompt patterns |
| [rag](./rag/) | Retrieval, chunking, vector stores, hybrid search, reranking |
| [agents](./agents/) | Planning, tools, memory, multi-step workflows, orchestration ([multi-agent patterns](./agents/multi-agent-architecture/)) |
| [fine-tuning](./fine-tuning/) | SFT, LoRA/QLoRA, preference tuning, when *not* to fine-tune |
| [evaluation](./evaluation/) | Benchmarks, LLM-as-judge, regression suites, offline vs online eval |
| [deployment](./deployment/) | Serving, batching, cost/latency, gateways, local vs cloud |
| [observability](./observability/) | Tracing, logging prompts/completions, metrics, debugging failures |
| [guard-rails](./guard-rails/) | Input/output validation, ACL, tool checks, policy layers |
| [safety](./safety/) | Injection, PII, alignment, human-in-the-loop (broader safety topics) |
| [mcp-and-integrations](./mcp-and-integrations/) | MCP servers, external tools, API design for agents |
| [patterns](./patterns/) | End-to-end recipes (e.g. “support bot”, “code assistant”) |

## Adding a new note

1. Pick the best-matching directory (or propose a new top-level folder if the topic doesn’t fit).
2. Use **kebab-case** filenames: `how-chunking-affects-recall.md`.
3. Start from [`_templates/topic.md`](./_templates/topic.md) for a consistent outline.
4. Link related notes from a short **See also** section at the bottom.
5. Update this README’s table if you add a new top-level directory.

## Repository

https://github.com/CaioHAndradeLima/AI-System-Architecturing-Engineering
