# Code Review Standard

**Status:** Draft 0.1 · **ID prefix:** REV

## Purpose
Every substantive change receives an evidence-based review appropriate to its risk, ideally by someone other than its author.

## Normative rules
- **REV-01 (MUST):** Describe what changed, why, how it was verified, and which risks remain.
- **REV-02 (MUST):** A reviewer checks correctness, maintainability, boundaries, tests, security, dependencies, and user-facing effects when applicable.
- **REV-03 (MUST):** The author cannot be the sole final approver for a high-risk change.
- **REV-04 (MUST):** Resolve or explicitly track material findings before merge; critical security, data-loss, and authorization blockers cannot be silently accepted.
- **REV-05 (MUST):** Approval is tied to a specific revision. Material new commits require renewed verification and review as appropriate.
- **REV-06 (MUST):** Require evidence for tests and scanners; unverified agent statements are not sufficient.
- **REV-07 (SHOULD):** Keep changes small and focused where practical, without enforcing a universal line-count cap.
- **REV-08 (SHOULD):** Provide actionable findings with impact, location, severity, and a suggested resolution.
- **REV-09 (MUST):** Changes to security controls, policy enforcement, deployment access, or test gates require explicit accountable review.

## Review outcomes
- **Approve:** no blocking findings, required evidence present.
- **Request changes:** blocking findings or missing mandatory evidence.
- **Comment:** non-blocking improvements or questions.

## Risk-based review
Low-risk documentation updates may use a lighter process. High-risk changes affecting secrets, identity, authorization, payments, personal data, persistence, deployment, or privileged agent actions require independent review and explicit authorization.

See [Pull Request template](../templates/PULL_REQUEST.md), [AI Reviewer Rules](../ai-agents/REVIEWER_RULES.md), and [Definition of Done](../governance/DEFINITION_OF_DONE.md).
