import math
from dataclasses import dataclass

from policy import User
from redaction import redact


@dataclass(frozen=True)
class Document:
    doc_id: str
    tenant_id: str
    branch_id: str
    data_class: str
    text: str


DOCUMENTS = [
    Document("doc-1", "bank-pl", "PL-WAW-01", "confidential", "Duplicate ATM fee process for Warsaw customers."),
    Document("doc-2", "bank-pl", "PL-KRK-01", "confidential", "Krakow mortgage escalation path includes ACCT-888888888."),
    Document("doc-3", "bank-de", "DE-BER-01", "confidential", "Berlin account closure process."),
]


def vectorize(text: str) -> dict[str, float]:
    vector: dict[str, float] = {}
    for token in text.lower().replace(".", "").replace(",", "").split():
        vector[token] = vector.get(token, 0.0) + 1.0
    return vector


def cosine(left: dict[str, float], right: dict[str, float]) -> float:
    keys = set(left) | set(right)
    dot = sum(left.get(key, 0.0) * right.get(key, 0.0) for key in keys)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)


def search_documents(query: str, user: User, tenant_id: str, limit: int = 2) -> list[dict]:
    query_vector = vectorize(query)
    authorized_docs = [
        doc for doc in DOCUMENTS
        if doc.tenant_id == tenant_id
        and (doc.branch_id == user.branch_id or user.role == "auditor")
        and doc.data_class != "restricted"
    ]
    ranked = sorted(
        authorized_docs,
        key=lambda doc: cosine(query_vector, vectorize(doc.text)),
        reverse=True,
    )
    return [
        {"doc_id": doc.doc_id, "text": redact(doc.text), "score": round(cosine(query_vector, vectorize(doc.text)), 4)}
        for doc in ranked[:limit]
    ]


if __name__ == "__main__":
    teller = User(user_id="u-123", role="teller", branch_id="PL-WAW-01")
    print(search_documents("ATM fee escalation", teller, tenant_id="bank-pl"))
