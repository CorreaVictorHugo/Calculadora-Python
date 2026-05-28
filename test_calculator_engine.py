import unittest

from calculator_engine import CalculatorError, calculate


class CalculatorEngineTest(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculate("2+3"), 5)
        self.assertEqual(calculate("10-4"), 6)
        self.assertEqual(calculate("6*7"), 42)
        self.assertEqual(calculate("8/2"), 4)

    def test_operator_precedence(self):
        self.assertEqual(calculate("2+3*4"), 14)
        self.assertEqual(calculate("(2+3)*4"), 20)

    def test_chained_sum(self):
        self.assertEqual(calculate("3+3+3"), 9)

    def test_decimal_result(self):
        self.assertEqual(calculate("5/2"), 2.5)

    def test_modulo_operation(self):
        self.assertEqual(calculate("10%3"), 1)

    def test_invalid_expression_raises_error(self):
        with self.assertRaises(CalculatorError):
            calculate("__import__('os').system('dir')")

    def test_division_by_zero_raises_error(self):
        with self.assertRaises(CalculatorError):
            calculate("10/0")


if __name__ == "__main__":
    unittest.main()
