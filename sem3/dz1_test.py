import unittest
from dz1 import even_odd_number


class EvenOddNumberTest(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(even_odd_number(2))
        self.assertTrue(even_odd_number(0))
        self.assertTrue(even_odd_number(-4))

    def test_odd_number(self):
        self.assertFalse(even_odd_number(5))
        self.assertFalse(even_odd_number(-7))

    def test_zero(self):
        self.assertTrue(even_odd_number(0))

    def test_negative_number(self):
        self.assertTrue(even_odd_number(-4))
        self.assertFalse(even_odd_number(-7))


if __name__ == '__main__':
    unittest.main()