# Evaluation Strategy

Agent evaluation should combine deterministic tests, adversarial tests, and production monitoring.

## Local demo

```bash
python examples/secure-agent/eval_runner.py
```

The demo checks whether core controls respond to:

- Prompt injection in retrieved content.
- Sensitive data in context.
- Wrong-branch access.
- Unapproved model routing.

## Production eval categories

- Golden path business tasks.
- Role and tenant isolation.
- Prompt injection and jailbreak attempts.
- Sensitive-data disclosure.
- Tool misuse and excessive agency.
- RAG citation and source correctness.
- Output schema validity.
- Human approval enforcement.
- Cost, latency, and denial-of-service boundaries.

## Release rule

No high-risk agent release should depend only on manual review. Every approved risk scenario should have at least one automated regression test and one monitoring signal.
