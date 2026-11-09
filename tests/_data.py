import os, random
from ezl.core import the, load

FILE = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "pom3a.csv")

def data(cap=256):
  "A small, seeded pom3a sample so tests stay fast and repeatable."
  random.seed(1); the["cap"] = cap
  return load(FILE)
