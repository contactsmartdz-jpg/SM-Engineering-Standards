# Reliability and Operations Standard

**Status:** Draft 0.1 · **ID prefix:** REL

## Goal
Make change and failure predictable, observable, and recoverable. Apply controls proportionate to the service's criticality.

## Normative rules
- **REL-01 (MUST):** Define operational ownership and expected recovery behavior for production-facing critical components.
- **REL-02 (MUST):** Expose actionable diagnostic signals without leaking secrets or personal information.
- **REL-03 (MUST):** Identify external failure modes, timeouts, retry policy, and idempotency needs for side-effecting operations.
- **REL-04 (MUST):** High-risk releases require an explicit deployment verification and recovery or rollback plan.
- **REL-05 (MUST):** Verify backup and restoration capability before a change that materially increases data-loss risk.
- **REL-06 (SHOULD):** Use suitable health checks, monitoring, alerts, and runbooks based on real service risks.
- **REL-07 (SHOULD):** Test capacity and performance against representative workloads rather than guessed thresholds.
- **REL-08 (SHOULD):** Use incremental rollouts and observe meaningful indicators before full release when feasible.

## Evidence
For relevant changes, record the health signals, alert ownership, deployment checks, recovery steps, and outcome of any restoration exercise.

This is not a promise of a specific uptime level. Service-level targets must be established by an adopting project using measured requirements.
