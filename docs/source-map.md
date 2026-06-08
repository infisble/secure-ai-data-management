# Source Map

This repository was created from public guidance available as of June 2026. The key sources to re-check during future updates are:

- OpenAI API docs: Agents SDK, guardrails, production best practices, safety best practices, structured outputs, function/tool calling, evaluations, and red teaming.
- Anthropic Claude docs: prompt engineering overview, prompting best practices, evaluations, guardrails, jailbreak mitigation, prompt leak reduction, tool use, and enterprise/security documentation.
- OWASP GenAI Security / Top 10 for LLM Applications: prompt injection, sensitive information disclosure, insecure plugin/tool design, excessive agency, overreliance, and supply chain risks.
- NIST AI Risk Management Framework and NIST AI 600-1 Generative AI Profile: governance, mapping, measurement, management, and generative-AI-specific risk actions.
- U.S. banking supervisory risk-management guidance such as Federal Reserve/OCC/FDIC third-party risk management principles and model risk management principles.

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
- GDPR Article 22: https://gdpr-info.eu/art-22-gdpr/
- EDPB Opinion 28/2024 on AI models and personal data: https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en

## How to use this map

For an internal standard, convert each source into controls:

- Control statement.
- Owner.
- Evidence expected in review.
- Test case.
- Production monitoring signal.

Keep source links in the internal GRC system so standards can be refreshed when vendor docs or regulatory guidance changes.
