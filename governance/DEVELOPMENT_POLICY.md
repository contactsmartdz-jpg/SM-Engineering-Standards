# Development Policy — Feature First

**Status:** Draft 0.1 · **Principle:** Build → Validate → Harden

## Purpose and scope
The default for iterative product development is to deliver the **smallest usable vertical slice**, obtain real feedback, and improve only what is needed. This policy applies to development and controlled validation; it never authorizes unsafe production actions or bypasses [Security](../standards/SECURITY.md), legal obligations, or locally configured required checks.

A feature can be **functionally validated** without being **production ready**. See [Production Readiness](PRODUCTION_READINESS_POLICY.md).

## The three phases
1. **Build:** Record the user outcome, 1–3 observable acceptance criteria, a risk track, and a verification method in the existing work item. Implement the simplest complete behavior. No speculative abstractions, future-proofing, or documentation packages.
2. **Validate:** Demonstrate the feature in an appropriate environment. Run proportionate behavior and safety checks. Record **accepted / changes requested / rejected**, the tested revision, and limitations in the same work item or PR.
3. **Harden when justified:** After acceptance, address release-blocking correctness, security, compatibility, and operational gaps before production. Track optional cleanup as prioritized technical debt with owner and trigger; do not make every stylistic improvement a release blocker.

## Risk tracks and default workflow
| Track | Examples | Development validation | Review/approval |
| --- | --- | --- | --- |
| **Fast (low)** | Copy, presentation, isolated UI without protected data or side effects | Relevant quick check or smoke test; supported formatter/build checks | Automated or lightweight review; **no extra sequential approvals by default** |
| **Standard (moderate)** | New ordinary feature, API, routine business behavior | Targeted tests of success and relevant failure paths, plus applicable checks | **One focused review** where the project's local profile requires it |
| **Critical (high)** | Auth, permissions, payments, secrets, personal data, destructive data operations, production infrastructure | Isolated environment, threat/permission checks, safe recovery and applicable tests **before hazardous execution** | Independent review and explicit accountable authorization for sensitive actions |

Classify the **change**, not the whole project. Escalate mixed changes to the highest applicable risk. Never downgrade risk to avoid a gate. A local profile may require stronger controls.

## Rules for speed without shortcuts
- **DEV-01 (MUST):** Prefer a working vertical slice and user validation over building a speculative, generalized framework.
- **DEV-02 (MUST):** Use the existing issue/PR as the single concise progress and decision record. Create separate specifications, ADRs, diagrams, or reports **only** when required by a material decision, consumer contract, regulated obligation, or concrete handoff need.
- **DEV-03 (MUST):** Do not introduce a new approval stage or reviewer chain without a named policy requirement and accountable owner. Reuse approvals and evidence already on record.
- **DEV-04 (MUST):** Do not treat an unverified prototype as production-ready, an unrun check as passed, or a user-visible mock as a connected feature. Missing integrations must be visibly identified.
- **DEV-05 (MUST):** Apply security, privacy, authorization, data-integrity, and irreversible-action safeguards **before** any relevant interaction with real systems or data, regardless of phase.
- **DEV-06 (SHOULD):** Limit review to changed behavior, applicable risks, and regression evidence. Record non-blocking cleanliness, architecture, and optimization work as follow-up tasks.
- **DEV-07 (SHOULD):** After two unproductive attempts to resolve the same blocker, report the concrete error and next decision rather than repeating approvals or speculative rewrites.
- **DEV-08 (MUST):** A high-risk operation requires the locally authorized independent review and approval; an implementing agent cannot approve itself.

No numeric coverage target, document count, review count, or universal time budget is imposed by this standard.

## Measures
Measure feature lead time, time waiting for approvals, usable features accepted, post-merge defects, and rework. Optimize delivery speed **without increasing escaped safety or correctness defects**.

See [Definition of Ready](DEFINITION_OF_READY.md), [Definition of Done](DEFINITION_OF_DONE.md), [Quality Gates](../quality-gates/QUALITY_GATES.md), and [AI Agent Rules](../ai-agents/AGENT_RULES.md).
