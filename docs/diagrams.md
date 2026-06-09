# Diagrams

These diagrams use Mermaid so GitHub can render them directly in Markdown.

## Secure agent reference architecture

```mermaid
flowchart LR
    U[Authenticated user] --> APP[Banking app]
    APP --> PDP[Policy decision point]
    PDP --> IDP[Identity provider]
    PDP --> TR[Tool registry]
    APP --> RET[ACL-aware retrieval service]
    RET --> IDX[(Vector index with tenant ACL metadata)]
    RET --> DMS[Data minimization and redaction]
    DMS --> GW[LLM provider gateway]
    GW --> GR[Guardrails and output checks]
    GW --> M[Approved model/provider]
    GR --> APP
    APP --> APPR{Human approval?}
    APPR -->|No side effect| OUT[User-visible answer]
    APPR -->|Required| H[Reviewer queue]
    H --> TOOL[Policy-gated tool execution]
    TOOL --> SYS[(Core banking systems)]
    APP --> AUD[(Redacted audit log)]
    PDP --> AUD
    TOOL --> AUD
```

## EU governance lifecycle

```mermaid
flowchart TD
    IDEA[Use case idea] --> PURPOSE[Intended purpose]
    PURPOSE --> CLASSIFY[AI Act risk classification]
    CLASSIFY --> GDPR[GDPR lawful basis and DPIA decision]
    GDPR --> DATA[Data inventory and minimization]
    DATA --> ARCH[Architecture and threat model]
    ARCH --> EVAL[Adversarial evals and quality evals]
    EVAL --> REVIEW[Security, legal, DPO, compliance review]
    REVIEW --> DEPLOY[Controlled deployment]
    DEPLOY --> MON[Post-market monitoring and observability]
    MON --> INCIDENT[Incident response and regression evals]
    INCIDENT --> EVAL
```

## RAG security flow

```mermaid
sequenceDiagram
    participant User
    participant App
    participant Policy
    participant Search
    participant Index
    participant Redactor
    participant LLM

    User->>App: Ask scoped question
    App->>Policy: Check role, purpose, tenant, branch
    Policy-->>App: Allow/deny
    App->>Search: Query with mandatory filters
    Search->>Index: tenant_id + ACL + data_class filters
    Index-->>Search: Candidate chunks
    Search->>Policy: Re-check chunk access
    Search->>Redactor: Minimize and redact
    Redactor-->>App: Safe context + source IDs
    App->>LLM: Trusted instructions + untrusted context
    LLM-->>App: Draft answer
    App->>Policy: Output and tool policy checks
    App-->>User: Cited answer or refusal
```

## Tool approval flow

```mermaid
flowchart TD
    PLAN[Agent proposes tool call] --> SCHEMA[Schema validation]
    SCHEMA --> ROLE[Role and purpose check]
    ROLE --> DATA[Data-class check]
    DATA --> SIDE[Side-effect classification]
    SIDE --> APPROVAL{Approval required?}
    APPROVAL -->|No| EXEC[Execute narrow tool]
    APPROVAL -->|Yes| QUEUE[Human approval queue]
    QUEUE --> REVIEW[Reviewer sees exact params, sources, risk flags]
    REVIEW --> DECIDE{Approve?}
    DECIDE -->|No| DENY[Deny and log]
    DECIDE -->|Yes| EXEC
    EXEC --> AUDIT[Redacted audit event]
    DENY --> AUDIT
```

## Prompt injection boundary

```mermaid
flowchart LR
    SYS[Trusted system and developer policy] --> ORCH[Server-side orchestrator]
    USER[User input: untrusted] --> SAN[Input validation]
    DOC[Retrieved docs/email/web/PDF: untrusted] --> SAN
    TOOL[Tool output: untrusted unless verified] --> SAN
    SAN --> LABEL[Explicit untrusted-content labels]
    LABEL --> MODEL[Model]
    MODEL --> OUT[Structured output]
    OUT --> VERIFY[Deterministic policy verifier]
    VERIFY -->|Allowed| ACT[Answer or action]
    VERIFY -->|Denied| BLOCK[Block/refuse/escalate]
```

## Incident response flow

```mermaid
flowchart TD
    ALERT[Alert or user report] --> TRIAGE[Triage severity and data class]
    TRIAGE --> FREEZE[Freeze agent version and preserve evidence]
    FREEZE --> KILL[Disable affected tools/model route]
    KILL --> SCOPE[Identify users, tenants, data, systems]
    SCOPE --> LEGAL[Legal/DPO/compliance notification assessment]
    SCOPE --> FIX[Patch policy, prompt, retrieval, or tool gateway]
    FIX --> REG[Add regression eval]
    REG --> REVIEW[Security and owner review]
    REVIEW --> REENABLE[Re-enable with monitoring]
```
