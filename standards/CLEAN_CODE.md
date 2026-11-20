# Clean Code Standard

**Status:** Draft 0.1 · **Scope:** All software projects · **ID prefix:** CC

## Purpose
Write code that a competent maintainer can understand, change, test, and safely operate. Correct behavior is necessary but not sufficient. Prefer evidence of maintainability over arbitrary numeric style limits.

## Normative rules
- **CC-01 (MUST):** Use names that express intent, domain meaning, and units where relevant. Avoid misleading abbreviations and ambiguous booleans.
- **CC-02 (MUST):** Keep each unit of code focused on a coherent responsibility. Separate unrelated reasons to change.
- **CC-03 (MUST):** Avoid duplicated *knowledge and business rules*. Do not create premature abstractions merely because two implementations look similar.
- **CC-04 (MUST):** Validate assumptions at system boundaries. Explicitly represent invalid, missing, and exceptional states.
- **CC-05 (MUST):** Handle expected failures deliberately. Never silently discard errors or expose sensitive diagnostics to end users.
- **CC-06 (MUST):** Changes must follow the repository's formatter, naming conventions, and supported language version.
- **CC-07 (SHOULD):** Prefer simple control flow, limited mutable state, small coherent interfaces, and self-explanatory code.
- **CC-08 (SHOULD):** Keep comments focused on *why*, contracts, risks, and non-obvious constraints. Remove misleading or obsolete comments.
- **CC-09 (SHOULD):** Avoid speculative features and unnecessary configuration. Refactor when a real requirement justifies it.
- **CC-10 (MUST):** Avoid unrelated reformatting, renaming, or refactoring in feature and bug-fix changes unless explicitly approved.

## Review evidence
Reviewers check naming, complexity, responsibility boundaries, duplication of rules, failure handling, testability, and the size of unrelated changes. A style checker is not a substitute for this review.

## Examples of unacceptable outcomes
- An unexplained magic value that controls business behavior.
- Catching every exception and reporting success.
- A single routine that performs authorization, storage, business rules, and presentation.
- A new abstraction with no current caller or documented purpose.

## Exceptions
A justified exception must be recorded under [Policy](../governance/POLICY.md) and must not waive security or correctness requirements without an approved risk assessment.
