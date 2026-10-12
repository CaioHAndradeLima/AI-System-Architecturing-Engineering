# Prompt injection

Defense-in-depth for **untrusted user input and retrieved documents**—from auth through delimiters, instructions, tools, and output checks.

```
Untrusted user input / retrieved documents
                  |
                  v
        Authentication and ACL checks
                  |
                  v
        Delimit untrusted evidence
                  |
                  v
        System instructions define task
                  |
                  v
        LLM interprets evidence
                  |
                  v
        Tool authorization and validation
                  |
                  v
        Output checks and safe response
```

## Practical measures

- Separate application instructions from retrieved content.
- Explicitly instruct the model to treat retrieved text as data.
- Never let retrieved text directly grant permissions or authorize tools.
- Validate tool arguments and enforce access controls outside the LLM.
- Avoid placing secrets in prompts.
- Test with adversarial documents and malicious user requests.

## Layer → guides

| Layer | Docs |
|-------|------|
| Authentication and ACL | [Metadata filtering](../retrieval/search/retrieval-strategy-metadata-filtering.md) · [Reliable architecture](../contexting/context-reliable-architecture.md) |
| Delimit evidence | [Prompt categories](./prompt-categories.md) · [Standard format — security](./prompt-standard-format.md) |
| System instructions | [Guard-rails strategy](../guard-rails/guard-rails-strategy.md) |
| Tool validation | [Analytical question](../contexting/context-analytical-question.md) · [Architecture evaluation — security](../retrieval/search/retrieval-architecture-evaluation.md) |
| Adversarial testing | [Guard-rails test use cases](../guard-rails/guard-rails-test-use-cases.md) · [AI controls](../guard-rails/) |

Prompting alone does not stop injection—**enforce** permissions and tool allowlists in application code ([architecturing decision — prompt injection row](../contexting/context-architecturing-decision-based.md)).

## See also

- [Prompting overview](./README.md)
