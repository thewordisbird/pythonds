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

@pytest.fixture(scope='function')
def full_bst():
    nodes = [
                (70, 'A'), (31, 'B'), (93, 'C'), (14, 'D'), (73, 'E'), 
                (94, 'F'), (23, 'G'), (71, 'H'), (80, 'I'), (96, 'J'),
                (75, 'K'), (85, 'L'), (95, 'M'), (74, 'N'), (76, 'O'),
                (20, 'P'), (19, 'Q')
            ]
    bst = BST()
    for node in nodes:
        bst.put(node[0], node[1])

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

# --- New delete method tests ---
def test_find_min(full_bst):
    '''Test find_min returns the minimum value in a sub-tree'''
    # GIVE a node
    # WHEN find_min is passed that node
    # THEN it will return the minimum key value in the subtree
    #   rooted at that node.
    node = full_bst._get(70, full_bst.root)
    min = full_bst.find_min(node)
    assert min.key == 14

def test_find_successor_single_item_tree(rooted_bst):
    '''Test find_successor returns None for a root node'''
    # GIVEN a root node
    # WHEN find_successor is passed that node
    # THEN it will return None
    node = rooted_bst.root
    successor = rooted_bst.find_successor(node)
    assert successor is None

def test_find_successor_leaf_node(full_bst):
    '''Test find_successor returns None for a leaf node'''
    # GIVEN a leaf node
    # WHEN find_successor is passed that node
    # THEN it will return None
    node = full_bst._get(19, full_bst.root)
    successor = full_bst.find_successor(node)
    assert successor is None

    node = full_bst._get(74, full_bst.root)
    successor = full_bst.find_successor(node)
    assert successor is None

    node = full_bst._get(95, full_bst.root)
    successor = full_bst.find_successor(node)
    assert successor is None

def test_find_successor_node_with_both_children(full_bst):
    '''Test find_successor returns minimum key value in the right
        tree when passed a node with both children'''
    # GIVEN a node with both children
    # WHEN find_successor is passed that node
    # THEN it will return the minimum value node of the right sub-tree
    node = full_bst._get(93, full_bst.root)
    successor = full_bst.find_successor(node)
    assert successor.key == 94

    node = full_bst._get(73, full_bst.root)
    successor = full_bst.find_successor(node)
    assert successor.key == 74

    node = full_bst._get(75, full_bst.root)
    successor = full_bst.find_successor(node)
    assert successor.key == 76

def test_find_successor_node_with_only_one_child(full_bst):
    '''Test find_successor returns its child when passed a
        node with only one child'''
    # GIVEN a node with only one child
    # WHEN find_successor is passed that node
    # THEN it will return its child node
    node = full_bst._get(14, full_bst.root)
    successor = full_bst.find_successor(node)
    assert successor.key == 23

    node = full_bst._get(31, full_bst.root)
    successor = full_bst.find_successor(node)
    assert successor.key == 14

    node = full_bst._get(94, full_bst.root)
    successor = full_bst.find_successor(node)
    assert successor.key == 96

def test_splice_leaf(full_bst):
    '''Test splice removes references to successor
        that is a leaf node'''
    # GIVEN a node that is a leaf
    # WHEN the node is spliced from the tree
    # THEN its parent's respective child refrence is
    #   set to None
    node = full_bst._get(76, full_bst.root)
    full_bst.splice(node)
    assert node.get_parent().get_right_child() == None

    node = full_bst._get(74, full_bst.root)
    full_bst.splice(node)
    assert node.get_parent().get_left_child() == None

def test_splice_with_right_child(full_bst):
    '''Test splice removes references to successor
        from parent and right child and connects the two nodes'''
    # GIVEN a successor node that has a right child
    # WHEN the node is splice from the tree
    # THEN its parents respective child will refrence the
    #   successor_node's right child and the right child will
    #   reference the parent
    successor_node = full_bst._get(14, full_bst.root)
    successor_parent_node = successor_node.get_parent()
    successor_child_node = successor_node.get_right_child()
    full_bst.splice(successor_node)
    assert successor_parent_node.get_left_child() == successor_child_node
    assert successor_child_node.get_parent() == successor_parent_node

    successor_node = full_bst._get(94, full_bst.root)
    successor_parent_node = successor_node.get_parent()
    successor_child_node = successor_node.get_right_child()
    full_bst.splice(successor_node)
    assert successor_parent_node.get_right_child() == successor_child_node
    assert successor_child_node.get_parent() == successor_parent_node

