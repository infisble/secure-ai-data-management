# Evidence Matrix

This matrix connects engineering controls to public sources. It is designed for architecture review, security review, DPO review, and audit preparation.

## Source priority

Use primary sources first:

- Law and regulator pages: EU AI Act, EUR-Lex, European Commission, GDPR, EDPB, NIS2, DORA.
- Standards and public frameworks: NIST AI RMF, NIST GenAI Profile, ISO/IEC 42001, OWASP GenAI Security.
- Vendor implementation docs: OpenAI, Anthropic, AWS, Azure, Google Cloud.
- Research papers only when they explain emerging risks not yet covered by formal guidance.

## Control matrix

| Control | Why it exists | Implementation evidence | Sources |
| --- | --- | --- | --- |
| Risk classification | AI Act obligations depend on the system's use, affected persons, and risk level. | Risk memo, intended purpose, high-risk analysis, owner approval. | [European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [EU AI Act text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) |
| Data minimization | Personal data should be limited to what is necessary for the purpose. | Field-level prompt schema, redaction tests, retrieval allowlist. | [GDPR Article 5](https://gdpr-info.eu/art-5-gdpr/), [EDPB AI models opinion](https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en) |
| Human oversight | High-risk and high-stakes contexts need meaningful human control. | Approval UI, reviewer role, override path, sampled decisions. | [European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [OpenAI safety best practices](https://platform.openai.com/docs/guides/safety-best-practices) |
| Prompt injection defense | Prompt injection can cause unauthorized tool use, data leakage, and compromised decisions. | Adversarial evals, tool policy gateway, untrusted-content labels. | [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/), [Azure Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection), [Anthropic jailbreak mitigation](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) |
| Sensitive output blocking | Model outputs can expose personal, confidential, or restricted data. | Output scanner, redaction, audit record of blocks. | [OWASP LLM06 Sensitive Information Disclosure](https://owasp.org/www-project-top-10-for-large-language-model-applications/), [AWS Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) |
| ACL-aware RAG | Retrieval can leak data when indexes ignore tenant, branch, user, or document permissions. | Metadata filters, post-filter tests, tenant isolation tests. | [OWASP LLM01 Prompt Injection](https://owasp.org/www-project-top-10-for-large-language-model-applications/), [OpenAI safety best practices](https://platform.openai.com/docs/guides/safety-best-practices) |
| Tool least privilege | Agents with broad tools can take unintended or unauthorized actions. | Tool registry, side-effect classification, policy tests. | [OWASP LLM07 Insecure Plugin Design](https://owasp.org/www-project-top-10-for-large-language-model-applications/), [OWASP LLM08 Excessive Agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| Evaluation and red teaming | Static review cannot predict all adversarial or edge-case behavior. | Eval suite, red-team report, release threshold. | [OpenAI evals](https://platform.openai.com/docs/guides/evals), [OpenAI safety best practices](https://platform.openai.com/docs/guides/safety-best-practices), [Microsoft Foundry observability](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai) |
| Observability | Teams need traces, metrics, and alerts to detect drift, abuse, and quality failures. | Dashboards, alert rules, trace sampling, incident playbook. | [Microsoft Foundry observability](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) |
| Provider/model gateway | Direct model calls bypass policy, retention, region, and audit controls. | Model registry, allowlist, region routing, data-use contract review. | [OpenAI production/safety docs](https://platform.openai.com/docs/guides/safety-best-practices), [AWS Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html), [Azure Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) |
| Incident response | Serious incidents may require technical rollback, user remediation, and regulatory assessment. | Runbook, kill switch, notification workflow, regression eval. | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) |

## Evidence reviewers should request

- Architecture diagram and data-flow diagram.
- Data inventory: source, owner, classification, lawful basis, retention.
- Tool registry with side-effect level and approval policy.
- RAG index metadata schema and ACL test results.
- Model/provider registry with approved regions and retention settings.
- Evaluation report with prompt injection, leakage, and excessive-agency tests.
- Human approval screenshots or workflow evidence.
- Audit log sample with redacted payloads.
- Incident response dry-run record.
