# Clean Code Standard

**Status:** Draft 0.1 · **Scope:** All software projects · **ID prefix:** CC

## Purpose
Make code understandable, testable, and safe to change while prioritizing **working user outcomes**. Do not mistake broad refactoring or aesthetic perfection for feature delivery.

## Normative rules
- **CC-01 (MUST):** Use names expressing intent and domain meaning; avoid misleading ambiguities.
- **CC-02 (MUST):** Keep code units focused on coherent responsibilities; do not combine unrelated business rules and privileged operations.
- **CC-03 (MUST):** Avoid duplicated business knowledge while resisting premature general-purpose abstractions.
- **CC-04 (MUST):** Validate assumptions at boundaries and represent relevant missing, invalid, or exceptional states.
- **CC-05 (MUST):** Handle expected failure deliberately; never swallow errors or leak sensitive diagnostics.
- **CC-06 (MUST):** Follow the configured formatter, compatible language version, and repository conventions.
- **CC-07 (SHOULD):** Prefer simple control flow, limited mutable state, and small coherent interfaces.
- **CC-08 (SHOULD):** Comment on non-obvious intent, contracts, and risks; remove misleading comments.
- **CC-09 (SHOULD):** Avoid speculative features, configuration, and future-proofing.
- **CC-10 (MUST):** Avoid unrelated reformatting, renaming, or refactoring in a feature/bug fix unless authorized.
- **CC-11 (SHOULD):** Defer non-blocking cleanup until functional acceptance or an identified release need. Track genuine debt with impact and owner, rather than refactoring for its own sake.
- **CC-12 (MUST):** Do not defer material correctness, security, permission, data-integrity, or irreversible-action defects under the label "refactor later."

## Review
Focus on real behavior, boundaries, maintainability hazards, and testability. Do not impose arbitrary universal file size, method length, abstraction count, or cleanup percentage. Use automated formatting rather than repeated manual style review.

See [Development Policy](../governance/DEVELOPMENT_POLICY.md), [Production Readiness](../governance/PRODUCTION_READINESS_POLICY.md), and [Code Review](CODE_REVIEW.md).
