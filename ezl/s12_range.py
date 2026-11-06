"""Step 12 (guess): step 2's neighbours also give a range."""
from .core import adds, fmt
from .s02_guess import near, split

def ask12(d):
  "Guess each goal as a range (mean +/- 2 sd of the neighbours); how often is the truth inside?"
  test, train = split(d)
  for c in d.y:
    inside = 0
    for r in test:
      ys = adds(x[c.at] for x in near(d, r, train))
      inside += abs(r[c.at] - ys.mu) <= 2 * ys.div()
    print(f"{c.name:>24}: truth inside the range {100 * inside // len(test)}% of the time"
          f"  (e.g. {fmt(ys.mu)} +/- {fmt(2 * ys.div())}, truth {fmt(r[c.at])})")
