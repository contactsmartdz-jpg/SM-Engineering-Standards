# SM Engineering Standards

**Open, project-independent engineering standards for software teams and AI coding agents.**

> **Status: Draft 0.1 (not yet a stable release).** The materials are proposed guidance for review. They do not automatically change any adopter's repository, branch protections, or deployment settings.

## Purpose

Provide a reusable, vendor-neutral baseline for readable code, maintainable architecture, security, tests, reviews, safe delivery, and evidence-based AI-agent work.

- **Project-agnostic:** No references to a particular product, customer, repository, internal process, or deployment.
- **Technology-neutral:** No required programming language, cloud provider, editor, AI model, or CI/CD vendor.
- **Verifiable:** Rules have stable area IDs and map to proportionate evidence.
- **Adoptable:** Projects pin a version and maintain their implementation details in their own repositories.
- **Risk-aware:** High-risk changes need stronger review, explicit approvals, and recovery plans.

This is a **framework of engineering expectations**, not a claim that using it guarantees correctness, security, or compliance.

## Standards

| Area | Document |
| --- | --- |
| Clean code | [Clean Code](standards/CLEAN_CODE.md) |
| Architecture | [Architecture](standards/ARCHITECTURE.md) |
| Security and privacy | [Security](standards/SECURITY.md) |
| Testing | [Testing](standards/TESTING.md) |
| Code review | [Code Review](standards/CODE_REVIEW.md) |
| Reliability | [Reliability](standards/RELIABILITY.md) |
| Documentation | [Documentation](standards/DOCUMENTATION.md) |
| Dependency and supply chain | [Dependencies](standards/DEPENDENCIES.md) |

## Governance and quality

| Area | Document |
| --- | --- |
| Requirements, authority, exceptions | [Engineering Policy](governance/POLICY.md) |
| Task readiness | [Definition of Ready](governance/DEFINITION_OF_READY.md) |
| Task completion | [Definition of Done](governance/DEFINITION_OF_DONE.md) |
| Evidence-based acceptance | [Quality Gates](quality-gates/QUALITY_GATES.md) |
| AI coding behavior | [AI Agent Rules](ai-agents/AGENT_RULES.md) |
| Independent AI review | [AI Reviewer Rules](ai-agents/REVIEWER_RULES.md) |

## Generic templates

- [Standards Adoption Profile](templates/STANDARDS_PROFILE.md) — local mapping to tools, risk, and evidence.
- [Exception](templates/EXCEPTION.md) — time-bounded accountable deviations.
- [Architecture Decision Record](templates/ADR.md) — technical decision rationale.
- [Pull Request](templates/PULL_REQUEST.md) — review and check evidence.
- [Issue](templates/ISSUE.md) — scope and testable acceptance criteria.

## How to adopt

1. Read the [Adoption Guide](docs/ADOPTION_GUIDE.md).
2. Pin a reviewed release or exact commit of this standard (avoid floating references).
3. Copy the [Adoption Profile](templates/STANDARDS_PROFILE.md) into the adopting project's **own** repository.
4. Select locally appropriate validation tools and map each relevant gate to verifiable results.
5. Run advisory checks before making merge gates mandatory; require independent review for high-risk changes.
6. Log exceptions locally and reassess at their expiry dates.

**Important:** An AI agent reading a Markdown policy does not itself enforce it. Actual enforcement requires repository settings, permissions, automated checks, and accountable reviewers.

## Contributing and validation

See [Contributing](CONTRIBUTING.md), [Glossary](docs/GLOSSARY.md), [Security Reporting](SECURITY.md), and [Changelog](CHANGELOG.md).

The repository checks internal Markdown file references using a dependency-free script:

    python3 tools/validate_docs.py

A [documentation CI workflow](.github/workflows/validate-docs.yml) runs this check on pull requests and pushes to the default branch. External links and heading anchors are not validated by that script.

## License

[Apache License 2.0](LICENSE). Users may use and adapt this work, including commercially, subject to the license terms. The license does not grant a right to use others' trademarks.
