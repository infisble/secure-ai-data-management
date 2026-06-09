# LLM Provider Gateway

A regulated environment should call models through a gateway, not directly from application code.

## Secure pattern

```bash
python examples/secure-agent/llm_gateway.py
```

The example demonstrates:

- Model allowlist.
- Redaction before model call.
- Output sensitive-data check.
- One place to add retention, logging, provider routing, and regional controls.

## Gateway responsibilities

- Enforce approved model/provider list.
- Attach data classification and purpose metadata.
- Apply redaction/tokenization policies.
- Enforce regional routing where required.
- Apply prompt and output logging rules.
- Add rate limits and budgets.
- Record model version and policy version.
- Block unsupported use cases.

## What not to do

- Do not let each service call arbitrary external model endpoints.
- Do not pass raw customer records as prompts.
- Do not use provider defaults without reviewing data retention and training settings.
- Do not hide model calls from audit and DPO/security review.
