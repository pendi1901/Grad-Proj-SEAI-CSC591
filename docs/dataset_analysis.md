# Data set analysis

This file describes the three MOOT data sets we use for our three
domains, why we picked each one, and the other data sets we tried and
did not pick. The files in `data/raw/` are copied unchanged from
[timm/moot](https://github.com/timm/moot/tree/master/optimize).

In MOOT files, the header row sets each column's role:
- a name starting with a lowercase letter is a text (symbolic) column;
- a name ending in `+` is a goal to maximise, and `-` a goal to minimise;
- every other column is a numeric input.

## The three domains

| | pom3a | health | hr |
|---|---|---|---|
| MOOT category | Software process model | Software project health | Behavioural |
| File | `pom3a.csv` | `Health-ClosedIssues0000.csv` | `WA_Fn-UseC_-HR-Employee-Attrition.csv` |
| Client | agile delivery office | open-source foundation | staff retention office |
| Rows × columns | 20,000 × 12 | 10,000 × 8 | 1,470 × 35 |
| Inputs | 9, all numeric | 5: 4 numeric, 1 text | 26 used: 18 numeric, 8 text |
| Goals | cost, score, idle (all minimise) | MRE (minimise); accuracy, PRED40 (maximise) | years at company, in role, with manager (all maximise) |
| What one row is | one simulated project | one tried setting of a random-forest model | one real employee (IBM sample data) |
| Rows used per run | 1,024 (random sample) | 1,024 (random sample) | 1,024 (random sample) |

We chose three data sets that differ in what a row is, in size and in
column types. The project brief warns against three domains that are
really one domain, and these three are clearly different.

## Notes on each domain

**pom3a.** We built the 20 steps on this domain first. Every input is a
number between 0 and 1, so it is the simplest of the three. Two of the
yes/no asks (3 and 13) give different answers depending on the random
seed, so we report how often each answer came up over 5 seeds.

**health.** This domain needed no new code in `ezl/`, only settings in
the Makefile. Most settings score close to the best possible value
(both our chooser and random picks score about 99 out of 100), so
methods are hard to tell apart here.

**hr.** This is the only domain with many text columns. We ignore six
columns:
- an ID column;
- three columns with the same value for everyone;
- two columns (`TotalWorkingYears`, `YearsSinceLastPromotion`) that
  mostly measure time already spent at the company, which is what we
  predict. Until we dropped them on Nov 8, they decided almost every
  answer.

The fix asks may only change columns the office controls; these are
listed in the Makefile as `--change`.

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

## Data sets we tried and did not pick

| MOOT category | File | Ran all 20 asks? | Why we did not pick it |
|---|---|---|---|
| Software process model | `nasa93dem.csv` | yes (extra domain) | Only 93 rows. We kept it as an extra domain because it exposed a bug in the chooser. |
| Human health data | `Medical_Data_and_Hospital_Readmissions.csv` | yes (extra domain) | It has one yes/no goal, and both our chooser and random picks score 100, so it cannot show which method is better. |
| Software project health | `Health-Commits0000.csv` | yes (extra domain) | It has the same columns as health, so it would count as the same domain twice. |
| Software process model | `xomo_flight.csv` | yes (Nov 9) | It is the same kind of model as nasa93dem and similar to pom3a, and project size alone explains most of the results. |
| Human health data | `Life_Expectancy_Data.csv` | yes (Nov 9) | A good candidate (real data, clear results), but health was already in our pre-registration at `step0`. |

The three extra domains are still in the repo (for example
`make demo D=nasa`). They read from a copy of MOOT that is downloaded
the first time you run them.
