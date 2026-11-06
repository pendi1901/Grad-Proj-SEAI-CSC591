"""Step 4 (flow): judge rows as they arrive, using only what came before."""
import random
from .core import Num, mean, fmt

def stream(d, rows, warm=32):
  "Yield (row, is_winner) per arriving row, once `warm` rows have been seen."
  seen, score = d.clone(), Num()
  for r in rows:
    seen.add(r); y = seen.disty(r)
    if score.n >= warm: yield r, y < score.mu - score.div()
    score.add(y)

def ask04(d):
  "As rows arrive one by one, flag the winners on the spot."
  got = list(stream(d, random.sample(d.rows, len(d.rows))))
  yes = [r for r, win in got if win]
  print(f"flagged {len(yes)} of {len(got)} rows as they arrived")
  if yes:
    print(f"in hindsight (0 = best): flagged rows score {fmt(mean(map(d.disty, yes)))}"
          f", all rows {fmt(mean(d.disty(r) for r, _ in got))}")
