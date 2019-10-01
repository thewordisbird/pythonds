import pytest
from queue import Queue

@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def populated_queue():
    q = Queue()
    q.items = ['justin', 'lindsay', 'amanda', 'laurie', 'steve']
    return q

def test_constuct_queue(empty_queue):
    q = empty_queue
    assert q.items == []

def test_queue_size(populated_queue):
    q = populated_queue
    assert q.size() == 5

def test_isEmpty(populated_queue):
    q = populated_queue
    assert q.isEmpty() == False

def test_enqueu(populated_queue):
    q = populated_queue
    q.enqueue('ray')
    assert q.size() == 6
    assert q.items[len(q.items) - 1] == 'ray'

def test_dequeue(populated_queue):
    q = populated_queue
    assert q.dequeue() == 'justin'
    assert q.size() == 4