# Prim's Spanning Tree Algorithm
# Find the Minimum Spanning Tree in a graph. This is a tree with a subset of edges in the graph
#   that hit all vertices and have the minimum total weight.

# This is a greedy algorithm. A queue will be maintained to continually evaluate the node with
#   The lowest weight at each iteration

# Steps:
# 1) Create a Min Heap of size V where V is the number of vertices in the given graph. 
#       Every node of min heap contains vertex number and key value of the vertex.
# 2) Initialize Min Heap with first vertex as root (the key value assigned to first vertex is 0). 
#       The key value assigned to all other vertices is INF (infinite).
# 3) While Min Heap is not empty, do following
#   a) Extract the min value node from Min Heap. Let the extracted vertex be u.
#   b) For every adjacent vertex v of u, check if v is in Min Heap (not yet included in MST). 
#       If v is in Min Heap and its key value is more than weight of u-v, then update the key value of v as weight of u-v.

from collection import defaultdict
import sys

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
        return self.get_left_child_index() < self.size

    def has_right_child(self, index):
        return self.get_right_child_index() < self.size

    def get_parent(self, index):
        return (index - 1) // 2

    def has_parent(self, index):
        return index != 0

    def get_smallest_child_index(self, index):
        if self.has_right_child(index) and \ 
            self.get_right_child(index).value < self.get_left_child(index).value
            return self.get_right_child_index(index)
        return self.get_left_child_index(index)

    def build_heap(self, graph):
        # Add all nodes to the priority queue with a path distance
        # set to infinity. 
        for node in graph:
            node = HeapNode(node, flaot('inf'))
            self.heap_list.append(node)
            self.node_map[node.key] = self.size
            self.size += 1

    def swap(self, node_a, node_b):
        self.heap_list[node_a], self.heap_list[node_b] = self.heap_list[node_b], self.heap_list[node_a]

    def heapify_down(self, index=0):
        while self.has_left_child(index):
            smallest_child_index = self.get_smallest_child_index(index)
            if self.heap_list[index].value > self.heap_list[smallest_child_index].value:
                self.swap(index, smallest_child_index)
                index = smallest_child_index
            else:
                break

    def heapify_up(self, index=None):
        if index == None:
            index = len(self.heap_list) - 1

        while self.has_parent(index) and self.get_parent(index).value > self.heap_list[index].value:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def extract_min(self):
        if len(self.heap_list) > 1:      
            root = self.heap_list[0]
            self.node_map[root.key] = None
            
            tail = self.heap_list.pop()
            self.heap_list[0] = tail
            
            self.node_map[tail.key] = 0
            self.heapify_down()
        else:
            item = self.heap_list.pop()
        return item

    def decrease_key(self, key, value):
        index = self.node_map[key]
        self.heap_list[index].value = value
        self.heapify_up(index)
    
def prim(graph, start):
    pq = MinHeap()
    pq.build_heap(graph)
    pq.decrease_key(start, 0)
    parent = {}
