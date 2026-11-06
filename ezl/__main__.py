"""usage: python3 -B -m ezl ASK.. [--file=csv] [--key=val ..]
ASK is ask01..ask20, or `all`. Each --key=val overrides ezl.core.the."""
import importlib, pkgutil, random, sys
import ezl
from ezl.core import the, coerce, load

def asks():
  "Every askNN function in every ezl module, so a new step needs no wiring."
  out = {}
  for m in pkgutil.iter_modules(ezl.__path__):
    if not m.name.startswith("_"):
      mod = importlib.import_module("ezl." + m.name)
      out.update({k: f for k, f in vars(mod).items() if k.startswith("ask")})
  return dict(sorted(out.items()))

def main(args):
  todo = asks()
  for a in args:
    if a.startswith("--"):
      k, _, v = a[2:].partition("="); the[k] = coerce(v)
  names = [a for a in args if not a.startswith("-")]
  if not names:
    print(__doc__); [print(f"  {k}: {f.__doc__}") for k, f in todo.items()]; return
  for name in (list(todo) if names == ["all"] else names):
    random.seed(the["seed"])
    print(f"\n## {name}: {todo[name].__doc__}")
    todo[name](load())

main(sys.argv[1:])
