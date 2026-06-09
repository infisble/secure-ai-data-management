# Command Cookbook

Run all local checks:

```bash
python tests/run_all.py
```

Run secure examples:

```bash
python examples/secure-agent/secure_banking_agent.py
python examples/secure-agent/secure_db_access.py
python examples/secure-agent/secure_rag.py
python examples/secure-agent/llm_gateway.py
```

Run anti-pattern examples:

```bash
python examples/anti-patterns/insecure_agent.py
python examples/anti-patterns/insecure_db_access.py
python examples/anti-patterns/insecure_rag.py
python examples/anti-patterns/insecure_llm_call.py
python examples/anti-patterns/unsafe_tool_access.py
```

Review git history with authored dates:

```bash
git log --pretty=format:"%h %ad %s" --date=short
```
