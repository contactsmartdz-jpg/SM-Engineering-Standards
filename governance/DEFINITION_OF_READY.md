# Definition of Ready (DoR)

**Status:** Draft 0.1

**Ready means actionable, not fully documented.** A work item can begin with its existing issue or task; an additional specification document is not required by default.

## Fast / Standard
- [ ] User outcome and smallest usable feature are clear.
- [ ] One to three observable acceptance criteria are recorded (including relevant failure behavior).
- [ ] Change-level risk track and basic verification plan are identified.
- [ ] Any essential missing input or permission that would prevent safe implementation is identified.

## Critical — additional prerequisites before risky action
- [ ] Trust boundaries, sensitive-data/authorization impacts, owner, and environmental scope are explicit.
- [ ] Required approval is obtained before executing a sensitive or irreversible operation.
- [ ] Applicable recovery, compatibility, isolation, and safety verification approach exists.

Open non-critical design or usability questions are **feedback items**, not automatic blockers to starting a safe vertical slice. Do not repeatedly request decisions already captured in the work item.

See [Development Policy](DEVELOPMENT_POLICY.md) and [Production Readiness](PRODUCTION_READINESS_POLICY.md).
