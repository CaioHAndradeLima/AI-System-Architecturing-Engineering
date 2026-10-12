# Prompt implementation flow

**Prompt engineering implementation checklist**—from separation of trusted instructions through rollout, regression gate, and production monitoring.

```
PROMPT ENGINEERING — IMPLEMENTATION CHECKLIST
=============================================

            Start
              |
              v
+---------------------------------------------+
| 1. Separate prompt instructions from       |
|    user requests and retrieved evidence    |
+---------------------------------------------+
              |
              v
+---------------------------------------------+
| 2. Define grounding and insufficient-       |
|    evidence behavior                        |
+---------------------------------------------+
              |
              v
+---------------------------------------------+
| 3. Build reusable prompt templates          |
+---------------------------------------------+
              |
              v
+---------------------------------------------+
| 4. Test few-shot examples when needed       |
+---------------------------------------------+
              |
              v
+---------------------------------------------+
| 5. Treat retrieved documents as             |
|    untrusted input                          |
+---------------------------------------------+
              |
              v
+---------------------------------------------+
| 6. Validate structured output and           |
|    tool arguments                           |
+---------------------------------------------+
              |
              v
+---------------------------------------------+
| 7. Version prompts and record model         |
|    configuration                            |
+---------------------------------------------+
              |
              v
+---------------------------------------------+
| 8. Run golden-dataset regression tests      |
+---------------------------------------------+
              |
              v
+---------------------------------------------+
| 9. Monitor quality, latency, token use,     |
|    and cost                                 |
+---------------------------------------------+
              |
              v
+---------------------------------------------+
| 10. Implement safe rollout and rollback     |
+---------------------------------------------+
              |
              v
       +------------------+
       | Regression found? |
       +------------------+
          |            |
         Yes           No
          |            |
          v            v
   Fix prompt,       Deploy / promote
   model, or data    gradually
          |            |
          v            v
   Re-run tests    Monitor production
          |            |
          +----<-------+
```

## Step → guides

| Step | Docs |
|------|------|
| 1. Separate instructions / evidence | [Prompt categories](./prompt-categories.md) · [Reliable architecture](../contexting/context-reliable-architecture.md) |
| 2. Grounding & insufficient evidence | [Standard format](./prompt-standard-format.md) · [Similarity abstain](../retrieval/search/retrieval-strategy-similarity.md) |
| 3. Reusable templates | [Standard format](./prompt-standard-format.md) · [Architecturing decision-based](./prompt-architecturing-decision-based.md) |
| 4. Few-shot | [Few-shot providing samples](./prompt-few-shot-providing-samples.md) |
| 5. Untrusted documents | [Prompt injection](./prompt-injection.md) |
| 6. Structured output & tools | [Variables — structured output](./prompt-relevant-variables-influences.md) · [Analytical question](../contexting/context-analytical-question.md) |
| 7. Version & model config | [Prompt versioning](./prompt-versioning.md) |
| 8. Golden regression | [Query evaluation](../retrieval/embedding/queries/embedding-user-query-evaluation.md) · [Evaluate assembling](../contexting/context-evaluate-assembling.md) |
| 9. Monitor | [Retrieval metrics observability](../retrieval/search/retrieval-metrics-observability.md) |
| 10. Rollout / rollback | [Prompt versioning — canary](./prompt-versioning.md) |
| Full RAG context path | [Context implementation](../contexting/context-algorithm.md) · [Retrieval implementation](../retrieval/search/retrieval-implementation-flow.md) |

## See also

- [Prompting overview](./README.md)
