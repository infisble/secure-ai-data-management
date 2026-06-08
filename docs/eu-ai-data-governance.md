# EU AI and Data Governance for Agentic Systems

This document maps practical engineering controls to EU regulatory themes. It is not legal advice; use it as a technical checklist for legal, DPO, security, and product review.

## Key EU regimes to consider

- EU AI Act, Regulation (EU) 2024/1689: risk-based AI obligations for providers and deployers.
- GDPR: personal data processing, lawful basis, data minimization, transparency, security, data subject rights, and automated decision-making constraints.
- NIS2: cybersecurity governance and incident handling for covered sectors.
- Data Act and Data Governance Act: data access, sharing, and governance obligations in relevant contexts.
- Cyber Resilience Act: product cybersecurity obligations where applicable.
- Sector rules: banking, credit, AML, consumer protection, outsourcing, model risk, and operational resilience.

## EU AI Act mapping for agents

Agentic systems should be classified by what they do, not only by which model they call.

| Agent capability | Possible EU AI Act concern | Engineering control |
| --- | --- | --- |
| Customer chatbot | Transparency duties if users interact with AI | Clear AI disclosure and handoff path |
| Credit scoring or loan eligibility | High-risk: access to essential private services | Risk management, data governance, logs, human oversight |
| Fraud triage | Possible high-risk or regulated decision support | Human review, explainability, auditability |
| Employee monitoring or ranking | High-risk employment/workplace context | Strict role governance and fundamental-rights review |
| Biometric identification | High-risk or prohibited depending use | Avoid unless explicitly approved by legal and compliance |
| Autonomous account action | Excessive agency and customer-impacting risk | Deterministic policy, approval, rollback, logs |

## High-risk obligations translated to controls

For high-risk or likely-high-risk use cases, implement:

- Risk management system: documented hazards, controls, residual risk, release gates.
- Data governance: representative data, bias checks, provenance, quality controls, access controls.
- Technical documentation: architecture, data flows, intended purpose, model/provider details, limitations.
- Logging: traceability for inputs, outputs, tool calls, approvals, incidents.
- Transparency to deployers/users: clear instructions, limitations, expected human role.
- Human oversight: reviewer workflow, authority to override, escalation paths.
- Robustness, accuracy, cybersecurity: adversarial testing, monitoring, access control, incident response.
- Post-market monitoring: production metrics, drift checks, incident reporting, regression evals.

## GDPR mapping

For personal data in prompts, retrieval, fine-tuning, logs, and outputs:

- Lawful basis: document why processing is allowed.
- Purpose limitation: bind every agent task to a purpose.
- Data minimization: send only fields needed for the task.
- Storage limitation: define retention for prompts, traces, embeddings, eval records, and audit logs.
- Transparency: explain AI involvement where required.
- Security: encrypt, restrict, monitor, and scrub logs.
- Data subject rights: support access, deletion, objection, and correction workflows where applicable.
- Automated decision-making: do not make solely automated legal or similarly significant decisions unless a legal route and safeguards exist.

## EU-oriented release gate

Before launch in the EU:

- Classify the system under the AI Act.
- Identify provider/deployer/importer/distributor roles.
- Map data categories and lawful bases under GDPR.
- Run a DPIA where personal-data risk is high.
- Run a fundamental rights impact assessment where required or prudent.
- Validate RAG retrieval respects EU data residency and access boundaries.
- Confirm model/provider contractual terms for data use, retention, and subprocessors.
- Confirm user disclosure and human escalation.
- Confirm incident reporting paths for security and serious AI incidents.
