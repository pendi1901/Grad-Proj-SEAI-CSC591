"""Step 1 (remember): columns, tables, distances, clusters.
Everything later steps share lives here."""
import csv, math, random, re

the = dict(file="moot/optimize/process/pom3a.csv", seed=1, p=2,
           few=128, stop=32, cap=1024, leaf=3, maxd=4, budget=50,
           check=5, more=4, keepf=0.66, k=5, drop="")
TINY = 1e-32

def coerce(s):
  s = s.strip()
  for f in (int, float):
    try: return f(s)
    except ValueError: pass
  return s

def csv_rows(file):
  with open(file) as f:
    for row in csv.reader(f):
      if row: yield [coerce(c) for c in row]

def mean(xs):
  xs = list(xs); return sum(xs) / len(xs)

def median(xs):
  xs = sorted(xs); return xs[len(xs) // 2]

def fmt(x): return f"{x:.3g}" if isinstance(x, float) else str(x)

class Num:
  "Running mean and sd; a trailing '-' in the name means minimize."
  def __init__(i, name="", at=0):
    i.name, i.at, i.n, i.mu, i.m2 = name, at, 0, 0.0, 0.0
    i.heaven = 0 if name.endswith("-") else 1
  def add(i, v, inc=1):
    if v == "?": return v
    i.n += inc
    if i.n <= 0: i.n, i.mu, i.m2 = 0, 0.0, 0.0; return v
    d = v - i.mu; i.mu += inc * d / i.n; i.m2 += inc * d * (v - i.mu)
    return v
  def mid(i): return i.mu
  def div(i): return 0 if i.n < 2 else math.sqrt(max(i.m2, 0) / (i.n - 1))
  def norm(i, v):
    if v == "?": return v
    z = (v - i.mu) / (i.div() + TINY)
    return 1 / (1 + math.exp(-1.702 * max(-3, min(3, z))))
  def dist(i, a, b):
    if a == b == "?": return 1
    a, b = i.norm(a), i.norm(b)
    if a == "?": a = 0 if b > .5 else 1
    if b == "?": b = 0 if a > .5 else 1
    return abs(a - b)

class Sym:
  "Symbol counts."
  def __init__(i, name="", at=0): i.name, i.at, i.n, i.has = name, at, 0, {}
  def add(i, v, inc=1):
    if v == "?": return v
    i.n += inc; i.has[v] = i.has.get(v, 0) + inc
    return v
  def mid(i): return max(i.has, key=i.has.get)
  def div(i):
    return -sum(n / i.n * math.log2(n / i.n) for n in i.has.values() if n > 0)
  def dist(i, a, b): return 1.0 if a == b == "?" else float(a != b)

def adds(xs, col=None):
  col = col or Num()
  for x in xs: col.add(x)
  return col

class Data:
  """Rows plus column summaries. Header names decide roles: lowercase
  first letter = symbolic; trailing +/- = goal; trailing X, or listed
  in the['drop'], = ignored; everything else = an x column."""
  def __init__(i, src):
    src = iter(src); i.names = next(src)
    drop = str(the["drop"]).split(",")
    i.cols = [(Sym if s[0].islower() else Num)(s, at)
              for at, s in enumerate(i.names)]
    i.y = [c for c in i.cols if re.search(r"[+-]$", c.name)]
    i.x = [c for c in i.cols if not re.search(r"[+\-!X]$", c.name)
           and c.name not in drop]
    i.rows = []
    for row in src: i.add(row)
  def add(i, row):
    for c in i.cols: c.add(row[c.at])
    i.rows.append(row); return row
  def clone(i, rows=()): return Data([i.names] + list(rows))
  def distx(i, r1, r2):
    return minkowski(c.dist(r1[c.at], r2[c.at]) for c in i.x)
  def disty(i, r):
    "Distance from the best possible goals; 0 = best."
    return minkowski(abs(c.norm(r[c.at]) - c.heaven) for c in i.y)

def minkowski(ds):
  n = d = 0
  for x in ds: n += 1; d += x ** the["p"]
  return (d / (n + TINY)) ** (1 / the["p"])

def col_named(d, name, default):
  return next((c for c in d.cols if c.name == name), default)

def load(file=None):
  d = Data(csv_rows(file or the["file"]))
  # shortcut: pure python is slow on 10k+ rows, so keep a random `cap`; raise cap for final runs
  return d if len(d.rows) <= the["cap"] else d.clone(random.sample(d.rows, the["cap"]))

def poles(d, rows):
  """Two far-apart rows, best (by disty) first, and a projector that
  ranks any row by how near it sits to the best one."""
  far = lambda r: max(rows, key=lambda z: d.distx(z, r))
  lo = far(random.choice(rows)); hi = far(lo)
  if d.disty(lo) > d.disty(hi): lo, hi = hi, lo
  c = d.distx(lo, hi) + TINY
  return (lambda r: (d.distx(lo, r)**2 + c*c - d.distx(hi, r)**2) / (2*c)), lo, hi

def cluster(d, rows=None):
  "Recursive halving on far poles; returns the leaves (lists of rows)."
  rows = rows or d.rows
  if len(rows) < 2 * the["stop"]: return [rows]
  proj, _, _ = poles(d, random.sample(rows, min(len(rows), the["few"])))
  rows = sorted(rows, key=proj); n = len(rows) // 2
  return cluster(d, rows[:n]) + cluster(d, rows[n:])

def report(d, rows, title):
  "One line: how many rows, and each goal's mean."
  ys = d.clone(rows)
  print(f"{title:>14}: n={len(rows):<5}",
        "  ".join(f"{c.name}={fmt(ys.cols[c.at].mid())}" for c in d.y))

def ask01(d):
  "Show the few rows that did best on every goal, and what they share."
  fams = sorted(cluster(d), key=lambda rows: mean(map(d.disty, rows)))
  report(d, d.rows, "everyone"); report(d, fams[0], "best few")
  best = d.clone(fams[0])
  print("what the best few look like (their typical value vs everyone's):")
  for c in d.x:
    print(f"  {c.name:>24}: {fmt(best.cols[c.at].mid()):>8}  vs {fmt(c.mid())}")
