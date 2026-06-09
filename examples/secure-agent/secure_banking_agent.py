from audit import AuditEvent, serialize_event
from policy import ToolRequest, User, authorize
from redaction import redact


AGENT_ID = "secure-banking-agent-demo"
POLICY_VERSION = "2026-06-10"


def summarize_transactions(user: User, customer_branch_id: str, customer_text: str) -> str:
    request = ToolRequest(
        tool_name="summarize_transactions",
        purpose="customer_service",
        customer_branch_id=customer_branch_id,
        side_effect="read",
        data_classes=("confidential",),
    )
    allowed, reason = authorize(user, request)

    event = AuditEvent(
        request_id="demo-001",
        actor_id=user.user_id,
        actor_role=user.role,
        agent_id=AGENT_ID,
        policy_version=POLICY_VERSION,
        tool_name=request.tool_name,
        tool_args={"customer_branch_id": customer_branch_id, "customer_text": customer_text},
        decision="allow" if allowed else "deny",
        reason=reason,
    )
    print(serialize_event(event))

    if not allowed:
        raise PermissionError(reason)

    safe_context = redact(customer_text)
    return f"Customer summary based on minimized context: {safe_context}"


if __name__ == "__main__":
    user = User(user_id="u-123", role="teller", branch_id="PL-WAW-01")
    raw_customer_context = (
        "Customer anna@example.com has account ACCT-123456789 and card "
        "4111 1111 1111 1111. Recent visible issue: duplicate ATM fee."
    )
    print(summarize_transactions(user, "PL-WAW-01", raw_customer_context))
