# Chunking tools

Reference **tools** for splitting, parsing, token counting, and evaluating chunk configs—not a mandatory stack; pick per [chunking architecturing](./chunking-architecturing.md) strategy.

| Tool | Role | When I'd use it |
|------|------|-----------------|
| **LangChain text splitters** | Recursive and token-aware splitting | Fast baseline and experimentation |
| **LlamaIndex** | Document nodes, metadata and hierarchical parsing patterns | When its indexing abstractions fit your RAG application |
| **PyMuPDF** | PDF extraction and page-level information | Ordinary text-based PDFs |
| **Tokenizer from your model provider or model family** | Token counting | When chunk limits must be expressed in tokens |
| **Python evaluation scripts** | Compare configurations and calculate retrieval metrics | From the first prototype onward |

## Notes

- **LangChain** — see [chunking simpler strategy](./chunking-simpler-strategy.md) for `RecursiveCharacterTextSplitter`; prefer token-aware splitters when limits must match the **embedding or chat model** context window.
- **LlamaIndex** — pairs well with [hierarchical parent-child](./chunking-hierarchical-parent-child.md) node trees.
- **PyMuPDF** — upstream of chunking in [basic document ingestion](../ingestion/basic-document-ingestion.md); attach **page** metadata to chunks.
- **Eval scripts** — feed [ingestion observability](../ingestion/ingestion-observability.md) (Recall@K, duplicate chunk rate) when comparing splitter settings.

## See also

- [Chunking architecturing](./chunking-architecturing.md)
- [Ingestion — parser choices](../ingestion/basic-document-ingestion.md#what-does-each-component-do)
- [Chunking overview](./README.md)
