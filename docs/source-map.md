# Source Map

This repository was created from public guidance available as of June 2026. The key sources to re-check during future updates are:

- OpenAI API docs: Agents SDK, guardrails, production best practices, safety best practices, structured outputs, function/tool calling, evaluations, and red teaming.
- Anthropic Claude docs: prompt engineering overview, prompting best practices, evaluations, guardrails, jailbreak mitigation, prompt leak reduction, tool use, and enterprise/security documentation.
- OWASP GenAI Security / Top 10 for LLM Applications: prompt injection, sensitive information disclosure, insecure plugin/tool design, excessive agency, overreliance, and supply chain risks.
- NIST AI Risk Management Framework and NIST AI 600-1 Generative AI Profile: governance, mapping, measurement, management, and generative-AI-specific risk actions.
- U.S. banking supervisory risk-management guidance such as Federal Reserve/OCC/FDIC third-party risk management principles and model risk management principles.
- European Union digital regulation relevant to AI systems, personal data, operational resilience, cloud, and data sharing.
- Cloud/provider guardrail documentation for implementation details.

## Direct source links

- OpenAI Agents SDK: https://platform.openai.com/docs/guides/agents
- OpenAI Safety best practices: https://platform.openai.com/docs/guides/safety-best-practices
- Anthropic prompt engineering overview: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- Anthropic reduce prompt leak: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 600-1 Generative AI Profile: https://www.nist.gov/itl/ai-risk-management-framework
- European Commission AI Act overview: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- EU AI Act text: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- European AI Office: https://digital-strategy.ec.europa.eu/en/policies/ai-office
- GDPR Article 22: https://gdpr-info.eu/art-22-gdpr/
- GDPR Article 5: https://gdpr-info.eu/art-5-gdpr/
- EDPB Opinion 28/2024 on AI models and personal data: https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en
- NIS2 Directive: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- DORA: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Data Governance Act: https://eur-lex.europa.eu/eli/reg/2022/868/oj
- Data Act: https://eur-lex.europa.eu/eli/reg/2023/2854/oj
- AWS Bedrock Guardrails: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html
- Azure Prompt Shields: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
- Microsoft Foundry observability: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai
- Anthropic jailbreak and prompt-injection mitigation: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
- OpenAI safety best practices: https://platform.openai.com/docs/guides/safety-best-practices
- OpenAI evals: https://platform.openai.com/docs/guides/evals

## How to use this map

For an internal standard, convert each source into controls:

- Control statement.
- Owner.
- Evidence expected in review.
- Test case.
- Production monitoring signal.

Keep source links in the internal GRC system so standards can be refreshed when vendor docs or regulatory guidance changes.
