# Agentic AI evaluation and improvement

Agentic systems combine model decisions, tools, state, and control flow. Evaluate whether the whole task succeeds and whether each step is safe, verifiable, and worth its cost before adding more autonomy or test-time compute.

## Evaluate the agent

Build a representative dataset of tasks with expected outcomes, allowed tools, constraints, and known failure cases. Score more than the final answer:

| Dimension | Example check |
|-----------|---------------|
| **Task success** | Did the agent reach the expected result or a valid safe handoff? |
| **Tool use** | Did it choose the right tool, arguments, and call order? |
| **Grounding** | Are claims supported by retrieved evidence or tool results? |
| **Verification** | Did it check consequential actions and outputs against explicit criteria? |
| **Safety** | Did it respect permissions, boundaries, and stop conditions? |
| **Efficiency** | How many model/tool calls, tokens, elapsed time, and dollars did it use? |

Use deterministic assertions where possible, and human review or a calibrated model judge for subjective quality. Inspect trajectories as well as end results: a correct answer reached through an unauthorized action is still a failure.

## Test-time compute scaling

At inference time, spend additional compute only when the task and budget justify it. Options include a second verification pass, bounded retries, generating and ranking multiple candidates, parallel specialist calls, or deeper search/tool use. Set explicit limits for attempts, tokens, wall-clock time, and tool calls.

Compare each strategy against a single-pass baseline on the same evaluation set. Report quality lift alongside latency and cost; route only uncertain or high-impact tasks to the more expensive path when evaluation supports that policy.

## Self-improving systems

Treat production feedback as candidate data, not automatic permission to change behavior. Capture failures and user corrections with privacy controls, review and label them, add validated examples to a versioned evaluation set, and use offline experiments to propose prompt, tool, or model changes. Gate releases against the baseline, safety checks, and cost/latency budgets; keep rollback available.

Do not let an agent rewrite its own production instructions, permissions, or evaluation criteria without an independently reviewed change and a controlled release.

## LangChain and LangGraph

LangChain provides model, prompt, retriever, and tool integrations that can be composed in an application. LangGraph is useful when orchestration needs explicit state, branching, loops, checkpoints, or human approval. Keep business authorization and validation in application-controlled boundaries, and test framework workflows with the same task dataset and trace-level checks as other agents.

| Need | Starting point |
|------|----------------|
| Straightforward model/tool composition | LangChain components or a small explicit function pipeline |
| Stateful branching, retries, or human review | LangGraph workflow with typed state and bounded transitions |
| Reliable evaluation | Trace each model and tool step; assert outputs and side effects against a fixed dataset |

## Practical checklist

- [ ] Define task success and failure labels before changing the agent.
- [ ] Include adversarial, ambiguous, and tool-error cases in the dataset.
- [ ] Compare against a single-pass baseline and inspect trajectories.
- [ ] Bound loops, tool permissions, latency, tokens, and spend.
- [ ] Gate self-improvement proposals with offline evaluation and reviewed rollout.

## See also

- [Agents overview](./README.md)
- [Sequential AI pipeline](./multi-agent-architecture/sequential-ai-pipeline.md)
- [Parallel agents architecture](./multi-agent-architecture/parallel-agents-architecture.md)
- [Observability and evaluation](../observability-evaluation/README.md)
