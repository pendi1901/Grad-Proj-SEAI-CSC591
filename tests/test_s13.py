import io, unittest
from contextlib import redirect_stdout
from ezl.core import the
from ezl.s13_onegoal import ask13
from _data import data

class TestOneGoal(unittest.TestCase):
  def test_named_goal_and_column_are_used(self):
    the.update(goal="Idle-", col2="Plan"); out = io.StringIO()
    with redirect_stdout(out): ask13(data())
    self.assertIn("goal: Idle- (lower", out.getvalue())
    self.assertIn("Plan <=", out.getvalue())
