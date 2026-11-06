#!/bin/sh
# New lines in ezl/ added at each step tag: the histogram's y-axis.
# Counts every added line (blank and comment lines too), as git diff --numstat does.
n=$(git tag -l 'step*' | sed 's/step//' | sort -n | tail -1)
for i in $(seq 1 "$n"); do
  printf "step%s %s\n" "$i" \
    "$(git diff --numstat "step$((i-1))" "step$i" -- ezl | awk '{a+=$1} END {print a+0}')"
done | awk '{s[NR]=$1; n[NR]=$2; t+=$2}
  END {for (i=1; i<=NR; i++) printf "%-7s %4d %5.1f%%\n", s[i], n[i], 100*n[i]/t
       printf "total   %4d\n", t}'
