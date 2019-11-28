# Adjaceny List implementation fot the representation of a sparsely connected graph.

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


        

    