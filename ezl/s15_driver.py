"""Step 15 (blame): step 5's tree, grown on one goal; its root is the top driver."""
from .core import the, col_named, fmt
from .s05_blame import Tree, header

def goal_y(c):
  "Distance of one goal from its best; 0 = best."
  return lambda r: abs(c.norm(r[c.at]) - c.heaven)

def ask15(d):
  "What is the single biggest driver of one goal?"
  g = col_named(d, the.get("goal2"), d.y[0])
  t = Tree(d, d.rows, goal_y(g))
  if t.c is None: return print(f"nothing splits {g.name}")
  print(f"biggest driver of {g.name}: {t.c.name} (split at {fmt(t.v)})")
  header(d); t.show(d)
