"""Step 13 (certify): step 3's compare, on one raw goal instead of all."""
from .core import the, col_named
from .s03_certify import compare

def ask13(d):
  "Does one setting really move one goal, or is the gap noise? (raw goal values)"
  g = col_named(d, the.get("goal"), d.y[-1])
  print(f"goal: {g.name} ({'lower' if g.heaven == 0 else 'higher'} is better)")
  compare(d, col_named(d, the.get("col2"), d.x[-2]), lambda r: r[g.at])
