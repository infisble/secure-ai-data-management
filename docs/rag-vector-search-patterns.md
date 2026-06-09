# RAG and Vector Search Patterns

## Secure pattern

```bash
python examples/secure-agent/secure_rag.py
```

The secure example uses a tiny local vectorizer only to show the control flow:

- Filter by tenant and branch before ranking.
- Exclude restricted data.
- Redact retrieved text before it enters model context.
- Return source IDs so outputs can cite evidence.

## Unsafe pattern

```bash
python examples/anti-patterns/insecure_rag.py
```

The unsafe example searches a global list of documents without tenant, branch, role, or data-class filters.

## Production guidance

- Store ACL metadata with every chunk.
- Use pre-filtering and post-filtering.
- Do not mix tenants in a vector index unless filters are mandatory and tested.
- Re-check permissions at answer time.
- Keep source lineage: document ID, chunk ID, ingestion time, owner, classification.
- Treat retrieved text as untrusted content; it can contain prompt injection.
