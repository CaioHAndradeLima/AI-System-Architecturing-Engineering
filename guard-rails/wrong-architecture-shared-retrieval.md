# Wrong architecture: shared retrieval without isolation

An **anti-pattern** for multi-tenant RAG: every customer’s documents sit in one vector index, and user questions hit that shared search before the LLM answers—with no strong tenant boundary in the retrieval path.

## Architecture (do not copy)

```
Customer A question ----+
                        |
Customer B documents ---+----> Shared vector search
                        |             |
Customer C documents ---+             v
                                  LLM prompt
                                       |
                                       v
                                  Final answer
```

## Why this fails

| Risk | What goes wrong |
|------|-----------------|
| **Cross-tenant leakage** | Customer A’s query can retrieve chunks from B or C’s documents; the model may summarize or quote another tenant’s data in the **final answer**. |
| **Broken authorization model** | ACL applied only *after* retrieval is too late—sensitive text is already in the prompt context. |
| **Ambiguous identity** | Mixing “Customer A question” with all customers’ corpora in one search assumes the retriever magically knows scope; without enforced filters, scope is undefined. |
| **Compliance and audit** | You cannot prove which tenant data was accessed for a given request if the index and logs are not partitioned by principal. |

This violates **security guardrails** (tenant isolation, data protection) from the [guard-rails overview](./README.md). It also undermines **AI safety** when answers appear grounded but cite another customer’s private content.

## What to do instead

1. **Bind every request to a principal** (user, tenant, org) before any search—see [guardrails-strategy.md](./guardrails-strategy.md) (Authentication / ACL → tool / retrieval checks).
2. **Scope retrieval server-side**: metadata filters, separate indexes per tenant, or row-level security on the vector store—never rely on the LLM to ignore wrong chunks.
3. **Validate outputs** for citations: retrieved doc IDs must belong to the same tenant as the session.
4. **Test with cross-tenant adversarial queries** (see [test use cases](./guard-rails-test-use-cases.md); e.g. “summarize Customer B’s contract” while authenticated as A).

## Reference implementation

**[guardrails-strategies](https://github.com/CaioHAndradeLima/guardrails-strategies)** — Shared-index leak metrics in `shared_index_simulation.py`. Keys: `wrong_architecture_shared_retrieval`, `scenarios.shared_index_antipattern`.

Recommended gate: `ci-guardrails-eval` (`evaluate-pipeline` + `check-measure`). Coverage: [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/guardrails-strategies/blob/main/docs/LAB_COVERAGE.md) (14/14).

## See also

- [Safer architecture: tenant-scoped retrieval](./safer-architecture-tenant-scoped-retrieval.md)
- [Guardrails strategy](./guardrails-strategy.md)
- [Guard-rails types](./README.md#guard-rails-types)
