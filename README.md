# Agent Governance Playbook

Practical repository for designing, reviewing, and testing AI agents in regulated environments such as banking, insurance, healthcare, legal operations, and enterprise data platforms.

This repository is intentionally vendor-neutral. It summarizes operational practices from OpenAI, Anthropic, OWASP, NIST, and financial-sector risk guidance, then turns them into checklists and runnable examples.

Every major recommendation should be traceable to a public source. Start with:

- [docs/evidence-matrix.md](docs/evidence-matrix.md) - control-by-control source matrix.
- [docs/diagrams.md](docs/diagrams.md) - Mermaid architecture, data-flow, approval, RAG, and incident diagrams.
- [docs/eu-regulatory-map.md](docs/eu-regulatory-map.md) - EU AI Act, GDPR, NIS2, DORA, Data Act, Data Governance Act, and banking implications.
- [docs/cloud-guardrails.md](docs/cloud-guardrails.md) - cloud/provider guardrails and where they do and do not help.
- [docs/source-map.md](docs/source-map.md) - curated primary source links.

## What is inside

- `docs/best-practices.md` - consolidated guidance for agent design, data protection, access control, guardrails, evaluations, and operations.
- `docs/banking-reference-architecture.md` - reference architecture for customer-data-heavy workflows.
- `docs/threat-model.md` - threat model for agents, tools, RAG, connectors, and audit trails.
- `docs/eu-ai-data-governance.md` - EU AI Act, GDPR, and data-governance mapping for agentic systems.
- `docs/evaluation-strategy.md` - what to test before release and in production.
- `docs/operations-runbook.md` - daily/weekly operations, kill switch, and incident triage.
- `docs/evidence-matrix.md` - recommended controls mapped to sources.
- `docs/cloud-guardrails.md` - AWS, Azure, OpenAI, Anthropic, and cloud control patterns.
- `docs/diagrams.md` - visual diagrams for reviewers and engineers.
- `docs/eu-regulatory-map.md` - EU-focused obligations and implementation artifacts.
- `docs/source-map.md` - source map and why each source matters.
- `policies/` - copyable policy templates for data classification, tool permissions, and human approval.
- `checklists/` - release and review checklists.
- `examples/secure-agent/` - runnable safe patterns: redaction, RBAC, policy checks, audit logging, database access, RAG/vector search, and LLM gateway.
- `examples/anti-patterns/` - runnable unsafe patterns showing what not to do with prompts, tools, databases, RAG, and model calls.
- `tests/run_all.py` - local test runner for examples.

## Quick start

Requires Python 3.10+ and no third-party dependencies.

```bash
python tests/run_all.py
python examples/secure-agent/secure_banking_agent.py
python examples/secure-agent/secure_db_access.py
python examples/secure-agent/secure_rag.py
python examples/secure-agent/llm_gateway.py
python examples/secure-agent/eval_runner.py
python examples/anti-patterns/insecure_agent.py
```

Expected result: secure examples redact sensitive values and block unauthorized actions; anti-pattern examples show how data leaks happen when raw prompts, broad tools, or unscoped retrieval are used.

## Core principle

Treat every AI agent as a privileged software actor:

- It needs identity, role, scope, audit, and least privilege.
- It must never receive more customer data than the current task requires.
- It must not execute irreversible or customer-impacting actions without deterministic policy checks and human approval.
- It needs continuous evaluation against prompt injection, sensitive data disclosure, excessive agency, insecure output handling, and overreliance.

## How to read this repository

1. Read [docs/eu-regulatory-map.md](docs/eu-regulatory-map.md) if the system touches EU customers, employees, financial services, credit, fraud, identity, or essential services.
2. Read [docs/evidence-matrix.md](docs/evidence-matrix.md) to understand why each control exists and which source supports it.
3. Review [docs/diagrams.md](docs/diagrams.md) with architecture, security, legal, and data-protection reviewers.
4. Run the examples in [docs/command-cookbook.md](docs/command-cookbook.md).
5. Use the checklists before release and after incidents.

## Non-goals

This repo is not legal advice, compliance certification, or a complete production framework. Use it as a starting point for internal security architecture, engineering standards, and audits.
