
class Node:
    '''Object containing tree nodes and data access methods'''
    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.balance_factor = 0

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

    def get_balance_factor(self):
        return self.balance_factor

    

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
                self._update_balance_factor(current_node.get_left_child())
        elif key > current_node.key:
            # Traverse right branches checking that key is greater than current_node
            if current_node.has_right_child():
                self.__put(key,value, current_node.get_right_child())
            else:
                current_node.set_right_child(Node(key, value, parent=current_node)) 
                self._update_balance_factor(current_node.get_right_child())

    def _update_balance_factor(self, node):
        '''Recursively work from node to root updating balance factor. Base case when
            bf at node is -1>x>1 or 0'''
        if node.get_balance_factor() > 1 or node.get_balance_factor() < -1:
            self.rebalance(node)
            return
        if node.get_parent() != None:
            if node == node.get_parent().get_left_child():
                node.get_parent().balance_factor += 1
            else:
                node.get_parent().balance_factor -= 1

            if node.get_parent().balance_factor != 0:
                self.update_balance_factor(node.parent)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result_node = self._get(key, self.root)
            if result_node:
                return result_node.value
            else:
                return None
        else:
            return None

    def _get(self, key, currrent_node):
        '''Recursively search tree for key and return node if found.'''        
        if currrent_node == None:
            return None
        elif currrent_node.key == key:
            return currrent_node
        elif key < currrent_node.key:
            return self._get(key, currrent_node.get_left_child())
        else:
            return self._get(key, currrent_node.get_right_child())

    def __getitem__(self, key):
        return self.get(key)

    def delete(self, key):
        node_to_remove = self._get(key, self.root)
        if node_to_remove is None:
            raise KeyError('Key not found in tree.')
        else:
            successor = self.find_successor(node_to_remove)
            # Case 1. Node is a leaf or single root
            if successor is None:
                if node_to_remove.has_parent():
                    if node_to_remove == node_to_remove.get_parent().get_left_child():
                        node_to_remove.get_parent().set_left_child(None)
                    else:
                        node_to_remove.get_parent().set_right_child(None)
                else:
                    self.root = None
            
            # Case 2. Node has both children
            elif node_to_remove.has_left_child() and node_to_remove.has_right_child():
                self.splice(successor)
                self.insert_successor(successor, node_to_remove)

            # Case 3. Node has only one child
            else:
                self.splice(node_to_remove)

            self.size -= 1

    def find_successor(self, node):
        '''Finds and returns the appropriate successor node depending
            on the position of the node being deleted''' 
        # Case 1 Node has no children       
        if not node.has_left_child() and not node.has_right_child():         
            return None      

        # Case 2 Node has both children. The successor is the node
        #   with the minimum key value in the right sub-tree
        elif node.has_left_child() and node.has_right_child():
            return self.find_min(node.get_right_child())        

        # Case 3 Node has only one child. The successor is the
        # child of the given node
        else:
            if node.has_left_child():
                return node.get_left_child()
            else:
                return node.get_right_child()

    def find_min(self, node):
        '''Returns the minimum node in a subtree rooted with the 
            instance node'''
        current_node = node
        while current_node.has_left_child():
            current_node = current_node.get_left_child()
            
        return current_node

    def splice(self, node):
        '''Removes all refrences to the successor node and re-directs 
            relatives to the appropriate node'''
        # Case 1. node is a leaf.
        if not node.has_left_child() and not node.has_right_child():
            if node == node.get_parent().get_left_child():
                node.get_parent().set_left_child(None) 
            else:
                node.get_parent().set_right_child(None)

        # Case 2. node has right child. Note: successor node can
        #   never have a left child since the successor node is the min key
        #   value in a sub-tree
        else:
            if node.has_left_child():
                if node == node.get_parent().get_left_child():
                    node.get_parent().set_left_child(node.get_left_child())
                else:
                    node.get_parent().set_right_child(node.get_left_child())
                
                # set right child's parent reference:
                node.get_left_child().set_parent(node.get_parent())

            else:
                if node == node.get_parent().get_left_child():
                    node.get_parent().set_left_child(node.get_right_child()) 
                else:
                    node.get_parent().set_right_child(node.get_right_child())
                
                # set right child's parent reference:
                node.get_right_child().set_parent(node.get_parent())
            
            if node.has_left_child():
                print('here')
                node.get_left_child().set_parent(node.get_parent())
            else:  
                node.get_right_child().set_parent(node.get_parent())
                
    def insert_successor(self, successor_node, deleted_node):
        '''replaces the successor node pointers with those of the deleted node.
            in effect de-refrenceing the deleted node and inserting the successor
            node in its place. This is only used in when the deleted node has
            both children'''
        # Case 2. deleted_node has both children
        # Set parent node references
        successor_node.set_parent(deleted_node.get_parent())
        if deleted_node == deleted_node.get_parent().get_left_child():
            deleted_node.get_parent().set_left_child(successor_node)
        else:
            deleted_node.get_parent().set_right_child(successor_node)
        
        # Set deleted_node's children's parent references to successor_node
        successor_node.set_left_child(deleted_node.get_left_child())
        deleted_node.get_left_child().set_parent(successor_node)

        successor_node.set_right_child(deleted_node.get_right_child())
        deleted_node.get_right_child().set_parent(successor_node)

    def __delitem__(self, key):
        self.delete(key)

    def inorder_traversal(self, node):
        return self.inorder_traversal(node.get_left_child()) + \
                    [{node.key: node.value}] + \
                    self.inorder_traversal(node.get_right_child()) \
                    if node else []

 
        


    
    




