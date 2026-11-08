"""Step 8 (fix): the fewest changes that move a row into a better branch."""
from .core import the, median, fmt
from .s03_certify import holds
from .s05_blame import Tree
from .s06_justify import rules, say

def broken(conds, row):
  "The conditions this row fails."
  return [k for k in conds if holds(k[0], row[k[0].at], k[1]) != k[2]]

def fix(d, row, t, goal):
  """Among branches scoring <= goal, the one needing fewest changes: (changes, leaf).
  Only columns named in the['change'] may change (empty = any). None if no branch qualifies."""
  can = [s for s in str(the["change"]).split(",") if s]
  ok = [(b, leaf) for cs, leaf in rules(t) if leaf.mu <= goal
        for b in [broken(cs, row)] if not can or all(k[0].name in can for k in b)]
  return min(ok, key=lambda z: (len(z[0]), z[1].mu)) if ok else None

def ask08(d):
  "This row is our worst: what is the smallest change that makes it at least typical?"
  t, row = Tree(d, d.rows), max(d.rows, key=d.disty)
  typical = median(map(d.disty, d.rows))
  print(f"worst row scores {fmt(d.disty(row))} (0 = best, typical = {fmt(typical)})")
  if not (got := fix(d, row, t, typical)): return print("no change to the allowed columns gets there")
  changes, leaf = got
  print("change:", "; ".join(map(say, changes)) or "nothing")
  print(f"-> it lands in a branch of {len(leaf.rows)} rows scoring {fmt(leaf.mu)}")
