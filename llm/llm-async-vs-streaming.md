# LLM async vs streaming

Two different ideas: **streaming** improves perceived latency for one generation; **async** lets the application do other work (or other requests) while I/O-bound steps run.

## Streaming

User sees tokens as the model produces them—lower **time to first token (TTFT)** ([latency measurement](./llm-latency-variables-measurement.md)).

```
Request -> LLM
             |
             +-> "Checkout"
             +-> " conversion"
             +-> " dropped"
             +-> " by 12%"
```

User sees output as it arrives.

## Async (concurrency)

Non-blocking waits on agents, tools, or provider APIs; the server can serve other traffic while operations are pending.

```
Async application
      |
      +--> Await Knowledge Agent
      |
      +--> Await Analytics Agent
      |
      +--> Handle other requests
           while operations are pending
```

Use **async** with **parallel** branches to reduce wall-clock time ([latency sample](./llm-latency-sample.md)). Streaming does not replace parallel retrieval or multi-agent fan-out—it only streams the **final** (or intermediate) model output.

| Pattern | Best for |
|---------|----------|
| **Streaming** | Chat UX, long answers, showing progress |
| **Async / parallel awaits** | Multiple tools or agents, high request concurrency |
| **Both** | Parallel evidence gathering, then stream synthesized answer |

Watch **timeout and cancellation**: abort streaming clients when the user navigates away; cancel pending agent tasks when the request is dropped.

## See also

- [LLM questions — streaming and async](./llm-questions.md)
- [LLM overview](./README.md)
