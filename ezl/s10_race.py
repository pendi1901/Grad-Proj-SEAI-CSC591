"""Step 10 (race): our chooser against random picks on the same budget."""
import random
from .core import the, median, fmt
from .s03_certify import same
from .s07_choose import choose, wins

def ask10(d):
  "Does our chooser really beat measuring `budget` random rows and keeping the best?"
  win = wins(d)
  ours = [win(choose(d)) for _ in range(20)]
  rand = [win(min(random.sample(d.rows, the["budget"]), key=d.disty)) for _ in range(20)]
  print(f"median win (100 = best row of all): ours {fmt(median(ours))}, random {fmt(median(rand))}")
  print("verdict:", "a tie: no real difference" if same(ours, rand) else
        ("ours really is better" if median(ours) > median(rand) else "random really is better"))
