# Sequential AI pipeline

A **linear multi-agent workflow**: each stage receives the output of the previous stage, transforms it, and passes control forward until a final user-facing response is produced.

## Prerequisites

- Basic agent concepts (system prompt, tool use, structured outputs)
- Familiarity with retrieval-augmented generation if the retrieval stage loads external evidence

## Core idea

Instead of one monolithic model call, the system decomposes work into **specialized agents** with narrow responsibilities. Execution order is fixed: planner → retrieval → specialist → reviewer → response. There is no branching or parallel fan-out in this pattern; simplicity and auditability come from the strict sequence.

## Architecture

```
User request
      |
      v
+-------------------+
| Intent / Planner  |
| Identify the task |
+-------------------+
      |
      v
+-------------------+
| Retrieval Agent   |
| Find evidence     |
+-------------------+
      |
      v
+-------------------+
| Specialist Agent  |
| Analyze evidence  |
+-------------------+
      |
      v
+-------------------+
| Reviewer Agent    |
| Check the answer  |
+-------------------+
      |
      v
+-------------------+
| Final response    |
+-------------------+
```

## Stage responsibilities

| Stage | Role | Typical output |
|-------|------|----------------|
| **Intent / Planner** | Parse the user message, classify intent, choose sub-task and success criteria | Structured plan: goal, constraints, required evidence types |
| **Retrieval Agent** | Query indexes, APIs, or tools to gather grounding material | Documents, snippets, citations, tool results |
| **Specialist Agent** | Reason over the plan + evidence; produce a draft answer | Draft answer with reasoning trace or structured fields |
| **Reviewer Agent** | Verify completeness, policy, factual alignment with evidence, tone | Approved answer, or feedback sent back (if you add a loop) |
| **Final response** | Format for the user (markdown, JSON, UI payload) | What the user sees |

In the **pure sequential** form shown above, the reviewer either passes through an approved draft or you fail closed (escalate, ask clarifying questions, or refuse) rather than silently shipping a bad answer.

## How it works

1. **Planner** turns natural language into a machine-readable task spec so downstream agents do not re-interpret the user request differently.
2. **Retrieval** runs only after the plan exists, so queries target the right corpus, filters, and time range.
3. **Specialist** is domain-focused (legal, code, support, etc.) and should be constrained to cite or quote retrieved evidence.
4. **Reviewer** acts as a separate “critic” model or rules layer, reducing single-model overconfidence.
5. **Final response** strips internal artifacts (raw JSON, internal IDs) unless the product needs them.

Data usually flows as a **shared context object** (plan, retrieved chunks, draft, review verdict) appended at each step rather than re-sending the entire chat history to every agent—though you may still include recent user turns for tone and continuity.

## Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| **Sequential pipeline (this pattern)** | Easy to reason about, debug, and log per stage; clear ownership per agent | Higher latency (sum of all calls); early mistakes propagate; limited parallelism |
| **Single mega-prompt** | One round-trip, lowest latency | Harder to enforce retrieval and review; weaker separation of concerns |
| **Parallel specialists + merge** | Faster for independent subtasks | Merge logic and conflict resolution add complexity |

## Practical checklist

- [ ] Define a **schema** for planner output so retrieval and specialist prompts stay stable
- [ ] Log **inputs/outputs per stage** (with redaction) for tracing failures
- [ ] Give the reviewer explicit **rubrics** (grounded in evidence, answered the question, safe to send)
- [ ] Set **timeouts and fallbacks** per stage so one slow agent does not hang the pipeline
- [ ] Measure **end-to-end latency** and cost per stage before adding more agents

## See also

- Other multi-agent architecture notes in [multi-agent-architecture](./) (more patterns as they are added)
- [Agents overview](../README.md)
