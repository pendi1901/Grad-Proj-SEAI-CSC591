# CSC 591 project, initial deliverable (Nov 9)

**Group:** _names_ · **Repo:** https://github.com/pendi1901/Grad-Proj-SEAI-CSC591 (tags `step0`..`step20`)

## 1. The pre-registered claim

> **The Timm hypothesis.** Neuro-symbolic systems improve when their
> symbolic half is factored into small reusable structures. The ten
> skills are synonyms: one machine (cluster, tree, leaf) wearing ten
> hats. Hence an LLM, or a human, extends a well-factored library
> with less new code, and fewer errors, than a monolithic one.

> **The rival.** The ten skills are ten separate problems. Factoring
> buys nothing: skill i+1 costs about the same whoever writes it, and
> whatever library sits underneath.

**Win conditions** (committed at `step0`, before code; full text in
`docs/hypotheses.md`). Metric: new LOC per step, counted only for steps
whose demo runs and whose test passes. Baseline: the no-reuse
treatments 1, 3, 5. Every comparison uses `same` (Cohen + KS +
Cliff's delta). *Timm wins* a domain if `same` says steps 11–20 need
less new code than steps 1–10 (in treatment 7 and in at least two of
treatments 2, 4, 6), **and** reuse beats cold in at least two of the
pairs 2<1, 4<3, 6<5. *The rival wins* if `same` calls both of those
ties. Anything else is reported as a split verdict. Transfer
prediction: domains 2 and 3 need less than 10% new code.

**Domains and data.** Three clients, three MOOT sets, one codebase.
*pom3a*: an agile delivery office choosing project setups
(`process/pom3a.csv`, 20k simulated projects, 9 knobs, goals: cost,
score, idle). *health*: an open-source foundation tuning its
closed-issue forecaster (`hpo/Health-ClosedIssues0000.csv`, 10k
random-forest settings, goals: MRE, accuracy, PRED40). *hr*: a
retention office studying who stays (IBM HR attrition, 1,470
employees, mixed symbolic/numeric, goals: years at the company, in
role, with manager).

## 2. Requirements (3 × 20 asks, awaiting the lecturer's OK)

`docs/requirements_pom3a.md`, `docs/requirements_health.md`, `docs/requirements_hr.md` (plus
extra domains `requirements_nasa.md`, `requirements_readmit.md`, `requirements_commits.md`): twenty
asks each, in the client's words, each tagged with its skill (asks 1–10
cover the ten skills once, asks 11–20 cover them again).

## 3. What runs now: domain 1's ladder (treatment 7, hand-built)

- 20 tagged steps; `make test` runs 35 tests; `make askNN D=pom3a`
  runs any ask in one command. The same commands run on every
  other domain (`D=health|hr|nasa|readmit|commits`).
- **New LOC per step** (`make loc`; `results/loc.md`): step 1 = 167 (28%); steps 2–10 =
  14–58; steps 11–20 = 9–21. `same` says steps 11–20 < steps 1–10
  (Cliff's δ 0.72), and still says so with step 1 left out (δ 0.69).
- **Transfer so far** (`results/transfer.md`): domain 2 (health) added **0 lines** to `ezl/`
  (2 lines of Makefile settings). Domain 3 (hr) first needed 0 lines
  plus 3 lines of settings and the `drop` option written in step 1;
  after the Nov 8 rewording of asks 8 and 18 ("change only what the
  office can change") it needed **13 lines** in `ezl/` (2.2% of the
  ladder), for a `change` option that limits which columns a fix may
  touch. Three more
  domains, added after step 20 (nasa93dem, hospital readmissions,
  OSS commits), cost **10 new lines in `ezl/`** (1.7% of the ladder,
  tag `domains6`). Those lines fixed a hang in the chooser on tiny
  pools (NASA has 93 rows), read TRUE/FALSE cells, and shrank the
  drift windows for small data.
- **Early findings, kept as-is.** On five of the six domains the
  active learner (ask 7) **loses** to "measure 50 random rows and
  keep the best" (ask 10, `same`-certified); on readmissions both hit
  the ceiling and tie. That is the "ezr loses at first"
  case; tuning comes next. In HR, `TotalWorkingYears` dominated the
  tenure trees (a leak); it and `YearsSinceLastPromotion` are now
  dropped, and `JobLevel` becomes the top driver.

## 4. Next (to Nov 30)

The LLM treatments 1–6 (headless `claude -p`, one fresh directory per
trial, no memory, N ≥ 3, the goal is 10), then `same` tables per
domain, tuning the chooser, and the report.
