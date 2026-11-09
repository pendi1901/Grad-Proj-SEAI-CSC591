# CSC 591 project: initial deliverable (Nov 9)

**Group:** G2
**Team:** Luke Shafer (lashafer), Pendyala Ritvik (rpendya) (0048)
**Repo:** https://github.com/pendi1901/Grad-Proj-SEAI-CSC591 (tags `step0` to `step20`)

## 1. Pre-registered claim

We committed both hypotheses and our win conditions at tag `step0`,
before writing any code. Full text: `docs/hypotheses.md`.

> **The Timm hypothesis.** Neuro-symbolic systems improve when their
> symbolic half is factored into small reusable structures. The ten
> skills are synonyms: one machine (cluster, tree, leaf) wearing ten
> hats. Hence an LLM, or a human, extends a well-factored library
> with less new code, and fewer errors, than a monolithic one.

> **The rival.** The ten skills are ten separate problems. Factoring
> buys nothing: skill i+1 costs about the same whoever writes it, and
> whatever library sits underneath.

**How we decide.** We measure new lines of code per step, and only
count a step if its demo runs and its test passes. The baseline is the
treatments where the LLM is not told to reuse earlier code (1, 3 and 5).
Every comparison uses the `same` test (Cohen's d, Kolmogorov-Smirnov
and Cliff's delta must all agree).

- **The Timm hypothesis wins a domain** if both are true:
  1. steps 11–20 need fewer new lines than steps 1–10, in treatment 7
     and in at least two of treatments 2, 4 and 6;
  2. telling the LLM to reuse code gives fewer new lines than not
     telling it, in at least two of the pairs (2 vs 1, 4 vs 3, 6 vs 5).
- **The rival wins a domain** if `same` finds no difference in both of
  those checks.
- **Any other result** is reported as a split.
- **Prediction for domains 2 and 3:** they need less than 10% new code.

**Domains and data.** We have three clients, three MOOT data sets and
one shared codebase.
- **pom3a:** an agile delivery office choosing how to set up projects.
  `process/pom3a.csv` has 20,000 simulated projects with 9 settings;
  the goals are cost, score and idle time.
- **health:** an open-source foundation tuning the model that forecasts
  closed issues. `hpo/Health-ClosedIssues0000.csv` has 10,000
  random-forest settings; the goals are error (MRE), accuracy and
  PRED40.
- **hr:** a retention office studying which employees stay.
  The IBM HR attrition data has 1,470 employees, with both text and
  number columns; the goals are years at the company, in the current
  role, and with the current manager.

## 2. Requirements (3 domains × 20 asks)

`docs/requirements_pom3a.md`, `docs/requirements_health.md` and
`docs/requirements_hr.md` each list 20 asks in the client's own words,
and each ask is tagged with the skill it shows. Asks 1–10 cover the ten
skills once, and asks 11–20 cover them a second time. We also wrote 20
asks each for three extra domains (`requirements_nasa.md`,
`requirements_readmit.md`, `requirements_commits.md`).

## 3. What runs now: domain 1 (pom3a)

- There are 20 tagged steps. `make test` runs 35 tests, and
  `make askNN D=pom3a` runs any ask with one command. The same commands
  work for every other domain (`D=health|hr|nasa|readmit|commits`).
- **New lines of code per step** (`make loc`, `results/loc.md`): step 1
  added 167 lines (28% of the total), steps 2–10 added 14–58 each, and
  steps 11–20 added 9–21 each. `same` says steps 11–20 needed less code
  than steps 1–10 (Cliff's delta 0.72), and still does when step 1 is
  left out (0.69).
- **Cost of the other domains** (`results/transfer.md`):
  - health needed 0 new lines in `ezl/`, plus 2 lines of settings in the
    Makefile.
  - hr first needed 0 new lines plus 3 lines of settings. On Nov 8 we
    reworded asks 8 and 18 so a fix may only change things the office
    controls; that needed 13 new lines in `ezl/` (2.2% of the 590).
  - The three extra domains (nasa, readmit, commits) together needed
    10 new lines (1.7%, tag `domains6`). They fixed a bug where the
    chooser looped forever on very small data (nasa has 93 rows),
    read TRUE/FALSE values as 1/0, and shortened the drift window for
    small data.
- **Early findings.**
  - On five of the six domains, our chooser (ask 7) does worse than
    picking 50 random rows and keeping the best (ask 10); `same` confirms
    the difference. On readmit both score 100, so they tie. The project
    brief expects this ("When ezr loses"), and tuning the chooser is our
    next step.
  - In hr, `TotalWorkingYears` and `YearsSinceLastPromotion` closely
    track how long someone has been at the company, so they gave the
    answer away. We dropped both; `JobLevel` is now the biggest factor.

## 4. Acknowledgment

Claude Code generated the implementation, tests and scripts and helped
with requirements, runs and documentation; our team reviewed and corrected
the work. This prototype is not the human-only treatment 7.
