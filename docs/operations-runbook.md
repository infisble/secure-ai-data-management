# Operations Runbook

## Daily checks

- Review deny-rate spikes.
- Review tool-call volume and unusual tool chains.
- Review sensitive-output blocks.
- Review unapproved-model attempts.
- Review retrieval queries returning empty or cross-scope results.

## Weekly checks

- Sample audit logs.
- Review human approval queues.
- Review model/provider changes.
- Review new data sources and connectors.
- Run adversarial eval suite.

## Kill switch

Every production agent should support:

- Disable model calls.
- Disable side-effect tools.
- Disable external egress.
- Force human review for all outputs.
- Roll back to previous prompt/policy/model version.

## Incident triage

1. Freeze affected agent version.
2. Preserve redacted audit logs and raw secure evidence in approved incident storage.
3. Identify affected users, customers, tools, and data classes.
4. Disable affected tools or connectors.
5. Add regression eval before re-enable.
