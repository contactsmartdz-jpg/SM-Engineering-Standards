# Security and Privacy Standard

**Status:** Draft 0.1 · **ID prefix:** SEC

## Principles
Treat all external input as untrusted, enforce least privilege, protect sensitive data throughout its lifecycle, and verify controls rather than assuming them.

## Normative rules
- **SEC-01 (MUST):** Enforce authorization on the server or trusted execution boundary for every protected operation and resource; UI checks alone are insufficient.
- **SEC-02 (MUST):** Use established, maintained cryptographic mechanisms and secure credential storage; never invent cryptographic algorithms.
- **SEC-03 (MUST):** Never put production secrets or private keys in source, logs, examples, tests, or agent prompts. Use approved secret storage and rotate exposed credentials.
- **SEC-04 (MUST):** Validate, constrain, and safely encode untrusted input and output according to context; use parameterized data access.
- **SEC-05 (MUST):** Protect sensitive data in transit and at rest where risk and legal requirements demand it. Minimize collection, retention, and visibility.
- **SEC-06 (MUST):** Treat authentication, permissions, payments, destructive operations, production data, and infrastructure credentials as high-risk changes requiring independent review.
- **SEC-07 (MUST):** Detect known vulnerable dependencies and triage findings based on reachability, severity, exploitation risk, and compensating controls.
- **SEC-08 (MUST):** Do not expose secrets or personal data in error messages, telemetry, test fixtures, or support artifacts.
- **SEC-09 (SHOULD):** Apply layered defenses, audit sensitive actions, rate-limit abuse-prone endpoints, and use secure defaults.
- **SEC-10 (MUST):** Block release for unresolved critical vulnerabilities affecting the release, unless a documented risk acceptance is authorized by the accountable owner.

## Evidence
Security review must include relevant threat scenarios, access-control tests, secrets/dependency scan results, and a decision log for residual risks. Passing a scanner does not prove security.

## References
Consider OWASP ASVS for application verification and the relevant secure development guidance for your stack. Select applicable controls based on the system's threat model.

See [Review](CODE_REVIEW.md), [Quality Gates](../quality-gates/QUALITY_GATES.md), and [Exception template](../templates/EXCEPTION.md).
