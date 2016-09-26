import unittest
from p import p

class pTestCase(unittest.TestCase):
    """Tests for `p.py`."""

    def test_7_p(self):
        """Is 7 successfully determined to be prime?"""
        self.assertTrue(p(7))

if __name__ == '__main__':
    unittest.main()


