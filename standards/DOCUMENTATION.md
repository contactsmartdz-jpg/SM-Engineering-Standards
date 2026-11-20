# Documentation Standard

**Status:** Draft 0.1 · **ID prefix:** DOC

## Purpose
Maintain the **minimum useful source of truth** needed to operate, use, and safely change software. Do not generate documentation merely to satisfy an agent workflow.

## Rules
- **DOC-01 (MUST):** Keep maintained setup, build, test, configuration, and relevant operational instructions accurate.
- **DOC-02 (MUST):** Document consumer-visible public contracts or behavior changes **before consumers rely on them**; an isolated prototype need not have a polished external API reference.
- **DOC-03 (MUST):** Record significant, hard-to-reverse architectural choices in a dated ADR; routine implementation decisions need no ADR.
- **DOC-04 (MUST):** Correct misleading operational or consumer documentation when the affected behavior changes.
- **DOC-05 (MUST):** Never publish secrets, unauthorized proprietary content, or personally identifying examples.
- **DOC-06 (SHOULD):** Include assumptions, limits, troubleshooting, and migration guidance **only where useful to the user or operator**.
- **DOC-07 (SHOULD):** Maintain a single source of truth, linking instead of duplicating text.
- **DOC-08 (MUST):** Use the issue/PR as the default feature-level record. Separate files require a real user, consumer, legal, operational, or high-risk decision need.
- **DOC-09 (MUST):** Do not block safe validation solely because full final documentation or optional diagrams are unfinished; required security and contract information must still exist when relevant.

## Minimum evidence by phase
- **Build/Validate:** outcome, acceptance criteria, tested revision, result, limitations, and critical safety facts in the existing work item.
- **Before production:** updated affected public contracts, essential operational instructions, and consequential decisions. Do not mandate a full documentation suite for every change.

See [Development Policy](../governance/DEVELOPMENT_POLICY.md) and [Production Readiness](../governance/PRODUCTION_READINESS_POLICY.md).
