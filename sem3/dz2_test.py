import unittest
from dz2 import number_in_interval


class TestNumberInInterval(unittest.TestCase):
    def test_number_in_interval(self):
        self.assertTrue(number_in_interval(50))
        self.assertTrue(number_in_interval(75))
        self.assertFalse(number_in_interval(10))
        self.assertFalse(number_in_interval(200))


if __name__ == '__main__':
    unittest.main()