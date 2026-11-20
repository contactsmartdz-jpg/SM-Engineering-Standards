# Adoption Guide

**Audience:** Maintainers, owners, and AI coding agents. This repository is general-purpose; no particular product or vendor is assumed.

1. **Pin an immutable reviewed release or commit.** Draft 0.x changes do not automatically update existing projects.
2. **Create a minimal [Standards Profile](../templates/STANDARDS_PROFILE.md)** in the adopting project's own repository: owner, risk tracks, required checks, where evidence is stored, and who may authorize production.
3. **Default to [Feature First](../governance/DEVELOPMENT_POLICY.md)** for ordinary iteration: record outcome and 1–3 acceptance criteria, build a vertical slice, test relevant behavior, collect user feedback.
4. **Classify each change**, not just the entire repository: Fast, Standard, or Critical. Require safeguards before high-risk or real-data interactions; do not treat prototypes as a bypass.
5. **Separate functional acceptance from [Production Readiness](../governance/PRODUCTION_READINESS_POLICY.md).** Only locally applicable gates and evidence are required. Do not invent extra review chains or document deliverables.
6. **Configure actual controls.** Use reproducible tools and protected branches or equivalents where needed. Distinguish **documented**, **configured**, and **verified**; unavailable CI is not PASS. Approved alternative validation may be used when configured.
7. **Link [AI Agent Rules](../ai-agents/AGENT_RULES.md)** and give agents only bounded authority. A prompt is not enforcement.
8. **Measure and revise.** Compare feature lead time, approval waiting, post-release defects, and rework. Address actual pain, not hypothetical process gaps.

## Common mistakes
- Requiring a separate design file, ADR, review memo, and approval for every low-risk feature.
- Treating the nine [Quality Gates](../quality-gates/QUALITY_GATES.md) as nine documents or nine approvers.
- Marking unrun checks as PASS, or agent self-review as independent high-risk approval.
- Deferring security, authorization, data integrity, or irreversible-action safeguards until after user testing.
- Treating a feature demo as production deployment approval.
- Copying this entire standard into every project instead of pinning a version and using a short local profile.
