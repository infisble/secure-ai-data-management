# Tool Permission Policy Template

Each tool must be registered before use.

Required fields:

- Tool name.
- Owner.
- Description.
- Input schema.
- Output schema and data classification.
- Allowed roles.
- Allowed purposes.
- Side-effect level: `read`, `write`, `customer-impacting`, `money-movement`, `admin`.
- Approval requirement.
- Rate limit.
- Timeout.
- Audit fields.

Default deny rules:

- Deny unregistered tools.
- Deny role mismatch.
- Deny purpose mismatch.
- Deny access to restricted data without exception.
- Deny side-effect actions without approval.
- Deny external egress unless destination is allowlisted.
