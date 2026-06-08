from dataclasses import dataclass

from redaction import contains_sensitive, redact


@dataclass(frozen=True)
class LLMRequest:
    task: str
    context: str
    model: str = "approved-frontier-model"


APPROVED_MODELS = {"approved-frontier-model", "approved-small-model"}


def mock_model_call(task: str, context: str, model: str) -> str:
    return f"[{model}] Draft answer for task '{task}' using context: {context}"


def call_llm(request: LLMRequest) -> str:
    if request.model not in APPROVED_MODELS:
        raise PermissionError("model_not_approved")

    safe_context = redact(request.context)
    response = mock_model_call(request.task, safe_context, request.model)

    if contains_sensitive(response):
        raise ValueError("sensitive_output_blocked")

    return response


if __name__ == "__main__":
    request = LLMRequest(
        task="Draft an internal case summary",
        context="Customer anna@example.com reports duplicate fee on ACCT-123456789.",
    )
    print(call_llm(request))
