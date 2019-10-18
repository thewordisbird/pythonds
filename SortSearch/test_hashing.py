import pytest
from hashing import remainder_hash, folding_hash, mid_square_hash
# Tests for hashing.py

@pytest.mark.parametrize('size, item, result',
                        [
                            (11, 10, 10),
                            (7, 13, 6),
                            (5, 11, 1),
                            (5, 0, 0)
                        ])
def test_remainder_hash(size, item, result):
    assert remainder_hash(size, item) == result

@pytest.mark.parametrize('size, item, result',
                        [
                            (11, 4365554601, 1),
                            (7, 2, 2)
                        ])
def test_folding_hash_default(size, item, result):
    assert folding_hash(size, item) == result

@pytest.mark.parametrize('size, item, group, result',
                        [
                            (11, 4365554601, 3, 6),
                            (7, 2, 4, 2)
                        ])
def test_folding_hash(size, item, group, result):
    assert folding_hash(size, item, group) == result

@pytest.mark.parametrize('size, item, result',
                        [
                            (7, 192343, 6),
                            (11, 0, 0),
                            (5, 1, 1),
                            (7, 2, 4),
                            (9, 3, 0),
                            (5, 4, 1),
                            (5, 11, 2)
                        ])
def test_mid_square_hash(size, item, result):
    assert mid_square_hash(size, item) == result

