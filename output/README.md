# Output

What happens **after model generation** and **before the user sees a response**: schema and policy checks, citation grounding, tool execution boundaries, and safe handling when validation fails.

Output validation sits at the end of [LLM flow](../llm/llm-flow.md) (after inference) and consumes the same evidence and metadata that [context assembly](../contexting/context-assembly-flow.md) prepared upstream.

## Topic areas (as docs are added)

| Area | Focus |
|------|--------|
| **Implementation strategies** | Deterministic checks through human review for grounded answers |
| **Citation validation** | Authorized source IDs and claim–evidence alignment |
| **Tool execution** | Policy gates, sandboxing, scoped credentials |
| **Failure handling** | Repair, retry, abstain, and escalation by failure type |
| **Scale & maturity** | Startup → production → enterprise output policies |

---

## Guides

### [output-implementation-flow.md](./output-implementation-flow.md)

`#checklist` · `#implementation` · `#guardrails`

Output validation and guardrails checklist—from schemas and citations through policy, failure handling, adversarial tests, and production monitoring.

→ [See more in output-implementation-flow.md](./output-implementation-flow.md)

### [output-decision-based.md](./output-decision-based.md)

`#architecture` · `#scale` · `#enterprise` · `#multi-agent`

How post-generation validation, delivery, and guardrails evolve from startup/prototype through growing production to enterprise / multi-agent.

→ [See more in output-decision-based.md](./output-decision-based.md)

### [output-implementation-strategies.md](./output-implementation-strategies.md)

`#validation` · `#groundedness` · `#quality`

How to validate LLM outputs against evidence and policy—pick strategies by risk, cost, and coverage (LLM flow — output validation).

→ [See more in output-implementation-strategies.md](./output-implementation-strategies.md)

### [output-citation-validation.md](./output-citation-validation.md)

`#citations` · `#grounding` · `#rag`

Validate citation IDs and claim support on the generated answer before delivery (context info — source metadata).

→ [See more in output-citation-validation.md](./output-citation-validation.md)

### [output-secure-tool-execution-flow.md](./output-secure-tool-execution-flow.md)

`#tools` · `#security` · `#sandbox`

Tool calls from the model are untrusted until validated, authorized, and executed with least privilege (prompt injection, reliable architecture).

→ [See more in output-secure-tool-execution-flow.md](./output-secure-tool-execution-flow.md)

### [output-validation-failure-impact.md](./output-validation-failure-impact.md)

`#failures` · `#abstain` · `#operations`

When post-generation or tool validation fails, respond in a bounded, safe way—repair, abstain, deny, or retry only where policy allows.

→ [See more in output-validation-failure-impact.md](./output-validation-failure-impact.md)

### [output-failure-procedure-flow.md](./output-failure-procedure-flow.md)

`#flow` · `#repair` · `#abstain` · `#escalation`

After generation, classify validation failures and apply the matching branch—pairs with the failure impact table.

→ [See more in output-failure-procedure-flow.md](./output-failure-procedure-flow.md)

### [output-failure-guardrails-via-langchain.md](./output-failure-guardrails-via-langchain.md)

`#langgraph` · `#routing` · `#repair` · `#safe-exit`

Validation routing in a LangGraph-style RAG loop: validate after generate, branch to repair, retrieve-more, or safe exit—implements failure procedure flow as graph edges.

→ [See more in output-failure-guardrails-via-langchain.md](./output-failure-guardrails-via-langchain.md)

### [output-validation-via-test-or-guardrails-metrics.md](./output-validation-via-test-or-guardrails-metrics.md)

`#metrics` · `#groundedness` · `#citations` · `#guardrails`

Metrics and tests for post-generation validation—schema, citations, grounding, abstain, blocks, repair, latency, and cost (implementation strategies, failure procedure flow).

→ [See more in output-validation-via-test-or-guardrails-metrics.md](./output-validation-via-test-or-guardrails-metrics.md)

### [output-validation-guardrails-practices.md](./output-validation-guardrails-practices.md)

`#testing` · `#adversarial` · `#tenant` · `#false-block`

Test and review scenarios for post-generation validation—cover in golden sets, CI eval, and adversarial suites (metrics, guard-rails test use cases).

→ [See more in output-validation-guardrails-practices.md](./output-validation-guardrails-practices.md)

## Reference implementation

**[output-strategies](https://github.com/CaioHAndradeLima/output-strategies)** is the **reference codebase** for the best practices in this section: layered post-generation validation, failure routing, adversarial fixtures, and CI profiles. It uses a bundled regression corpus; swap in your labeled outputs and evidence IDs for production adoption.

| Command | What it exercises |
|---------|-------------------|
| `python -m output_strategies.cli evaluate-pipeline --profile ci-output-eval` | **[Validation metrics](./output-validation-via-test-or-guardrails-metrics.md) scorecard** — schema, citations, grounding, tool safety, scenarios ([PIPELINE_EVAL.md](https://github.com/CaioHAndradeLima/output-strategies/blob/main/docs/PIPELINE_EVAL.md)) |
| `python -m output_strategies.cli evaluate` | [Implementation strategies](./output-implementation-strategies.md) — `schema_only` vs `schema_plus_citation` vs `layered_pipeline` |
| `python -m output_strategies.cli evaluate-scenarios` | [Failure procedure](./output-failure-procedure-flow.md), abstention, adversarial and tool scenarios |
| `python -m output_strategies.cli evaluate-full` | **100% output guide coverage** — [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/output-strategies/blob/main/docs/LAB_COVERAGE.md) (10/10) |
| Docker + `check-measure` | Profiles in [measure_profiles.json](https://github.com/CaioHAndradeLima/output-strategies/blob/main/config/measure_profiles.json); **`ci-output-eval`** uses `evaluate-pipeline`. GitHub Actions `measure-gate`. |

Pair with **[contexting-strategies](https://github.com/CaioHAndradeLima/contexting-strategies)** for authorized evidence assembly before generation ([context assembly flow](../contexting/context-assembly-flow.md)).

## Related

- [LLM flow](../llm/llm-flow.md) · [LangGraph validate node](../contexting/context-assembly-langchain-langgraph.md)
- [Evaluate assembling](../contexting/context-evaluate-assembling.md)
- [Prompt injection](../prompting/prompt-injection.md) · [Retry fallbacks and routing](../llm/llm-retry-fallbacks-routing.md)

## See also

- [Repository overview](../README.md)
