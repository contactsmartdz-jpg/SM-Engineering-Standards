# Production Readiness Policy

**Status:** Draft 0.1 · **Principle:** Production quality before release

## Two separate decisions
**Functional acceptance** confirms that a tested feature addresses the user's intended outcome; it is **not** release authorization.

**Production readiness** confirms that the exact release revision satisfies applicable safety, quality, operational, and governance gates. The authorized release owner decides whether and when to deploy. A code merge is not automatically a production release.

## Release checklist — only where applicable
- [ ] The accepted behavior and relevant regressions are verified against the release revision; failed, skipped, or unrun checks are honestly reported.
- [ ] Required formatting, build/type, tests, secrets/dependency/security gates pass under the locally adopted profile.
- [ ] Server-side authorization, privacy, sensitive-data handling, and state-changing operations are safe and verified for the affected surface.
- [ ] Public contracts, user-facing instructions, and essential operational documentation are correct; no unnecessary documentation bundle is required.
- [ ] Data compatibility, migrations, backups, recovery/rollback, idempotency, and monitoring are evaluated and verified **where risk makes them relevant**.
- [ ] Any required independent review and accountable approval are linked to the exact material revision.
- [ ] Residual risks and non-blocking technical debt have owners; unresolved blocking risks are not hidden as backlog items.

## Non-negotiable release blockers
An unresolved exploitable critical security defect, missing authorization for protected actions, unacceptable risk of data loss, required but failed/unrun safety check, or missing mandatory independent high-risk approval **blocks release**. Do not present an exception as PASS. Only a legitimate, scoped exception may be considered where policy and law explicitly permit it; certain controls cannot be waived.

## Documentation and refactoring boundary
Prior to functional acceptance: produce only what is needed to build, validate, and use a safe feature. Prior to production: complete only the **applicable** operational, consumer-contract, and safety evidence. Improvements unrelated to release safety or verified acceptance may be scheduled later, with an owner and review trigger.

## Evidence and ownership
The local [Standards Profile](../templates/STANDARDS_PROFILE.md) declares environment, gates, release authority, and evidence locations. Passing status refers to a specific revision and environment; unavailable CI is **NOT RUN**, not a free pass. A reproducible local or alternate runner can supply evidence if the profile authorizes it and ownership is clear.

See [Quality Gates](../quality-gates/QUALITY_GATES.md), [Security](../standards/SECURITY.md), [Reliability](../standards/RELIABILITY.md), and [Policy](POLICY.md).
