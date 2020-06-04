import unittest

from src.problem_001 import get_multiples_sum


class MyTestCase(unittest.TestCase):
    def test_get_multiples_sum_numbers_0(self):
        """
        可変長引数のnumbersが0個の場合
        """
        below_num_list = [0, 1, 5, 10]
        for i in below_num_list:
            with self.subTest(below_num=i):
                result = get_multiples_sum(below_num=i)
                self.assertEqual(0, result)

    def test_get_multiples_sum_numbers_1(self):
        """
        可変長引数のnumbersが1個の場合
        """
        test_list = [
            {'below_num': 5, 'numbers': [1], 'result': 10},
            {'below_num': 10, 'numbers': [1], 'result': 45},
            {'below_num': 5, 'numbers': [2], 'result': 6},
            {'below_num': 10, 'numbers': [2], 'result': 20},
        ]

        for m in test_list:
            with self.subTest(**m):
                result = get_multiples_sum(*m['numbers'], below_num=m['below_num'])
                self.assertEqual(m['result'], result)

    def test_get_multiples_sum_numbers_2(self):
        """
        可変長引数のnumbersが2個の場合
        """
        test_list = [
            {'below_num': 5, 'numbers': [1, 2], 'result': 10},
            {'below_num': 10, 'numbers': [1, 2], 'result': 45},
            {'below_num': 5, 'numbers': [2, 3], 'result': 9},
            {'below_num': 10, 'numbers': [2, 3], 'result': 32},
            {'below_num': 10, 'numbers': [3, 5], 'result': 23},
        ]

        for m in test_list:
            with self.subTest(**m):
                result = get_multiples_sum(*m['numbers'], below_num=m['below_num'])
                self.assertEqual(m['result'], result)

    def test_get_multiples_sum_below_num_0(self):
        """
        below_numが0の場合
        """
        numbers_list = [[1], [1, 2], [1, 2, 3]]
        for numbers in numbers_list:
            with self.subTest(numbers=numbers):
                result = get_multiples_sum(*numbers, below_num=0)
                self.assertEqual(0, result)

    def test_get_multiples_sum_below_num_1(self):
        """
        below_numが1の場合
        """
        numbers_list = [[1], [1, 2], [1, 2, 3]]
        for numbers in numbers_list:
            with self.subTest(numbers=numbers):
                result = get_multiples_sum(*numbers, below_num=0)
                self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
