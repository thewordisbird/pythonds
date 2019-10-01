import pytest
from pascals import factorial, choose, pascals

@pytest.mark.parametrize('num, result',
                        [
                            (0, 1),
                            (1, 1),
                            (2, 2),
                            (3, 6),
                            (4, 24),
                            (5, 120)
                        ])
def test_factorial(num, result):
    assert factorial(num) == result

@pytest.mark.parametrize('num, result',
                        [
                            (0, [1]),
                            (1, [1, 1]),
                            (2, [1, 2, 1]),
                            (3, [1, 3, 3, 1]),
                            (4, [1, 4, 6, 4, 1])
                        ])
def test_choose(num, result):
    assert choose(num) == result

def test_pascals(rows):
    pass