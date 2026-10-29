# Guard-rails test use cases

Scenarios to prove tenant isolation, tool safety, and content handling behave as intended. Use as a checklist for integration tests and release gates.

| Test | Expected result |
|------|-----------------|
| Tenant A requests Tenant B's document ID | Denied; no document content returned |
| Tenant A changes `tenant_id` in the request | Denied unless independently authorized |
| Tenant A searches for a unique phrase present only in Tenant B's documents | No Tenant B chunks returned |
| Tenant A tries to access another tenant's cached answer | Cache isolation prevents access |
| An agent calls a tool using another tenant's identifier | Tool rejects the request |
| A user loses tenant membership | Subsequent access is denied |
| A retrieved document contains prompt-injection instructions | Instructions are treated as untrusted content |
| A model cites an unauthorized document | The result is rejected or safely regenerated |
| A background worker processes a queued job | The worker uses the job's verified tenant context |
| Logs or traces contain retrieved content | Access and retention controls prevent unintended disclosure |

These cases align with [what good guardrails do](./README.md#what-good-guardrails-do) (testable, fail safely), [robust cloud rules implementation](./guard-rails-robust-cloud-rules-implementation.md), and [data isolation strategies](./guardrails-data-isolation.md).

## Reference implementation

**[guardrails-strategies](https://github.com/CaioHAndradeLima/guardrails-strategies)** — One scenario per table row in `scenario_evaluation.py` / `data/test_use_cases.json`. Keys: `guard_rails_test_use_cases`, `scenarios.test_use_cases`.

Recommended gate: `ci-guardrails-eval` (`evaluate-pipeline` + `check-measure`). Coverage: [LAB_COVERAGE.md](https://github.com/CaioHAndradeLima/guardrails-strategies/blob/main/docs/LAB_COVERAGE.md) (14/14).

## See also

- [Safer architecture: tenant-scoped retrieval](./safer-architecture-tenant-scoped-retrieval.md)
- [Wrong architecture: shared retrieval](./wrong-architecture-shared-retrieval.md)
- [Guard-rails overview](./README.md)
