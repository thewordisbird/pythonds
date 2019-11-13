# Implementation of Binary Search Tree (bst)

# A BST should have the following properties:
#   - Insert: method to insert a key into the BST in the proper place
#   - Find: method to find and return a key in the BST
#   - Remove: method to remove and return a key in the BST
#   - Traversal: methods for inorder, postorder and preorder traversal

class Node:
    '''Object containing tree nodes and data access methods'''
    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_parent(self):
        return self.parent

    def set_left_child(self, left_child_node):
        self.left_child =left_child_node

    def set_right_child(self, right_child_node):
        self.right_child = right_child_node

    def set_parent(self, parent_node):
        self.parent = parent_node

    def has_left_child(self):
        return self.left_child != None

    def has_right_child(self):
        return self.right_child != None
    
    def has_parent(self):
        return self.parent != None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, value):
        if self.root:
            self.__put(key, value, self.root)
        else:
            self.root = Node(key, value)
        self.size += 1

    def __put(self, key, value, current_node):
        '''recursevely search for entry point and insert at correct location.'''       
        if key < current_node.key:
            # Traverse left branches checking that key is less than current_node.key
            if current_node.has_left_child():
                self.__put(key, value, current_node.get_left_child())
            else:
                current_node.set_left_child(Node(key, value, parent=current_node))
        elif key > current_node.key:
            # Traverse right branches checking that key is greater than current_node
            if current_node.has_right_child():
                self.__put(key,value, current_node.get_right_child())
            else:
                current_node.set_right_child(Node(key, value, parent=current_node))
        


    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result_node = self.__get(key, current_node)
            if result_node:
                return result_node.value
            else:
                return None
        else:
            return None

    def __get(self, key, currrent_node):
        '''Recursively search tree for key and return value if found.'''
        if currrent_node == None:
            return None
        elif currrent_node.key == key:
            return currrent_node
        elif key < currrent_node.key:
            return self.__get(key, currrent_node.get_left_child())
        else:
            return self.__get(key, currrent_node.get_right_child())

    def __getitem__(self, key):
        return self.get(key)





    










###
class TreeNode:
    def __init__(self, key, val, left_child=None, right_child=None, parent=None):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.left_child and not self.right_child

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_childern(self):
        return self.left_child and self.right_child

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                self.parent.left_child = self.left_child
            else:
                self.parent.right_child = self.left_child
            self.left_child.parent = self.parent



class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size
    
    def __len__(self):
        return self.size

    def put(self, key, val):
        '''Insert a key, value pair into the bst'''
        # If the tree exists, use the recursive _put method to find where the new item
        # should go in the bst.
        if self.root:
            self._put(key, val, self.root)

        # If the tree is empty add the new item as the bst root.
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def __iter__(self):
        return self.root.__iter__()