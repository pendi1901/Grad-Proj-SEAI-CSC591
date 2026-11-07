"""Step 14 (flow): stream windows of rows; step 3's `same` raises the alarm."""
from .core import the, fmt, col_named
from .s03_certify import same

def drift(d, rows, n=None):
  "Index of the first window whose scores differ from the first window's, else None."
  n = n or min(100, len(rows) // 5)
  ws = [rows[i:i+n] for i in range(0, len(rows) - n + 1, n)]
  first = list(map(d.disty, ws[0]))
  return next((j for j, w in enumerate(ws[1:], 1) if not same(first, list(map(d.disty, w)))), None)

def ask14(d):
  "Warn me when new rows stop looking like the old ones."
  c = col_named(d, the.get("drift"), d.x[0])
  rows = sorted(d.rows, key=lambda r: (r[c.at] == "?", r[c.at]))
  n = min(100, len(rows) // 5)
  print(f"(replaying rows in order of {c.name}, {n} at a time, to simulate a slow drift)")
  j = drift(d, rows, n)
  print("no drift detected" if j is None else
        f"drift alarm at window {j+1} ({c.name} around {fmt(rows[j*n][c.at])})")
