import pytest
from bst import BST, Node

# Run the below command to see the coverage missing report
# pytest --cov-report term-missing --cov=bst

@pytest.fixture(scope='function')
def empty_bst():
    return BST()

@pytest.fixture(scope='function')
def rooted_bst():
    bst = BST()
    bst.put(35, 'Justin')
    return bst

@pytest.fixture(scope='function')
def non_empty_bst():
    bst = BST()
    node_a = Node(70, 'A')
    node_b = Node(31, 'B')
    node_c = Node(14, 'C')
    node_d = Node(23, 'D')
    node_e = Node(93, 'E')
    node_f = Node(73, 'F')
    node_g = Node(94, 'G')
    
    node_a.left_child = node_b
    node_b.parent = node_a

    node_b.left_child = node_c
    node_c.parent = node_b

    node_c.right_child = node_d
    node_d.parent = node_c

    node_a.right_child = node_e
    node_e.parent = node_a

    node_e.left_child = node_f
    node_f.parent = node_e

    node_e.right_child = node_g
    node_g.parent = node_e

    bst.root = node_a
    bst.size = 7

    return bst

@pytest.fixture(scope='function')
def new_node():
    return Node(35, 'Justin', 'left_child', 'right_child', 'parent')

@pytest.fixture(scope='function')
def no_children_node():
    return Node(35, 'Justin')

def test_BST_construct(empty_bst):
    bst = empty_bst
    assert bst.root == None
    assert bst.size == 0

def test_Node_construct(new_node):
    node = new_node
    assert node.key == 35
    assert node.value == 'Justin'
    assert node.left_child == 'left_child'
    assert node.right_child == 'right_child'
    assert node.parent == 'parent'

def test_get_left_child(new_node):
    node = new_node
    assert node.get_left_child() == 'left_child'

def test_get_right_child(new_node):
    node = new_node
    assert node.get_right_child() == 'right_child'

def test_get_parent(new_node):
    node = new_node
    assert node.get_parent() == 'parent'

def test_set_left_child(new_node):
    node = new_node
    node.set_left_child('new_left_child')
    assert node.get_left_child() == 'new_left_child'

def test_set_right_child(new_node):
    node = new_node
    node.set_right_child('new_right_child')
    assert node.get_right_child() == 'new_right_child'

def test_set_parent(new_node):
    node = new_node
    node.set_parent('new_left_child')
    assert node.get_parent() == 'new_left_child'


def test_has_children(new_node, no_children_node):
    node_a = new_node
    assert node_a.has_left_child() == True
    assert node_a.has_right_child() == True
    assert node_a.has_parent() == True

    node_b = no_children_node
    assert node_b.has_left_child() == False
    assert node_b.has_right_child() == False
    assert node_b.has_parent() == False

def test_bst_put_root_node(empty_bst):
    bst = empty_bst
    assert bst.root == None
    bst.put(32, 'Lindsay')
    assert bst.root != None
    assert bst.root.key == 32
    assert bst.root.value == 'Lindsay'
    assert bst.size == 1

def test_bst_put_smaller_than_root(rooted_bst):
    '''Test BST.put(key, value) for bst with one item'''
    # GIVEN a bst with only a root node
    # WHEN a new node with a key less than the root key is added
    # THEN the root node should be updated with a left_child
    #   pointer to the new_node and the new_node should be
    #   given a parent pointer to the root node
    bst = rooted_bst
    bst.put(32, 'Lindsay')
    assert bst.root.key == 35
    assert bst.root.get_left_child().key == 32
    assert bst.root.get_left_child().value == 'Lindsay'
    assert bst.root.has_right_child() == False
    assert bst.root == bst.root.get_left_child().get_parent()

def test_bst_put_larger_than_root(rooted_bst):
    '''Test BST.put(key, value) for bst with one item'''
    # GIVEN a bst with only a root node
    # WHEN a new node with a key greater than the root key is added
    # THEN the root node should be updated with a right_child
    #   pointer to the new_node and the new_node should be
    #   given a parent pointer to the root node
    bst = rooted_bst
    bst.put(69, 'Steve')
    assert bst.root.key == 35
    assert bst.root.get_right_child().key == 69
    assert bst.root.get_right_child().value == 'Steve'
    assert bst.root.has_left_child() == False
    assert bst.root == bst.root.get_right_child().get_parent()

def test_bst_put_min_leaf_non_empty(non_empty_bst):
    # GIVEN a non empty bst with size greater than 1
    # WHEN a node with a smaller value than any other nodes is added
    # THEN the new node should be at left most leaf
    bst = non_empty_bst
    bst.put(3, 'new_node')
    assert bst.root.key == 70
    assert bst.root.get_left_child().get_left_child().get_left_child().key == 3
    assert bst.root.get_left_child().get_left_child().get_left_child().value == 'new_node'
    assert bst.root.get_left_child().get_left_child().get_left_child().has_left_child() == False
    assert bst.root.get_left_child().get_left_child().get_left_child().has_right_child() == False

