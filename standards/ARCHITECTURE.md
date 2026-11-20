# Architecture Standard

**Status:** Draft 0.1 · **ID prefix:** AR

## Goal
Design systems whose responsibilities, dependencies, data boundaries, and operational constraints are explicit. Architecture must fit actual requirements; no specific architectural style or framework is mandatory.

## Normative rules
- **AR-01 (MUST):** Document system context, trust boundaries, important data flows, and ownership of external integrations for significant systems.
- **AR-02 (MUST):** Keep business rules insulated from avoidable implementation details and unrelated presentation concerns.
- **AR-03 (MUST):** Make module boundaries explicit and minimize cyclic dependencies and implicit coupling.
- **AR-04 (MUST):** Any significant, hard-to-reverse architectural choice requires a dated Architecture Decision Record (ADR) with options and consequences.
- **AR-05 (MUST):** Changes to persistent data must identify compatibility, migration, backup, rollback or safe recovery, and validation strategy.
- **AR-06 (MUST):** Design external interfaces with clear contracts, error behavior, authorization, and compatibility expectations.
- **AR-07 (SHOULD):** Prefer the least complex architecture that meets current reliability, scale, and security needs.
- **AR-08 (SHOULD):** Make dependencies injectable or replaceable where doing so materially improves testing or resilience.
- **AR-09 (SHOULD):** Prefer incremental, reversible delivery for risky changes instead of all-at-once replacement.

## Required design evidence for high-risk changes
State the affected components, interfaces, data flows, non-functional constraints, risks, migration approach, and verification plan.

## Anti-patterns
Unbounded shared state, hidden cross-module writes, circular dependencies, framework-driven business rules with no clear domain boundary, and irreversible migrations without explicit approval.

See [ADR template](../templates/ADR.md) and [Reliability](RELIABILITY.md).
