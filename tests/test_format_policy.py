import unittest
from orchestrator.format_policy import choose_format,output_profile,SHORT,STANDARD
class T(unittest.TestCase):
 def test_empty(self): self.assertEqual(choose_format([]),SHORT)
 def test_short_underrepresented(self): self.assertEqual(choose_format([STANDARD,STANDARD,SHORT]),SHORT)
 def test_standard_underrepresented(self): self.assertEqual(choose_format([SHORT,SHORT,STANDARD]),STANDARD)
 def test_profiles(self): self.assertEqual(output_profile(SHORT)["aspect"],"9:16");self.assertEqual(output_profile(STANDARD)["aspect"],"16:9")
 def test_bad_format(self):
  with self.assertRaises(ValueError): output_profile("square")
if __name__=="__main__":unittest.main()
