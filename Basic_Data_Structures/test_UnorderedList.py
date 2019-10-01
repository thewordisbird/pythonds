import pytest
from UnorderedList import Node, UnorderedList, UnorderedList_1

# Test Node class
@pytest.fixture
def create_node(scope='session'):
    return Node('justin')

def test_node_construct(create_node):
    n = create_node
    assert n.data == 'justin'
    assert n.next == None

def test_node_getData(create_node):
    n = create_node
    assert n.getData() == 'justin'

def test_node_getNext(create_node):
    n = create_node
    assert n.getNext() == None

def test_node_setData(create_node):
    n = create_node
    assert n.getData() == 'justin'
    n.setData('ray')
    assert n.getData() == 'ray'

def test_node_setNext(create_node):
    n = create_node
    assert n.getNext() == None
    n.setNext('next node')
    assert n.getNext() == 'next node'

# Test UnorderedList class
@pytest.fixture(scope='function')
def create_unordered_list():
    return UnorderedList()

@pytest.fixture(scope='function')
def create_unordered_list_one_item():
    ul = UnorderedList()
    ul.add('justin')
    return ul

@pytest.fixture(scope='function')
def create_unordered_list_multi_item():
    ul = UnorderedList()
    ul.add('justin')
    ul.add('lindsay')
    ul.add('amanda')
    ul.add('laurie')
    ul.add('steve')
    ul.add(34)
    ul.add(31)
    ul.add(31)
    ul.add(62)
    ul.add(69)
    return ul

def test_UL_construct(create_unordered_list):
    ul = create_unordered_list
    assert ul.head == None

def test_UL_add_first(create_unordered_list):
    ul = create_unordered_list
    ul.add('justin')
    assert ul.head.getData() == 'justin'
    assert ul.head.getNext() == None

def test_UL_add(create_unordered_list_one_item):
    ul = create_unordered_list_one_item
    assert ul.head.getData() == 'justin'
    assert ul.head.getNext() == None
    ul.add('ray')
    assert ul.head.getData() == 'ray'
    assert ul.head.getNext().getData() == 'justin'

def test_UL_size(create_unordered_list_multi_item):
    ul = create_unordered_list_multi_item
    assert ul.size() == 10

def test_UL_remove_only_item(create_unordered_list_one_item):
    ul = create_unordered_list_one_item
    assert ul.head.getData() == 'justin'
    ul.remove('justin')
    assert ul.head == None

def test_UL_remove_item(create_unordered_list_multi_item):
    ul = create_unordered_list_multi_item
    print(ul.head.getData(), ul.size())
    ul.remove('justin')
    assert ul.head != None
    assert ul.size() == 9
    ul.remove(34)
    assert ul.size() == 8
    ul.remove(69)
    assert ul.size() == 7

def test_UL_isEmpty(create_unordered_list):
    ul = create_unordered_list
    assert ul.isEmpty() == True
    ul.add('item1')
    assert ul.isEmpty() == False

def test_UL_search(create_unordered_list_multi_item):
    ul = create_unordered_list_multi_item
    assert ul.search('justin') == True
    assert ul.search(31) == True
    assert ul.search(43) == False

def test_UL_append_first(create_unordered_list):
    ul = create_unordered_list
    assert ul.head == None
    ul.append('justin')
    assert ul.head.getData() == 'justin'

def test_UL_append(create_unordered_list_multi_item):
    ul = create_unordered_list_multi_item
    ul_size = ul.size()
    assert ul.head.getData() == 69
    ul.append('ray')
    assert ul.head.getData() == 69
    assert ul.search('ray') == True
    assert ul.size() == ul_size + 1


# Test UnorderedList_1 class. This class adds a tail attribute to make append
# O(1) rather than O(n) operation
@pytest.fixture
def create_unordered_list_1():
    return UnorderedList_1()

@pytest.fixture(scope='function')
def create_unordered_list_one_item_1():
    ul = UnorderedList_1()
    ul.add('justin')
    return ul

@pytest.fixture(scope='function')
def create_unordered_list_multi_item_1():
    ul = UnorderedList_1()
    ul.add('justin')
    ul.add('lindsay')
    ul.add('amanda')
    ul.add('laurie')
    ul.add('steve')
    ul.add(34)
    ul.add(31)
    ul.add(31)
    ul.add(62)
    ul.add(69)
    return ul

def test_UL1_construct(create_unordered_list_1):
    ul = create_unordered_list_1
    assert ul.head == None
    assert ul.tail == None

def test_UL1_add_first(create_unordered_list_1):
    ul = create_unordered_list_1
    ul.add('justin')
    assert ul.head.getData() == 'justin'
    assert ul.head.getNext() == None
    assert ul.tail.getData() == 'justin'

def test_UL1_add(create_unordered_list_one_item_1):
    ul = create_unordered_list_one_item_1
    assert ul.head.getData() == 'justin'
    assert ul.head.getNext() == None
    assert ul.tail.getData() == 'justin'
    ul.add('ray')
    assert ul.head.getData() == 'ray'
    assert ul.head.getNext().getData() == 'justin'
    assert ul.tail.getData() == 'justin'

def test_UL1_size(create_unordered_list_multi_item_1):
    ul = create_unordered_list_multi_item_1
    assert ul.size() == 10

def test_UL1_remove_only_item(create_unordered_list_one_item_1):
    ul = create_unordered_list_one_item_1
    assert ul.head.getData() == 'justin'
    assert ul.tail.getData() == 'justin'
    ul.remove('justin')
    assert ul.head == None
    assert ul.tail == None

def test_UL1_remove_item(create_unordered_list_multi_item_1):
    ul = create_unordered_list_multi_item_1
    ul.remove('justin')
    assert ul.head != None
    assert ul.size() == 9
    ul.remove(34)
    assert ul.size() == 8
    ul.remove(69)
    assert ul.size() == 7

def test_UL1_isEmpty(create_unordered_list_1):
    ul = create_unordered_list_1
    assert ul.isEmpty() == True
    ul.add('item1')
    assert ul.isEmpty() == False

def test_UL1_append_first(create_unordered_list_1):
    ul = create_unordered_list_1
    assert ul.head == None
    ul.append('justin')
    assert ul.head.getData() == 'justin'

def test_UL1_append(create_unordered_list_multi_item_1):
    ul = create_unordered_list_multi_item_1
    ul_size = ul.size()
    assert ul.head.getData() == 69
    ul.append('ray')
    assert ul.head.getData() == 69
    assert ul.search('ray') == True
    assert ul.size() == ul_size + 1