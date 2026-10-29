# GCP microservices agent platform

Reference layout for a **TypeScript and/or Python** agent platform on **GCP**: microservices, async work, state, and observability—parallel to the AWS design guides.

## Prerequisites

- [AWS intermediate](./aws-intermediate.md) (conceptual comparison)
- [Production components](../deployment/production-components.md)
- [Agent platform starter-kit primitives](../agents/agent-platform-starter-kit-primitives.md)

## Core idea

Split **API edge**, **orchestration**, **retrieval**, and **integrations** so teams can scale and deploy independently. The agent runtime (starter kit) lives in orchestration services; tools and MCP adapters sit at integration boundaries.

## Intermediate topology (ASCII)

```
                    Internet
                        |
                        v
              +-------------------+
              | Cloud Load        |
              | Balancing +       |
              | Cloud Armor (WAF) |
              +-------------------+
                        |
                        v
              +-------------------+
              | Cloud Run or GKE    |
              | Agent API + auth  |
              +-------------------+
                        |
          +-------------+-------------+
          |                           |
          v                           v
+-------------------+       +-------------------+
| Cloud Run / GKE   |       | Cloud Run / GKE   |
| Orchestrator      |       | Retrieval service |
| (LangGraph/SDK)   |       | hybrid search     |
+-------------------+       +-------------------+
          |                           |
          |                           v
          |                 +-------------------+
          |                 | Vertex AI         |
          |                 | embeddings / LLM  |
          |                 +-------------------+
          v
+-------------------+       +-------------------+
| Pub/Sub           |       | Firestore /       |
| async jobs        |       | Spanner / Redis   |
| (ingest, HITL)    |       | checkpoints       |
+-------------------+       +-------------------+
          |
          v
+-------------------+
| Cloud Storage     |
| docs + artifacts  |
+-------------------+
```

## Component mapping

| Concern | GCP services (typical) | Notes |
|---------|------------------------|-------|
| **API** | Cloud Run, API Gateway, Identity-Aware Proxy / OAuth | JWT → tenant principal |
| **Orchestration** | Cloud Run or GKE | Horizontal scale; CPU for graph logic |
| **LLM** | Vertex AI (Gemini, partner models) | Central quotas and logging |
| **Retrieval** | Vertex AI Search, AlloyDB/pgvector, or managed vector | Tenant filters in app code |
| **Async** | Pub/Sub + Cloud Run jobs or GKE workers | Ingestion, batch eval, HITL timeouts |
| **State** | Firestore or Spanner for checkpoints; Memorystore for hot cache | Version policy with checkpoint |
| **Secrets** | Secret Manager | Per-integration credentials |
| **Observability** | Cloud Logging, Cloud Monitoring, Cloud Trace; OpenTelemetry export | Align with LLM trace vendor if used |
| **CI/CD** | Cloud Build, Artifact Registry | Eval gate before promote |

## TypeScript vs Python split

| Layer | Common choice | Rationale |
|-------|---------------|-----------|
| Public API / BFF | TypeScript (Node) | Typed contracts, fast I/O |
| Agent orchestration | Python or TS | Match team skills; share proto/OpenAPI between services |
| Retrieval / ML utilities | Python | Ecosystem for eval and embeddings |
| Shared contracts | Protobuf, OpenAPI, JSON Schema for tools | Language-agnostic starter kit |

One **tool and policy registry** (service or config bundle) avoids drift between TS edge and Python workers.

## Microservice boundaries

- **Do not** put tenant authz only in the API—retrieval and tool services re-validate principal.
- **Do** keep MCP servers as separate deployables with their own IAM and breakers.
- **Prefer** synchronous orchestration for interactive chat; offload long ingest/eval to Pub/Sub.

## Trade-offs vs single Lambda/monolith

| Approach | Pros | Cons |
|----------|------|------|
| **Split services (this note)** | Independent scale, blast radius | Network latency, distributed debugging |
| **Single Cloud Run service** | Simpler ops | Coupled release of retrieval and agents |

## Practical checklist

- [ ] Define service SLOs and trace propagation (W3C trace context) across Run/GKE.
- [ ] Pub/Sub dead-letter topics for failed agent jobs.
- [ ] Secret Manager per MCP/integration; no keys in agent containers.
- [ ] Staging project or namespace with production-like IAM.
- [ ] CI eval against golden agent tasks before Artifact Registry promote.

## See also

- [Design overview](./README.md)
- [Deployment cloud tools](../deployment/deployment-cloud-tools.md)
- [Agent production guardrails at scale](../agents/agent-production-guardrails-at-scale.md)
