# Code Review Standard

**Status:** Draft 0.1 · **ID prefix:** REV

## Objective
Review the **changed behavior and its real risks**, rather than maximizing reviewer count, document length, or style comments.

## Normative rules
- **REV-01 (MUST):** Identify what changed, its acceptance result, the exact tested revision, and remaining material risks in the existing PR/task.
- **REV-02 (MUST):** Check affected correctness, boundaries, relevant tests, security, dependencies, and user-facing effects in proportion to change risk.
- **REV-03 (MUST):** The implementer cannot be the sole final approver of a high-risk change.
- **REV-04 (MUST):** Resolve material blocking findings before the corresponding gate; do not silently accept security, data-loss, or authorization blockers.
- **REV-05 (MUST):** Bind approvals and evidence to the applicable revision. Recheck only material changes or invalidated evidence.
- **REV-06 (MUST):** Distinguish tested evidence from assertions; an agent's unverified report is insufficient.
- **REV-07 (SHOULD):** Prefer small focused changes and concise actionable review notes.
- **REV-08 (SHOULD):** Separate blockers with concrete impact and evidence from optional readability or architecture suggestions.
- **REV-09 (MUST):** Changes to security policy, enforcement, production credentials, and approval boundaries require accountable review.
- **REV-10 (MUST):** Do not require sequential reviewer chains or extra approval passes without a documented local risk/control requirement.
- **REV-11 (SHOULD):** Defer non-blocking style-only or speculative architecture improvements to a tracked follow-up instead of blocking a validated feature.

## Risk-based default
**Fast:** automated/quick verification; no independent review by default. **Standard:** targeted checks and one focused independent review where the local profile requires it. **Critical:** independent review and explicit owner approval before the affected sensitive action or production merge.

## Decision
**APPROVE** (applicable evidence present), **REQUEST_CHANGES** (concrete blocker), or **COMMENT** (non-blocking). Documentation volume is not a quality criterion.

See [Development Policy](../governance/DEVELOPMENT_POLICY.md), [Quality Gates](../quality-gates/QUALITY_GATES.md), and [Pull Request template](../templates/PULL_REQUEST.md).
