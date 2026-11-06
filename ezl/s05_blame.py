"""Step 5 (blame): a tree of if-then splits that sorts good rows from bad."""
from .core import Num, Sym, the, adds, fmt
from .s03_certify import holds

def spread(a, b): return (a.div()*a.n + b.div()*b.n) / (a.n + b.n)

def cuts(d, rows, Y):
  "Every legal split of rows, as (spread of Y after the split, column, value)."
  for c in d.x:
    xy = [(r[c.at], Y(r)) for r in rows if r[c.at] != "?"]
    if isinstance(c, Sym):
      for v in {x for x, _ in xy}:
        yes, no = adds(y for x, y in xy if x == v), adds(y for x, y in xy if x != v)
        if min(yes.n, no.n) >= the["leaf"]: yield spread(yes, no), c, v
    else:
      xy.sort(key=lambda p: p[0])
      left, right = Num(), adds(y for _, y in xy)
      for j, (x, y) in enumerate(xy[:-1]):
        left.add(y); right.add(y, -1)
        if x != xy[j+1][0] and min(left.n, right.n) >= the["leaf"]:
          yield spread(left, right), c, x

class Tree:
  "Split on the best cut, to depth the['maxd']. Y defaults to disty (0 = best)."
  def __init__(t, d, rows, Y=None, lvl=0):
    Y = Y or d.disty
    t.rows, t.mu, t.c, t.v, t.yes, t.no = rows, adds(map(Y, rows)).mu, None, None, None, None
    if len(rows) >= 2 * the["leaf"] and lvl < the["maxd"]:
      best = min(cuts(d, rows, Y), key=lambda z: z[0], default=None)
      if best:
        _, c, v = best
        yes = [r for r in rows if holds(c, r[c.at], v)]
        no = [r for r in rows if not holds(c, r[c.at], v)]
        if yes and no:
          t.c, t.v = c, v
          t.yes, t.no = Tree(d, yes, Y, lvl+1), Tree(d, no, Y, lvl+1)

  def leaf(t, row):
    while t.c is not None: t = t.yes if holds(t.c, row[t.c.at], t.v) else t.no
    return t

  def leaves(t): return [t] if t.c is None else t.yes.leaves() + t.no.leaves()

  def show(t, d, pre="", txt="all rows"):
    "One line per node: rows, score, goal means, then the branch; better branch first."
    ys = d.clone(t.rows)
    print(f"{len(t.rows):5} {fmt(t.mu):>6}",
          *(f"{fmt(ys.cols[c.at].mid()):>9}" for c in d.y), " " + pre + txt)
    if t.c is not None:
      op, nop = ("==", "!=") if isinstance(t.c, Sym) else ("<=", ">")
      kids = sorted([(t.yes, op), (t.no, nop)], key=lambda z: z[0].mu)
      for kid, o in kids: kid.show(d, pre + "|  ", f"{t.c.name} {o} {fmt(t.v)}")

def header(d): print(f"{'n':>5} {'score':>6}", *(f"{c.name:>9}" for c in d.y), " (score 0 = best)")

def ask05(d):
  "Why are the bad rows bad? Splits that separate good from bad, worst branches last."
  header(d); Tree(d, d.rows).show(d)
