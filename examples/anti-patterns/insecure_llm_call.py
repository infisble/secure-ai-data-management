def call_any_model(model: str, raw_context: str) -> str:
    return f"Sending raw context to {model}: {raw_context}"


if __name__ == "__main__":
    print(call_any_model("unknown-external-model", "anna@example.com ACCT-123456789"))
