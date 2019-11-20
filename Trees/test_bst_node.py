import pytest
from bst import Node

# ------FIXTURES------
@pytest.fixture(scope='function')
def new_node():
    '''Fixture for node with all atributes given'''
    return Node(35, 'Justin', 'left_child', 'right_child', 'parent')

@pytest.fixture(scope='function')
def no_children_node():
    '''Fixture fir nide with only required attributes given'''
    return Node(35, 'Justin')

# ------TESTS------
def test_Node_construct(new_node):
    '''Test node construction'''
    assert new_node.key == 35
    assert new_node.value == 'Justin'
    assert new_node.left_child == 'left_child'
    assert new_node.right_child == 'right_child'
    assert new_node.parent == 'parent'

def test_get_left_child(new_node):
    '''Test get_left_child method of Node class'''
    assert new_node.get_left_child() == 'left_child'

def test_get_right_child(new_node):
    '''Test get_right_child method of Node class'''
    assert new_node.get_right_child() == 'right_child'

def test_get_parent(new_node):
    '''Test get_parent method of Node Class'''
    assert new_node.get_parent() == 'parent'

def test_set_left_child(new_node):
    '''Test set_left_child method of Node class'''
    new_node.set_left_child('new_left_child')
    assert new_node.get_left_child() == 'new_left_child'

def test_set_right_child(new_node):
    '''Test set_right_child method of Node class'''
    new_node.set_right_child('new_right_child')
    assert new_node.get_right_child() == 'new_right_child'

def test_set_parent(new_node):
    '''Test set_parent_method of Node class'''
    new_node.set_parent('new_left_child')
    assert new_node.get_parent() == 'new_left_child'

def test_has_children(new_node, no_children_node):
    '''Test has_children method of Node class, for both fixture cases'''
    assert new_node.has_left_child() == True
    assert new_node.has_right_child() == True
    assert new_node.has_parent() == True

    assert no_children_node.has_left_child() == False
    assert no_children_node.has_right_child() == False
    assert no_children_node.has_parent() == False
