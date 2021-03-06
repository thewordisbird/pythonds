import pytest
from dijkstra import PriorityQueueMap, dijkstra

@pytest.fixture(scope='function')
def graph():
    return {
                'u': {'v': 2, 'x': 1, 'w': 5}, 'v': {'u': 2, 'x': 2, 'w': 3},
                'x': {'u': 1, 'v': 2, 'w': 3, 'y': 1}, 'w': {'v': 3, 'u': 5, 'x': 3, 'y': 1, 'z': 5},
                'y': {'x': 1, 'w': 1, 'z': 1}, 'z': {'w': 5, 'y': 1}
            } 

@pytest.fixture(scope='function')
def empty_pqm():
    return PriorityQueueMap()

@pytest.fixture(scope='function')
def loaded_pqm(graph):
    pqm = PriorityQueueMap()
    pqm.build_from_graph(graph)
    return pqm

@pytest.fixture(scope='function')
def loaded_pqm_non_inf():
    pqm = PriorityQueueMap()
    pqm.heap_list = [
                        ('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 5), 
                        ('f', 7), ('g', 11), ('h', 13)
                    ]
    pqm.node_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    return pqm

def test_graph_fixture(graph):
    assert graph == {
                'u': {'v': 2, 'x': 1, 'w': 5}, 'v': {'u': 2, 'x': 2, 'w': 3},
                'x': {'u': 1, 'v': 2, 'w': 3, 'y': 1}, 'w': {'v': 3, 'u': 5, 'x': 3, 'y': 1, 'z': 5},
                'y': {'x': 1, 'w': 1, 'z': 1}, 'z': {'w': 5, 'y': 1}
            } 


# Test Priority Queue via Heap/Map
def test_build_from_graph(empty_pqm, graph):
    empty_pqm.build_from_graph(graph)
    assert len(empty_pqm.heap_list) == 6

def test_swap(loaded_pqm):
    assert loaded_pqm.heap_list[0][0] == 'u' 
    assert loaded_pqm.node_map['u'] == 0
    assert loaded_pqm.heap_list[5][0] == 'z'
    assert loaded_pqm.node_map['z'] == 5
    loaded_pqm.swap(0, 5)
    assert loaded_pqm.heap_list[0][0] == 'z' 
    assert loaded_pqm.node_map['z'] == 0
    assert loaded_pqm.heap_list[5][0] == 'u'
    assert loaded_pqm.node_map['u'] == 5

# NEED TO FINSIH BUILDING TEST TO MAKE SURE NODE MAP IS UPDATED CORRECTLY
def test_heapify_up_from_bottom(loaded_pqm):
    loaded_pqm.heap_list.append(('t', 3))
    loaded_pqm.node_map['t'] = len(loaded_pqm.heap_list) - 1
    print(loaded_pqm.node_map)
    assert loaded_pqm.heap_list[-1] == ('t', 3)
    loaded_pqm.heapify_up()
    position = loaded_pqm.node_map['t']
    assert loaded_pqm.heap_list[position] == ('t', 3)

def test_heapify_up_from_mid(loaded_pqm):
    loaded_pqm.heap_list.insert(3, ('t', 3))
    
    for k,v in loaded_pqm.node_map.items():
        if v >= 3:
            loaded_pqm.node_map[k] = v + 1
    loaded_pqm.node_map['t'] = 3
    assert loaded_pqm.heap_list[3] == ('t', 3)
    loaded_pqm.heapify_up(3)
    position = loaded_pqm.node_map['t']
    assert loaded_pqm.heap_list[position] == ('t', 3)

def test_heapify_down_from_top(loaded_pqm_non_inf):
    loaded_pqm_non_inf.heap_list.insert(0, ('t', 20))
    for k,v in loaded_pqm_non_inf.node_map.items():
        if v >= 0:
            loaded_pqm_non_inf.node_map[k] = v + 1
    loaded_pqm_non_inf.node_map['t'] = 0
    assert loaded_pqm_non_inf.heap_list[0] == ('t', 20)
    loaded_pqm_non_inf.heapify_down()
    position = loaded_pqm_non_inf.node_map['t']
    assert loaded_pqm_non_inf.heap_list[position] == ('t', 20)

def test_poll(loaded_pqm_non_inf):
    assert loaded_pqm_non_inf.poll() == ('a', 0)
    assert loaded_pqm_non_inf.heap_list[3] == ('h', 13)

def test_set_distance(loaded_pqm):
    loaded_pqm.set_distance('w', 5)
    assert loaded_pqm.heap_list[loaded_pqm.node_map['w']] == ('w', 5)

def test_dijkstra(graph):
    parent = dijkstra(graph, 'u')
    assert parent == {'u': None, 'v': 'u', 'x': 'u', 'w': 'y', 'y': 'x', 'z': 'y'}