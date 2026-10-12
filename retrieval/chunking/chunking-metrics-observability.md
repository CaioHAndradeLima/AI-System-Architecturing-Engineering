# Chunking metrics observability

Metrics for **chunking, embedding, indexing, retrieval, and answers**—what to measure at startup vs enterprise. Complements [ingestion observability](../ingestion/ingestion-observability.md) with chunk-specific signals.

## Ingestion and chunking pipeline

| Metric | What it measures | Why it matters | Startup | Enterprise |
|--------|------------------|----------------|---------|------------|
| **Ingestion success rate** | Percentage of documents processed successfully | Detects pipeline failures | Log successes and failures | Dashboards, alerts and SLOs |
| **Parsing failure rate** | Percentage of documents with extraction errors | Poor extraction leads to bad chunks | Log parser errors | Break down by source, format and parser version |
| **Chunk count per document** | Number of chunks produced per document | Detects unexpected splitting behavior | Log per document | Analyze distributions and outliers |
| **Chunk size distribution** | Actual chunk lengths in tokens or characters | Detects oversized, tiny or inconsistent chunks | Inspect min, median and max | Track percentiles by document type and configuration |
| **Empty / low-quality chunk rate** | Chunks containing little useful content | Prevents wasted embeddings and noisy retrieval | Validate before embedding | Alert on spikes by source or parser version |
| **Duplicate chunk rate** | Repeated chunks within an index | Reveals duplicate ingestion or poor update handling | Check hashes | Track duplicates across versions and sources |
| **Embedding latency** | Time to generate vectors | Identifies embedding bottlenecks | Measure request duration | Track percentiles, throughput and provider errors |

## Indexing, retrieval, and answer quality

| Metric | What it measures | Why it matters | Startup | Enterprise |
|--------|------------------|----------------|---------|------------|
| **Embedding cost** | Cost of processing text into vectors | Helps control ingestion spend | Estimate cost per document | Track cost per tenant, source, and configuration |
| **Indexing latency** | Time from ingestion to searchable availability | Measures freshness | Measure end-to-end duration | Monitor percentiles and freshness SLOs |
| **Recall@K** | Fraction of relevant evidence found in the top K results | Measures retrieval coverage | Evaluate a golden dataset | Regression gates and domain-specific test suites |
| **Precision@K** | Fraction of retrieved results that are relevant | Measures retrieval noise | Evaluate top-K results | Segment by query type and tenant where appropriate |
| **Duplicate retrieval rate** | Redundant results among retrieved chunks | Detects excessive overlap or duplicate indexing | Inspect result sets | Track by chunking and retrieval configuration |
| **Context relevance** | Whether retrieved passages are useful for the question | Assesses context sent to the LLM | Manual review | Automated evaluation plus human sampling |
| **Answer correctness** | Whether the final answer is supported and correct | Validates end-to-end RAG performance | Test representative questions | Continuous evaluation and controlled releases |
| **Stale chunk rate** | Results tied to outdated document versions | Prevents obsolete facts from being returned | Test update/delete flows | Monitor index freshness and deletion propagation |

## Security and isolation

| Metric | What it measures | Why it matters | Startup | Enterprise |
|--------|------------------|----------------|---------|------------|
| **Cross-tenant isolation failures** | Unauthorized data exposed across customers | Critical security signal | Automated isolation tests | Continuous security testing, audit and incident alerts |

Treat any failure as **incident-grade**—see [guard-rails test use cases](../../guard-rails/guard-rails-test-use-cases.md).

## When metrics regress

Use [ingestion procedures](../ingestion/ingestion-procedures.md) to map symptoms to components (e.g. high duplicate retrieval → overlap or re-ingestion; poor Recall@K → chunking strategy per [architecturing matrix](./chunking-architecturing.md)).

## See also

- [Chunking architecturing decision-based](./chunking-architecturing-decision-based.md)
- [Ingestion observability](../ingestion/ingestion-observability.md)
- [Chunking overview](./README.md)
