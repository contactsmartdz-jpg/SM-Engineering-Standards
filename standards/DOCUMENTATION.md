# Documentation Standard

**Status:** Draft 0.1 · **ID prefix:** DOC

## Purpose
Document how to use, maintain, evaluate, and safely change software without duplicating every implementation detail.

## Rules
- **DOC-01 (MUST):** Keep setup, build, test, configuration, and relevant operational instructions accurate for maintained software.
- **DOC-02 (MUST):** Document public interfaces and behavior changes affecting consumers.
- **DOC-03 (MUST):** Record significant design decisions and their consequences with dated ADRs.
- **DOC-04 (MUST):** Update or retire documentation that becomes inaccurate in the same change when feasible.
- **DOC-05 (MUST):** Never publish secrets, proprietary data without permission, or personally identifying examples.
- **DOC-06 (SHOULD):** Explain assumptions, limitations, troubleshooting, and migration considerations.
- **DOC-07 (SHOULD):** Favor a single clear source of truth and link to it instead of copying text across many files.

## Minimum evidence
Changes that alter instructions or contracts include a documentation diff or a reason no documentation change is needed.

Use the [ADR template](../templates/ADR.md) and [Pull Request template](../templates/PULL_REQUEST.md).
