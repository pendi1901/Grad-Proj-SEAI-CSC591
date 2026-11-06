"""Step 7 (choose): find a great row while looking at the goals of only a few."""
import random
from .core import the, median, fmt, poles, report, TINY
from .s05_blame import Tree

def acquire(d, rows, budget):
  """Label `more` rows at a time; after each round keep the part of the
  pool nearest the best label so far. Restart from the unlabelled rows
  when the pool runs dry. Returns labelled rows, best first."""
  lab, seen = [], set()
  while len(lab) < budget:
    pool = [r for r in random.sample(rows, len(rows)) if id(r) not in seen]
    if not pool: break
    while len(pool) >= 2 * the["leaf"] and len(lab) < budget:
      fresh = [r for r in pool if id(r) not in seen][:min(the["more"], budget - len(lab))]
      lab += fresh; seen |= {id(r) for r in fresh}
      near_best, _, _ = poles(d, lab)
      pool = sorted(pool, key=near_best)[:int(the["keepf"] * len(pool))]
  return sorted(lab, key=d.disty)

def choose(d, rows=None, budget=None):
  """Honest pick: label (budget - check) rows from one half, grow a tree
  on them, then label only its top `check` picks from the unseen half."""
  budget = budget or the["budget"]
  rows = random.sample(rows or d.rows, len(rows or d.rows)); n = len(rows) // 2
  t = Tree(d, acquire(d, rows[:n], budget - the["check"]))
  top = sorted(rows[n:], key=lambda r: t.leaf(r).mu)[:the["check"]]
  return min(top, key=d.disty)

def wins(d):
  "Grader: 100 = as good as the best row of all, 0 = no better than the median row."
  ys = sorted(map(d.disty, d.rows)); lo, mid = ys[0], ys[len(ys) // 2]
  return lambda r: max(-100, min(100, 100 * (1 - (d.disty(r) - lo) / (mid - lo + TINY))))

def ask07(d):
  "Find a near-best row while measuring only `budget` of them."
  win = wins(d); picks = [choose(d) for _ in range(20)]
  print(f"measured {the['budget']} of {len(d.rows)} rows, 20 tries;"
        f" median win {fmt(median(map(win, picks)))} (100 = best row of all, 0 = median row)")
  report(d, d.rows, "everyone"); report(d, [min(picks, key=d.disty)], "best pick")
