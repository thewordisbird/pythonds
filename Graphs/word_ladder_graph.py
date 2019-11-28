from collections import deque
# Solution to word latter problem using an adjacency list graph data structure

# Word Ladder Problem:
# Go from one word to another by only changing one character at a time.

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
    
    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_to[connected_node]


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.vertex_count = 0
    
    def add_vertex(self, key):
        self.vertex_count += 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, vertex_key):
        if vertex_key in self.vertex_list:
            return self.vertex_list[vertex_key]
        else:
            return None

    def __contains__(self, vertex_key):
        return vertex_key in self.vertex_list

    def add_edge(self, from_vertex_key, to_vertex_key, weight=0):
        if from_vertex_key not in self.vertex_list:
            self.add_vertex(from_vertex_key)
        if to_vertex_key not in self.vertex_list:
            self.add_vertex(to_vertex_key)
        self.vertex_list[from_vertex_key].add_neighbor(self.vertex_list[to_vertex_key], weight)

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())

    def bfs_mit(self, start):
        level = {start: 0}
        parent = {start: None}
        i = 1
        frontier = [start]
        while frontier:
            next = []
            for start_node in frontier:
                for vertex in self.vertex_list:
                    if vertex not in level:
                        level[vertex] = i
                        parent[vertex] start_node
                        next.append(vertex)
            frontier = next
            i += 1

    def bfs(self, start, target):
        to_visit = deque()
        to_visit.append(start)
        # visited dict will store the node visited as the key, and it's parent as the value
        visited = {start: None}

        if start == target:
            return visited
        
        while to_visit:
            node = to_visit.popleft()
            for neighbor in self.vertex_list[node]:
                if neighbor not in visited:
                    visited[neighbor] = node
                    to_visit.append(neighbor)



        
        


def build_graph(word_file):
    d = {}
    g = Graph()
    with open(word_file, 'r') as f:
        for line in f:
            word = line[:1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
        
    # Add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word_1 in d[bucket]:
            for word_2 in d[bucket]:
                if word_1 != word_2:
                    g.add_edge(word_1, word_2)
    return g

