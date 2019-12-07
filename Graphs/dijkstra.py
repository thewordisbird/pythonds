# Implementation of Dijkstra's Algorithm to find shortest path in graph

class PriorityQueueMap:
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

    def build_from_graph(self, graph):
        # Add all nodes to the priority queue with a path distance
        # set to infinity. 
        for node in graph:
            self.heap_list.append((node, float('inf')))
            self.node_map[node] = len(self.heap_list) - 1

    def set_distance(self, key, value):
        # Modify the distance value in the min-heap. 
        # After modification, rebalance the heap
        self.heap_list[self.node_map[key]][1] = value
        # Check if value is larger than parent and heapify accordingly
        if self.has_parent(self.node_map[key]) and self.get_parent(self.node_map[key]) > value:
            self.heapify_up(self.node_map[key])
        else:
            heapify_down(self.node_map[key])

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

    def poll(self):
        try:
            item = self.heap_list[0]
            self.heap_list[0] = self.heap_list.pop()
            self.heapify_down
        except:
            raise IndexError

    def heapify_up(self, index=None):
        if index == None:
            index = len(self.heap_list) - 1

        while self.has_parent(index) and self.get_parent(index) > self.heap_list[index][1]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)


    def heapify_down(self, index=0):
        while self.has_left_child(index):
            smallest_child_index = get_smallest_child(index)
            if self.heap_list[index] > self.heap_list[smallest_child_index]:
                self.swap(index, get_smallest_child_index(index) )
            else:
                break

    


    


def dijkstra(graph, start):
    pq = PriorityQueueMap()
    pq.build_from_graph(graph)
    parent = {}
    distance = {}
    # Set the path distance to the starting node to 0
    pq.set_distance(start, 0)
    parent[start] = None
    while not pq.is_empty():
        # take the node with the minimum path distance from the priority queue
        current_node = pq.poll()
        distance[current_node[0]] = current_node[1]
        # Explore the current nodes neighbors and compare the path distances from the
        # start node. Update if neccessary
        for neighbor in graph[current_node]:
            if neighbor not in distance:
                # Calculate the new path distance from the starting node
                # Through the current node to its neighbor
                path_dist = distance[current_node[0]] + graph[current_node][neighbor]
                if path_dist < pq.get_path_dist[neighbor]:
                    pq.set_distance(neighbor, path_dist)
                    parent[neighbor] = current_node

  
if __name__ == '__main__':
    graph = {
                'u': {'v': 2, 'x': 1, 'w': 5}, 'v': {'u': 2, 'x': 2, 'w': 3},
                'x': {'u': 1, 'v': 2, 'w': 3, 'y': 1}, 'w': {'v': 3, 'u': 5, 'x': 3, 'y': 1, 'z': 5},
                'y': {'x': 1, 'w': 1, 'z': 1}, 'z': {'w': 5, 'y': 1}
            }   