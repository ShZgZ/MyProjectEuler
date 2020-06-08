import pytest

from src.problem_001 import get_multiples_sum


@pytest.mark.parametrize('number, expected', [
    (0, 0),
    (1, 0),
    (5, 0),
    (10, 0),
])
def test_get_multiples_sum_numbers_0(number, expected):
    """
    可変長引数のnumbersが0個の場合
    """
    result = get_multiples_sum(below_num=number)
    assert expected == result


@pytest.mark.parametrize('below_num, numbers, expected', [
    (5, [1], 10),
    (10, [1], 45),
    (5, [2], 6),
    (10, [2], 20),
])
def test_get_multiples_sum_numbers_1(below_num, numbers, expected):
    """
    可変長引数のnumbersが1個の場合
    """
    result = get_multiples_sum(*numbers, below_num=below_num)
    assert expected == result


@pytest.mark.parametrize('below_num, numbers, expected', [
    (5, [1, 2], 10),
    (10, [1, 2], 45),
    (5, [2, 3], 9),
    (10, [2, 3], 32),
    (10, [3, 5], 23),
])
def test_get_multiples_sum_numbers_2(below_num, numbers, expected):
    """
    可変長引数のnumbersが2個の場合
    """
    result = get_multiples_sum(*numbers, below_num=below_num)
    assert expected == result


@pytest.mark.parametrize('numbers, expected', [
    ([1], 0),
    ([1, 2], 0),
    ([1, 2, 3], 0),
])
def test_get_multiples_sum_below_num_0(numbers, expected):
    """
    below_numが0の場合
    """
    result = get_multiples_sum(*numbers, below_num=0)
    assert expected == result


@pytest.mark.parametrize('numbers, expected', [
    ([1], 0),
    ([1, 2], 0),
    ([1, 2, 3], 0),
])
def test_get_multiples_sum_below_num_1(numbers, expected):
    """
    below_numが1の場合
    """
    result = get_multiples_sum(*numbers, below_num=1)
    assert expected == result
