"""Step 16 (justify): step 6's rules, for one row: the branch it fell into."""
import random
from .core import fmt, report
from .s05_blame import Tree
from .s06_justify import rules, say

def why(t, row):
  "The conditions that put this row in its leaf."
  leaf = t.leaf(row)
  return next(conds for conds, l in rules(t) if l is leaf), leaf

def ask16(d):
  "Why did you rate this one row the way you did?"
  t, row = Tree(d, d.rows), random.choice(d.rows)
  conds, leaf = why(t, row)
  print(f"this row scores {fmt(d.disty(row))} (0 = best) because:")
  for c, v, yes in conds: print(f"  {say((c, v, yes)):>40}   (it has {fmt(row[c.at])})")
  report(d, [row], "this row"); report(d, leaf.rows, "rows like it"); report(d, d.rows, "everyone")
