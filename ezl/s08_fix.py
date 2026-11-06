"""Step 8 (fix): the fewest changes that move a row into a better branch."""
from .core import median, fmt
from .s03_certify import holds
from .s05_blame import Tree
from .s06_justify import rules, say

def broken(conds, row):
  "The conditions this row fails."
  return [k for k in conds if holds(k[0], row[k[0].at], k[1]) != k[2]]

def fix(d, row, t, goal):
  "Among branches scoring <= goal, the one needing fewest changes: (changes, leaf)."
  ok = [(broken(cs, row), leaf) for cs, leaf in rules(t) if leaf.mu <= goal]
  return min(ok, key=lambda z: (len(z[0]), z[1].mu))

def ask08(d):
  "This row is our worst: what is the smallest change that makes it at least typical?"
  t, row = Tree(d, d.rows), max(d.rows, key=d.disty)
  typical = median(map(d.disty, d.rows))
  changes, leaf = fix(d, row, t, typical)
  print(f"worst row scores {fmt(d.disty(row))} (0 = best, typical = {fmt(typical)})")
  print("change:", "; ".join(map(say, changes)) or "nothing")
  print(f"-> it lands in a branch of {len(leaf.rows)} rows scoring {fmt(leaf.mu)}")
