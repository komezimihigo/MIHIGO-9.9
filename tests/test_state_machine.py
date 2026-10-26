import unittest
from orchestrator.models import Job,State
from orchestrator.state_machine import transition
class T(unittest.TestCase):
 def test_transition(self):
  j=Job("https://example.org");transition(j,State.RIGHTS_CHECK.value);self.assertEqual(j.state,State.RIGHTS_CHECK.value)
 def test_illegal(self):
  j=Job("https://example.org")
  with self.assertRaises(ValueError):transition(j,State.PUBLISHED.value)
if __name__=="__main__":unittest.main()
