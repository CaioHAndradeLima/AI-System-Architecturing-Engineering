# Embedding user context compact flow

When the **latest user message** is ambiguous alone, use **authorized** conversation history to rewrite the question before embed and retrieve—without leaking other users’ or tenants’ context.

## Flow

```
  Latest user message
          |
          v
  Is it understandable on its own?
       /          \
     Yes           No
      |             |
      |       Use authorized
      |       conversation context
      |             |
      |             v
      |       Rewrite question
      |             |
      +------+------+
             |
             v
      Embed query
             |
             v
      Retrieve evidence
```

## Stage notes

| Step | Role |
|------|------|
| **Understandable on its own?** | Heuristic or classifier: pronouns (“it”, “that policy”), ellipsis, or follow-ups often need context |
| **Authorized conversation context** | Load only this user’s thread for this tenant; enforce session identity server-side ([guard-rails](../../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)) |
| **Rewrite question** | Produce a **standalone** search query (rules or LLM); log rewrite for debugging, not cross-tenant training without consent |
| **Embed query** | Same model as document index; apply query encoding rules ([user query flow](./embedding-user-query-flow.md)) |
| **Retrieve evidence** | Vector search + metadata filters; optional techniques from [cleaning user query](./embedding-cleaning-user-query.md) after rewrite |

If the message **is** self-contained, skip rewrite and embed the latest text directly—avoid injecting stale history that steers retrieval wrong.

## Memory and isolation

- Conversation store must be **scoped** by tenant + user (or session)—same requirements as [chunking metrics — memory isolation](../../chunking/chunking-metrics-observability.md) and [robust cloud rules](../../../guard-rails/guard-rails-robust-cloud-rules-implementation.md).
- Do not put rewritten queries in a **shared cache key** without tenant/user in the key.

## See also

- [Embedding cleaning user query](./embedding-cleaning-user-query.md)
- [Embedding user query flow](./embedding-user-query-flow.md)
- [Queries overview](./README.md) · [Embedding overview](../README.md)
