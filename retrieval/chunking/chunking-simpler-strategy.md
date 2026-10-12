# Chunking simpler strategy

A **fixed-size window** with overlap: split long text into passages small enough for precise retrieval, with shared boundary tokens so facts split across cuts still appear whole in at least one chunk.

## Example parameters

For a **~1,000 token** document (illustrative):

| Setting | Value |
|---------|--------|
| Chunk size | 200 tokens |
| Overlap | 40 tokens |
| Step (stride) | 160 tokens (`size − overlap`) |

### Illustrative token positions

```
Chunk 1     [||||||||||||||||||||]  tokens 0–199
Chunk 2          [||||||||||||||||||||]  tokens 160–359
                      ^^^^^ overlap (40)
Chunk 3               [||||||||||||||||||||]  tokens 320–519
                           ^^^^^ overlap (40)
```

Each chunk spans **200** consecutive tokens; the next chunk starts **160** tokens after the previous start, so tokens **160–199** appear in both chunk 1 and chunk 2 (and similarly between 2 and 3).

## Trade-offs

| Choice | Advantage | Risk |
|--------|-----------|------|
| **Small chunks** | More precise retrieval | May lose context |
| **Large chunks** | Preserve more context | Can retrieve irrelevant information |
| **More overlap** | Preserves boundary information | More duplicated text, embeddings, and storage |
| **Less overlap** | Lower cost and less redundancy | More facts may be split across boundaries |

Tune with [ingestion observability](../ingestion/ingestion-observability.md) (**Recall@K**, duplicate chunk rate) and golden questions—not defaults alone.

## Python example (LangChain)

`RecursiveCharacterTextSplitter` measures **`chunk_size` and `chunk_overlap` in characters**, not tokens. Use it when you target a character budget; for token budgets, use a tokenizer-aware splitter or multiply by a rough chars-per-token ratio for your language.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,       # characters, not tokens
    chunk_overlap=250,
    add_start_index=True,
)

chunks = splitter.create_documents(
    [document_text],
    metadatas=[{
        "document_id": "doc_123",
        "tenant_id": "tenant_a",
    }],
)
```

**Mapping the 200-token / 40-token idea:** if ~4 characters per token (English prose, rough), `200 × 4 ≈ 800` characters and `40 × 4 ≈ 160` character overlap—still validate on your corpus. `add_start_index=True` helps map chunks back to offsets for citations.

Always persist **`tenant_id`** (and document ACL fields) on chunk metadata for filtered vector search ([guard-rails](../../guard-rails/safer-architecture-tenant-scoped-retrieval.md)).

## See also

- [Chunking recursive structure-aware](./chunking-recursive-structure-aware.md)
- [Ingestion procedures — Chunking](../ingestion/ingestion-procedures.md)
- [Retrieval architecturing decisions — Chunking row](../retrieval-architecturing-decision-based.md)
- [Chunking overview](./README.md)
