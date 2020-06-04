import unittest

from src.problem_002 import get_even_fibonacci_sum


class MyTestCase(unittest.TestCase):
    def test_get_even_fibonacci_sum_n(self):
        """
        nの値
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

    def test_get_even_fibonacci_sum_t_error(self):
        """
        エラーとなること
        """
        test_list = [
            # どちらか負
            {'t1': -1, 't2': -1, 'error_flg': True},
            {'t1': -1, 't2': 0, 'error_flg': True},
            {'t1': -1, 't2': 1, 'error_flg': True},
            {'t1': -1, 't2': -1, 'error_flg': True},
            {'t1': 0, 't2': -1, 'error_flg': True},
            {'t1': 1, 't2': -1, 'error_flg': True},
            # どちらも0
            {'t1': 0, 't2': 0, 'error_flg': True},
            # どちらか正
            {'t1': 1, 't2': 0, 'expect': 10, 'error_flg': False},
            {'t1': 0, 't2': 1, 'expect': 10, 'error_flg': False},
            {'t1': 1, 't2': 1, 'expect': 10, 'error_flg': False},
        ]
        for test in test_list:
            with self.subTest(**test):
                if test['error_flg']:
                    with self.assertRaises(Exception):
                        get_even_fibonacci_sum(n=10, t1=test['t1'], t2=test['t2'])
                else:
                    result = get_even_fibonacci_sum(n=10, t1=test['t1'], t2=test['t2'])
                    self.assertEqual(test['expect'], result)


if __name__ == '__main__':
    unittest.main()
