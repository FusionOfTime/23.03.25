import unittest
import math


def check_equality(a, b, c):
    return math.isclose(a + b, c)


class EqualityCheckTestCase(unittest.TestCase):
    def test_equal1(self):
        self.assertEqual(check_equality(0.1, 0.2, 0.3), True)

    def test_equal2(self):
        self.assertEqual(check_equality(2, 3, 5), True)

    def test_not_equal1(self):
        self.assertEqual(check_equality(2, 3, 7), False)

    def test_not_equal2(self):
        self.assertEqual(check_equality(0.1, 0.2, 0.4), False)

    def test_tolerance(self):
        calculated_sum = 0.1 + 0.2
        self.assertEqual(check_equality(calculated_sum, 0.0, calculated_sum), True)


def main():
    a = float(input())
    b = float(input())
    c = float(input())

    if check_equality(a, b, c):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()