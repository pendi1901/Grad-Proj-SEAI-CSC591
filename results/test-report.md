# Test report

This report lists what we ran, what passed, and which results hold up.
Unless marked with †, all runs used tag `domains6` (Nov 6). Runs marked
† are the hr rerun after commit `355679b` (Nov 8). The script for the
5-seed runs is `experiments/sweep.py`. We did not keep the raw output,
but the commands at the end rerun everything.

## 1. Does every step pass its own tests?

We made a fresh clone, checked out each tag in turn, and ran the tests
that existed at that tag.

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

All 21 tags pass. So every step counted in the lines-of-code table
(`make loc`, 590 lines in total) worked when it was tagged.

**Known bug in tags step7 to step20:** the chooser (`acquire` in
`ezl/s07_choose.py`) loops forever when it still has budget left but
fewer than 6 unmeasured rows. pom3a, health and hr never hit this;
nasa (93 rows) did. We fixed it at tag `domains6` and added a test for
it. Running `make ask07 D=nasa` on an older tag will hang.

## 2. Does every ask run on every domain?

We ran all 20 asks on all six domains, at seed 1:

| domain | rows used | asks OK | total time | slowest ask |
|---|---:|---:|---:|---|
| pom3a | 1,024 of 20,000 | 20/20 | 92 s | ask09 (15 s) |
| health | 1,024 of 10,000 | 20/20 | 45 s | ask09 (8 s) |
| hr | 1,024 of 1,470 | 20/20 | 147 s | ask09 (32 s) |
| nasa | 93 | 20/20 | 7 s | ask10 (3 s) |
| readmit | 1,024 of 25,000 | 20/20 | 128 s | ask09 (28 s) |
| commits | 1,024 of 10,000 | 20/20 | 45 s | ask09 (8 s) |

There were no crashes or errors. Ask 9 (spot) is the slowest in every
domain, because for each row it sorts 256 other rows by distance. We
ran the six domains at the same time, so a single run is faster than
the times shown.

## 3. Do the results change with the random seed?

We reran the asks that give a yes/no answer at seeds 1 to 5. The seed
changes which 1,024 rows are sampled, and every random choice after
that.

| ask | pom3a | health | hr † | nasa | readmit | commits |
|---|---|---|---|---|---|---|
| 3: does one setting matter for all goals? | **real 3, noise 2** | real 5 | noise 5 | noise 5 | real 5 | real 5 |
| 13: does one setting change one goal? | **real 3, noise 2** | noise 5 | noise 5 | real 5 | **real 1, noise 4** | noise 5 |
| 10: our chooser vs 50 random rows | random better 5 | random better 2, tie 3 | random better 5 | random better 5 | tie 3, equal medians 2 * | random better 2, tie 3 |
| 20: our guesses vs the average | ours better on 2 of 3 goals, tie on idle, all 5 seeds | ours better 5 | over 15 goal-seed pairs: ours better 5, tie 9, average better 1 | ours better 5 (one tie) | ours better 5 | ours better 5 |

Ask 7 result over the 5 seeds (100 = the best row in the data,
0 = the median row):

| pom3a | health | hr † | nasa | readmit | commits |
|---|---|---|---|---|---|
| 58–76 | 99.1–99.6 | 80.8–91.4 | 37–85 | 100 (highest possible) | 98.4–99.0 |

**Results that are the same at every seed:**
- **Our guesses beat quoting the average** in five domains, apart from a
  few ties. hr is the exception: after we removed the two columns that
  gave the answer away, our guesses mostly tie the average, and the
  average was better once (seed 2, years in current role).
- **Our chooser never beats random picks.** Over 30 domain-seed runs,
  `same` never found it better. (Before the hr fix it won once, at hr
  seed 5. That win went away after the fix.) This is our clearest
  result so far, and it is a negative one.

**Results that change with the seed:**
- **pom3a asks 3 and 13.** "Do small teams do better?" and "Does more
  planning cut idle time?" have no stable answer on 1,024 sampled rows.
  We report the 5-seed count for these, not a single run.
- **readmit ask 13** is "real" at seed 1 only.

\* **A bug in ask 10, fixed after `domains6`.** When both medians were
equal (readmit: 100 vs 100) but `same` said the results differed, ask
10 printed "random really is better", because it only compared
medians. It now prints "different, but the medians tie" and says which
side has the higher mean (random, at both seeds). A test covers this.
health's 99.6 vs 99.7 is still reported as a win for random at seeds 1
and 2. `same` says the difference is real, but it is 0.1 points, so we
treat it as a tie in practice.

