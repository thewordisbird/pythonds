# Prim's Spanning Tree Algorithm
# Find the Minimum Spanning Tree in a graph. This is a tree with a subset of edges in the graph
#   that hit all vertices and have the minimum total weight.

# This is a greedy algorithm. A queue will be maintained to continually evaluate the node with
#   The lowest weight at each iteration

# Steps:
# 1. Initialization
#   a. Initialize MinHeap and populate with all nodes setting distance to infinity
#   b. Initialize parent dict to maintain map of child to parent. This will be used to create
#       the MST
# 2. decrease_key() for the starting node, setting it's value to 0. This allows it to be the first
#       node extracted once in the while loop
# 3. Enter while loop
#   a. extract_min to get the min distance node
#   b. iterate over neighbors and if they are in the MinHeap, decrease_key if the edge distance is 
#       less than the stored distance in the MinHeap and update parent in the parent dict
# 4. Return the parent set.


class HeapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    
class MinHeap:
    
    def __init__(self):
        self.heap_list = []
        self.size = 0
        self.node_map = {}

    def is_empty(self):
        return len(self.heap_list) == 0

    def get_left_child_index(self, index):
        return (2 * index) + 1

    def get_left_child(self, index):
        return self.heap_list[self.get_left_child_index(index)]

    def get_right_child_index(self, index):
        return (2 * index) + 2 

    def get_right_child(self, index):
        return self.heap_list[self.get_right_child_index(index)]

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size - 1

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size - 1

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_parent(self, index):
        return self.heap_list[self.get_parent_index(index)]

    def has_parent(self, index):
        return index != 0

    def get_smallest_child_index(self, index):
        # Find the smalles child given a node index. This is only called from a method that checks
        # that the node has a left child to maintain validity
        if self.has_right_child(index) and self.get_right_child(index).value < self.get_left_child(index).value:
            return self.get_right_child_index(index)
        return self.get_left_child_index(index)

    def build_heap(self, graph):
        # Add all nodes to the priority queue with a path distance
        # set to infinity. 
        for node in graph:
            node = HeapNode(node, float('inf'))
            self.heap_list.append(node)
            self.node_map[node.key] = self.size
            self.size += 1

    def swap(self, index_a, index_b):
        # Swap nodes and update their location in the node map
        a = self.heap_list[index_a].key
        b = self.heap_list[index_b].key
        self.heap_list[index_a], self.heap_list[index_b] = self.heap_list[index_b], self.heap_list[index_a]
        self.node_map[a] = index_b
        self.node_map[b] = index_a

    def heapify_down(self, index=0):
        # Settle node into position from top dowin in the heap
        while self.has_left_child(index):
            smallest_child_index = self.get_smallest_child_index(index)
            if self.heap_list[index].value > self.heap_list[smallest_child_index].value:
                self.swap(index, smallest_child_index)
                index = smallest_child_index
            else:
                break

    def heapify_up(self, index=None):
        # Settle node into position from bottom up in the heap
        if index == None:
            index = len(self.heap_list) - 1

        while self.has_parent(index) and self.get_parent(index).value > self.heap_list[index].value:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def extract_min(self):
        # Return the minimum valued node in the heap
        if len(self.heap_list) > 1:      
            root = self.heap_list[0]
            del self.node_map[root.key]
            
            tail = self.heap_list.pop()
            self.size -= 1
            self.heap_list[0] = tail
            
            self.node_map[tail.key] = 0
            self.heapify_down()
        else:
            root = self.heap_list.pop()
        return root

    def decrease_key(self, key, value):
        # Update the node distance, value, of a node with key, key in the heap
        index = self.node_map[key]
        self.heap_list[index].value = value
        self.heapify_up(index)

    def get_weight(self, key):
        # Return the value of a node in the heap
        index = self.node_map[key]
        return self.heap_list[index].value
    
def prim(graph, start):
    # Initialization. Create heap instance, add graph to heap set starting node and initialize parent
    # dictionary
    pq = MinHeap()
    pq.build_heap(graph)
    pq.decrease_key(start, 0)
    parent = {}
    parent[start] = None

    # Loop until MinHeap priority queue is empty
    while not pq.is_empty():
        current_node = pq.extract_min()
        print(pq.node_map)
        # Iterate over current node's neighbors and update wieghts in pq for nodes in pq who's 
        # values are less than the stored value
        for neighbor in graph[current_node.key]:
            if neighbor in pq.node_map:
                neighbor_weight = graph[current_node.key][neighbor]
                if neighbor_weight < pq.get_weight(neighbor):
                    pq.decrease_key(neighbor, neighbor_weight)
                    parent[neighbor] = current_node.key

    return parent

if __name__ == '__main__':
    

    graph = {
                'a': {'f': 7, 'h': 15, 'b': 10}, 'b': {'a': 10, 'c': 3, 'd': 8},
                'c': {'b': 3, 'd': 14}, 'd': {'b': 8, 'c': 14, 'e': 6, 'f': 5},
                'e': {'d': 6, 'f': 12}, 'f': {'a': 7, 'd': 5, 'e': 12, 'g': 9},
                'g': {'f': 9}, 'h': {'a': 15}
            }  

    graph = {
                'u': {'v': 2, 'x': 1, 'w': 5}, 'v': {'u': 2, 'x': 2, 'w': 3},
                'x': {'u': 1, 'v': 2, 'w': 3, 'y': 1}, 'w': {'v': 3, 'u': 5, 'x': 3, 'y': 1, 'z': 5},
                'y': {'x': 1, 'w': 1, 'z': 1}, 'z': {'w': 5, 'y': 1}
            }    

    print(prim(graph, 'y'))