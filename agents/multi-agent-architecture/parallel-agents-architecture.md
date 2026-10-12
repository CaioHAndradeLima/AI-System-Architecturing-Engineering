# Parallel agents architecture

A **fan-out / fan-in multi-agent workflow**: a coordinator decomposes the user request, independent agents work on disjoint subtasks at the same time, and an aggregator merges their outputs into one final response.

## Prerequisites

- [Sequential AI pipeline](./sequencial-ai-pipeline.md) (contrast: fixed order vs parallel work)
- Tool/API access patterns per domain agent (docs, tickets, metrics, etc.)

## Core idea

Latency and coverage improve when subtasks **do not depend on each other**. A coordinator assigns work (often by source or capability), agents A/B/C run in parallel against different systems, and an aggregator resolves overlaps, conflicts, and gaps before the user sees a single answer.

## Architecture

```
                    User request
                        |
                        v
                 +--------------+
                 | Coordinator  |
                 +--------------+
                        |
             +----------+----------+
             |          |          |
             v          v          v
        +---------+ +---------+ +---------+
        | Agent A | | Agent B | | Agent C |
        | Docs    | | Jira    | | Metrics |
        +---------+ +---------+ +---------+
             |          |          |
             +----------+----------+
                        |
                        v
                 +--------------+
                 | Aggregator   |
                 | Merge results|
                 +--------------+
                        |
                        v
                  Final response
```

## Stage responsibilities

| Stage | Role | Typical output |
|-------|------|----------------|
| **Coordinator** | Parse request, decide which agents to invoke, pass scoped sub-queries and deadlines | Per-agent task specs (query, filters, output schema) |
| **Agent A (Docs)** | Search knowledge base, wikis, runbooks | Snippets, links, summaries grounded in docs |
| **Agent B (Jira)** | Search issues, sprints, assignees | Ticket IDs, status, relevant comments |
| **Agent C (Metrics)** | Query dashboards, logs, or analytics APIs | Numbers, trends, anomaly notes |
| **Aggregator** | Merge partial answers, dedupe, rank by relevance, note conflicts | Unified draft + citations per source |
| **Final response** | User-facing formatting; optional reviewer pass | Single coherent reply |

Agent labels (Docs / Jira / Metrics) are **examples**—swap them for any set of parallel specialists (code repos, CRM, calendar, etc.).

## How it works

1. **Coordinator** must output **narrow subtasks** so agents do not duplicate the same search or contradict scopes.
2. **Parallel execution** uses async jobs, a worker pool, or separate tool sessions; cap concurrency and per-agent timeouts.
3. Each specialist returns **structured results** (findings, confidence, source refs) so the aggregator is not parsing free-form prose from three models.
4. **Aggregator** handles: empty results from one branch, contradictory facts (Jira says “done”, docs say “deprecated”), and ordering (executive summary first, details after).
5. Optionally run a **light reviewer** after aggregation for policy and tone—cheaper than re-running all agents.

Partial failure is normal: ship an answer that states which sources failed rather than blocking the entire request unless all branches are mandatory.

## Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| **Parallel agents (this pattern)** | Lower wall-clock time when I/O-bound; natural fit for multi-source questions | Merge logic is non-trivial; duplicate/conflicting evidence; higher burst cost |
| **Sequential pipeline** | Simple trace; each step refines the last | Latency sums; later stages wait on earlier ones |
| **Single agent with many tools** | One orchestration loop | Tool-choice errors; context bloat; harder to specialize prompts |

## Practical checklist

- [ ] Coordinator outputs **explicit agent list** (skip agents that are irrelevant to the query)
- [ ] Define a **shared result schema** for all parallel agents
- [ ] Set **per-agent timeouts** and include partial results in the aggregator prompt
- [ ] Aggregator prompt includes **conflict resolution rules** (prefer primary source, prefer recency, ask user)
- [ ] Trace **which agent contributed** each claim for debugging and trust

## See also

- [Sequential AI pipeline](./sequencial-ai-pipeline.md)
- [Multi-agent architecture index](./README.md)
