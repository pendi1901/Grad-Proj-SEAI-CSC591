# New code per step (treatment 7)

Added lines in `ezl/` between consecutive step tags, from
`git diff --numstat step(i-1) step(i) -- ezl`. Regenerate with `make loc`
(`experiments/loc.sh`).

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

Steps 1–10 add 433 lines (step 1 alone 167); steps 11–20 add 157. `same`
calls steps 11–20 smaller than steps 1–10 (Cliff's δ 0.72), and still
does with step 1 left out (δ 0.69).
