from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib
import json

from redaction import redact


@dataclass(frozen=True)
class AuditEvent:
    request_id: str
    actor_id: str
    actor_role: str
    agent_id: str
    policy_version: str
    tool_name: str
    tool_args: dict
    decision: str
    reason: str


def stable_hash(value: dict) -> str:
    encoded = json.dumps(value, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def serialize_event(event: AuditEvent) -> str:
    payload = asdict(event)
    payload["timestamp"] = datetime.now(timezone.utc).isoformat()
    payload["tool_args_hash"] = stable_hash(event.tool_args)
    payload["tool_args"] = redact(json.dumps(event.tool_args, sort_keys=True))
    return json.dumps(payload, sort_keys=True)
