# Requirements (six domains, one codebase)

Six clients, six MOOT data sets, twenty asks each. The first three
were written down before any code (tag `step0`). The last three were
added on Nov 6, after the ladder existed, to test transfer.

Ask *N* in every domain demos the same skill, so later
domains test whether the domain-1 machinery transfers.

| domain | client | data | doc |
|--------|--------|------|-----|
| pom3a  | agile delivery office | `process/pom3a.csv` (20,000 × 12) | [requirements_pom3a.md](requirements_pom3a.md) |
| health | open-source health forecasting | `hpo/Health-ClosedIssues0000.csv` (10,000 × 8) | [requirements_health.md](requirements_health.md) |
| hr     | staff retention office | `behavior_data/WA_Fn-UseC_-HR-Employee-Attrition.csv` (1,470 × 35) | [requirements_hr.md](requirements_hr.md) |
| nasa   | NASA project estimation office | `process/nasa93dem.csv` (93 × 29) | [requirements_nasa.md](requirements_nasa.md) |
| readmit | hospital readmissions team | `health_data/Medical_Data_and_Hospital_Readmissions.csv` (25,000 × 65) | [requirements_readmit.md](requirements_readmit.md) |
| commits | open-source commit forecasting | `hpo/Health-Commits0000.csv` (10,000 × 8) | [requirements_commits.md](requirements_commits.md) |

Skills per ask (the same in every domain):

| asks | skill |
|------|-------|
| 1, 11 | remember |
| 2, 12 | guess |
| 3, 13 | certify |
| 4, 14 | flow |
| 5, 15 | blame |
| 6, 16 | justify |
| 7, 17 | choose |
| 8, 18 | fix |
| 9, 19 | spot |
| 10, 20 | race |

## Submitted domains

**pom3a, health and hr** are the three submitted domains, the three
pre-registered at `step0`. nasa, readmit and commits are extra transfer
evidence. (`commits` uses the same knobs as `health`, so it is not
counted as a new domain.)

## Baseline and change control

- **`step0` (Nov 6):** the first three requirement docs, before any
  code. At that tag they were named `docs/req-<domain>.md`; they were
  renamed to `docs/requirements_<domain>.md` on Nov 9, with no change
  to the text.
- **Nov 8 amendment (wording only, every skill tag unchanged):**
  pom3a ask 1, hr asks 2, 8 and 18. Each doc ends with a note saying
  what changed and why. The `step0` wording is still at that tag:
  `git show step0:docs/req-hr.md`.

Status: awaiting the lecturer's OK.
