# Standards Adoption Profile — Minimal Template

> Copy into the adopting project's own repository, not the public central standard.

- **Project / accountable owner:**
- **Pinned standard tag or commit:**
- **Effective date and affected components:**
- **Environment boundaries (dev / validation / production):**
- **Risk classification owner and escalation rule:**
- **Functional acceptance owner:**
- **Production release authority:**

## Tracks and applicable controls
| Track | Scope examples | Required validation checks | Required production checks | Reviewer/approver | Evidence location |
| --- | --- | --- | --- | --- | --- |
| Fast | [non-sensitive UI/content] | [quick relevant behavior/build] | [applicable safety and release checks] | [if any] | [existing issue/PR] |
| Standard | [ordinary feature] | [targeted tests] | [applicable controls] | [single review if required] | [existing issue/PR] |
| Critical | [sensitive/irreversible] | [isolation/security/permissions] | [independent review, release safety] | [named owner] | [existing issue/PR] |

- **Tools and alternate evidence if hosted CI is unavailable:**
- **Protected branch / merge requirements (actually configured):**
- **Exception registry and expiry owner:**
- **Recovery and data handling where relevant:**
- **Known gaps (documented / configured / verified):**
- **Next assessment date:**

**Adoption approval:** [accountable owner, date]. Optional cleanup is not automatically a production blocker. This profile may increase controls, but cannot waive mandatory safety controls silently.
