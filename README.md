# Shrinking-code experiment (CSC 591, group G2)

We built 20 features ("asks") one at a time, as 20 git-tagged steps, on
one small Python library (`ezl/`, standard library only). We count the
new lines of code each step needed, to test whether later features cost
less than earlier ones. We run the same code on three main data sets
(pom3a, health, hr) and three extra ones (nasa, readmit, commits).

- Requirements, 20 asks per domain: [docs/requirements.md](docs/requirements.md)
- Hypotheses and win conditions, committed at tag `step0` before any code: [docs/hypotheses.md](docs/hypotheses.md)
- Nov 9 initial deliverable: [deliverables/initial_submission.md](deliverables/initial_submission.md)
- The data sets and why we chose them: [docs/dataset_analysis.md](docs/dataset_analysis.md)
- New lines of code per step: [results/loc.md](results/loc.md)
- Code needed for each new domain: [results/transfer.md](results/transfer.md)
- Test results (every tag, every domain, 5 random seeds): [results/test-report.md](results/test-report.md)

## How to run it

You need Python 3.9 or later and git. No packages need installing. The
three main data sets are in `data/raw/`. The extra domains (nasa,
readmit, commits) download the MOOT data repository into `./moot` the
first time you run them.

```sh
make test                 # run the 35 unit tests (about 40 s)
make ask07                # run ask 7 on pom3a (the default domain)
make ask07 D=health       # run ask 7 on another domain: D=pom3a|health|hr|nasa|readmit|commits
make demo D=hr            # run all 20 asks on one domain
make demos                # run all 20 asks on all six domains
make loc                  # print new lines of code per step tag
make                      # list every ask
```

| ask | skill | command | | ask | skill | command |
|---:|---|---|---|---:|---|---|
| 1 | remember | `make ask01` | | 11 | remember | `make ask11` |
| 2 | guess | `make ask02` | | 12 | guess | `make ask12` |
| 3 | certify | `make ask03` | | 13 | certify | `make ask13` |
| 4 | flow | `make ask04` | | 14 | flow | `make ask14` |
| 5 | blame | `make ask05` | | 15 | blame | `make ask15` |
| 6 | justify | `make ask06` | | 16 | justify | `make ask16` |
| 7 | choose | `make ask07` | | 17 | choose | `make ask17` |
| 8 | fix | `make ask08` | | 18 | fix | `make ask18` |
| 9 | spot | `make ask09` | | 19 | spot | `make ask19` |
| 10 | race | `make ask10` | | 20 | race | `make ask20` |

Add `D=<domain>` to any of these commands to change the data set. Any
setting in `the` (in `ezl/core.py`) can be changed on the command line,
for example `python3 -B -m ezl ask07 --budget=30 --file=...`.

## What is where

| path | contents |
|---|---|
| `ezl/core.py` | step 1: reading data, columns, distances, clustering. Every later step uses it. |
| `ezl/sNN_*.py` | step NN: one file per ask, importing from earlier steps |
| `ezl/__main__.py` | runs any function named `askNN`, so a new step needs no extra setup |
| `tests/test_sNN.py` | the tests for step NN |
| `experiments/loc.sh` | counts new lines in `ezl/` between step tags (`make loc`) |
| `experiments/sweep.py` | runs every ask on every domain, then reruns the yes/no asks at 5 seeds |
| `data/raw/` | the three main MOOT data sets, unchanged |
| `docs/` | hypotheses, requirements, data set analysis |
| `results/` | lines of code per step, cost per new domain, test results |
| `deliverables/` | the Nov 9 submission |
| `Makefile` | the file path and settings for each domain. This is the only place domains differ. |

## New lines of code per step

These counts are for our current build, where each step reuses earlier
steps as much as possible. The code was written with Claude Code (see
"AI use" in the [initial deliverable](deliverables/initial_submission.md)).
Source: `make loc`.

```
step1    167  28.3%    step11    11   1.9%
step2     22   3.7%    step12    14   2.4%
step3     51   8.6%    step13     9   1.5%
step4     20   3.4%    step14    18   3.1%
step5     58   9.8%    step15    15   2.5%
step6     22   3.7%    step16    18   3.1%
step7     40   6.8%    step17    18   3.1%
step8     23   3.9%    step18    21   3.6%
step9     16   2.7%    step19    17   2.9%
step10    14   2.4%    step20    16   2.7%
                       total    590
```
