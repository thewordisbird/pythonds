import pytest
from radix import radix_sort, max_digits, get_digit

@pytest.mark.parametrize('num, digits',
                        [
                            (1, 1),
                            (13, 2),
                            (423, 3)
                        ])
def test_max_digits(num, digits):
    assert max_digits(num) == digits

@pytest.mark.parametrize('num, digit, target',
                        [
                            (5, 1, 5),
                            (5, 2, 0),
                            (5, 3, 0),
                            (12, 1, 2),
                            (12, 2, 1),
                            (54321, 4, 4),
                            (0, 1, 0)
                        ])
def test_get_digit(num, digit, target):
    assert get_digit(num, digit) == target

@pytest.mark.parametrize('nums, result',
                        [
                            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
                            ([0, 100, 10, 10000], [0, 10, 100, 10000]),
                            ([312, 45, 709, 543, 8439, 45, 3], [3, 45, 45, 312, 543, 709, 8439])
                        ])
def test_radix_sort(nums, result):
    assert radix_sort(nums) == result