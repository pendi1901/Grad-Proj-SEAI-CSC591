"""Step 19 (spot): rows whose outcome is far from what their look-alikes (step 2) got."""
import random
from .core import mean, fmt
from .s02_guess import near

def surprise(d, row):
  "Actual score minus the mean score of the k most similar other rows."
  others = [r for r in d.rows if r is not row]
  return d.disty(row) - mean(map(d.disty, near(d, row, others)))

def ask19(d):
  "Which rows look ordinary but did much better or worse than their look-alikes?"
  got = sorted(((surprise(d, r), r) for r in random.sample(d.rows, min(200, len(d.rows)))),
               key=lambda z: z[0])
  print("score 0 = best; surprise < 0 means better than look-alikes")
  for s, r in got[:3] + got[-3:]:
    print(f"  surprise {fmt(s):>7}  score {fmt(d.disty(r)):>6}  goals", [fmt(r[c.at]) for c in d.y])
