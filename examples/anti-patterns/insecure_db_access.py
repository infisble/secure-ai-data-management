def build_sql_from_prompt(user_prompt: str) -> str:
    return f"SELECT * FROM customers WHERE note LIKE '%{user_prompt}%'"


if __name__ == "__main__":
    print(build_sql_from_prompt("%' OR '1'='1"))