## 4. nasa with a smaller budget (`--budget=20`)

With 93 rows, a budget of 50 lets the chooser see more than half the
data. We reran the budget asks with 20 instead.

| seed | ask 7 result | ask 10: ours vs random | verdict |
|---|---:|---|---|
| 1 | 51.4 | 51.4 vs 79.4 | random better |
| 2 | 37.4 | 37.4 vs 84.7 | random better |
| 3 | 42.6 | 42.6 vs 86.1 | random better |
| 4 | 30.9 | 30.9 vs 52.8 | random better |
| 5 | 30.2 | 30.2 vs 84.7 | random better |

The smaller budget is a fairer test, but random still wins at all 5
seeds. With a budget of 20, the chooser builds its tree from 15
measured rows (out of 46) and then gets only 5 more picks. Ask 17 ran
at 4 of the 5 seeds. At the fifth seed only 11 rows matched the fixed
settings, so it printed "too few rows" and stopped, which is what it is
meant to do.

## 5. The three domains we submit

We submit **pom3a, health and hr**, the three in our `step0`
pre-registration. All of their asks run, and none of them give
meaningless results. For pom3a we report the two seed-dependent answers
as 5-seed counts.

| domain | role | notes |
|---|---|---|
| pom3a | main | Large and all numeric. Two yes/no answers depend on the seed, so we report counts. |
| health | main | Same results at every seed. |
| hr | main | Same results at every seed. We removed the two columns that gave the answer away (Nov 8, below). |
| nasa | extra | Fair at budget 20, but the clustering asks (1, 11) only find 2–3 groups. Needed 10 new lines. |
| readmit | extra | The goal is yes/no, so both our chooser and random score 100 and cannot be told apart. |
| commits | extra | Behaves almost like health (same settings), so it repeats health rather than adding a new domain. |

## 6. hr rerun after the Nov 8 changes

We reworded hr asks 2, 8 and 18 (see the note at the end of
`docs/requirements_hr.md`):
- We now ignore the two columns that mostly measure time already spent
  at the company.
- A fix may now change only pay, overtime, travel, level, role,
  training, stock and work-life balance. This is the new `--change`
  option: 13 lines in `ezl/`, plus one new test (35 tests in all).

All 20 hr asks still run. What changed:
- **The biggest factor** for years at the company is now `JobLevel`,
  not `TotalWorkingYears`.
- **Fixes** now look like "raise JobLevel above 1; MonthlyIncome above
  10,239". They no longer suggest changing age.
- **Guessing is harder.** Over 5 seeds × 3 goals, ask 20 is now ours
  better 5, tie 9, average better 1 (before: ours better at 3 seeds,
  tie at 2).
- **The chooser** lost all 5 races (before: lost 4, won 1).
- **Asks 3 and 13** are still noise at every seed.

The hr column in section 3 (marked †) shows this rerun.

## 7. Still to do

1. Done: fixed the ask 10 tie bug, in a new commit after `domains6`.
   No tags were moved.
2. In the final report, give the 5-seed count for every yes/no result,
   not a single run.
3. Tune the chooser before running the LLM treatments. It loses in
   every domain, which the project brief expects ("When ezr loses").
   Two ideas: compare the chooser's own pick with the pick after its
   tree check, and try a larger `check` value.
4. Run LLM treatments 1–6 (not started).

## Rerun

```sh
make test                                   # tests at the current commit
for t in $(seq 1 20); do git checkout -q step$t && python3 -B -m unittest discover -s tests -q; done; git checkout -q main
make demos                                  # every ask, every domain, seed 1
python3 -B experiments/sweep.py out.json hr # every ask, plus the yes/no asks at 5 seeds, one domain
python3 -B -m ezl ask10 --file=data/raw/pom3a.csv --seed=3     # one ask at another seed
python3 -B -m ezl ask07 ask10 ask17 --file=moot/optimize/process/nasa93dem.csv --budget=20 --fixed=rely,cplx
```

Note: tags step1 to step20 have their own `tests/_data.py`, which reads
pom3a from `moot/`. To rerun the per-tag loop, download MOOT first:
`git clone --depth 1 https://github.com/timm/moot.git moot`.
