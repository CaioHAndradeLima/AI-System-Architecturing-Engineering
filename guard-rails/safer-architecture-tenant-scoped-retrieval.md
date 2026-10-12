# Safer architecture: tenant-scoped retrieval

A **multi-tenant RAG pattern** where identity and authorization are resolved in a trusted backend before any search, retrieval is filtered by `tenant_id`, and the response is validated before it reaches the user.

## Architecture

```
         Authenticated request
                  |
                  v
        +--------------------+
        | Identity provider  |
        | Verify user        |
        +--------------------+
                  |
                  v
        +--------------------+
        | Trusted backend    |
        | Resolve tenant ID  |
        +--------------------+
                  |
                  v
        +--------------------+
        | Authorization      |
        | Check membership   |
        +--------------------+
                  |
                  v
        +--------------------+
        | Tenant-scoped      |
        | retrieval          |
        |                    |
        | tenant_id = A      |
        +--------------------+
                  |
                  v
        +--------------------+
        | Authorized chunks  |
        | ONLY from Tenant A |
        +--------------------+
                  |
                  v
                 LLM
                  |
                  v
        +--------------------+
        | Validate response  |
        +--------------------+
                  |
                  v
             Tenant A user
```

## Stage responsibilities

| Stage | Role |
|-------|------|
| **Identity provider** | Validates tokens/credentials; returns a stable subject (user ID), not tenant scope by itself. |
| **Trusted backend** | Maps the authenticated subject to **tenant ID(s)** using server-side directory data—never trust client-supplied `tenant_id`. |
| **Authorization** | Confirms the user is a member (or has a role) for the tenant and action (e.g. read knowledge base). |
| **Tenant-scoped retrieval** | Every vector/BM25 query includes a mandatory filter (e.g. `tenant_id = A`) enforced in the adapter layer. |
| **Authorized chunks** | Post-retrieval check optional but useful: drop any hit whose metadata does not match the session tenant. |
| **LLM** | Sees only approved chunks; prompts should not include other tenants’ identifiers. |
| **Validate response** | Schema, policy, citation-to-tenant checks, PII/redaction per [guardrails strategy](./guardrails-strategy.md). |
| **Tenant A user** | Response is delivered only on the authenticated channel for that user. |

## Contrast with the anti-pattern

| | [Wrong: shared retrieval](./wrong-architecture-shared-retrieval.md) | This pattern |
|---|------|--------------|
| Index scope | All customers in one search | Filter bound to resolved tenant |
| Trust boundary | Model/context absorbs cross-tenant chunks | Backend enforces scope before LLM |
| Proof of isolation | Weak | Logs: principal, tenant_id, doc IDs retrieved |

## Practical checklist

- [ ] Reject or ignore client-provided tenant headers unless cross-checked against membership
- [ ] Implement filters in **adapters** (vector store client), not only in agent prompts
- [ ] Log `tenant_id`, user ID, and retrieved document IDs for audit
- [ ] Run cross-tenant retrieval tests in [evaluation](../evaluation/)
- [ ] Fail closed if tenant cannot be resolved or membership check fails

## See also

- [Wrong architecture: shared retrieval](./wrong-architecture-shared-retrieval.md)
- [Guardrails strategy](./guardrails-strategy.md)
- [Guard-rails overview](./README.md)
