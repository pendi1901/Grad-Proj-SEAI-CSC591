"""Step 18 (fix): step 8's fix, aimed at the best branch instead of the median."""
import random
from .core import Sym, fmt
from .s05_blame import Tree
from .s06_justify import say
from .s08_fix import fix

def tight(conds):
  "Drop conditions implied by tighter ones on the same column (x <= 3 implies x <= 7)."
  best = {}
  for c, v, yes in conds:
    k = (c.at, yes, v if isinstance(c, Sym) else None)
    if k not in best or (v < best[k][1] if yes else v > best[k][1]): best[k] = (c, v, yes)
  return list(best.values())

def ask18(d):
  "What would this row need to change to look like our best group?"
  t, row = Tree(d, d.rows), random.choice(d.rows)
  if not (got := fix(d, row, t, min(l.mu for l in t.leaves()))):
    return print("no change to the allowed columns reaches the best group")
  changes, leaf = got
  print(f"this row scores {fmt(d.disty(row))} (0 = best); the best group scores {fmt(leaf.mu)}")
  print("change:", "; ".join(map(say, tight(changes))) or "nothing, it is already there")
