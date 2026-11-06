"""Step 9 (spot): rows unlike any other: typos, glitches, scams."""
import random
from .core import median, fmt
from .s02_guess import near

def oddness(d, row, ref):
  "Distance to the k-th nearest reference row."
  return d.distx(row, near(d, row, ref)[-1])

def ask09(d):
  "Flag the 1% of rows that look like nobody else."
  ref = random.sample(d.rows, min(256, len(d.rows)))
  scores = sorted(((oddness(d, r, ref), r) for r in d.rows), key=lambda z: z[0])
  print(f"typical oddness {fmt(median(s for s, _ in scores))}; the oddest:")
  for s, r in scores[-max(1, len(scores) // 100):]:
    print(f"  {fmt(s):>6}", [fmt(r[c.at]) for c in d.x])
