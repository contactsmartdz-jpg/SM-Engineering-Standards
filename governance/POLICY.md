# Engineering Policy and Governance

**Status:** Draft 0.1 · **Scope:** Technology-neutral and project-independent

## 1. Language
The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express normative requirements:
- **MUST / MUST NOT:** mandatory for the chosen adoption scope.
- **SHOULD / SHOULD NOT:** strong default; deviations need a documented rationale.
- **MAY:** optional.
Descriptive examples are informative, not requirements.

## 2. Adoption model
An adopting project references a fixed release or commit of this standard in its own [Standards Profile](../templates/STANDARDS_PROFILE.md).
- The core standard defines **outcomes and minimum controls**, not mandatory vendors, languages, deployment platforms, or organization structures.
- The local profile selects applicable checks, tools, risk owners, and any additional restrictions.
- Local rules **MAY** be stronger. They **MUST NOT** silently weaken mandatory security, privacy, data-integrity, or approval rules.
- Legal, contractual, and regulatory obligations remain controlling. Where requirements conflict, the accountable owner documents the resolution before proceeding.

## 3. Accountability and authority
- An accountable human or expressly authorized governance body owns policy adoption, exceptions, sensitive approvals, and release risk.
- Implementers, reviewers, and automated agents cannot grant themselves exception, deployment, or merge authority.
- Every material decision should have a traceable owner, date, and evidence.

## 4. Risk classification
- **Low:** documentation or isolated changes with no material operational or trust-boundary impact.
- **Moderate:** ordinary behavior, API, dependency, or interface changes.
- **High:** identity, authorization, payments, secrets, personal data, destructive migrations, privileged operations, security policy, or production infrastructure changes.
A local project may increase risk levels, never lower them solely to bypass controls.

## 5. Exceptions
Use the [Exception template](../templates/EXCEPTION.md). Every approved exception records the rule ID, reason, scope, compensating controls, risk owner, review date, and expiration. No blanket or indefinite approval. Unapproved exceptions are failures, not passes.

## 6. Changes to the standard
- Propose changes through documented review and explain compatibility impacts.
- Do not retrospectively change requirements already adopted by a pinned release.
- Draft releases use 0.x; stable releases use semantic versioning. Major versions may break requirements; minor versions add compatible guidance; patches clarify without changing obligations.
- Security corrections may require expedited review with a recorded justification.
- Project-specific names, secrets, customer data, vendor assumptions, and confidential operating details do not belong in this public standard.

## 7. Evidence and interpretation
Written policies are not proof of enforcement. A control is **documented** when the rule exists, **configured** when a verifiable mechanism exists, and **verified** when evidence from the relevant revision and environment is available.

See [Quality Gates](../quality-gates/QUALITY_GATES.md), [Definition of Ready](DEFINITION_OF_READY.md), and [Definition of Done](DEFINITION_OF_DONE.md).
