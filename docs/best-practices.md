# Best Practices for Secure AI Agents

## 1. Start with governance, not prompts

Before prompt engineering, define:

- Business owner and technical owner.
- Allowed users, roles, and data domains.
- Explicit success criteria and failure criteria.
- Required evaluations before release.
- Whether outputs are advisory, decision-support, or action-taking.
- Which actions require human approval.
- Audit retention, incident response, and rollback process.

In regulated domains, an agent should be approved like a service account plus an application workflow, not like a chat prompt.

## 2. Classify data before it reaches the model

Use a data classification policy:

- `public`: safe to disclose externally.
- `internal`: company-confidential, no customer secrets.
- `confidential`: customer, employee, contract, or business-sensitive data.
- `restricted`: credentials, full account numbers, full card numbers, authentication data, regulated secrets.

Rules:

- Do not send `restricted` data to a model unless there is a documented exception and a contractually approved deployment boundary.
- Redact or tokenize identifiers before model calls.
- Retrieve the smallest sufficient set of fields.
- Keep raw source records out of prompts when a derived feature or summary is enough.
- Separate prompt logs from application logs and scrub both.

## 3. Separate trusted instructions from untrusted content

Agents often combine system instructions, user input, retrieved documents, emails, web pages, tickets, and tool outputs. Only system/developer policy and server-side code should control behavior.

Use these boundaries:

- Treat retrieved documents, user text, web pages, emails, PDFs, and tool output as untrusted data.
- Label untrusted content clearly.
- Never let retrieved content define tool permissions, approval rules, output destinations, or security policy.
- Prefer structured tool inputs over free-form command strings.
- Parse model output through schemas before using it downstream.

## 4. Least privilege for tools and connectors

Every tool should have:

- Stable name and owner.
- Purpose statement.
- Input schema.
- Output classification.
- Required role or attribute-based policy.
- Side-effect level: `read`, `write`, `customer-impacting`, `money-movement`, `admin`.
- Approval requirement.
- Rate limits and budget.
- Audit fields.

Avoid broad tools such as unrestricted SQL, unrestricted shell, unrestricted HTTP, or "send email to any address." If unavoidable, put them behind a policy gateway that validates every call.

## 5. Human approval for consequential actions

Require human approval for:

- Payments, transfers, refunds, card blocks, account closure.
- Customer communications sent externally.
- Credit, fraud, eligibility, compliance, or employment decisions.
- Permission changes.
- Deleting or exporting sensitive data.
- Any action combining external content with privileged tools.

Approval screens should show:

- Actor identity.
- Customer or account affected.
- Exact action and parameters.
- Data sources used.
- Risk flags.
- Diff from prior state.
- Reversible/irreversible status.

## 6. Guardrails are layered controls

Do not rely on a single prompt instruction. Combine:

- Pre-input checks: authentication, authorization, data minimization, PII redaction, malware/file validation.
- Retrieval checks: source allowlists, document classification, tenant filters, ACL-aware search.
- Runtime checks: tool policy enforcement, step limits, cost limits, approval gates.
- Output checks: sensitive data leakage detection, schema validation, citation/source checks.
- Human review for high-risk cases.
- Monitoring and incident response.

## 7. RAG and search must be ACL-aware

Retrieval can leak data if search indexes ignore row-level or document-level permissions.

Baseline controls:

- Index tenant IDs, data classification, owner, source system, and ACLs.
- Filter before vector search when possible; always filter after retrieval too.
- Never use one shared embedding index without metadata filters for multi-tenant or role-scoped data.
- Store document lineage and chunk IDs.
- Show citations and source metadata to reviewers.
- Re-run permission checks at answer time, not only at ingestion time.

## 8. Protect against prompt injection

Prompt injection is not solved by clever wording. Practical mitigations:

- Restrict what untrusted content can influence.
- Separate planning from untrusted-content summarization when possible.
- Do not expose privileged tools to the same model context that reads untrusted web/email/document content.
- Run tool calls through deterministic policy checks.
- Block instructions found in retrieved content from changing agent rules.
- Use adversarial tests with hidden instructions, malicious documents, and exfiltration attempts.

## 9. Avoid excessive agency

An agent should not be able to freely chain tools until it finds a path around policy.

Set:

- Maximum tool-call count.
- Maximum wall-clock time.
- Maximum data rows/chunks read.
- Maximum cost.
- Explicit stop conditions.
- Per-step authorization.
- Approval gates before side effects.

## 10. Logging and observability

Log enough to investigate without creating a second data leak.

Recommended audit event fields:

- `request_id`, `session_id`, `actor_id`, `actor_role`.
- `agent_id`, `agent_version`, `policy_version`, `model`.
- `data_classes_accessed`.
- `retrieval_sources`.
- `tool_name`, `tool_args_hash`, `tool_side_effect_level`.
- `approval_id`, if applicable.
- `decision`, `denial_reason`, `risk_flags`.

Do not log raw full card numbers, full account numbers, credentials, auth tokens, or unnecessary customer records.

## 11. Evaluation before release

Minimum eval suite:

- Normal business workflows.
- Boundary-role tests: teller, analyst, manager, auditor, admin.
- Tenant isolation tests.
- Prompt injection tests.
- Sensitive-data leakage tests.
- Tool misuse tests.
- Insecure output handling tests.
- Hallucination and citation tests.
- Refusal tests for prohibited tasks.
- Cost and rate-limit tests.

Every production incident should add a regression eval.

## 12. Banking-specific controls

For banking-like environments:

- Use strong customer and employee identity binding.
- Scope every query to a customer, account, case, and purpose.
- Separate advisory outputs from regulated decisions.
- Record model-assisted decision provenance.
- Keep explainability artifacts for credit/fraud/compliance workflows.
- Never allow autonomous money movement.
- Never allow direct customer-facing messages without policy and approval for high-risk contexts.
- Route suspicious activity, fraud, sanctions, and complaints through existing regulated workflows.

## 13. Anti-patterns

Avoid:

- "Give the agent database access and tell it not to leak."
- Sending entire customer profiles when only one field is needed.
- Logging full prompts with PII.
- Letting retrieved documents override system instructions.
- Using one global vector index without ACL filters.
- Allowing free-form shell, SQL, HTTP, or email tools.
- Letting the model decide whether approval is needed.
- Treating redaction as the only security control.
- Shipping without adversarial tests.
