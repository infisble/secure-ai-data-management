import sqlite3
from dataclasses import dataclass

from policy import ToolRequest, User, authorize
from redaction import redact


@dataclass(frozen=True)
class CustomerScope:
    customer_id: str
    branch_id: str
    purpose: str


def build_demo_db() -> sqlite3.Connection:
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE transactions (
            id INTEGER PRIMARY KEY,
            customer_id TEXT NOT NULL,
            branch_id TEXT NOT NULL,
            description TEXT NOT NULL,
            amount_cents INTEGER NOT NULL
        )
        """
    )
    connection.executemany(
        "INSERT INTO transactions(customer_id, branch_id, description, amount_cents) VALUES (?, ?, ?, ?)",
        [
            ("cust-1", "PL-WAW-01", "ATM fee reversal for anna@example.com", -500),
            ("cust-1", "PL-WAW-01", "Grocery store", 12500),
            ("cust-2", "PL-KRK-01", "Wire transfer ACCT-999999999", 900000),
        ],
    )
    return connection


def list_transactions(connection: sqlite3.Connection, user: User, scope: CustomerScope) -> list[dict]:
    request = ToolRequest(
        tool_name="summarize_transactions",
        purpose=scope.purpose,
        customer_branch_id=scope.branch_id,
        side_effect="read",
        data_classes=("confidential",),
    )
    allowed, reason = authorize(user, request)
    if not allowed:
        raise PermissionError(reason)

    rows = connection.execute(
        """
        SELECT id, description, amount_cents
        FROM transactions
        WHERE customer_id = ? AND branch_id = ?
        ORDER BY id
        LIMIT 20
        """,
        (scope.customer_id, scope.branch_id),
    ).fetchall()

    return [
        {"id": row[0], "description": redact(row[1]), "amount_cents": row[2]}
        for row in rows
    ]


if __name__ == "__main__":
    db = build_demo_db()
    teller = User(user_id="u-123", role="teller", branch_id="PL-WAW-01")
    scope = CustomerScope(customer_id="cust-1", branch_id="PL-WAW-01", purpose="customer_service")
    print(list_transactions(db, teller, scope))
