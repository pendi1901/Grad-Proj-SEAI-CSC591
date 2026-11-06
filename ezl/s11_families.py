"""Step 11 (remember): the clusters from step 1, coarser, shown as families."""
from .core import the, mean, cluster, report

def ask11(d):
  "Group the rows into a handful of families; each family's size and outcomes, best first."
  old, the["stop"] = the["stop"], max(the["stop"], len(d.rows) // 8)
  try: fams = cluster(d)
  finally: the["stop"] = old
  report(d, d.rows, "everyone")
  for j, rows in enumerate(sorted(fams, key=lambda rows: mean(map(d.disty, rows)))):
    report(d, rows, f"family {j+1}")
