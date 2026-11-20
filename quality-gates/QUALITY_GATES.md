# Quality Gates

**Status:** Draft 0.1 · **Scope:** Proportionate, evidence-based controls

## Two gate moments
**Validation gate:** prove the current user outcome and the applicable safety controls; allow rapid feedback without inventing extra reviews or documentation.

**Production gate:** verify the release revision and operational readiness. Production cannot be approved by merely pointing to the earlier demonstration. Required checks at any stage remain required; a risky action cannot be performed while waiting for a later gate.

Each result is **PASS**, **FAIL**, **NOT RUN**, or **NOT APPLICABLE** (with rationale). Never recast a failure or outage as a pass.

## Control catalog
| ID | Gate | Fast (low) | Standard (moderate) | Critical (high) |
| --- | --- | --- | --- | --- |
| QG-01 | Outcome/traceability | Short issue/PR acceptance | Same | Same plus sensitive-operation owner |
| QG-02 | Formatting/static quality | Automated where supported | Automated where supported | Automated where supported |
| QG-03 | Build/type checks | When affected/applicable | When affected/applicable | When affected/applicable |
| QG-04 | Behavior tests | Relevant smoke/changed behavior | Targeted positive/failure/regression | Targeted behavior and safety/permission/edge cases |
| QG-05 | Secrets/dependencies | When source/dependency/build surfaces change | When relevant | When relevant; assess high-risk findings |
| QG-06 | Security/authorization | Applicable trust boundary | Applicable trust boundary | Mandatory focused analysis and evidence |
| QG-07 | Independent review | Not default | One focused review if local profile requires | Mandatory before high-risk approval/merge |
| QG-08 | Documentation/contracts | Only affected user instructions/contracts | Only affected instructions/contracts | Affected contracts, operational instructions, risk decisions |
| QG-09 | Data/release safety | If data/release impact exists | If data/release impact exists | Required for affected migrations, recovery, privileged operations |

## Evidence contract and enforcement
- The **local** [Standards Profile](../templates/STANDARDS_PROFILE.md) identifies required gates at validation and release, owner, tool, and evidence source. This table is a applicability guide, **not** nine documents or nine approval requests.
- Applicable required **FAIL** or **NOT RUN** controls block the corresponding gate. A legitimate, scoped exception is possible only where [Policy](../governance/POLICY.md) allows it; the original result stays visible.
- Evidence refers to the tested revision and environment. An old test does not prove a new commit.
- If hosted CI is unavailable, an owner-approved reproducible alternate check may provide evidence; absence of any required check remains **NOT RUN**.
- Do not make approval for one unrelated discipline a prerequisite for a low-risk change. Do not accept agent self-review as an independent high-risk approval.
- An assertion in a Markdown file is not configured enforcement. Apply branch protection or equivalent checks only after the local project has actually configured them.

See [Development Policy](../governance/DEVELOPMENT_POLICY.md) and [Production Readiness](../governance/PRODUCTION_READINESS_POLICY.md).
