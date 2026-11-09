# Test report (Nov 6)

What was run, what passed, and what the results do and don't support.
All runs used the repo at tag `domains6`, except the HR rerun (†), made after commit `355679b`. The sweep script is `experiments/sweep.py`; raw outputs are not kept, but the
commands below rerun everything.

## 1. Does every step stand on its own?

A fresh clone was checked out at each tag in turn, and the unit tests
present at that tag were run.

| tag | tests | result | | tag | tests | result |
|---|---:|---|---|---|---:|---|
| step1 | 5 | OK | | step11 | 22 | OK |
| step2 | 7 | OK | | step12 | 23 | OK |
| step3 | 10 | OK | | step13 | 24 | OK |
| step4 | 11 | OK | | step14 | 25 | OK |
| step5 | 14 | OK | | step15 | 26 | OK |
| step6 | 16 | OK | | step16 | 27 | OK |
| step7 | 18 | OK | | step17 | 28 | OK |
| step8 | 19 | OK | | step18 | 30 | OK |
| step9 | 20 | OK | | step19 | 31 | OK |
| step10 | 21 | OK | | step20 | 32 | OK |
| | | | | domains6 | 33 | OK |

All 21 tags pass, so the histogram (`make loc`, 590 lines in total)
comes from steps that each worked at the time they were tagged.

**Known defect in tags step7–step20:** `acquire` (the chooser) loops
forever when it has budget left but fewer than 6 unlabelled rows. The
three original domains never hit it; NASA (93 rows) did. It was fixed
at `domains6`, and a regression test was added. If a marker checks out
an old tag and runs `make ask07 D=nasa`, it will hang.

## 2. Does every ask run on every domain?

Every one of the 20 asks, on all six domains, at seed 1:

| domain | rows used | asks OK | total time | slowest ask |
|---|---:|---:|---:|---|
| pom3a | 1,024 of 20,000 | 20/20 | 92 s | ask09 (15 s) |
| health | 1,024 of 10,000 | 20/20 | 45 s | ask09 (8 s) |
| hr | 1,024 of 1,470 | 20/20 | 147 s | ask09 (32 s) |
| nasa | 93 | 20/20 | 7 s | ask10 (3 s) |
| readmit | 1,024 of 25,000 | 20/20 | 128 s | ask09 (28 s) |
| commits | 1,024 of 10,000 | 20/20 | 45 s | ask09 (8 s) |

No crashes and no errors. ask09 (spot) is the slowest everywhere,
because it sorts 256 reference rows for every row. The times were
measured with six domains running in parallel, so single runs are faster.

## 3. Do the verdicts survive a change of seed?

The asks that end in a yes/no verdict were rerun at seeds 1–5. The
seed changes which 1,024 rows are sampled, and every random choice
after that.

| ask | pom3a | health | hr | nasa | readmit | commits |
|---|---|---|---|---|---|---|
| 3: setting matters on all goals? | **3 real / 2 noise** | 5 real | 5 noise | 5 noise | 5 real | 5 real |
| 13: setting moves one goal? | **3 real / 2 noise** | 5 noise | 5 noise | 5 real | **1 real / 4 noise** | 5 noise |
| 10: chooser vs 50 random | random wins 5/5 | random 2, tie 3 | random wins 5/5 † | random wins 5/5 | tie 3, medians tie 2* | random 2, tie 3 |
| 20: guesses vs the average | ours wins 2 of 3 goals, ties Idle, 5/5 | ours 5/5 | ours 5, tie 9, average 1 (of 15 goal-seeds) † | ours 5/5 (one tie) | ours 5/5 | ours 5/5 |

Median win for ask 7 over the 5 seeds (100 = best row of all, 0 = median row):

| pom3a | health | hr | nasa | readmit | commits |
|---|---|---|---|---|---|
| 58–76 | 99.1–99.6 | 80.8–91.4 † | 37–85 | 100 (ceiling) | 98.4–99.0 |

**What holds up:**
- **Guessing mostly works.** Nearest-neighbour guesses beat "quote
  the average" in five domains at every seed, apart from a few ties.
  HR is the exception once its leak is removed: on day-one data the
  guesses mostly tie the average, and lose once (seed 2, years in role).
- **The chooser never beats random sampling.** Over 30 domain-seed
  runs it was never certified better. (Before the HR leak was removed
  it won once, at HR seed 5; that win went away with the leak.) This is the clearest result in the repo,
  and it is negative.

**What does not hold up:**
- **pom3a's ask 3 and ask 13 flip with the seed.** "Do small teams do
  better?" and "Does planning cut idle time?" have no stable answer on
  1,024 sampled rows. Don't quote either verdict from a single run.
  Either raise `cap` or report the 5-seed tally.