def left_rotation(node):
    '''Node rebalancing for right heavy tree'''
    # Step 1. Store new node (node's right child) to a temp variable
    new_root = node.get_right_child()
  
    # Step 2. Set Right child refrences for node. If the new node
    #   has a left child, it becomes the right child of node, else
    #   set node.right_child to None
    if new_root.has_left_child():
        node.set_right_child(new_root.get_left_child())
        new_root.get_left_child().set_parent(node)
    else:
        node.set_right_child(None)

    # Step 3. Set subtree parent
    new_root.set_parent(node.get_parent())
    if node.isroot():
        self.root = new_root
    else:
        if node == node.get_parent().get_left_child():
            parent.set_left_child(new_root)
        else:
            parent.set_right_child(new_root)
    
    # Step 4. Set node as left child to new_root
    node.set_parent(new_root)
    new_root.set_left_child(node)

    # Step 5. Update balance factors
    node.balance_factor = node.balance_factor + 1 - min(new_root.balance_factor, 0)
    new_root.balance_factor = new_root.balance_factor + 1 + max(node.balance_factor, 0)


def right_rotation(node):
    '''Node rebalancing for left heavy tree'''
    # Step 1. Store new node (node's left child) to a temp variable
    new_root = node.get_left_child()
  
    # Step 2. Set left child refrences for node. If the new node
    #   has a right child, it becomes the left child of node, else
    #   set node.left_child to None
    if new_root.has_right_child():
        node.set_left_child(new_root.get_right_child())
        new_root.get_right_child().set_parent(node)
    else:
        node.set_left_child(None)

    # Step 3. Set subtree parent
    new_root.set_parent(node.get_parent())
    if node.isroot():
        self.root = new_root
    else:
        if node == node.get_parent().get_left_child():
            parent.set_left_child(new_root)
        else:
            parent.set_right_child(new_root)
    
    # Step 4. Set node as right child to new_root
    node.set_parent(new_root)
    new_root.set_right_child(node)

    # Step 5. Update balance factors
    node.balance_factor = node.balance_factor + 1 - min(new_root.balance_factor, 0)
    new_root.balance_factor = new_root.balance_factor + 1 + max(node.balance_factor, 0)

def rebalance(self, node):
    if node.get_balance_factor() < 0:
        if node.get_right_child().get_balance_factor() > 0:
            self.right_rotation(node.get_right_child())
            self.left_rotation(node)
        else:
            self.left_rotation(node)
    elif node.get_balance_factor > 0:
        if node.get_left_child().get_balance_factor() < 0:
            self.left_rotation(node.get_left_child())
            self.right_rotation(node)
        else:
            self.right_rotation(node)


