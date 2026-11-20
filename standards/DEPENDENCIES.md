# Dependency and Supply Chain Standard

**Status:** Draft 0.1 · **ID prefix:** DEP

## Normative rules
- **DEP-01 (MUST):** Justify new runtime dependencies by capability, maintenance risk, and alternatives.
- **DEP-02 (MUST):** Keep dependency manifests and lockfiles consistent when the stack supports locking.
- **DEP-03 (MUST):** Detect and triage known vulnerabilities; never ignore a material exploitable finding without accountable risk acceptance.
- **DEP-04 (MUST):** Verify license compatibility and provenance before incorporating third-party code or assets.
- **DEP-05 (MUST):** Review privileged build steps and external actions; prefer immutable references for security-sensitive CI components when supported.
- **DEP-06 (SHOULD):** Limit dependency count, permissions, network access, and update blast radius.
- **DEP-07 (SHOULD):** Maintain a documented update and deprecation process for critical dependencies.

## Evidence
Dependency-related changes state why an alternative was not chosen, license implications where relevant, vulnerability review results, and reproducibility implications.

This standard does not prescribe one package manager, software bill of materials format, or external scanning vendor.
