def unsafe_sql_tool(model_generated_sql: str) -> str:
    return f"Executing SQL without validation: {model_generated_sql}"


def unsafe_email_tool(to: str, body: str) -> str:
    return f"Sending email to {to}: {body}"


if __name__ == "__main__":
    print(unsafe_sql_tool("SELECT * FROM customers"))
    print(unsafe_email_tool("external@example.com", "Attached: full customer export"))
