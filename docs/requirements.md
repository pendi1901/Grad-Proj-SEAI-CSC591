# Requirements (six domains, one codebase)

Six clients, six MOOT data sets, twenty asks each. The first three
were written down before any code (tag `step0`). The last three were
added on Nov 6, after the ladder existed, to test transfer.

Ask *N* in every domain demos the same skill, so later
domains test whether the domain-1 machinery transfers.

| domain | client | data | doc |
|--------|--------|------|-----|
| pom3a  | agile delivery office | `process/pom3a.csv` (20,000 × 12) | [req-pom3a.md](req-pom3a.md) |
| health | open-source health forecasting | `hpo/Health-ClosedIssues0000.csv` (10,000 × 8) | [req-health.md](req-health.md) |
| hr     | staff retention office | `behavior_data/WA_Fn-UseC_-HR-Employee-Attrition.csv` (1,470 × 35) | [req-hr.md](req-hr.md) |
| nasa   | NASA project estimation office | `process/nasa93dem.csv` (93 × 29) | [req-nasa.md](req-nasa.md) |
| readmit | hospital readmissions team | `health_data/Medical_Data_and_Hospital_Readmissions.csv` (25,000 × 65) | [req-readmit.md](req-readmit.md) |
| commits | open-source commit forecasting | `hpo/Health-Commits0000.csv` (10,000 × 8) | [req-commits.md](req-commits.md) |

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

The gproj rubric asks for three domains. Pick which three to submit
(the other three can be extra transfer evidence). Note that `commits`
uses the same knobs as `health`, so the two together risk counting as
"one domain wearing two hats".

Status: awaiting the lecturer's OK.
