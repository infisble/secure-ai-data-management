from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class User:
    user_id: str
    role: str
    branch_id: str


@dataclass(frozen=True)
class ToolRequest:
    tool_name: str
    purpose: str
    customer_branch_id: str
    side_effect: str
    data_classes: tuple[str, ...]
    approved: bool = False


ROLE_PURPOSES = {
    "teller": {"customer_service"},
    "fraud_analyst": {"fraud_review", "customer_service"},
    "auditor": {"audit"},
}

ROLE_TOOLS = {
    "teller": {"summarize_transactions"},
    "fraud_analyst": {"summarize_transactions", "draft_case_note"},
    "auditor": {"read_audit_log"},
}

RESTRICTED_CLASSES = {"restricted"}
SIDE_EFFECTS_REQUIRING_APPROVAL = {"customer-impacting", "money-movement", "admin"}


def authorize(user: User, request: ToolRequest) -> tuple[bool, str]:
    if request.purpose not in ROLE_PURPOSES.get(user.role, set()):
        return False, "purpose_not_allowed_for_role"

    if request.tool_name not in ROLE_TOOLS.get(user.role, set()):
        return False, "tool_not_allowed_for_role"

    if user.branch_id != request.customer_branch_id and user.role != "auditor":
        return False, "branch_scope_mismatch"

    if RESTRICTED_CLASSES.intersection(request.data_classes):
        return False, "restricted_data_blocked"

    if request.side_effect in SIDE_EFFECTS_REQUIRING_APPROVAL and not request.approved:
        return False, "human_approval_required"

    return True, "allowed"


def require_all_authorized(user: User, requests: Iterable[ToolRequest]) -> None:
    for request in requests:
        allowed, reason = authorize(user, request)
        if not allowed:
            raise PermissionError(reason)
