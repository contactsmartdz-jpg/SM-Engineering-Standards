# SM Engineering Standards

**Open, project-independent engineering standards for software teams and AI coding agents.**

> **Status: Draft 0.1 — not yet a stable release or automatically adopted policy.** This draft is being reviewed. No adopter's repository, protections, or production settings are changed by publishing it.

## Philosophy: Feature First, Production Quality Before Release
**Build → Validate → Harden.** Deliver the smallest usable feature, test its real behavior, obtain user feedback, and then complete the **applicable** quality and operational work before production. Never postpone authorization, security, privacy, data integrity, or irreversible-action safeguards that are required **during** development.

| Decision | Policy | Outcome |
| --- | --- | --- |
| Iterative development | [Development Policy](governance/DEVELOPMENT_POLICY.md) | Working vertical slice and verified functional acceptance with minimal paperwork |
| Production deployment | [Production Readiness Policy](governance/PRODUCTION_READINESS_POLICY.md) | Applicable gates, accountable approval, and verified release safety |
| Overarching authority | [Engineering Policy](governance/POLICY.md) | Change-level Fast / Standard / Critical risk tracks, adoption, and exceptions |

## Core standards
- [Clean Code](standards/CLEAN_CODE.md)
- [Architecture](standards/ARCHITECTURE.md)
- [Security & Privacy](standards/SECURITY.md)
- [Testing](standards/TESTING.md)
- [Code Review](standards/CODE_REVIEW.md)
- [Reliability](standards/RELIABILITY.md)
- [Documentation](standards/DOCUMENTATION.md)
- [Dependencies](standards/DEPENDENCIES.md)

## Workflow and evidence
- [Definition of Ready](governance/DEFINITION_OF_READY.md) — actionable, not fully documented
- [Definition of Done](governance/DEFINITION_OF_DONE.md) — functionally validated versus production ready
- [Quality Gates](quality-gates/QUALITY_GATES.md) — proportionate checks, not nine documents or approvers
- [AI Coding Agent Rules](ai-agents/AGENT_RULES.md)
- [Independent AI Reviewer Rules](ai-agents/REVIEWER_RULES.md)
- [Adoption Guide](docs/ADOPTION_GUIDE.md)

## Lightweight templates
- [Standards Profile](templates/STANDARDS_PROFILE.md) — local risk and enforcement contract
- [Issue](templates/ISSUE.md) — outcome, acceptance, track, evidence
- [Pull Request](templates/PULL_REQUEST.md) — concise results and blockers
- [ADR](templates/ADR.md) — only for consequential architecture decisions
- [Exception](templates/EXCEPTION.md) — scoped authorized deviation

## Adoption and enforcement
1. Review and pin a specific standard release/commit; drafts are not self-applying.
2. Maintain a short **local** profile with gate applicability, owner, and available execution tools.
3. Use fast iteration for low/moderate risk and explicit accountable review for high risk.
4. Do not claim enforced checks until configured and verified. When hosted CI is unavailable, use authorized reproducible alternatives rather than treating missing results as PASS.

## Contributing, validation, and license
See [Contributing](CONTRIBUTING.md), [Glossary](docs/GLOSSARY.md), [Security Reporting](SECURITY.md), and [Changelog](CHANGELOG.md).

Validate internal Markdown links and required files with `python3 tools/validate_docs.py`. A [GitHub workflow](.github/workflows/validate-docs.yml) is configured for this check; hosted execution depends on CI availability.

Licensed under [Apache License 2.0](LICENSE).
