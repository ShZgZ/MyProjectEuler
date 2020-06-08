"""Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

和訳
13195の素因数は5, 7, 13, 29である。

では600851475143の素因数の内、最大のものは何か？
"""
import doctest
from typing import List


def main():
    """
    600851475143の素因数の内、最大のものを求める。
    """
    target_num = 600851475143

    result = GetPrimeFactor(target_num).execute()
    print(f'{target_num}の素因数の内、最大のもの: {result[-1]}')


class GetPrimeFactor:
    """
    素因数のリスト取得を行うクラス
    """
    # 最小の素数
    MINIMAL_PRIME = 2

    def __init__(self, num):
        """
        :param num: この数以下の素因数を対象とする。
        """
        self._num = num

    # getter
    @property
    def num(self):
        return self._num

    def execute(self) -> List[int]:
        """
        self.num以下の素因数を取得する。
        :return: 素因数のリスト

        >>> GetPrimeFactor(5).execute()
        [5]

        >>> GetPrimeFactor(10).execute()
        [2, 5]

        >>> GetPrimeFactor(33).execute()
        [3, 11]
        """
        target_num = self.num
        # 素因数のリストを作っていく
        prime_list = []
        # 2未満の数が指定された場合には空のリストを返す。
        if target_num < self.MINIMAL_PRIME:
            return prime_list
        # 素数2で判定
        test_num = self.MINIMAL_PRIME
        if target_num % test_num == 0:
            prime_list.append(test_num)
            target_num = self.divide(target_num, test_num)
        # 3以降の奇数にて判定
        test_num += 1
        while target_num != 1:
            if target_num % test_num == 0:
                prime_list.append(test_num)
                target_num = self.divide(target_num, test_num)
            test_num += 2

        return prime_list

    @staticmethod
    def divide(divisor: int, dividend: int) -> int:
        """
        与えられたaをbで割り切った値を返す。
        割れなかった場合にはaを返す。

        :param divisor: 割られる数
        :param dividend: 割りきる数
        :return: 割り切られた数

        >>> GetPrimeFactor.divide(10, 2)
        5

        >>> GetPrimeFactor.divide(5, 2)
        5
        """
        target_num = divisor
        while target_num % dividend == 0:
            target_num /= dividend
        return int(target_num)


if __name__ == '__main__':
    doctest.testmod()
    main()  # 600851475143の素因数の内、最大のもの: 6857
