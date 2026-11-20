# Engineering Policy and Governance

**Status:** Draft 0.1 · **Scope:** Technology-neutral and project-independent

## 1. Governing principle
**Feature First, Production Quality Before Release.** Optimize for a usable feature and actual user feedback, not a volume of documents, review rounds, or approvals. Development and release are **distinct** decisions:

- [Development Policy](DEVELOPMENT_POLICY.md): build → validate → harden, using a change-level risk track.
- [Production Readiness Policy](PRODUCTION_READINESS_POLICY.md): the applicable release gates and accountable authorization before deployment.

Security, privacy, authorization, data integrity, and irreversible-action safeguards apply **from the beginning** where relevant, not only after user acceptance. These two policies govern interpretation of the standard's other process requirements; stricter legal/contractual obligations prevail.

## 2. Language
**MUST / MUST NOT** are binding in the adopted scope. **SHOULD / SHOULD NOT** are strong defaults with a rationale for material deviation. **MAY** is optional. Examples are informative, not obligations.

## 3. Adoption
An adopting project pins an immutable release or commit in a local [Standards Profile](../templates/STANDARDS_PROFILE.md). This central standard mandates outcomes and minimum controls, not vendors, document volume, programming languages, or organization structures.
- A project defines its applicable checks, owners, environment boundaries, and release authority in its **local** profile.
- A local rule may be stricter but MUST NOT silently weaken security, privacy, data-integrity, or mandatory sensitive-action approval rules.
- A Markdown statement alone is not enforced policy; actual branch settings, tests, permissions, and evidence must support any enforcement claim.

## 4. Change-level risk classification
| Track | Risk | Default process |
| --- | --- | --- |
| **Fast** | Low: isolated non-sensitive UI, content, documentation | Short task and acceptance evidence; automated checks; no extra sequential approval by default |
| **Standard** | Moderate: ordinary behavior, API, integration | Targeted tests and one focused review if the adopted profile requires it |
| **Critical** | High: authorization, secrets, payments, sensitive data, destructive migration, privileged or production operations | Safeguards before risky action; independent review and explicit authorized approval |

Risk MUST be evaluated per change, escalated for mixed impacts, and MUST NOT be reduced simply to bypass controls.

## 5. Accountability, exceptions, and approval boundaries
A named accountable human or expressly authorized governance body owns adoption, sensitive approvals, exceptions, and release risk. Implementers and agents cannot grant themselves exceptional, merge, or deploy authority. **No one may add mandatory approval chains solely because more review seems desirable**; a required stage needs an applicable control and named owner.

Use the [Exception template](../templates/EXCEPTION.md) for legitimate scoped exceptions. Record rule, evidence, owner, compensating controls, expiry, and recheck trigger. An unapproved exception is a failure, not a pass. Certain security, legal, and authorization obligations are non-waivable.

## 6. Evidence and interpretation
A control is **documented** when text exists, **configured** when a mechanism is verifiably set, and **verified** when results for the relevant revision/environment exist. Reuse issue/PR comments as evidence; avoid duplicating reports. Review or clean-code preferences alone MUST NOT block a functionally validated low-risk change unless an adopted gate or concrete defect justifies the block.

## 7. Standard evolution
Propose changes with compatibility impact. Do not rewrite obligations of an already pinned release. Drafts use 0.x; stable releases use semantic versioning. Security corrections may have expedited review with justification. Keep project-specific names, confidential details, secrets, and customer data out of this public standard.

See [Quality Gates](../quality-gates/QUALITY_GATES.md), [Definition of Ready](DEFINITION_OF_READY.md), and [Definition of Done](DEFINITION_OF_DONE.md).
