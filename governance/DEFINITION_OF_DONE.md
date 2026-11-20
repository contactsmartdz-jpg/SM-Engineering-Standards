# Definition of Done (DoD)

**Status:** Draft 0.1

There are **two completion states**. Never describe the first as permission to release to production.

## A. Functionally validated (Build → Validate)
- [ ] The smallest usable feature meets the recorded observable acceptance criteria in a suitable environment.
- [ ] Relevant behavior checks and **all safety checks required for the affected action/environment** have been executed; failures and unrun checks are explicit.
- [ ] User/product validation outcome (accepted / changes requested / rejected), revision, limitations, and owner are recorded in the existing issue/PR.
- [ ] Any unconnected or simulated capability is clearly marked as such.

At this stage, unrelated refactoring, speculative scalability, presentation polish, exhaustive documentation, and non-blocking technical debt are **not required**. This state does not override merge protections or mandatory controls.

## B. Production ready (Harden → Release)
- [ ] All **applicable** locally configured [Quality Gates](../quality-gates/QUALITY_GATES.md) pass, or a permitted authorized exception is recorded without falsifying results.
- [ ] No unresolved security, privacy, authorization, data-integrity, or release-safety blocker remains.
- [ ] Required review/authorization, compatibility and migration evidence, recovery, and essential documentation are complete **where relevant**.
- [ ] Release owner accepts residual risk for the exact revision and environment; non-blocking debt is tracked with owner and priority.

A passing build is not proof of completion. A user's functional approval is not production approval. See [Development Policy](DEVELOPMENT_POLICY.md) and [Production Readiness](PRODUCTION_READINESS_POLICY.md).
