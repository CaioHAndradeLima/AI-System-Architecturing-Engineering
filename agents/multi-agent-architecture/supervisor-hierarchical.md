# Supervisor hierarchical architecture

A **tree of supervisors**: a main supervisor delegates to domain supervisors, each domain supervisor manages specialist worker agents, and results roll back up the hierarchy for synthesis and the final user response.

## Prerequisites

- [Parallel agents architecture](./parallel-agents-architecture.md) (flat coordinator vs layered delegation)
- [Sequential AI pipeline](./sequencial-ai-pipeline.md) (when to prefer a linear chain instead)

## Core idea

Large or ambiguous requests benefit from **two levels of routing**. The main supervisor chooses domains (engineering vs business); domain supervisors know which workers to run and how to interpret their outputs. Workers stay narrow (code, Jira, analytics, docs); supervisors handle scope, quality, and escalation within their branch.

## Architecture

```
                        User
                        |
                        v
                 +--------------+
                 | Main         |
                 | Supervisor   |
                 +--------------+
                    /        \
                   v          v
           +-----------+  +-----------+
           | Engineering|  | Business  |
           | Supervisor |  | Supervisor|
           +-----------+  +-----------+
              /    \         /    \
             v      v       v      v
          Code    Jira   Analytics Docs
          Agent   Agent  Agent    Agent
             \      /       \      /
              +----+         +----+
                  \           /
                   v         v
                  Main Supervisor
                         |
                         v
                  Final response
```

## Role responsibilities

| Layer | Role | Typical output |
|-------|------|----------------|
| **Main supervisor** | Interpret user intent; activate zero, one, or both domain branches; merge branch summaries | Delegation plan, combined answer or clarifying question |
| **Engineering supervisor** | Scope technical work; assign Code and Jira agents; reconcile eng vs ticket state | Branch report: changes, blockers, ticket links |
| **Business supervisor** | Scope product/ops questions; assign Analytics and Docs agents | Branch report: metrics narrative + policy/docs alignment |
| **Worker agents** | Execute tools against a single system class | Structured findings + citations |
| **Final response** | Main supervisor formats after **second pass** (rollup) | User-facing reply |

Worker names in the diagram are illustrative; the pattern generalizes to any domain split (security / legal / support, etc.).

## How it works

1. **Main supervisor (downward pass)** decides which domain supervisors participate. Skip entire subtrees when the question is clearly single-domain.
2. **Domain supervisors** fan out to workers—often **in parallel** within the branch, like a nested [parallel agents](./parallel-agents-architecture.md) pattern.
3. Workers return to their **domain supervisor**, which dedupes, resolves local conflicts, and produces one branch artifact.
4. **Main supervisor (upward pass)** merges branch reports. It may ask domain supervisors for follow-up (second hop) before answering the user.
5. **Final response** should attribute sources by domain so users can trust engineering vs business claims separately.

Escalation paths: a worker can signal “out of scope” to its domain supervisor; the domain supervisor can reassign or bubble a question to the main supervisor instead of hallucinating.

## Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| **Hierarchical supervisors (this pattern)** | Scales org structure; limits prompt/tool sprawl per agent; clear ownership per domain | Multiple LLM rounds; coordination bugs at merge points; harder end-to-end testing |
| **Flat parallel coordinator** | Fewer layers; simpler mental model | Coordinator prompt overloaded; weak domain-specific routing |
| **Sequential pipeline** | Easiest audit trail | Poor fit when many independent sources must be consulted |

## Practical checklist

- [ ] Main supervisor prompt lists **domains and when to invoke each**
- [ ] Domain supervisors share a **branch output schema** for upward merge
- [ ] Workers **must not** call cross-domain tools unless explicitly escalated
- [ ] Log **supervisor decisions** (which branches, which workers) for replay
- [ ] Define **max depth and max rounds** to avoid supervisor ping-pong loops
- [ ] Integration test **single-domain**, **multi-domain**, and **empty branch** cases

## See also

- [Parallel agents architecture](./parallel-agents-architecture.md)
- [Sequential AI pipeline](./sequencial-ai-pipeline.md)
- [Multi-agent architecture index](./README.md)
