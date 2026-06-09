# AI Agent Design Review

## Questions

- What customer or business decision can this agent influence?
- What data does it need, and what data can be removed?
- Which tool calls can change state?
- Who approves high-risk actions?
- What is the maximum blast radius of one compromised session?
- Can retrieved content influence policy or tool permissions?
- Can a user access another customer, tenant, branch, or region?
- What happens when the model is wrong?
- What logs are needed, and what logs would be dangerous?

## Required artifacts

- Architecture diagram.
- Data flow diagram.
- Threat model.
- Tool permission table.
- Evaluation report.
- Rollback plan.
