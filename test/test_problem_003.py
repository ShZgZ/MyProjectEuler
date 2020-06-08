import pytest

from src.problem_003 import GetPrimeFactor


@pytest.mark.parametrize('number, expected', [
    (-2, []),
    (-1, []),
    (0, []),
    (1, []),
    (2, [2]),
])
def test_execute_under_two(number, expected):
    assert GetPrimeFactor(number).execute() == expected
