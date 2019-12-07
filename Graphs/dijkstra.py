# Implementation of Dijkstra's Algorithm to find shortest path in graph

class PriorityQueueMap(self):
    def __init__(self):
        self.heap_list = []
        self.node_map ={}

    def is_empty(self):
        return len(self.heap_list) == 0

    def has_parent(self, index):
        return index != 0

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_parent(self,index):
        return self.heap_list[self.get_parent_index(index)][1]

    def has_left_child(self, index):
        return get_left_child_index(index) < len(self.heap_list)

    def get_left_child_index(self, index):
        return (index * 2) + 1

    def get_left_child(self, index):
        return self.heap_list[self.get_left_child_index(index)][1]

    def has_right_child(self, index):
        return get_right_child_index < len(self.heap_list)

    def get_right_child_index(self, index):
        return (index * 2) + 2

    def get_right_child(self, index):
        return self.heap_list[self.get_right_child_index(index)][1]

    def get_smallest_child(self, index):
        if has_right_child(index) and get_right_child(index) < get_left_child(index):
            return get_right_child(index)
        return get_left_child(index)

    def swap(self, index_a, index_b):
        a = self.heap_list[index_a]
        b = self.heap_list[index_b]
        self.heap_list[index_a], self.heap_list[index_b] = self.heap_list[index_b], self.heap_list[index_a]
        self.node_map[a] = index_b
        self.node_map[b] = index_a

    def add(self, item):
        '''Insert item into binary heap and set location in node map'''
        # Items are appended to the heap_list and heapifyied up to their
        # proper location
        self.heap_list.append(item)
        self.node_map[item] = len(self.heap_list) - 1
        self.heapify_up

    def poll(self):
        try:
            item = self.heap_list[0]
            self.heap_list[0] = self.heap_list.pop()
            self.heapify_down
        except:
            raise IndexError

    def heapify_up(self, item):
        index = len(self.heap_list) - 1
        while self.has_parent(index) and self.get_parent(index) > self.heap_list[index]:
            self.swap(get_parent_index(index), index)
            index = self.get_parent_index(index)


    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smallest_child_index = get_smallest_child(index)
            if self.heap_list[index] > self.heap_list[smallest_child_index]:
                self.swap(index, get_smallest_child_index(index) )
            else:
                break

    def build(self, items):
        for item in items:
            self.add(item)



def dijkstra(graph, start):
    pq = PriorityQueueMap()
    pq.build(graph)
    visited = {}
    while not pq.is_empty():
        current_node = pq.poll()
        for neighbor in graph[current_node]:
            


    





if __name__ == '__main__':
    graph = {
                'A': {'B'}, 'B': {'C', 'D'}, 'C': {'A'}, 'D': {'E'}, 
                'E': {'F'}, 'F': {'D'}, 'G': {'F', 'H'}, 'H': {'I'},
                'I': {'J'}, 'J': {'G', 'K'}, 'K': {}
            }   