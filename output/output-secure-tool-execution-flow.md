# Secure tool execution flow

Tool calls proposed by the model are **untrusted** until policy, identity, and schema checks pass ([prompt injection](../prompting/prompt-injection.md), [reliable architecture](../contexting/context-reliable-architecture.md)).

```
LLM proposes tool call
       |
       v
Policy / guardrail check
       |
       v
Allowed?
       |
   No--+--> Block / log
       |
      Yes
       |
       v
Execute in sandbox with scoped credentials
       |
       v
Return bounded result
```

**Policy / guardrail check** includes tool allowlists, argument validation, tenant scope, rate limits, and sensitive-action rules—mirroring [guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md).

**Sandbox with scoped credentials** means short-lived, least-privilege tokens per tenant/user, no broad IAM from the model thread, and timeouts on external calls. **Bounded result** = truncate large payloads, redact secrets, and structured errors back to the model—not raw stack traces.

## See also

- [Prompt injection](../prompting/prompt-injection.md)
- [Reliable architecture](../contexting/context-reliable-architecture.md)
- [Guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md)
- [Validation failure impact](./output-validation-failure-impact.md)
- [Output overview](./README.md)
