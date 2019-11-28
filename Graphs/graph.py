from collections import deque
# Graph Implementations where nodes only store data about themselves and the graph stores the 
# structure. This would allow a node to exist in multiple graphs depending on how data was 
# decided to be linked

class Node:
    def __init__(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def set_key(self, new_key):
        self.key = new_key

class Graph:
    def __init__(self):
        # The adjacency list format is:
        # {
        #   Node_a:{neighbor_1: edge_weight, neighbor_2: edge_weight, ...}, 
        #   Node_b:{neighbor_1: edge_weight, neighbor_2: edge_weight, ...},
        #   Node_c:{neighbor_1: edge_weight, neighbor_2: edge_weight, ...},
        #   ...,
        #   Node_n:{neighbor_1: edge_weight, neighbor_2: edge_weight, ...}
        # }
        self.adj_list = {}
    
    def add_node(self, node_key):
        self.adj_list[node_key] = {}

    def get_node(self, node_key):
        if node_key in self.adj_list:
            return get_node(node_key)
        else:
            return None
    
    def __contains__(self, node_key):
        return node_key in self.adj_list

    def add_edge_undirected(self, from_node_key, to_node_key, weight=0):
        if from_node_key not in self.adj_list:
            self.add_node(from_node_key)
        if to_node_key not in self.adj_list:
            self.add_node(to_node_key)
        self.adj_list[from_node_key][to_node_key] = weight
        self.adj_list[to_node_key][from_node_key] = weight

    def get_nodes(self):
        return self.adj_list.keys()

    def __iter__(self):
        return iter(self.adj_list.keys())

    def bfs(self, start_node_key, target_node_key):
        in_path = {start_node_key: None}
        to_explore = deque()
        to_explore.append(start_node_key)

        if start_node_key == target_node_key:
            return in_path

        while to_explore:
            node = deque.popleft()
            for neighbor in self.adj_list[node]:
                if neighbor not in in_path:
                    in_path[neighbor] = node
                    to_explore.append(neighbor)

    def dfs(self, start_node_key, target_node_key):
        pass


if __name__ == '__main__':
    g = Graph()
    g.add_node('fool')
    g.add_node('foul')
    g.add_edge_undirected('fool', 'foul')
    print(g.adj_list)