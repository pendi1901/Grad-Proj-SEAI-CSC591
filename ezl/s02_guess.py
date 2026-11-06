"""Step 2 (guess): predict the goals from the k nearest known rows."""
import random
from .core import the, mean, fmt

def near(d, row, rows=None):
  return sorted(rows or d.rows, key=lambda r: d.distx(row, r))[:the["k"]]

def guess(d, row, rows=None):
  "Each goal's mean over the nearest rows."
  return [mean(r[c.at] for r in near(d, row, rows)) for c in d.y]

def split(d, n=50):
  "Shuffled rows: n to test, the rest to learn from."
  rows = random.sample(d.rows, len(d.rows)); return rows[:n], rows[n:]

def ask02(d):
  "Guess each goal before it is measured; report the typical miss."
  test, train = split(d)
  gs = [(r, guess(d, r, train)) for r in test]
  for j, c in enumerate(d.y):
    miss = mean(abs(g[j] - r[c.at]) for r, g in gs)
    print(f"{c.name:>24}: typical miss {fmt(miss):>6}   (the data's own spread: {fmt(c.div())})")
