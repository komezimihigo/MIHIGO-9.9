import unittest
from orchestrator.rights_gate import evaluate
class T(unittest.TestCase):
 def test_unknown(self): self.assertFalse(evaluate("UNKNOWN","https://example.org/license").approved)
 def test_no_evidence(self): self.assertFalse(evaluate("CC0","").approved)
 def test_cc_by(self): self.assertTrue(evaluate("CC-BY","https://creativecommons.org/licenses/by/4.0/").approved)
 def test_nd_rejected(self): self.assertFalse(evaluate("CC-BY-ND","https://example.org/license").approved)
if __name__=="__main__":unittest.main()
