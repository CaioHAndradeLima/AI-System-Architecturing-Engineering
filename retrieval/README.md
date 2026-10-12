# Retrieval

Design and operate **retrieval** for LLM applications: indexing, query-time search, grounding, and quality—together with authorization and tenant scope ([guard-rails](../guard-rails/) retrieval notes).

## Topic areas (as docs are added)

| Area | What we cover |
|------|----------------|
| **Pipeline** | Ingest → chunk → embed → index → query → rerank → context assembly |
| **Chunking** | Size, overlap, structure-aware splits, metadata |
| **Search** | Dense, sparse, hybrid, filters, reranking |
| **Grounding** | Citations, context limits, when retrieval fails |
| **Operations** | Freshness, reindexing, eval metrics (recall, MRR, grounded answers) |
| **Multi-tenant** | Scoped indexes, ACL sync, safe caching |

## Guides

_Guide entries (tags, short description, see-more links) will appear here as markdown files are added—same style as [guard-rails README](../guard-rails/README.md) and [agents README](../agents/README.md)._

## Related guard-rails

- [Safer architecture: tenant-scoped retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md)
- [Wrong architecture: shared retrieval](../guard-rails/wrong-architecture-shared-retrieval.md)
- [Retrieval authorization in decision assistance](../guard-rails/guard-rails-decision-architecturing-assistance.md)
