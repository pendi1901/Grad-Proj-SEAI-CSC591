# New lines of code per step

For each step tag, this counts the lines added to `ezl/` since the
previous tag, using `git diff --numstat step(i-1) step(i) -- ezl`. To
regenerate it, run `make loc` (which runs `experiments/loc.sh`).

```
step1    167  28.3%
step2     22   3.7%
step3     51   8.6%
step4     20   3.4%
step5     58   9.8%
step6     22   3.7%
step7     40   6.8%
step8     23   3.9%
step9     16   2.7%
step10    14   2.4%
step11    11   1.9%
step12    14   2.4%
step13     9   1.5%
step14    18   3.1%
step15    15   2.5%
step16    18   3.1%
step17    18   3.1%
step18    21   3.6%
step19    17   2.9%
step20    16   2.7%
total    590
```

Steps 1–10 added 433 lines (step 1 alone added 167). Steps 11–20 added
157. The `same` test says steps 11–20 needed less code than steps 1–10
(Cliff's delta 0.72), and it still says so when step 1 is left out
(0.69).
