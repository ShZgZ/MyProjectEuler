import unittest

from src.problem_003 import GetPrimeFactor


class MyTestCase(unittest.TestCase):
    def test_execute_under_2(self):
        """
        nの値
        """
        test_list = [
            {'n': -2, 'expect': []},
            {'n': -1, 'expect': []},
            {'n': 0, 'expect': []},
            {'n': 1, 'expect': []},
            {'n': 2, 'expect': [2]},
        ]
        for test in test_list:
            with self.subTest(**test):
                result = GetPrimeFactor(test['n']).execute()
                self.assertEqual(test['expect'], result)


if __name__ == '__main__':
    unittest.main()
