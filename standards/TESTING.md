# Testing Standard

**Status:** Draft 0.1 · **ID prefix:** TST

## Objective
Provide repeatable evidence that the change behaves as required, respects boundaries, and does not break critical existing behavior.

## Normative rules
- **TST-01 (MUST):** Define testable acceptance criteria before implementing non-trivial behavior.
- **TST-02 (MUST):** Every feature or bug fix needs proportionate automated tests, or a documented reason why automation is impractical and a verified alternative.
- **TST-03 (MUST):** Verify positive paths, important failures, edge cases, and relevant permission boundaries.
- **TST-04 (MUST):** Reproduce reported defects with a regression test where feasible, then demonstrate that the fix passes.
- **TST-05 (MUST):** Report the exact test commands, environment or CI job, revision, outcome, and unresolved limitations; never claim tests ran if they did not.
- **TST-06 (MUST):** Use isolated and reproducible test data. Do not use sensitive production data without explicit authorization and appropriate safeguards.
- **TST-07 (SHOULD):** Use unit, integration, contract, end-to-end, and non-functional tests according to the risks and architecture of the change.
- **TST-08 (SHOULD):** Minimize flaky tests, nondeterminism, real external dependencies, and fragile timing assumptions.
- **TST-09 (MUST):** Do not delete, disable, skip, or weaken a failing test simply to obtain a green result without a documented, approved reason.
- **TST-10 (SHOULD):** Track meaningful coverage trends, but never treat a single coverage percentage as proof of correctness.

## Test design checklist
Tests should be independent, readable, deterministic, focused on observable behavior, and maintainable. Record failures as failures, not unverified passes.

## Acceptance
A required test that cannot run is **not passed**. Its effect on merging is determined by [Quality Gates](../quality-gates/QUALITY_GATES.md) and a documented exception, if allowed.
