import pytest

from src.problem_002 import get_even_fibonacci_sum


@pytest.mark.parametrize('number, expected', [
    (-3, 0),
    (-1, 0),
    (0, 0),
    (1, 0),
    (3, 2),
])
def test_get_even_fibonacci_sum_n(number, expected):
    """
    nの値
    """
    result = get_even_fibonacci_sum(n=number)
    assert expected == result


@pytest.mark.parametrize('t1, t2, expected, error_flg', [
    # どちらか負
    (-1, -1, 0, True),
    (-1, 0, 0, True),
    (-1, 1, 0, True),
    (-1, -1, 0, True),
    (0, -1, 0, True),
    (1, -1, 0, True),
    # どちらも0
    (0, 0, 0, True),
    # どちらか正
    (1, 0, 10, False),
    (0, 1, 10, False),
    (1, 1, 10, False),
])
def test_get_even_fibonacci_sum_t_error(t1, t2, expected, error_flg):
    """
    エラーとなること
    """
    if error_flg:
        with pytest.raises(Exception):
            get_even_fibonacci_sum(n=10, t1=t1, t2=t2)
    else:
        result = get_even_fibonacci_sum(n=10, t1=t1, t2=t2)
        assert expected == result
