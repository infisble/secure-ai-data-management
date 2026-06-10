import json
import pathlib

from llm_gateway import LLMRequest, call_llm
from policy import ToolRequest, User, authorize
from redaction import redact


ROOT = pathlib.Path(__file__).resolve().parents[1]


def run_eval_cases() -> list[dict]:
    cases = json.loads((ROOT / "eval_cases.json").read_text(encoding="utf-8"))
    results = []

    for case in cases:
        control = case["expected_control"]
        passed = False

        if control == "redaction_before_model":
            passed = "ACCT-" not in redact(case["input"]) and "anna@example.com" not in redact(case["input"])
        elif control == "branch_scope_mismatch":
            user = User("u-1", "teller", "PL-WAW-01")
            request = ToolRequest("summarize_transactions", "customer_service", "PL-KRK-01", "read", ("confidential",))
            passed = authorize(user, request)[1] == "branch_scope_mismatch"
        elif control == "model_not_approved":
            try:
                call_llm(LLMRequest("summarize", case["input"], "unknown-external-model"))
            except PermissionError as error:
                passed = str(error) == "model_not_approved"
        elif control == "tool_policy_blocks_export":
            user = User("u-1", "teller", "PL-WAW-01")
            request = ToolRequest("export_all_accounts", "customer_service", "PL-WAW-01", "admin", ("confidential",))
            passed = not authorize(user, request)[0]

        results.append({"name": case["name"], "passed": passed, "control": control})

    return results


if __name__ == "__main__":
    for result in run_eval_cases():
        status = "PASS" if result["passed"] else "FAIL"
        print(f"{status} {result['name']} {result['control']}")