def test_bst_put_max_leaf_non_empty(non_empty_bst):
    # GIVEN a non empty bst with size greater than 1
    # WHEN a node with a greater value than any other nodes is added
    # THEN the new node should be at right most leaf
    bst = non_empty_bst
    bst.put(100, 'new_node')
    assert bst.root.key == 70
    assert bst.root.get_right_child().get_right_child().get_right_child().key == 100
    assert bst.root.get_right_child().get_right_child().get_right_child().value == 'new_node'
    assert bst.root.get_right_child().get_right_child().get_right_child().has_left_child() == False
    assert bst.root.get_right_child().get_right_child().get_right_child().has_right_child() == False

def test_bst_put_mid_leaf_non_empty(non_empty_bst):
    # GIVEN a non empty bst with size greater than 1
    # WHEN a node with a greater value than any other nodes is added
    # THEN the new node should be at right most leaf
    bst = non_empty_bst
    bst.put(74, 'new_node')
    assert bst.root.key == 70
    assert bst.root.get_right_child().get_left_child().get_right_child().key == 74
    assert bst.root.get_right_child().get_left_child().get_right_child().value == 'new_node'
    assert bst.root.get_right_child().get_left_child().get_right_child().has_left_child() == False
    assert bst.root.get_right_child().get_left_child().get_right_child().has_right_child() == False

def test_bst_setitem(empty_bst):
    bst = empty_bst
    bst[3] = 'setitem'
    assert bst.root.key == 3
    assert bst.root.value == 'setitem'

def test_bst_length(non_empty_bst):
    bst = non_empty_bst
    assert bst.length() == 7
    assert len(bst) == 7

def test_bst_get(non_empty_bst):
    bst = non_empty_bst
    assert bst.get(3) == None
    assert bst.get(73) == 'F'
    assert bst.get(14) == 'C'

def test_bst_getitem(non_empty_bst):
    bst = non_empty_bst
    assert bst[3] == None
    assert bst[73] == 'F'
    assert bst[14] == 'C'

def test_bst_get_empty(empty_bst):
    bst = empty_bst
    assert bst[3] == None

def test_inorder_traversal(non_empty_bst):
    bst = non_empty_bst
    result = bst.inorder_traversal(bst.root)
    assert result == [{14: 'C'}, {23: 'D'}, {31: 'B'}, {70: 'A'}, {73: 'F'}, {93: 'E'}, {94: 'G'}]

def test_delete_root_node(non_empty_bst):
    bst = non_empty_bst
    bst.delete(70)
    assert bst.root.key == 73

def test_delete_leaf_node(non_empty_bst):
    bst = non_empty_bst
    bst.delete(23)
    assert bst.size == 6
    assert bst.inorder_traversal(bst.root) == [{14: 'C'},  {31: 'B'}, {70: 'A'}, {73: 'F'}, {93: 'E'}, {94: 'G'}]
    bst.delete(73)
    assert bst.size == 5
    assert bst.inorder_traversal(bst.root) == [{14: 'C'},  {31: 'B'}, {70: 'A'}, {93: 'E'}, {94: 'G'}]
    

def test_delete_node_sigle_left_tree(non_empty_bst):
    bst = non_empty_bst
    bst.delete(31)
    assert bst.size == 6
    assert bst.inorder_traversal(bst.root) == [{14: 'C'}, {23: 'D'}, {70: 'A'}, {73: 'F'}, {93: 'E'}, {94: 'G'}]

def test_delete_key_not_in_tree(non_empty_bst, rooted_bst, empty_bst):
    # Test tree greater than 1   
    with pytest.raises(KeyError): 
        non_empty_bst.delete(69)
    
    with pytest.raises(KeyError): 
        rooted_bst.delete(69)

    with pytest.raises(KeyError): 
        empty_bst.delete(69)

def test_delete_root_sigle_node_tree(rooted_bst):
    rooted_bst.delete(35)
    assert rooted_bst.root == None

def test_delete_full_parent_node(non_empty_bst):
    print(non_empty_bst.inorder_traversal(non_empty_bst.root))
    non_empty_bst.delete(93)
    print(non_empty_bst.inorder_traversal(non_empty_bst.root))
    assert non_empty_bst.inorder_traversal(non_empty_bst.root) == [{14: 'C'}, {23: 'D'}, {31: 'B'}, {70: 'A'}, {73: 'F'}, {94: 'G'}]

def test_delete_full_tree_root(non_empty_bst):
    non_empty_bst.delete(70)
    assert non_empty_bst.inorder_traversal(non_empty_bst.root) == [{14: 'C'}, {23: 'D'}, {31: 'B'}, {73: 'F'}, {93: 'E'}, {94: 'G'}]

# WRITE TEST TO TARGET LINES 175-176
    
def test_bst_delitem(rooted_bst):
    del rooted_bst[35]
    assert rooted_bst.root == None




    

