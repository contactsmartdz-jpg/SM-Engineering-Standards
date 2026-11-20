# Quality Gates

**Status:** Draft 0.1 · **Scope:** Vendor-neutral acceptance contract

## Control model
A gate has a unique ID, applicability, evidence source, owner, and decision. Every result is **PASS**, **FAIL**, **NOT RUN**, or **NOT APPLICABLE** (with justification). Only an authorized exception can convert a permitted failure into a conditional release decision; it must never falsify the result.

## Baseline gates
| ID | Gate | Required evidence | Default rule |
| --- | --- | --- | --- |
| QG-01 | Scope & traceability | Change links to task/requirements | MUST |
| QG-02 | Formatting & static quality | Configured formatter, linter, analysis output | MUST when supported by stack |
| QG-03 | Build / type validation | Build or equivalent validation at target revision | MUST when applicable |
| QG-04 | Behavioral tests | Relevant automated test results | MUST |
| QG-05 | Dependency & secret checks | Scan results with triage | MUST for code and build changes |
| QG-06 | Security & authorization | Risk-based analysis / security test evidence | MUST for relevant surfaces |
| QG-07 | Independent review | Approval linked to final revision | MUST for high-risk changes |
| QG-08 | Docs & contracts | Documentation diff or explicit no-change rationale | MUST |
| QG-09 | Data / release safety | Migration, restore, rollback or recovery proof | MUST for high-risk releases |

## Merge contract
- Required FAIL or NOT RUN gates block the normal merge path.
- NOT APPLICABLE requires a rationale, not merely a checkbox.
- Results must identify revision and execution context. An older passing run does not validate changed code.
- An exception needs the authority and safeguards described in [Policy](../governance/POLICY.md).
- A self-attested agent review does not substitute for independent review on high-risk changes.

## Gradual adoption
1. Record a baseline without blocking the existing project.
2. Configure reproducible checks and remove false positives.
3. Define applicable required gates in a local profile.
4. Enforce via protected branches or equivalent mechanism.
5. Review audit evidence and periodically revise the risk model.

A written gate is not an enforced gate until the repository's settings actually require it.
