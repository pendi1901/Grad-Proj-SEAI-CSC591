"""Step 6 (justify): tree branches as if-then rules a skeptic can check."""
from .core import Sym, fmt, report
from .s05_blame import Tree

def say(cond):
  c, v, yes = cond
  op = ("==" if yes else "!=") if isinstance(c, Sym) else ("<=" if yes else ">")
  return f"{c.name} {op} {fmt(v)}"

def rules(t, conds=()):
  "Every leaf, with the (column, value, yes?) conditions that lead to it."
  if t.c is None: return [(list(conds), t)]
  return (rules(t.yes, conds + ((t.c, t.v, True),)) +
          rules(t.no, conds + ((t.c, t.v, False),)))

def ask06(d):
  "Rules of thumb: what the best and the worst groups have in common."
  rs = sorted(rules(Tree(d, d.rows)), key=lambda z: z[1].mu)
  report(d, d.rows, "everyone")
  for label, (conds, leaf) in [("best", rs[0]), ("worst", rs[-1])]:
    report(d, leaf.rows, label)
    print(f"{'':>16}if", " and ".join(map(say, conds)) or "always")
