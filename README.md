# ezl: the shrinking-code ladder (CSC 591, six domains)

Twenty customer asks, built as twenty git-tagged steps on one small
plain-Python library (`ezl/`, standard library only), run on six
MOOT data sets. Does each new skill need less new code than the last?

- Requirements (6 domains × 20 asks): [docs/requirements.md](docs/requirements.md)
- Pre-registered claim (tag `step0`, before any code): [docs/claim.md](docs/claim.md)
- Nov 9 initial deliverable, one page: [docs/nov9.md](docs/nov9.md)
- Test report (every tag, every domain, 5 seeds): [docs/test-report.md](docs/test-report.md)

## Run it

Needs Python 3.9+ and git. The first command clones MOOT into `./moot`.

```sh
make test                 # 35 unit tests, ~40 s
make ask07                # one ask, on pom3a (the default domain)
make ask07 D=health       # other domains: D=pom3a|health|hr|nasa|readmit|commits
make demo D=hr            # all twenty asks on one domain
make demos                # all twenty asks on all six domains
make loc                  # new lines of code per step tag: the histogram
make                      # list every ask
```

| ask | skill | demo | | ask | skill | demo |
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

Add `D=health`, `D=hr`, `D=nasa`, `D=readmit` or `D=commits` to any of them. Any setting in
`ezl/core.py:the` can be overridden: `python3 -B -m ezl ask07 --budget=30 --file=...`.

## Layout

| path | what |
|---|---|
| `ezl/core.py` | step 1: columns, tables, distances, clustering (everything shared) |
| `ezl/sNN_*.py` | step NN: one module per ask; it imports from earlier steps |
| `ezl/__main__.py` | runs any `askNN` function it finds, so a new step needs no wiring |
| `tests/test_sNN.py` | one test file per step |
| `sh/loc.sh` | per-tag `git diff --numstat` over `ezl/` |
| `Makefile` | per-domain data paths and settings (the only per-domain code) |

## New code per step (`make loc`, treatment 7: hand-built, reuse as much as possible)

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
