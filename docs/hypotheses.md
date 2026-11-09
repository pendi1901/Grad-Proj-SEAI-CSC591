# Pre-registered claim

Written and committed (tag `step0`) before any code.

## The two hypotheses (verbatim from uproj.md)

> **The Timm hypothesis.** Neuro-symbolic systems improve when
> their symbolic half is factored into small reusable structures.
> The ten skills are synonyms: one machine (cluster, tree, leaf)
> wearing ten hats. Hence an LLM, or a human, extends a
> well-factored library with less new code, and fewer errors, than
> a monolithic one.

> **The rival.** The ten skills are ten separate problems. Factoring
> buys nothing: skill i+1 costs about the same whoever writes it,
> and whatever library sits underneath.

## Metric and baseline

- **Metric:** new lines of code per step. For treatment 7 (hand-built
  ladder) this is `git diff --numstat step(i-1) step(i) -- ezl`
  (`experiments/loc.sh`). For LLM treatments 1–6 it is the line count of what
  the LLM returns for skill i. A step only counts if its demo runs
  and its test passes.
- **Baseline:** the no-reuse treatments (1, 3, 5): an LLM asked for
  each skill cold.
- **Statistics:** every comparison uses `same` (Cohen's d ≤ 0.35,
  Cliff's delta ≤ 0.195, KS ≤ 1.36, all three must agree), ported
  in `ezl/s03_certify.py`. A difference is only reported when `same`
  says the two samples differ.

## Win conditions (fixed now, judged on Nov 30)

**The Timm hypothesis wins, per domain, if both of these hold:**

1. *Falling bars:* `same` says new LOC for steps 11–20 is smaller
   than for steps 1–10, in treatment 7 and in at least two of the
   three reuse treatments (2, 4, 6).
2. *Reuse beats cold:* for each library (plain Python, scikit-learn,
   ezr), `same` says the reuse treatment's new-LOC-per-step is
   smaller than its no-reuse twin's (2 < 1, 4 < 3, 6 < 5), in at
   least two of the three pairs.

**Transfer (across domains):** the hypothesis also predicts that
domains 2 and 3 need less than 10% new code relative to domain 1,
counted as new lines in `ezl/` plus per-domain settings.

**The rival wins, per domain, if** `same` calls steps 11–20 and
steps 1–10 the same, *and* calls at least two of the three reuse /
no-reuse pairs the same.

**Anything else is a split verdict**, reported as such: which
library, which domain, which steps.

## Domains and data

Three clients, three MOOT data sets, one shared codebase (`ezl/`,
plain Python, standard library only). **pom3a**
(`process/pom3a.csv`, 20,000 simulated agile projects, 9 knobs, 3
goals: cost, score, idle) is an agile delivery office choosing
project setups. **health** (`hpo/Health-ClosedIssues0000.csv`,
10,000 random-forest settings, 5 knobs, 3 goals: error, accuracy,
PRED40) is an open-source foundation tuning its closed-issue
forecaster. **hr** (`behavior_data/WA_Fn-UseC_-HR-Employee-Attrition.csv`,
1,470 employees, ~30 attributes, 3 goals: years at the company, in
role, with manager) is a retention office studying who stays. They
differ in size (1.5k–20k rows), in kind (simulation output vs
hyperparameter logs vs people records), and in column types (all
numeric vs mixed symbolic). Pure Python on the larger sets samples
at most 1,024 rows per run (`cap`), recorded as a threat to validity.

## Amendment (Nov 6, after step 20)

Three more domains were added after the ladder was built: **nasa**
(`process/nasa93dem.csv`), **readmit**
(`health_data/Medical_Data_and_Hospital_Readmissions.csv`) and
**commits** (`hpo/Health-Commits0000.csv`). Because they came after
the code, they are a transfer test, not part of the pre-registration.
The win conditions above apply to them unchanged. Any code they force
into `ezl/` is counted as their transfer cost
(`git diff --numstat step20 domains6 -- ezl`).
