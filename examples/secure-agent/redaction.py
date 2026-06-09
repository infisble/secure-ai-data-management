import re


PATTERNS = [
    ("card", re.compile(r"\b(?:\d[ -]*?){13,19}\b")),
    ("ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("email", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("account", re.compile(r"\bACCT-[0-9]{6,12}\b")),
]


def redact(text: str) -> str:
    redacted = text
    for label, pattern in PATTERNS:
        redacted = pattern.sub(f"[REDACTED_{label.upper()}]", redacted)
    return redacted


def contains_sensitive(text: str) -> bool:
    return any(pattern.search(text) for _, pattern in PATTERNS)
