import math
import random
import unittest
from parameterized import parameterized
from app.main import Calculator
from math import inf
from app.error import InvalidInputException


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def tearDown(self) -> None:
        ...

    @parameterized.expand(
        # 1. arrange
        [
            ("integers", 2, 3, 5),
            ("floats", 2.5, 3.1, 5.6),
            ("negative", -2.5, 3.0, 0.5)
        ]
    )
    def test_sum(self, name, a, b, expected_result):
        # 2. act
        actual_result = self.calc.sum(a, b)

        # 3. assert
        self.assertEqual(actual_result, expected_result)

    @parameterized.expand([
        ("strings", 'aaa', 'bbb', TypeError),
        ("int_None", 1, None, TypeError),
        ("None_float", None, 1.1, TypeError),
        ("None_None", None, None, TypeError)

    ])
    def test_sum_invalid_values(self, name, a, b, expected_result):
        with self.assertRaises(expected_result):
            self.calc.sum(a, b)

    @parameterized.expand([
        ("list_integers", [1, 2, 3, 4], 10),
        ("list_empty", [], 0),
        ("list_single", [1], 1)
    ])
    def test_sum_list(self, name, a, expected_result):
        # 2. act
        actual_result = self.calc.sum(*a)
        # 3. assert
        self.assertEqual(actual_result, expected_result)

    @parameterized.expand([
        ("tuple_integers", (1, 2, 3, 4), 10),
        ("tuple_empty", (), 0),
        ("tuple_single", (1,), 1),
        ("set_integers", {1, 2, 3, 4}, 10),
        ("set_empty", {}, 0),
        ("set_single", {1}, 1),
    ])
    def test_sum_tuple(self, name, a, expected_result):
        # 2. act
        actual_result = self.calc.sum(*a)
        # 3. assert
        self.assertEqual(actual_result, expected_result)

    def test_greater_less(self):
        a = random.randint(1, 10)
        b = random.randint(1, 10)

        print(a, b)

        if b - a > 0:
            print("assert less")
            self.assertLess(a, b)
        else:
            print("assert greater")
            self.assertGreater(a, b)

        #actual_result = self.calc.greater(a, b)
        #expected_result = a > b

    def test_multiply(self):
        a = 5
        b = 0.000000005

        actual_result = self.calc.multiply(a, b)
        expected_result = 0

        self.assertAlmostEqual(actual_result, expected_result)

    def test_divide(self):
        a = 5
        b = 0

        expected_result = ZeroDivisionError

        with self.assertRaises(expected_result):
            self.calc.divide(a, b)

    def test_divide_inf(self):
        a = inf
        b = inf

        expected_result = None
        actual_result = self.calc.divide(a, b)

        self.assertNotEqual(actual_result, expected_result)
        self.assertIsInstance(actual_result, type(math.inf))
        self.assertIsInstance(actual_result, float)

    @parameterized.expand([
        # Тесты на обычное правильное использование функции
        ("positive_integers", 10, 2, math.log(10, 2)),
        ("positive_floats", 2.5, 1.5, math.log(2.5, 1.5)),
        ("large_values", 1000, 10, math.log(1000, 10)),
        ("log_base_e", math.e, math.e, 1.0),  # log(e) по основанию e = 1
    ])

    def test_log_valid(self, name, a, base, expected_result):
        actual_result = self.calc.log(a, base)
        self.assertAlmostEqual(actual_result, expected_result)

    @parameterized.expand([
        # Тесты на неправильные типы входных данных
        ("string_base", '10', 2, TypeError),
        ("string_a", 10, '2', TypeError),
        ("list_base", 10, [2], TypeError),
        ("dict_a", {'a': 10}, 2, TypeError),
        ("None_base", 10, None, TypeError),
        ("None_a", None, 2, TypeError)
    ])
    def test_log_invalid_types(self, name, a, base, expected_exception):
        with self.assertRaises(expected_exception):
            self.calc.log(a, base)

    @parameterized.expand([
        # Тесты на значения, которые не входят в ОДЗ функции
        ("zero_base", 10, 0, InvalidInputException),
        ("negative_a", -10, 2, InvalidInputException),
        ("negative_base", 10, -2, InvalidInputException),
        ("zero_a", 0, 2, InvalidInputException),
        ("a_is_one", 1, 2, InvalidInputException)  # Логарифм от 1 не определен для положительного основания
    ])
    def test_log_invalid_values(self, name, a, base, expected_exception):
        with self.assertRaises(expected_exception):
            self.calc.log(a, base)


    @parameterized.expand([
        # Дополнительные тесты на граничные значения, такие как очень малые и очень большие числа
        ("very_small_values", 1e-10, 2, math.log(1e-10, 2)),
        ("very_large_values", 1e10, 2, math.log(1e10, 2)),
    ])
    def test_log_edge_cases(self, name, a, base, expected_result):
        actual_result = self.calc.log(a, base)
        self.assertAlmostEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()
