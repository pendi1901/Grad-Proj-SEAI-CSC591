"""Step 3 (certify): is a gap real, or noise? A port of ezr's `same`."""
import math
from .core import Sym, the, adds, median, fmt, col_named, TINY

def cohen(xs, ys):
  x, y = adds(xs), adds(ys)
  sd = math.sqrt(((x.n-1)*x.div()**2 + (y.n-1)*y.div()**2) / (x.n + y.n - 2))
  return abs(x.mu - y.mu) / (sd + TINY)

def ks(xs, ys):
  "Max gap between the two cdfs, in critical units. Sorted lists in."
  nx, ny, d, p, q = len(xs), len(ys), 0, 0, 0
  while p < nx and q < ny:
    v = min(xs[p], ys[q])
    while p < nx and xs[p] == v: p += 1
    while q < ny and ys[q] == v: q += 1
    d = max(d, abs(p/nx - q/ny))
  return d / ((nx + ny) / (nx * ny)) ** .5

def cliffs(xs, ys):
  "Rank imbalance, 0..1. Sorted lists in."
  gt = lt = j = k = 0
  for x in xs:
    while j < len(ys) and ys[j] < x: j += 1; k = j
    while k < len(ys) and ys[k] == x: k += 1
    gt += j; lt += len(ys) - k
  return abs(gt - lt) / (len(xs) * len(ys))

def same(xs, ys):
  "True when all three tests call the samples indistinguishable."
  xs, ys = sorted(xs), sorted(ys)
  return cohen(xs, ys) <= .35 and cliffs(xs, ys) <= .195 and ks(xs, ys) <= 1.36

def holds(c, x, v):
  "Does cell x fall on the 'yes' side of a cut at v? Unknowns say yes."
  return x == "?" or (x == v if isinstance(c, Sym) else x <= v)

def compare(d, c, Y):
  "Split rows on column c (at its mean or mode); are the halves' Y scores really different?"
  v = c.mid()
  a = [Y(r) for r in d.rows if holds(c, r[c.at], v)]
  b = [Y(r) for r in d.rows if not holds(c, r[c.at], v)]
  if not a or not b: return print(f"{c.name}: only one kind of value, nothing to compare")
  op, nop = ("==", "!=") if isinstance(c, Sym) else ("<=", ">")
  print(f"{c.name} {op} {fmt(v)}: n={len(a):<5} median {fmt(median(a))}")
  print(f"{c.name} {nop} {fmt(v)}: n={len(b):<5} median {fmt(median(b))}")
  print("verdict:", "noise: no real difference" if same(a, b) else "a real difference")

def ask03(d):
  "Is one setting really better on all goals, or is the gap noise? (score: 0 = best)"
  compare(d, col_named(d, the.get("col"), d.x[-1]), d.disty)
