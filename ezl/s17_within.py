"""Step 17 (choose): step 7's chooser, on only the rows that keep fixed settings."""
import random
from .core import the, col_named, report, fmt
from .s07_choose import choose

def alike(d, ref, fixed, tol=.2):
  "Rows matching ref on every fixed column (syms equal, nums within tol on the 0..1 scale)."
  return [r for r in d.rows if all(c.dist(r[c.at], ref[c.at]) <= tol for c in fixed)]

def ask17(d):
  "Some settings cannot change: find the best row among those that keep them."
  names = str(the.get("fixed", "")).split(",")
  fixed = [c for c in (col_named(d, n, None) for n in names) if c] or d.x[:2]
  ref = random.choice(d.rows); rows = alike(d, ref, fixed)
  print("fixed:", ", ".join(f"{c.name} ~ {fmt(ref[c.at])}" for c in fixed), f"({len(rows)} rows qualify)")
  budget = min(the["budget"], len(rows) // 2)
  if budget <= the["check"]: return print("too few rows qualify to choose among")
  report(d, rows, "all such rows"); report(d, [choose(d, rows, budget)], "our pick")
