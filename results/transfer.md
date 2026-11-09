# Transfer: what each domain cost after domain 1

The ladder (tags `step1`–`step20`) was built on pom3a: 590 lines in
`ezl/`. Every later change to `ezl/` is listed here, with what forced
it. Per-domain settings live in the `Makefile` (file path, which
columns each ask studies, columns to ignore).

| domain | new lines in `ezl/` | Makefile settings | what forced the code |
|---|---:|---:|---|
| health | 0 | 2 | nothing |
| hr (as first run) | 0 | 3 | nothing (the `drop` option was written in step 1) |
| nasa, readmit, commits | 10 (+10 −5), commit `ea499fa`, tag `domains6` | 2–3 each | a chooser hang on 93-row data, TRUE/FALSE cells, drift windows on small data |
| hr (Nov 8 rewording) | 13 (+13 −7), commit `355679b` | +1 | a `change` option, so fixes only touch columns the office controls |

One more `ezl/` change was a bug fix, not transfer: commit `60550ca`
(+9 −3), where ask 10 had called equal medians a win.

**Against the prediction** (domains 2 and 3 need under 10% new code):
health 0%, hr 13 / 590 = 2.2%. Both pass.

Regenerate:

```sh
git log --reverse --format='%h %ad %s' --date=short step20..HEAD -- ezl
git diff --numstat step20 domains6 -- ezl
```
