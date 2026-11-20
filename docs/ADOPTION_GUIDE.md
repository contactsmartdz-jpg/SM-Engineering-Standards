# Adoption Guide

**Audience:** Maintainers, engineering leaders, project owners, and AI coding agents.

This repository contains a reusable engineering standard, **not** instructions for any particular project, technology, or organization.

## Step 1: Pin a version
Use an immutable release tag or commit SHA. While this standard is in draft (0.x), do not interpret its presence as an adopted project policy without explicit local approval.

## Step 2: Create the local profile
Copy [Standards Profile](../templates/STANDARDS_PROFILE.md) into the adopting project's repository. Declare scope, local tools, evidence sources, accountable owner, and required quality gates. Do not place confidential project details in this public standards repository.

## Step 3: Baseline existing behavior
Run current tests and scans, inspect review and deployment controls, and record what is **documented**, **configured**, and **verified**. Do not claim every control is already active.

## Step 4: Map controls to implementation
Choose stack-appropriate formatters, analyzers, test tools, scanners, and CI/CD gates. The standard states outcomes, not vendors. Each applicable [gate](../quality-gates/QUALITY_GATES.md) needs a reproducible evidence source.

## Step 5: Roll out safely
Start with advisory results, repair established failures, then enforce required checks via branch protections or an equivalent gate. High-risk security, privacy, or data controls must never be silently relaxed for convenience.

## Step 6: Integrate agent workflows
In the project's own agent entrypoint, link to the pinned version of [Agent Rules](../ai-agents/AGENT_RULES.md) and local profile. Provide a bounded task scope and permissions. A prompt alone does not enforce rules.

## Step 7: Assess regularly
Review findings, false positives, exceptions, incident learning, and operational overhead. Update the local profile or adopt a newer version explicitly.

## Example acceptance states
| Condition | Meaning |
| --- | --- |
| Documented | Rule exists in text |
| Configured | Tool or branch rule exists |
| Verified | Evidence proves it ran at a relevant revision |
| Exception | Authorized, scoped, expiring risk acceptance |
| Not applicable | Documented rationale why control does not apply |

## Common mistakes
- Claiming an 80% coverage target alone proves correctness.
- Treating an agent self-review as independent approval.
- Marking blocked or unrun CI checks as successful.
- Copying an entire standard into every repository and letting versions drift.
- Adding confidential implementation details to this public project.

## Suggested adoption artifact
An adopted project should publish its **local** profile, quality-gate configuration, review policy, and exception register in the location appropriate to that project.
