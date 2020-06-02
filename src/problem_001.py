"""Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

和訳:3と5の倍数
10未満の自然数で3と5の倍数は3,5,6,9となり、これらの倍数の和は23となる。
1000未満の3と5の倍数の和を求めよ。
"""
import doctest


def main():
    """
    1000未満で3と5の倍数の和を求める。
    """
    below_num = 1000
    n0 = 3
    n1 = 5

    result = get_multiples_sum(n0, n1, below_num=below_num)
    print(result)


def get_multiples_sum(*numbers: int, below_num: int) -> int:
    """
    below_num未満の自然数でnumbersに含まれる数の倍数の和を求める。
    :param numbers: 倍数の判定対象となる数字
    :param below_num: 最大数
    :return: 倍数の和

    >>> get_multiples_sum(3, 5, below_num=10)
    23
    """
    count = 0
    for i in range(1, below_num):
        for j in numbers:
            if i % j == 0:
                count += i
                break

    return count


if __name__ == '__main__':
    doctest.testmod()
    main()  # 233168
