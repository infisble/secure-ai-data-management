# AI Agent Incident Response Checklist

- [ ] Identify agent ID, version, policy version, model, and provider.
- [ ] Disable affected side-effect tools.
- [ ] Preserve audit logs under incident-retention rules.
- [ ] Determine whether personal data, restricted data, or customer-impacting actions were involved.
- [ ] Identify affected users/customers/tenants.
- [ ] Review prompt injection, tool misuse, retrieval leakage, and model-output failure paths.
- [ ] Notify security, legal, DPO, compliance, and business owner.
- [ ] Determine regulatory notification duties.
- [ ] Patch policy, prompt, retrieval, or tool gateway.
- [ ] Add regression evals before re-enabling.
- [ ] Document root cause and residual risk.
