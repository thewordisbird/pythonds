import pytest
from bst import BST, Node

# Run the below command to see the coverage missing report
# pytest --cov-report term-missing --cov=bst

# ------FIXTURES------
@pytest.fixture(scope='function')
def empty_bst():
    '''Fixture for an empty bst'''
    return BST()

@pytest.fixture(scope='function')
def rooted_bst():
    '''Fixture for bst with only root node'''
    bst = BST()
    bst.put(35, 'Justin')
    return bst

@pytest.fixture(scope='function')
def non_empty_bst():
    '''Fixture for non-empty bst. Does not use proper insert methods to avoid any errors'''
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

# ------TESTS------
def test_BST_construct(empty_bst):
    '''Test bst construction'''
    assert empty_bst.root == None
    assert empty_bst.size == 0

@pytest.mark.put_tests
def test_bst_put_root_node(empty_bst):
    '''Test adding a root node to and empty bst using 
        the put method of the BST class'''
    # GIVEN a bst with no root node
    # WHEN a new node is added to the bst using the put method
    # THEN the root, key, value and size attributes will be set
    #   for the bst instance.
    assert empty_bst.root == None
    empty_bst.put(32, 'Lindsay')
    assert empty_bst.root != None
    assert empty_bst.root.key == 32
    assert empty_bst.root.value == 'Lindsay'
    assert empty_bst.size == 1

@pytest.mark.put_tests
def test_bst_put_smaller_than_root(rooted_bst):
    '''Test adding a node smaller than the root to a bst with
        only a root node using the put method of the BST class'''
    # GIVEN a bst with only a root node
    # WHEN a new node with a key less than the root key is added
    # THEN the root node should be updated with a left_child
    #   pointer to the new_node and the new_node should be
    #   given a parent pointer to the root node
    rooted_bst.put(32, 'Lindsay')
    assert rooted_bst.root.key == 35
    assert rooted_bst.root.get_left_child().key == 32
    assert rooted_bst.root.get_left_child().value == 'Lindsay'
    assert rooted_bst.root.has_right_child() == False
    assert rooted_bst.root == rooted_bst.root.get_left_child().get_parent()

@pytest.mark.put_tests
def test_bst_put_larger_than_root(rooted_bst):
    '''Test adding a node larger than the root to a bst with
        only a root node using the put method of the BST class'''
    # GIVEN a bst with only a root node
    # WHEN a new node with a key greater than the root key is added
    # THEN the root node should be updated with a right_child
    #   pointer to the new_node and the new_node should be
    #   given a parent pointer to the root node
    rooted_bst.put(69, 'Steve')
    assert rooted_bst.root.key == 35
    assert rooted_bst.root.get_right_child().key == 69
    assert rooted_bst.root.get_right_child().value == 'Steve'
    assert rooted_bst.root.has_left_child() == False
    assert rooted_bst.root == rooted_bst.root.get_right_child().get_parent()

@pytest.mark.put_tests
def test_bst_put_min_leaf_non_empty(non_empty_bst):
    '''Test adding a node smaller than any current value in a
        non-empty bst using the put method of the BST class'''
    # GIVEN a non empty bst with size greater than 1
    # WHEN a node with a smaller value than any other nodes is added
    # THEN the new node should be at left most leaf
    non_empty_bst.put(3, 'new_node')
    assert non_empty_bst.root.key == 70
    assert non_empty_bst.root.get_left_child().get_left_child().get_left_child().key == 3
    assert non_empty_bst.root.get_left_child().get_left_child().get_left_child().value == 'new_node'
    assert non_empty_bst.root.get_left_child().get_left_child().get_left_child().has_left_child() == False
    assert non_empty_bst.root.get_left_child().get_left_child().get_left_child().has_right_child() == False

@pytest.mark.put_tests
def test_bst_put_max_leaf_non_empty(non_empty_bst):
    '''Test adding a node larger than any current value in a
        non-empty bst using the put method of the BST class'''
    # GIVEN a non empty bst with size greater than 1
    # WHEN a node with a greater value than any other nodes is added
    # THEN the new node should be at right most leaf
    non_empty_bst.put(100, 'new_node')
    assert non_empty_bst.root.key == 70
    assert non_empty_bst.root.get_right_child().get_right_child().get_right_child().key == 100
    assert non_empty_bst.root.get_right_child().get_right_child().get_right_child().value == 'new_node'
    assert non_empty_bst.root.get_right_child().get_right_child().get_right_child().has_left_child() == False
    assert non_empty_bst.root.get_right_child().get_right_child().get_right_child().has_right_child() == False

@pytest.mark.put_tests
def test_bst_put_mid_leaf_non_empty(non_empty_bst):
    '''Test adding a node between the largest and smallest current 
        value that will still end up a leaf in a non-empty bst 
        using the put method of the BST class'''
    # GIVEN a non empty bst with size greater than 1
    # WHEN a node with a value between the largest and smalled
    #   but still resulting in a leaf node is added
    # THEN the new node should not be the furthest left or right leaf
    non_empty_bst.put(74, 'new_node')
    assert non_empty_bst.root.key == 70
    assert non_empty_bst.root.get_right_child().get_left_child().get_right_child().key == 74
    assert non_empty_bst.root.get_right_child().get_left_child().get_right_child().value == 'new_node'
    assert non_empty_bst.root.get_right_child().get_left_child().get_right_child().has_left_child() == False
    assert non_empty_bst.root.get_right_child().get_left_child().get_right_child().has_right_child() == False

@pytest.mark.put_tests
def test_bst_setitem(empty_bst):
    '''Test __setitem__ overwrite functions correctly'''
    empty_bst[3] = 'setitem'
    assert empty_bst.root.key == 3
    assert empty_bst.root.value == 'setitem'

