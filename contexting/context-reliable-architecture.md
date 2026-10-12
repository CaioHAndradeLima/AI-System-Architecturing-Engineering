# Context reliable architecture

Rules for **safe, trustworthy context assembly**—what may enter the prompt and how evidence is handled before and after the LLM.

1. **Enforce document permissions before including evidence.**
2. **Separate trusted application instructions from retrieved content.**
3. **Treat retrieved text and user-provided files as untrusted input.**
4. **Avoid placing secrets or unnecessary personal data into model context.**
5. **Validate tool calls and outputs independently of the model's decisions.**
6. **Prevent unauthorized cross-tenant access at retrieval, caching, and application layers.**
7. **Preserve source provenance so suspicious evidence can be traced and investigated.**

## How to implement

| Rule | Guides |
|------|--------|
| **1. Permissions before evidence** | [Metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md) · [Context algorithm — step 1](./context-algorithm.md) |
| **2. Instructions vs retrieved content** | Delimiters, system vs user blocks, no blending untrusted text into system prompt |
| **3. Untrusted retrieved / user files** | Prompt-injection awareness ([guard-rails strategy](../guard-rails/guard-rails-strategy.md)); do not execute instructions embedded in docs |
| **4. Secrets and PII in context** | Redact logs; minimal fields in chunks; [guard-rails decision assistance](../guard-rails/guard-rails-decision-architecturing-assistance.md) |
| **5. Validate tools independently** | [Analytical question — validated SQL](./context-analytical-question.md) · [Architecture evaluation — security](../retrieval/search/retrieval-architecture-evaluation.md) |
| **6. Cross-tenant at retrieval, cache, app** | [Data isolation](../guard-rails/guardrails-data-isolation.md) · [Wrong architecture: shared retrieval](../guard-rails/wrong-architecture-shared-retrieval.md) · [Safer tenant-scoped retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md) |
| **7. Source provenance** | Citation metadata ([context info for output](./context-info-for-output.md)); audit IDs on chunks |

These rules apply in **assemble_context_node** and earlier—validation after generation cannot undo a prompt that already contained forbidden evidence ([LangGraph workflow](./context-assembly-langchain-langgraph.md)).

## See also

- [Evaluate context assembling](./context-evaluate-assembling.md) — unauthorized-evidence tests, groundedness, no-answer handling
- [Guard-rails overview](../guard-rails/README.md)
- [Contexting overview](./README.md)
