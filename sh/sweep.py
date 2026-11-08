"""Run every ask on every domain (seed 1), then the verdict asks over seeds 1-5.
usage: python3 -B sh/sweep.py OUT.json [domain ...]   (from the repo root)"""
import io, json, random, re, shlex, sys, time, traceback
from contextlib import redirect_stdout
sys.path.insert(0, ".")
from ezl.core import the, coerce, load
import importlib, pkgutil, ezl

BASE = dict(the)  # the defaults, before any domain's settings

def asks():
  "Same discovery as ezl/__main__.py (importing that module would run it)."
  out = {}
  for m in pkgutil.iter_modules(ezl.__path__):
    if not m.name.startswith("_"):
      mod = importlib.import_module("ezl." + m.name)
      out.update({k: f for k, f in vars(mod).items() if k.startswith("ask")})
  return dict(sorted(out.items()))

def domain_args():
  "Parse the per-domain file + args out of the Makefile."
  mk = open("Makefile").read().replace("\\\n", " ")
  v = dict(re.findall(r"^(\w+)\s*=\s*(.*)$", mk, re.M))
  out = {}
  for d in ["pom3a", "health", "hr", "nasa", "readmit", "commits"]:
    args = re.sub(r"\$\((\w+)\)", lambda m: v.get(m.group(1), ""), v.get(d + "_args", ""))
    out[d] = (v[d].replace("$(MOOT)", "moot"), shlex.split(args))
  return out

def setup(file, args, seed, extra=()):
  the.clear(); the.update(BASE)
  for a in list(args) + list(extra):
    k, _, val = a[2:].partition("="); the[k] = coerce(val)
  the["file"], the["seed"] = file, seed

def run(todo, name, seed):
  random.seed(seed); out = io.StringIO(); t0 = time.time()
  try:
    with redirect_stdout(out): todo[name](load())
    ok, err = True, ""
  except Exception:
    ok, err = False, traceback.format_exc(limit=3)
  return dict(ok=ok, secs=round(time.time() - t0, 2), out=out.getvalue(), err=err)

def main(path, only):
  todo = asks(); res = {}
  for d, (file, args) in domain_args().items():
    if only and d not in only: continue
    r = res[d] = {"all": {}, "seeds": {}, "nasa20": {}}
    for name in todo:
      setup(file, args, 1); r["all"][name] = run(todo, name, 1)
      print(d, name, r["all"][name]["ok"], r["all"][name]["secs"], flush=True)
    for name in ["ask03", "ask07", "ask10", "ask13", "ask20"]:
      r["seeds"][name] = []
      for s in range(1, 6):
        setup(file, args, s); r["seeds"][name].append(run(todo, name, s)["out"])
      print(d, name, "seeds done", flush=True)
    if d == "nasa":
      for name in ["ask07", "ask10", "ask17"]:
        r["nasa20"][name] = []
        for s in range(1, 6):
          setup(file, args, s, ["--budget=20"]); r["nasa20"][name].append(run(todo, name, s)["out"])
  json.dump(res, open(path, "w"), indent=1)

if __name__ == "__main__": main(sys.argv[1], sys.argv[2:])
