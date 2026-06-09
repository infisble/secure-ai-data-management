# Database Access Patterns

## Secure pattern

Use a narrow server-side function for each business operation.

```bash
python examples/secure-agent/secure_db_access.py
```

What this demonstrates:

- Parameterized SQL.
- Explicit customer and branch scope.
- Role and purpose check before the query.
- Redaction before returning model-facing context.
- `LIMIT` to reduce accidental bulk disclosure.

## Unsafe pattern

```bash
python examples/anti-patterns/insecure_db_access.py
```

What this demonstrates:

- User prompt becomes SQL text.
- No role check.
- No tenant/customer/branch filter.
- Query could expand to all customers.

## Production guidance

- Prefer stored procedures or service-layer functions over raw SQL tools.
- Never expose unrestricted database consoles to an agent.
- Add row-level security in the database and enforce policy again in application code.
- Keep write operations separate from read operations.
- Require approval for irreversible writes.
