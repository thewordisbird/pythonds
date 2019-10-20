import pytest
from hashing import remainder_hash, folding_hash, mid_square_hash, Map
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

@pytest.fixture(scope='function')
def map_fixture_empty():
    size = 7
    return Map(size)

@pytest.fixture(scope='function')
def map_fixture_data():
    size = 7
    testMap = Map(size)
    testMap.put(0, 'Justin')
    testMap.put(1, 'Lindsay')
    testMap.put(2, 'Amanda')
    testMap.put(3, 'Laurie')
    testMap.put(5, 'Steve')

def test_Map_construction_empty(map_fixture_empty):
    '''Test that class constructor works'''
    testMap = map_fixture_empty
    assert testMap.size == 7
    assert testMap.slots[1] == None
    assert testMap.data[5] == None
    assert testMap.items == 0

def tets_Map_construction_data(map_fixture_data):
    testMap = map_fixture_data
    assert testMap.size == 7
    assert testMap.slots[0] == 0
    assert testMap.data[0] == 'Justin'


@pytest.mark.parametrize('item, result',
                        [
                            (10, 3),
                            (13, 6),
                            (11, 4),
                            (0, 0)
                        ])
def test_Map_hash(map_fixture_empty, item, result):
    testMap = map_fixture_empty
    assert testMap.remainder_hash(item) == result


#def test_Map_rehash(map_fixture_datagit):
#    pass

@pytest.mark.parametrize('key, val, result_slot',
                        [
                            (10, 'justin', 3),
                            (13, 'lindsay', 6)
                        ])
def test_Map_put_empty(map_fixture_empty, key, val, result_slot):
    testMap = map_fixture_empty
    assert testMap.slots[result_slot] == None
    assert testMap.data[result_slot] == None
    testMap.put(key, val)
    assert testMap.slots[result_slot] == key
    assert testMap.data[result_slot] == val

def tets_Map_put_update(map_fixture_data):
    testMap = map_fixture_data
    assert testMap.size == 7
    assert testMap.slots[0] == 0
    assert testMap.data[0] == 'Justin'
    testMap.put(0, 'new_name')
    assert testMap.slots[0] == 0
    assert testMap.data[0] == 'new_name'