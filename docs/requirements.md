# Requirements

We wrote 20 asks for each domain, in the client's words. Ask N demos
the same skill in every domain, so we can check whether code written
for pom3a also answers the other domains' asks.

## Domains

**pom3a, health and hr are the three domains we are submitting.** We
wrote their requirements at tag `step0`, before any code. We added
nasa, readmit and commits on Nov 6, after step 20, to get more evidence
on how well the code carries over. `commits` uses the same settings as
`health`, so we do not count it as a new kind of domain.

| domain | client | data (rows × columns) | requirements |
|--------|--------|------|-----|
| pom3a  | agile delivery office | `process/pom3a.csv` (20,000 × 12) | [requirements_pom3a.md](requirements_pom3a.md) |
| health | open-source foundation forecasting closed issues | `hpo/Health-ClosedIssues0000.csv` (10,000 × 8) | [requirements_health.md](requirements_health.md) |
| hr     | staff retention office | `behavior_data/WA_Fn-UseC_-HR-Employee-Attrition.csv` (1,470 × 35) | [requirements_hr.md](requirements_hr.md) |
| nasa (extra) | NASA project estimation office | `process/nasa93dem.csv` (93 × 29) | [requirements_nasa.md](requirements_nasa.md) |
| readmit (extra) | hospital readmissions team | `health_data/Medical_Data_and_Hospital_Readmissions.csv` (25,000 × 65) | [requirements_readmit.md](requirements_readmit.md) |
| commits (extra) | open-source fund forecasting commits | `hpo/Health-Commits0000.csv` (10,000 × 8) | [requirements_commits.md](requirements_commits.md) |

## Skill for each ask (the same in every domain)

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

## Changes since `step0`

- **Nov 9, file names:** at `step0` the files were called
  `docs/req-<domain>.md`. On Nov 9 we renamed them to
  `docs/requirements_<domain>.md` and rewrote the short introductions
  in plainer language. We did not change the asks themselves.
- **Nov 8, ask wording:** we reworded pom3a ask 1 and hr asks 2, 8 and
  18. Every ask still demos the same skill. Each changed file ends with
  a note saying what changed and why. The `step0` wording is still in
  git, for example `git show step0:docs/req-hr.md`.

Status: waiting for the lecturer's OK.
