import unittest

from src.problem_002 import get_even_fibonacci_sum


class MyTestCase(unittest.TestCase):
    def test_get_even_fibonacci_sum_n(self):
        """
        nの値が負の場合
        """
        test_list = [
            {'n': -3, 'expect': 0},
            {'n': -1, 'expect': 0},
            {'n': 0, 'expect': 0},
            {'n': 1, 'expect': 0},
            {'n': 3, 'expect': 2},
        ]
        for test in test_list:
            with self.subTest(**test):
                result = get_even_fibonacci_sum(n=test['n'])
                self.assertEqual(test['expect'], result)


if __name__ == '__main__':
    unittest.main()