- **readmit's ask 13** is real at seed 1 only.

\* **A reporting bug in ask 10 (fixed after `domains6`):** when both
medians hit the same value (readmit: 100 vs 100), but `same` still
said the two distributions differ, the code printed "random really is
better", because it broke the tie on medians only. It now prints
"different, but the medians tie", and names the higher mean (random,
at both seeds). A unit test covers it (34 tests). Health's 99.6 vs
99.7 still reads as a win for random at seeds 1–2: `same` calls it
real, but it is 0.1 points, so call it a practical tie in the report.

## 4. NASA with a smaller budget (`--budget=20`)

The suggestion was to run NASA's budgeted asks with 20 labels instead
of 50, so the budget isn't more than half the data.

| seed | ask 7 median win | ask 10: ours vs random | verdict |
|---|---:|---|---|
| 1 | 51.4 | 51.4 vs 79.4 | random better |
| 2 | 37.4 | 37.4 vs 84.7 | random better |
| 3 | 42.6 | 42.6 vs 86.1 | random better |
| 4 | 30.9 | 30.9 vs 52.8 | random better |
| 5 | 30.2 | 30.2 vs 84.7 | random better |

A smaller budget makes the test fair, but it doesn't rescue the
chooser: random still wins 5/5. With budget 20, the chooser trains its
tree on 15 labels from 46 rows and then gets just 5 picks. Ask 17 with
budget 20 ran at 4 of 5 seeds. At the fifth, only 11 rows matched the
fixed settings, so it said "too few rows" and stopped, which is the
intended behaviour.

## 5. Which three domains to submit

**Recommended: pom3a, health, hr.**
- They are the three in the step0 pre-registration.
- All their asks run, and nothing in them is degenerate.
- One caveat: pom3a's two certify verdicts are seed-unstable, so
  report them as tallies.

| domain | keep as main? | why |
|---|---|---|
| pom3a | yes | Large and numeric. Two certify verdicts are seed-unstable (report the tally). |
| health | yes | Stable on every check. |
| hr | yes | Stable. The `TotalWorkingYears` leak is fixed (Nov 8, see below). |
| nasa | extra | Its asks are fair at budget 20, but the clustering asks (1, 11) only make 2–3 groups. Good transfer evidence: 10 lines. |
| readmit | extra | The yes/no goal makes choose/race hit the ceiling (100 vs 100), so they can't tell methods apart. |
| commits | extra | Behaves almost the same as health (same knobs): it reproduces health, it isn't a new domain. |

## 5b. HR rerun after the Nov 8 changes

HR asks 2, 8 and 18 were reworded (see the note at the end of
`requirements_hr.md`). Two tenure-in-disguise columns are now dropped, and fixes
may only change pay, overtime, travel, level, role, training, stock
and work-life balance (new `--change` option, 13 lines in `ezl/`, one
new test, 35 tests in all). All 20 HR asks still run. What moved:

- **The top driver** of tenure is now `JobLevel`, not `TotalWorkingYears`.
- **Fixes** now read like "raise JobLevel above 1; MonthlyIncome above
  10,239", with no "make them older".
- **Guessing got harder, honestly:** with the leak gone, ask 20 over 5
  seeds × 3 goals is ours 5, tie 9, average 1 (before: ours 3 seeds,
  ties 2). The chooser lost all 5 races (before: lost 4, won 1). Asks 3
  and 13 are still noise at every seed. The HR column above (marked †)
  is the rerun, made with `experiments/sweep.py`.

## 6. Before Nov 9 / Nov 30

1. ~~Fix the ask-10 tie-breaker~~ (done: a new commit after `domains6`, no retag).
2. For any verdict quoted in the report, quote the 5-seed tally, not a single run.
3. Tune the chooser before the LLM treatments: it loses everywhere, and uproj.md
   expects that ("When ezr loses"). Two things to try: compare its
   acquire-only pick against the tree-then-check pick, and try a larger `check`.
4. Then run the LLM treatments 1–6 (not run yet).

## Rerun

```sh
make test                                   # current tag
for t in $(seq 1 20); do git checkout -q step$t && python3 -B -m unittest discover -s tests -q; done; git checkout -q master
make demos                                  # every ask, every domain, seed 1
python3 -B experiments/sweep.py out.json hr          # every ask + the 5-seed verdicts, one domain
python3 -B -m ezl ask10 --file=moot/optimize/process/pom3a.csv --seed=3     # one ask, another seed
python3 -B -m ezl ask07 ask10 ask17 --file=moot/optimize/process/nasa93dem.csv --budget=20 --fixed=rely,cplx
```