def test_bst_length(non_empty_bst):
    '''Test the lenght method of the BST class'''
    assert non_empty_bst.length() == 7
    assert len(non_empty_bst) == 7

@pytest.mark.get_tests
def test_bst_get_empty(empty_bst):
    '''Test get method of the BST class for an
        empty bst instance'''
    # GIVEN an empty bst
    # WHEN a key is serached for using the get method
    # THEN the method should return None
    assert empty_bst[3] == None

@pytest.mark.get_tests
def test_bst_get(non_empty_bst):
    '''Test get method of the BST class for a
        non-empty bst'''
    # GIVEN a non-empty bst
    # WHEN the get method is called given a 
    #   node key
    # THEN if the key is NOT found the function
    #   will return None. Otherwise it will return
    #   the value of the node.
    assert non_empty_bst.get(3) == None
    assert non_empty_bst.get(73) == 'F'
    assert non_empty_bst.get(14) == 'C'

@pytest.mark.get_tests
def test_bst_getitem(non_empty_bst):
    '''Test __getitem__ overwrite functions correctly'''
    assert non_empty_bst[3] == None
    assert non_empty_bst[73] == 'F'
    assert non_empty_bst[14] == 'C'

def test_inorder_traversal(non_empty_bst):
    '''Test inorder traversal method of BST class'''
    # GIVEN a bst
    # WHEN the inorder_traversal method is called
    # THEN a list with the items in ascending order by key will
    #   be returned
    assert non_empty_bst.inorder_traversal(non_empty_bst.root) == [{14: 'C'}, {23: 'D'}, {31: 'B'}, {70: 'A'}, {73: 'F'}, {93: 'E'}, {94: 'G'}]

@pytest.mark.delete_method_tests
def test_delete_root_sigle_node_tree(rooted_bst):
    '''Test deleting the root node in a bst with only a root node'''
    # GIVEN a bst with only a root node
    # WHEN using the delete method passed a key to the node
    # THEN the node is removed from the bst and the bst atributes are
    #   reset to the values for an empty bst
    rooted_bst.delete(35)
    assert rooted_bst.root == None
    assert rooted_bst.size == 0

@pytest.mark.delete_method_tests
def test_delete_root_node(non_empty_bst):
    '''Test deleting the root node of a non-empty bst
        using the delete method of the bst class'''
    # GIVEN a non-empty bst
    # WHEN using the delete method passed a key to a node
    # THEN the node is deleted, and replaced with the minimum keyed
    #   node in the right sub-tree
    non_empty_bst.delete(70)
    assert non_empty_bst.root.key == 73
    assert non_empty_bst.inorder_traversal(non_empty_bst.root) == [{14: 'C'}, {23: 'D'}, {31: 'B'}, {73: 'F'}, {93: 'E'}, {94: 'G'}]

def test_delete_root_node_only_one_child(rooted_bst):
    pass


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

def test_delete_full_parent_node(non_empty_bst):
    print(non_empty_bst.inorder_traversal(non_empty_bst.root))
    non_empty_bst.delete(93)
    print(non_empty_bst.inorder_traversal(non_empty_bst.root))
    assert non_empty_bst.inorder_traversal(non_empty_bst.root) == [{14: 'C'}, {23: 'D'}, {31: 'B'}, {70: 'A'}, {73: 'F'}, {94: 'G'}]

def test_delete_successor_with_right_child(non_empty_bst):
    non_empty_bst[96] = 'New Node'
    print(f'Items: {non_empty_bst.inorder_traversal(non_empty_bst.root)}')
    non_empty_bst.delete(93)
    print(f'Items after delete: {non_empty_bst.inorder_traversal(non_empty_bst.root)}')
    assert non_empty_bst.inorder_traversal(non_empty_bst.root) == [{14: 'C'}, {23: 'D'}, {31: 'B'}, {70: 'A'}, {73: 'F'}, {94: 'G'}, {96: 'New Node'}]

def test_delete_successor_with_left_child(non_empty_bst):
    non_empty_bst[80] = 'New Node 1'
    non_empty_bst[75] = 'New Node 1'
    print(f'Items: {non_empty_bst.inorder_traversal(non_empty_bst.root)}')
    non_empty_bst.delete(73)
    print(f'Items after delete: {non_empty_bst.inorder_traversal(non_empty_bst.root)}')
    assert non_empty_bst.inorder_traversal(non_empty_bst.root) == [{14: 'C'}, {23: 'D'}, {31: 'B'}, {70: 'A'}, {75: 'New Node 1'}, {80: 'New Node 1'}, {93: 'E'}, {94: 'G'}]

def test_delete_successor_with_right_child_b(non_empty_bst):
    non_empty_bst[80] = 'New Node 1'
    non_empty_bst[75] = 'New Node 2'
    non_empty_bst[76] = 'New Node 3'
    non_empty_bst[71] = 'New Node 4'
    print(f'Items: {non_empty_bst.inorder_traversal(non_empty_bst.root)}')    
    non_empty_bst.delete(73)    
    print(f'Items after delete: {non_empty_bst.inorder_traversal(non_empty_bst.root)}')
    assert non_empty_bst.inorder_traversal(non_empty_bst.root) == [{14: 'C'}, {23: 'D'}, {31: 'B'}, {70: 'A'}, {71: 'New Node 4'}, {75: 'New Node 2'}, {80: 'New Node 1'}, {93: 'E'}, {94: 'G'}]


def test_bst_delitem(rooted_bst):
    del rooted_bst[35]
    assert rooted_bst.root == None




    

