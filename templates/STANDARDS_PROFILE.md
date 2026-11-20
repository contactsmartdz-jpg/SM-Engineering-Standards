# Standards Adoption Profile — Template

> Copy this template into the **adopting project**. Do not submit project-specific profiles to the central standards repository.

## Project metadata
- Project/repository: [name]
- Accountable owner: [role or team]
- Effective date: [YYYY-MM-DD]
- Standard version: [immutable release tag and/or commit SHA]
- Profile version: [version]
- Risk classification: [low / moderate / high; explain]

## Scope
- Included components: [areas]
- Excluded components: [areas and rationale]
- Applicable obligations: [legal / contractual / regulatory requirements if relevant]

## Local implementation
| Standard area | Tool or control | Evidence location | Required? | Owner |
| --- | --- | --- | --- | --- |
| Clean code | [formatter/linter/review] | [CI or report] | [yes/no + why] | [role] |
| Architecture | [ADR and review] | [path] | [yes/no + why] | [role] |
| Security | [scans and access tests] | [path] | [yes/no + why] | [role] |
| Testing | [test suites] | [path] | [yes/no + why] | [role] |
| Dependencies | [audit and license check] | [path] | [yes/no + why] | [role] |
| Release safety | [deploy/recovery gates] | [path] | [yes/no + why] | [role] |

## Change controls
- Mainline protection or equivalent: [configuration and evidence]
- Independent reviewer requirements: [review model]
- High-risk approval authority: [role]
- Exception registry: [link]
- Data classification and handling: [link]

## Verification
- Baseline assessment date and findings: [date/link]
- Required quality-gate identifiers: [QG-...]
- Last verified revision: [commit]
- Unverified or planned controls: [list]
- Next reassessment: [date]

Approval: [accountable owner / date]
