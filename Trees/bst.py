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

    def find_succesor(self):        
        if not self.has_left_child() and self.has_right_child():
            # Case 1 Node has no children
            successor_node = None          
        elif self.has_left_child() and self.has_right_child():
            # Case 2 Node has both children
            # Find the minimum node in the right tree
            successor_node = self.get_right_child().find_min()        
        else:
            # Case 3 Node has one Child 
            if self.has_left_child():
                # Case 3.1 Node has only left child
                successor_node = self.get_left_child()
            else:
                # Case 3.2 Node has only right child
                successor_node = self.get_right_child

        return successor_node

    def find_min(self):
        '''Returns the minimum node in a subtree rooted with the 
            instance node'''
        current_node = self
        while current_node.has_left_child():
            current_node = current_node.get_left_child()
            
        return current_node

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
            result_node = self.__get(key, self.root)
            if result_node:
                return result_node.value
            else:
                return None
        else:
            return None

    def __get(self, key, currrent_node):
        '''Recursively search tree for key and return node if found.'''
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

    # Needs testing
    def delete(self, key):
        if self.size > 1:
            node_to_remove = self.__get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not found in tree.')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not found in tree.')
    
    # Needs testing
    def __delitem__(self, key):
        self.delete(key)
    
    # Needs testing
    def remove(self, node):
        #print(f'Node to remove: {node.key}')
        if not node.has_left_child() and not node.has_right_child():
            # Node is a leaf node
            if node == node.get_parent().get_left_child():
                node.get_parent().set_left_child(None)
            else:
                node.get_parent().set_right_child(None)
        
        elif node.has_left_child() and node.has_right_child():
            # Node has both children
            successor = node.find_succesor()
            print(successor.get_right_child().key)
            #print(f'successor key: {successor.key}')
            # Note: the successor will be the minimum node in the right sub tree. 
            # Because it's the minimum it will have no left branches
            # so we need to check to see if the successor is a leaf or not, modify the
            # child pointers if so, and replace the node to be deleted with the successor

            # The below two if statements will remove all references to the successor in the tree
            if not successor.has_left_child() and not successor.has_right_child():
                if successor == successor.get_parent().get_left_child():
                    successor.get_parent().set_left_child(None)
                else:
                    successor.get_parent().set_right_child(None)

            #NEEDS TESTING. SOMETHING ABOUT CHILD POINTER TRANSFER. IT WAS SET TO NONE
            if successor.has_right_child():
                if successor == successor.get_parent().get_left_child():
                    successor.get_parent().set_left_child(successor.get_left_child())
                else:
                    successor.get_parent().set_right_child(successor.get_right_child())
            
            # Once the successor has been splice from its original location, it can
            # replace the node to be deleted. We need to update the node to be deleted's 
            # right and left children to point to the successor as parent and the successor
            # to point to them as children
            
            # Set successor new left child
            
            # The below statements will update the successor with the node's references             
            if node.has_parent():
                successor.set_parent(node.get_parent())
                if node == node.get_parent().get_left_child():
                    node.get_parent().set_left_child(successor)
                else:
                    node.get_parent().set_right_child(successor)
            else:
                successor.set_parent(None)
                self.root = successor

            if node.has_left_child():
                successor.set_left_child(node.get_left_child())
                node.get_left_child().set_parent(successor)
            else:
                successor.set_left_child(None)
            
            if node.has_right_child():
                successor.set_right_child(node.get_right_child())
                node.get_right_child().set_parent(successor)
            else:
                successor.set_right_child(None)

        else:
            # Node has only one child
            if node.has_left_child():
                if node.has_parent():
                    if node == node.get_parent().get_left_child():
                        node.get_left_child().set_parent(node.get_parent())
                        node.get_parent().set_left_child(node.get_left_child())
                    elif node == node.get_parent().get_right_child():
                        node.get_left_child().set_parent(node.get_parent())
                        node.get_parent().set_right_child(node.get_left_child())
                else:
                    node.get_left_child().set_parent(None)
                    self.root = node.get_left_child()
            else:
                if node.has_parent():
                    if node == node.get_parent().get_left_child():
                        node.get_right_child().set_parent(node.get_parent())
                        node.get_parent().set_left_child(node.get_right_child())
                    elif node == node.get_parent().get_right_child():
                        node.get_right_child().set_parent(node.get_parent())
                        node.get_parent().set_right_child(node.get_right_child())
                else:
                    node.get_right_child().set_parent(None)
                    self.root = node.get_right_child()

    def inorder_traversal(self, node):
        return self.inorder_traversal(node.get_left_child()) + \
                    [{node.key: node.value}] + \
                    self.inorder_traversal(node.get_right_child()) \
                    if node else []

        
            

        


    
    


