"""Step 20 (race): step 2's guesses against quoting the average, judged by `same`."""
from .core import mean, median, fmt
from .s02_guess import guess, split
from .s03_certify import same

def ask20(d):
  "Do our guesses really beat just quoting the average?"
  test, train = split(d)
  gs = [(r, guess(d, r, train)) for r in test]
  for j, c in enumerate(d.y):
    mu = mean(r[c.at] for r in train)
    ours = [abs(g[j] - r[c.at]) for r, g in gs]
    base = [abs(mu - r[c.at]) for r, _ in gs]
    verdict = ("a tie" if same(ours, base) else
               "ours really better" if median(ours) < median(base) else "average really better")
    print(f"{c.name:>24}: median miss ours {fmt(median(ours)):>6}, average {fmt(median(base)):>6} -> {verdict}")
