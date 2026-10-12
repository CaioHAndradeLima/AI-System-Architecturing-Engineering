# Retrieval architecture decision

Pick **how retrieval is wired into agents** by requirement—not by defaulting to an LLM for every search.

| Requirement | Recommended design |
|-------------|-------------------|
| Search one knowledge base and return the top relevant chunks | Retrieval service/tool |
| Search multiple indexes with a fixed strategy | Retrieval service with multiple search backends |
| Choose dynamically between vector search, keyword search, or hybrid search | Usually a tool with explicit routing logic; an agent only if reasoning adds value |
| Decide which knowledge source to search, inspect evidence, and retry | Retrieval agent may be justified |
| Coordinate knowledge retrieval, SQL analytics, and engineering investigation | Multi-agent architecture may be justified |

## Guide links

| Recommended design | Doc |
|--------------------|-----|
| Retrieval service/tool | [Supervisor with retrieval as service](./retrieval-architecture-supervisor-as-service.md) |
| Multiple backends (fixed strategy) | [Combined retrieval strategies](./retrieval-strategies-combined.md) · [Hybrid search](./retrieval-strategy-hybrid-search-vector-plus-keyword.md) |
| Explicit routing (vector / keyword / hybrid) | [Retrieval decision-based by scale](./retrieval-decision-based.md) · service doc above |
| Retrieval agent | [Supervisor with retrieval agent](./retrieval-architecture-supervisor-as-agent.md) |
| Multi-agent coordination | [Multi-agent retrieval architecture](./retrieval-architecture-multi-agent.md) |

Start with the **simplest design that meets the requirement**; add agent autonomy only when eval shows routing or retry logic cannot be expressed safely in code ([implementation flow](./retrieval-implementation-flow.md)).

## See also

- [Agents overview](../../agents/README.md)
- [Search overview](./README.md)
