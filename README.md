# Agent Governance Playbook

Practical repository for designing, reviewing, and testing AI agents in regulated environments such as banking, insurance, healthcare, legal operations, and enterprise data platforms.

This repository is intentionally vendor-neutral. It summarizes operational practices from OpenAI, Anthropic, OWASP, NIST, and financial-sector risk guidance, then turns them into checklists and runnable examples.

## What is inside

- `docs/best-practices.md` - consolidated guidance for agent design, data protection, access control, guardrails, evaluations, and operations.
- `docs/banking-reference-architecture.md` - reference architecture for customer-data-heavy workflows.
- `docs/threat-model.md` - threat model for agents, tools, RAG, connectors, and audit trails.
- `docs/eu-ai-data-governance.md` - EU AI Act, GDPR, and data-governance mapping for agentic systems.
- `docs/evaluation-strategy.md` - what to test before release and in production.
- `docs/operations-runbook.md` - daily/weekly operations, kill switch, and incident triage.
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

## Non-goals

This repo is not legal advice, compliance certification, or a complete production framework. Use it as a starting point for internal security architecture, engineering standards, and audits.
