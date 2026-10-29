# MCP — native tools vs servers

When agents should expose or consume capabilities through **Model Context Protocol (MCP) servers** versus **in-process native tools**, and how that fits a vendor-agnostic platform.

## Prerequisites

- [Agent platform starter-kit primitives](./agent-platform-starter-kit-primitives.md)
- [Agent lifecycle internals](./agent-lifecycle-internals.md)

## Core idea

**MCP** standardizes how a host discovers resources, prompts, and tools from a separate process or service. **Native tools** are functions registered directly in the agent runtime. Both can appear as the same `ToolSpec` to the model if the platform normalizes schemas and execution behind one executor interface.

## How MCP fits the stack

```
Agent host (your SDK)                MCP server (optional)
---------------------                ----------------------
Tool registry  ←── discover ──→     tools/list, resources/read
Hook pipeline                        isolated credentials
Unified invoke_tool() ──transport──→ JSON-RPC / stdio / SSE
```

The host remains responsible for **authz, hooks, tracing, and budgets**—MCP does not replace [secure tool execution](../output/output-secure-tool-execution-flow.md) or [guardrails](../guard-rails/guardrails-strategy.md).

## When to use native tools

| Signal | Native in-process tool |
|--------|-------------------------|
| Low latency, same trust zone | DB read inside your service |
| Tight coupling to session state | Needs current `AgentRun` context |
| Simple, stable schema | Few parameters, no separate deployable |
| Shared memory with orchestration | Graph state updates in same process |

Implement as registered executors behind the platform `ToolExecutor`; still run pre/post-tool hooks.

## When to use MCP servers

| Signal | MCP server |
|--------|------------|
| Separate team owns the capability | CRM, ticketing, internal data product |
| Different release cycle or language | Python agent host, Go MCP tool service |
| Credential isolation | Server holds OAuth tokens; host never sees secrets |
| Reuse across hosts | Same MCP server for IDE, CLI, and production agent |
| Sandboxing | Untrusted or experimental tools in a restricted process |

Prefer MCP when the capability is a **product boundary**, not when it is a one-line helper.

## Hybrid pattern (common in platforms)

1. **Core tools** native: auth checks, internal APIs, retrieval, payment initiation stubs.
2. **Domain integrations** via MCP: third-party systems and slowly changing tool surfaces.
3. **Single registry** merges native and MCP-discovered tools with unified naming and versioning.
4. **Capability flags** per tenant: which MCP servers are enabled ([tenant-scoped retrieval](../guard-rails/safer-architecture-tenant-scoped-retrieval.md)).

## Native vs MCP — trade-offs

| Dimension | Native tools | MCP servers |
|-----------|--------------|-------------|
| Latency | Lower | Extra hop + serialization |
| Ops | Deploy with agent | Separate health checks, versioning |
| Security | Same process = shared blast radius | Smaller credential scope |
| Testing | Unit test executors | Contract tests + integration |
| Discovery | Static registration | Dynamic `tools/list` |

## Interview framing

- **Expose** capabilities: your platform can publish an MCP server so other teams’ agents consume your APIs with a standard contract—document tools, not ad-hoc REST wrappers in prompts.
- **Consume** capabilities: MCP adapters plug into the same hook pipeline as native tools; the model should not know transport details.
- **Do not** move authz into MCP alone— the host enforces principal, tenant, and approval before forwarding calls.

## Practical checklist

- [ ] One `invoke_tool` path for native and MCP; shared validation and audit fields.
- [ ] Pin MCP server versions in config; handle `tools/list` drift on deploy.
- [ ] Timeouts, circuit breakers, and retries at the host transport layer ([production components](../deployment/production-components.md)).
- [ ] Redact MCP payloads in traces; avoid logging secrets from `resources/read`.
- [ ] Integration tests for each enabled MCP server in CI golden tasks.

## See also

- [Agent platform starter-kit primitives](./agent-platform-starter-kit-primitives.md)
- [Output secure tool execution flow](../output/output-secure-tool-execution-flow.md)
- [Example Python directories — `tools/` and `adapters/`](./multi-agent-architecture/example-python-directories.md)

## References

- [Model Context Protocol specification](https://modelcontextprotocol.io/)
