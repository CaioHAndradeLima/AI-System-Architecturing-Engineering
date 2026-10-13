# Pipeline evaluation YAML sample

**Pinned experiment config** for one candidate run in [pipeline evaluation](./pipeline-evaluation.md)—store alongside results so baseline comparison replays the same model, prompt, retrieval, and dataset versions ([pipeline evaluation components](./pipeline-evaluation-components.md)).

```yaml
experiment_id: rag-eval-042
model:
  provider: example_provider
  name: model_A
  version: pinned_version
prompt:
  id: incident_assistant
  version: v4
retrieval:
  strategy: hybrid
  top_k: 5
  reranker: enabled
context:
  max_tokens: 12000
evaluation:
  dataset_version: golden_v7
```

## Field → pipeline dimension

| YAML block | Dimension | Notes |
|------------|-----------|--------|
| `experiment_id` | Run identity | Tie to CI job, PR, or artifact URL |
| `model.*` | Model | Provider, name, **pinned** version ([select LLM flow](../llm/select-llm-flow.md)) |
| `prompt.*` | Prompt | Logical id + version ([prompt versioning](../prompting/prompt-versioning.md)) |
| `retrieval.*` | Retrieval | Strategy, top-K, reranker ([hybrid](../retrieval/search/retrieval-strategy-hybrid-search-vector-plus-keyword.md)) |
| `context.max_tokens` | Context assembly | Token budget ([context algorithm](../contexting/context-algorithm.md)) |
| `evaluation.dataset_version` | Golden set | Frozen eval set ([observability decision-based](../observability-evaluation/observability-decision-based.md)) |

Emit the same fields (or hashes) on **traces** during canary so production traffic matches the config that passed the quality gate ([tracing metrics — attributes](../observability-evaluation/tracing-for-observability-metrics.md)).

Compare candidates by swapping one block at a time—e.g. only `prompt.version` or only `retrieval.strategy`—while holding `evaluation.dataset_version` constant.

## See also

- [Regression and canary releases](../observability-evaluation/regression-and-canary-releases.md)
- [Deployment overview](./README.md)
