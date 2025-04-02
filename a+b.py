import unittest


def sum_a_and_b(a, b):
    return a + b


class SumExpressionTestCase(unittest.TestCase):
    def test_simple1(self):
        estimated_result = 5
        real_result = sum_a_and_b(2, 3)
        self.assertEqual(real_result, estimated_result)

    def test_simple2(self):
        estimated_result = 10
        real_result = sum_a_and_b(8, 2)
        self.assertEqual(real_result, estimated_result)

    def test_simple3(self):
        estimated_result = 15
        real_result = sum_a_and_b(10, 5)
        self.assertEqual(real_result, estimated_result)

def main():
    try:
        line = input()
        a, b = map(int, line.split())
        result = sum_a_and_b(a, b)
        print(result)
    except:
        print("Ошибка: Введите два целых числа, разделенных пробелом.")


if __name__ == "__main__":
    main()