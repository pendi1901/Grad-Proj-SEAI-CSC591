# Code needed for each new domain

We built steps 1–20 on pom3a, which came to 590 lines in `ezl/`. This
table lists every later change to `ezl/` and what caused it. Each
domain's own settings are in the Makefile: the file path, the columns
each ask looks at, and the columns to ignore.

| domain | new lines in `ezl/` | lines of Makefile settings | why the code was needed |
|---|---:|---:|---|
| health | 0 | 2 | no new code needed |
| hr (first version) | 0 | 3 | no new code needed (the option to ignore columns was already in step 1) |
| nasa, readmit, commits | 10 (+10 −5), commit `ea499fa`, tag `domains6` | 2–3 each | the chooser looped forever on 93 rows; TRUE/FALSE values crashed numeric columns; the drift window was bigger than the data |
| hr (Nov 8 rewording) | 13 (+13 −7), commit `355679b` | 1 more | a `change` option, so a fix only changes columns the office controls |

One more change to `ezl/` was a bug fix, not a new domain: commit
`60550ca` (+9 −3), where ask 10 reported a win when the two medians
were equal.

**Our prediction** was that domains 2 and 3 would need less than 10%
new code. health needed 0%, and hr needed 13 / 590 = 2.2%. Both are
under 10%.

To regenerate:

```sh
git log --reverse --format='%h %ad %s' --date=short step20..HEAD -- ezl
git diff --numstat step20 domains6 -- ezl
```
