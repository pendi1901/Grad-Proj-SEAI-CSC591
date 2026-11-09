# Dataset analysis

The three MOOT data sets behind the three domains, why each was
picked, and the candidates we looked at and set aside. The files are in
`data/raw/`, copied unchanged from
[timm/moot](https://github.com/timm/moot/tree/master/optimize).

MOOT's header row sets each column's role. A name that starts with a
lowercase letter is symbolic; a trailing `+` or `-` marks a goal to
maximise or minimise; everything else is a numeric input.

## The three domains side by side

| | pom3a | health | hr |
|---|---|---|---|
| MOOT type | Software process model | Software project health | Behavioural |
| File | `pom3a.csv` | `Health-ClosedIssues0000.csv` | `WA_Fn-UseC_-HR-Employee-Attrition.csv` |
| Client | agile delivery office | open-source foundation | staff retention office |
| Rows × columns | 20,000 × 12 | 10,000 × 8 | 1,470 × 35 |
| Inputs | 9, all numeric | 5: 4 numeric, 1 symbolic | 26 used: 18 numeric, 8 symbolic |
| Goals | 3 (cost, score, idle: all minimise) | 3 (MRE minimise; accuracy, PRED40 maximise) | 3 (years at company, in role, with manager: all maximise) |
| Where it comes from | a simulator (POM3) | logged hyperparameter runs of a random forest | real employee records (IBM sample) |
| Rows used per run | 1,024 sampled (`cap`) | 1,024 sampled | 1,024 sampled |

They differ in what a row is (a simulated project, a model setting, a
person), in size, and in column types. That matters: the brief warns
against "three domains that are one domain wearing three hats".

## What each one needed

**pom3a.** Domain 1: the ladder was built and measured on it. Every
input is a 0–1 knob, so it is the cleanest case. Two certify verdicts
(asks 3 and 13) flip with the random seed, so they are reported as
5-seed tallies.

**health.** No new library code; only Makefile settings. The goals are
squeezed near their best values (the chooser and random both score about
99 out of 100), so methods are hard to tell apart here.

**hr.** The only domain with many symbolic columns. Six columns are
ignored: an ID, three constants, and two that are tenure in disguise
(`TotalWorkingYears`, `YearsSinceLastPromotion`). Those two dominated
every tree until they were dropped on Nov 8. Fixes may only change
columns the office controls (`--change`, set in the Makefile).

## Column tables

### `pom3a.csv` (20,000 rows × 12 columns)

| Column | Role | Kind | Range / values |
|---|---|---|---|
| `Culture` | input | numeric | 1.22e-05 – 1 |
| `Criticality` | input | numeric | 1.67e-05 – 1 |
| `Criticality Modifier` | input | numeric | 1.85e-05 – 1 |
| `Initial Known` | input | numeric | 2.07e-05 – 1 |
| `Inter-Dependency` | input | numeric | 1.57e-06 – 1 |
| `Dynamism` | input | numeric | 4.9e-06 – 1 |
| `Size` | input | numeric | 0.000125 – 1 |
| `Plan` | input | numeric | 1.16e-05 – 1 |
| `Team Size` | input | numeric | 3.74e-05 – 1 |
| `Cost-` | goal, minimise | numeric | 0.0116 – 1 |
| `Score-` | goal, minimise | numeric | 0 – 1 |
| `Idle-` | goal, minimise | numeric | 0 – 1 |

### `Health-ClosedIssues0000.csv` (10,000 rows × 8 columns)

| Column | Role | Kind | Range / values |
|---|---|---|---|
| `MRE-` | goal, minimise | numeric | 0 – 1 |
| `ACC+` | goal, maximise | numeric | 0 – 1 |
| `PRED40+` | goal, maximise | numeric | 0 – 1 |
| `N_estimators` | input | numeric | 10 – 200 |
| `criterion` | input | symbolic | absolute_error, poisson, squared_error |
| `Min_sample_leaves` | input | numeric | 1 – 20 |
| `Min_impurity_decrease` | input | numeric | 0 – 10 |
| `Max_depth` | input | numeric | 1 – 20 |

### `WA_Fn-UseC_-HR-Employee-Attrition.csv` (1,470 rows × 35 columns)

| Column | Role | Kind | Range / values |
|---|---|---|---|
| `Age` | input | numeric | 18 – 60 |
| `attrition` | input | symbolic | No, Yes |
| `businessTravel` | input | symbolic | Non-Travel, Travel_Frequently, Travel_Rarely |
| `DailyRate` | input | numeric | 102 – 1.5e+03 |
| `department` | input | symbolic | Human Resources, Research & Development, Sales |
| `DistanceFromHome` | input | numeric | 1 – 29 |
| `Education` | input | numeric | 1 – 5 |
| `educationField` | input | symbolic | Human Resources, Life Sciences, Marketing, Medical … (6 values) |
| `EmployeeCount` | ignored (constant) | numeric | 1 – 1 |
| `EmployeeNumber` | ignored (ID) | numeric | 1 – 2.07e+03 |
| `EnvironmentSatisfaction` | input | numeric | 1 – 4 |
| `gender` | input | symbolic | Female, Male |
| `HourlyRate` | input | numeric | 30 – 100 |
| `JobInvolvement` | input | numeric | 1 – 4 |
| `JobLevel` | input | numeric | 1 – 5 |
| `jobRole` | input | symbolic | Healthcare Representative, Human Resources, Laboratory Technician, Manager … (9 values) |
| `JobSatisfaction` | input | numeric | 1 – 4 |
| `maritalStatus` | input | symbolic | Divorced, Married, Single |
| `MonthlyIncome` | input | numeric | 1.01e+03 – 2e+04 |
| `MonthlyRate` | input | numeric | 2.09e+03 – 2.7e+04 |
| `NumCompaniesWorked` | input | numeric | 0 – 9 |
| `over18` | ignored (constant) | symbolic | Y |
| `overTime` | input | symbolic | No, Yes |
| `PercentSalaryHike` | input | numeric | 11 – 25 |
| `PerformanceRating` | input | numeric | 3 – 4 |
| `RelationshipSatisfaction` | input | numeric | 1 – 4 |
| `StandardHours` | ignored (constant) | numeric | 80 – 80 |
| `StockOptionLevel` | input | numeric | 0 – 3 |
| `TotalWorkingYears` | ignored (tenure leak) | numeric | 0 – 40 |
| `TrainingTimesLastYear` | input | numeric | 0 – 6 |
| `WorkLifeBalance` | input | numeric | 1 – 4 |
| `YearsAtCompany+` | goal, maximise | numeric | 0 – 40 |
| `YearsInCurrentRole+` | goal, maximise | numeric | 0 – 18 |
| `YearsSinceLastPromotion` | ignored (tenure leak) | numeric | 0 – 15 |
| `YearsWithCurrManager+` | goal, maximise | numeric | 0 – 17 |

## Candidates we looked at and set aside

| MOOT type | File | Ran all 20 asks? | Why not picked |
|---|---|---|---|
| Software process model | `nasa93dem.csv` | yes (extra domain) | Only 93 rows. Kept as transfer evidence: it found a hang in the chooser. |
| Human health data | `Medical_Data_and_Hospital_Readmissions.csv` | yes (extra domain) | Its one yes/no goal pins both the chooser and random at 100, so it cannot tell methods apart. |
| Software project health | `Health-Commits0000.csv` | yes (extra domain) | The same kind of data as health: it would be the same domain twice. |
| Software process model | `xomo_flight.csv` | yes (Nov 9) | The same family of model as nasa93dem and close to pom3a; size (KLOC) explains almost everything. |
| Human health data | `Life_Expectancy_Data.csv` | yes (Nov 9) | A strong candidate (real data, clear verdicts), but health was already pre-registered at `step0`. |

The three extra domains are still in the repo (`make demo D=nasa`, and so
on; they read from a MOOT clone made on first use).
