# Guardrails data isolation

Strategies for keeping each tenant’s data separate in storage and retrieval. Pick based on compliance needs, operational cost, and blast radius if a filter bug slips through.

## Strategies

### 1. Shared database, tenant-scoped records

One logical database (or schema) holds all customers. Every row carries a **tenant identifier**; queries and retrieval must always filter on that ID.

```
Shared database
|
+-- tenant_id = A --> Customer A records
+-- tenant_id = B --> Customer B records
+-- tenant_id = C --> Customer C records
```

**When it fits:** Many tenants, moderate isolation requirements, strong app-layer and DB policy discipline.

**Guardrails:**

- Mandatory `tenant_id` on all tenant-owned tables and vector metadata
- Composite indexes that include `tenant_id` so filters are cheap and hard to forget
- Row-level security (RLS) or equivalent so a bug in one code path cannot scan the whole table
- Integration tests that prove cross-tenant reads return empty

**Risk if done wrong:** A single missing `WHERE tenant_id = ?` clause becomes a [shared-retrieval anti-pattern](./wrong-architecture-shared-retrieval.md) at the data layer.

---

### 2. Separate schemas or databases

The application routes each tenant to its **own schema or database**. Isolation is structural: there is no shared row set to leak across customers with a forgotten filter.

```
Application
    |
    +----> Database A
    |
    +----> Database B
    |
    +----> Database C
```

**When it fits:** Stronger isolation (regulated data, enterprise contracts), fewer very large tenants, or when you can automate provisioning per customer.

**Guardrails:**

- Resolve tenant → connection string (or schema name) in the **trusted backend** after authorization—not from client input alone
- Connection pools per tenant or validated pool routing; log which datastore served each request
- Migrations, backups, and retention run per tenant or via a controlled provisioning pipeline
- Vector indexes live inside the tenant’s schema/DB so retrieval cannot cross wires without switching connections

**Trade-off vs strategy 1:** Higher ops surface (more instances/schemas) but smaller blast radius and simpler mental model for queries (no omnipresent `tenant_id` filter).

---

### 3. Dedicated infrastructure per tenant

Each customer runs in a **separate environment** (account, cluster, or stack). Compute, data stores, keys, and often networking are not shared with other tenants.

```
Customer A --> Dedicated environment A
Customer B --> Dedicated environment B
Customer C --> Dedicated environment C
```

**When it fits:** Maximum isolation (government, health, large enterprise), contractual dedicated hosting, or noisy-neighbor / data-residency requirements.

**Guardrails:**

- **IAM and network boundaries** per environment; no shared service roles across tenants unless strictly controlled
- Separate secrets, encryption keys, and observability tenants so logs/traces never co-mingle by default
- Deployment pipelines that promote the same *artifact* but parameterize per environment—avoid manual snowflakes
- Clear DNS/routing so users and API keys always land in the correct environment
- Disaster recovery and patching tested **per** environment or via automated fleet management

**Trade-offs:** Highest cost and operational complexity; best isolation story for audits and blast radius. Often combined with strategy 2 (dedicated DB inside each environment).

## Choosing among strategies

| Strategy | Isolation strength | Typical cost / ops |
|----------|-------------------|-------------------|
| 1. Shared DB + `tenant_id` | Moderate (policy + code dependent) | Lowest |
| 2. Separate schemas or databases | Strong | Medium |
| 3. Dedicated infrastructure per tenant | Strongest | Highest |

## Reference implementation

**[guardrails-strategies](https://github.com/CaioHAndradeLima/guardrails-strategies)** — Isolation mode fixtures in `data_isolation.py`. Keys: `guardrails_data_isolation`.

Recommended gate: `ci-guardrails-eval` (`evaluate-pipeline` + `check-measure`). Coverage: [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/guardrails-strategies/blob/main/docs/LAB_COVERAGE.md) (14/14).

## See also

- [Safer architecture: tenant-scoped retrieval](./safer-architecture-tenant-scoped-retrieval.md)
- [Guard-rails category — Tenant isolation](./guard-rails-category.md)
- [Guardrails AWS services](./guardrails-aws-services.md)
