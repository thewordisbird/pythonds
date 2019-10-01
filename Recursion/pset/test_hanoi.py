import pytest
from hanoi import Stack, load_disks

#@pytest.fixture
#def stacks():  
#    return Stack(), Stack(), Stack()

def test_load_disks():
    a = Stack()
    disks = 5
    load_disks(disks, a)
    assert a.items == [5, 4, 3, 2, 1]