def test_splice_with_left_child(full_bst):
    '''Test splice removes references to successor
        from parent and left child and connects the two nodes'''
    # GIVEN a successor node that has a left child
    # WHEN the node is splice from the tree
    # THEN its parents respective child will refrence the
    #   successor_node's left child and the left child will
    #   reference the parent
    successor_node = full_bst._get(96, full_bst.root)
    successor_parent_node = successor_node.get_parent()
    successor_child_node = successor_node.get_left_child()
    full_bst.splice(successor_node)
    assert successor_parent_node.get_right_child() == successor_child_node
    assert successor_child_node.get_parent() == successor_parent_node

    node = full_bst._get(20, full_bst.root)
    print(node.key)
    node_parent = node.get_parent()
    node_child = node.get_left_child()
    print(node, node_parent, node_child)
    full_bst.splice(node)
    assert node_parent.get_left_child() == node_child
    assert node_child.get_parent() == node_parent

# def test_insert_successor_single_root(rooted_bst):
#     '''Test insert_successor passed a None value and a root
#         node with no children'''
#     # GIVEN a bst with only a root node
#     # WHEN insert_successor is called with a None value
#     #   given as the successor_node
#     # THEN the bst root attribute will be set to None
#     rooted_bst.insert_successor(None, rooted_bst.root)
#     assert rooted_bst.root == None

# def test_insert_successor_leaf_node(full_bst):
#     '''Test insert_successor passed a None value and a leaf
#         node'''
#     # GIVEN a deleted_node that is a leaf node
#     # WHEN insert_successor is called with a successor_node
#     #  of value None
#     # THEN the leaf node's parent's respective child node
#     #   will be set to None
#     deleted_node = full_bst._get(74, full_bst.root)
#     deleted_node_parent = deleted_node.get_parent()
#     full_bst.insert_successor(None, deleted_node)
#     assert deleted_node_parent.get_left_child() == None

#     deleted_node = full_bst._get(76, full_bst.root)
#     deleted_node_parent = deleted_node.get_parent()
#     full_bst.insert_successor(None, deleted_node)
#     assert deleted_node_parent.get_right_child() == None

def test_insert_successor_both_children(full_bst):
    '''Test insert_successor passed a valid successor and
        a deleted_node with both children'''
    # GIVEN a deleted node that has both children
    # WHEN insert_successor is called with a valid Non-None
    #   successor_node
    # THEN the successor node will be inserted in the place of
    #   the deleted_node

    # Test for deleted node that is a left child
    deleted_node = full_bst._get(73, full_bst.root)
    successor_node = full_bst.find_successor(deleted_node)
    full_bst.splice(successor_node)
    
    deleted_node_parent = deleted_node.get_parent()
    deleted_node_left_child = deleted_node.get_left_child()
    deleted_node_right_child = deleted_node.get_right_child()
    
    full_bst.insert_successor(successor_node, deleted_node)
    assert deleted_node_parent.get_left_child() == full_bst._get(74, full_bst.root)

    # Test for deleted node that is a right child
    deleted_node = full_bst._get(93, full_bst.root)
    successor_node = full_bst.find_successor(deleted_node)
    full_bst.splice(successor_node)
    
    deleted_node_parent = deleted_node.get_parent()
    deleted_node_left_child = deleted_node.get_left_child()
    deleted_node_right_child = deleted_node.get_right_child()
    
    full_bst.insert_successor(successor_node, deleted_node)
    assert deleted_node_parent.get_right_child() == full_bst._get(94, full_bst.root)

def test_delete_key_not_found(full_bst):
    '''Test delete method of BST class for a key not found'''
    # GIVEN a bst 
    # WHEN delete is passed a key that is not in the tree
    # THEN a KeyError will be raised
    with pytest.raises(KeyError):
        full_bst.delete(100)

def test_delete_single_root(rooted_bst):
    '''Test delete method of BST class for a BST with only
        a root node that has no children'''
    # GIVEN a bst with only one item at the root
    # WHEN the delete method is called passing in the root key
    # THEN the root will be set to None and the size will be set to 0
    rooted_bst.delete(35)
    assert rooted_bst.root == None
    assert rooted_bst.size == 0

def test_delete_leaf(full_bst):
    '''Test delete method of BST class when removing a leaf node'''
    # GIVEN a bst 
    # WHEN the delete method is called passing in a valid leaf node
    # THEN the leafs parent's respective child will be set to None and
    #   the size of the bst will decrease by 1
    
    print(full_bst.root.key)
    leaf_node = full_bst._get(19, full_bst.root)
    leaf_node_parent = leaf_node.get_parent()
    full_bst.delete(leaf_node)
    assert leaf_node_parent.get_left_child() == None
    assert full_bst.size == bst_size - 1












#def test_bst_delitem(rooted_bst):
#    del rooted_bst[35]
#    assert rooted_bst.root == None




    

