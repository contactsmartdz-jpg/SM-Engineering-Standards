# Definition of Done (DoD)

**Status:** Draft 0.1

A change is done only when all **applicable** requirements below are satisfied with evidence:

- [ ] Acceptance criteria are demonstrated and linked to the change.
- [ ] Code follows the chosen [Clean Code](../standards/CLEAN_CODE.md) and [Architecture](../standards/ARCHITECTURE.md) rules.
- [ ] Tests are implemented and executed at the final relevant revision; failures and skips are accurately reported.
- [ ] Mandatory [Quality Gates](../quality-gates/QUALITY_GATES.md) pass, or an authorized bounded exception exists where policy permits.
- [ ] Security, privacy, dependency, and data-integrity risks are assessed and addressed.
- [ ] Independent review is complete where risk requires it; blocking findings are resolved.
- [ ] Documentation, changelog, and ADRs are updated when applicable.
- [ ] Migration and recovery evidence is available for risky persistent-data or production changes.
- [ ] Delivery, release, and handoff records contain links to evidence, open limitations, and operational ownership.

**Not done:** a passing build without appropriate tests; an agent's unsupported success claim; a missing mandatory review; or a blocked security control disguised as a pass.

Completion and production deployment are distinct decisions. The project release owner determines when an accepted change can safely ship.
