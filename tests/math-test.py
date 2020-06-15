import unittest
from src.math import addition

class MathTest(unittest.TestCase):
    def test_addition(self):
        actual = addition(3,4)
        expected = 7
        self.assertEqual(actual, expected)