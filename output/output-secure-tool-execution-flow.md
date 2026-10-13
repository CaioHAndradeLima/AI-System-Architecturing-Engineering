# Secure tool execution flow

Tool calls from the model are **untrusted** until validated, authorized, and executed with least privilege ([prompt injection](../prompting/prompt-injection.md), [reliable architecture](../contexting/context-reliable-architecture.md)).

```
LLM proposes a tool call
          |
          v
Validate tool name and arguments
          |
          v
Authenticate requesting identity
          |
          v
Authorize requested operation
          |
          v
Check business rules and limits
          |
          v
Approval required?
       /       \
     Yes        No
      |          |
      v          v
Human approval  Execute within
if granted      least privilege
       \         /
        v       v
       Record outcome
              |
              v
       Return bounded result
```

Do not **retry** the same unauthorized tool call automatically ([validation failure impact — unauthorized tool](./output-validation-failure-impact.md)). Test with [guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md).

## See also

- [Output overview](./README.md)
