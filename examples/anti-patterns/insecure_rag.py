DOCUMENTS = [
    {"tenant_id": "bank-pl", "branch_id": "PL-WAW-01", "text": "Warsaw customer fee policy."},
    {"tenant_id": "bank-pl", "branch_id": "PL-KRK-01", "text": "Krakow VIP account ACCT-999999999."},
    {"tenant_id": "bank-de", "branch_id": "DE-BER-01", "text": "Berlin customer complaint."},
]


def global_rag_search(query: str) -> list[dict]:
    return [doc for doc in DOCUMENTS if query.lower() in doc["text"].lower()]


if __name__ == "__main__":
    print(global_rag_search("account"))
