# AI Agent Release Checklist

- [ ] Owner and approver are assigned.
- [ ] Use case, scope, and prohibited actions are documented.
- [ ] Data classes and source systems are documented.
- [ ] Data minimization is implemented.
- [ ] RBAC/ABAC checks are implemented server-side.
- [ ] Tool registry entries exist for every tool.
- [ ] Tool calls are schema-validated.
- [ ] Side-effect tools require deterministic approval checks.
- [ ] RAG retrieval is ACL-aware.
- [ ] Prompt injection tests pass.
- [ ] Sensitive-data leakage tests pass.
- [ ] Tenant isolation tests pass.
- [ ] Output validation is implemented.
- [ ] Audit logging is implemented and redacted.
- [ ] Monitoring dashboards and alert routes exist.
- [ ] Rollback and kill-switch are tested.
- [ ] Legal/compliance/security review is complete.
