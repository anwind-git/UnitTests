from discount import Calculator
import unittest


class CalculatorTest(unittest.TestCase):
    def test_calculateDiscount(self):
        calculator = Calculator()
        expected_discounted_amount = 900
        discounted_amount = calculator.calculateDiscount(1000, 10)

        self.assertEqual(discounted_amount, expected_discounted_amount)


if __name__ == '__main__':
    unittest.main()