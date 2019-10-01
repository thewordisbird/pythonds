import pytest
from queue2 import Node, LinkedList, Queue

# Tests for Node Class
def test_constuct_node():
    n = Node('test')
    assert n.data == 'test'
    assert n.next == None
    assert n.previous == None

def test_setNext():
    n = Node('test')
    n.setNext('next node')
    assert n.next == 'next node'
    assert n.previous == None

def test_setPrevious():
    n = Node('test')
    n.setPrevious('previous node')
    assert n.previous == 'previous node'
    assert n.next == None

def test_getNext():
    n = Node('test')
    assert n.getNext() == None
    n.setNext('next node')
    assert n.getNext() == 'next node'

def test_getPrevious():
    n = Node('test')
    assert n.getPrevious() == None
    n.setPrevious('previous node')
    assert n.getPrevious() == 'previous node'

def test_getData():
    n = Node('test')
    assert n.getData() == 'test'

# Tests for LinkedList Class
@ pytest.fixture
def empty_LinkedList():
    return LinkedList()

@pytest.fixture
def populated_LinkedList():
    l = LinkedList()
    l.append('justin')
    l.append('lindsay')
    l.append('amanda')
    l.append('laurie')
    l.append('steve')
    return l

def test_constuct_LinkedList(empty_LinkedList):
    l = empty_LinkedList
    assert l.head == None
    assert l.tail == None

def test_append_LinkedList(empty_LinkedList):
    l = empty_LinkedList
    l.append('justin')
    assert l.head.getData() == 'justin'
    assert l.tail.getData() == 'justin'
    l.append('lindsay')
    assert l.head.getData() == 'justin'
    assert l.tail.getData() == 'lindsay'

def test_append_left_LinkedList(empty_LinkedList):
    l = empty_LinkedList
    l.append_left('justin')
    assert l.head.getData() == 'justin'
    assert l.tail.getData() == 'justin'
    l.append_left('lindsay')
    assert l.head.getData() == 'lindsay'
    assert l.tail.getData() == 'justin'

def test_pop_LinkedList(populated_LinkedList):
    l = populated_LinkedList
    assert l.pop() == 'steve'
    assert l.pop() == 'laurie'

def test_pop_left_LinkedList(populated_LinkedList):
    l = populated_LinkedList
    assert l.pop_left() == 'justin'
    assert l.pop_left() == 'lindsay'

# Tests for Queue Class
@pytest.fixture
def empty_queue():
    return Queue()

def test_construct_queue(empty_queue):
    q = empty_queue
    assert q.items.head == None
    assert q.items.tail == None

def test_enque_queue(empty_queue):
    q = empty_queue
    q.enqueue('justin')
    assert q.items.head.getData() == 'justin'
    assert q.items.tail.getData() == 'justin'
    q.enqueue('lindsay')
    assert q.items.head.getData() == 'justin'
    assert q.items.tail.getData() == 'lindsay'
    q.enqueue('amanda')
    assert q.items.head.getData() == 'justin'
    assert q.items.tail.getData() == 'amanda'

def test_dequeue_queue(empty_queue):
    q = empty_queue
    q.enqueue('justin')
    q.enqueue('lindsay')
    q.enqueue('amanda')
    q.enqueue('laurie')
    q.enqueue('steve')
    assert q.dequeue() == 'justin'
    assert q.dequeue() == 'lindsay'
