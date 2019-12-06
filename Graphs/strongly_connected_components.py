# Implementation of Strongly Connected Components Algorithm
# This algorithm find the strongly connected components in a graph
# Steps:
# 1) Call DFS for the graph G to compute the finish times for each vertex
# 2) Compute G-Transform
# 3) Call for G-Transform, but in the main loop of DFS explore each vertex in decreasing
#       order of finish time from DFS(G)
# 4) Each Tree in teh forest computed in step 3 is a strongly connected component. Output the
#       vertex in each tree in the forest to identify the component

class DFSResult:
    def __init__(self):
        self.parents = {}
        self.start_time = {}
        self.finish_time = {}
        self.order = []
        self.tree_sets = {}
        self.tree_count = 0
        self.t = 0

def dfs(graph):
    result = DFSResult()
    for node in graph:
        if node not in result.parents:
            dfs_visit(graph, node, result)
    return result


def dfs_visit(graph, node, result, parent=None):
    if parent == None:
        # A node with no parent is the root of a New Tree
        result.tree_count += 1
        result.tree_sets[result.tree_count] = {node}

    result.parents[node] = parent
    result.t += 1
    result.start_time[node] = result.t

    # Explore neighbors
    for n in graph[node]:
        if n not in result.parents:
            dfs_visit(graph, n, result, node)
    
    # Finish node when no more neighbors to explore
    result.t += 1
    result.finish_time[node] = result.t
    result.order.append(node)
    if node not in result.tree_sets[result.tree_count]:
        result.tree_sets[result.tree_count].add(node)

def transform_graph(graph):
    # Set keys with empty neighbor sets in transform
    gt = {n:set() for n in graph.keys()}

    for node in graph:
        for neighbor in graph[node]:
            gt[neighbor].add(node)
    
    return gt

def scc(graph_transform, t_order):
    result = DFSResult()
    while t_order:
        node = t_order.pop()        
        if node not in result.parents:
            tree = [node]
            dfs_visit(graph_transform, node, result)
    
    return result.tree_sets

    



if __name__ == '__main__':
    graph = {
                'A': {'B'}, 'B': {'C', 'D'}, 'C': {'A'}, 'D': {'E'}, 
                'E': {'F'}, 'F': {'D'}, 'G': {'F', 'H'}, 'H': {'I'},
                'I': {'J'}, 'J': {'G', 'K'}, 'K': {}
            }   

    # Test dfs:
    #r = dfs(graph)
    #print(r.order)
    #print(graph)
    #print(transform_graph(graph))
    r_1 = dfs(graph)
    gt = transform_graph(graph)
    r_2 = scc(gt, r_1.order)
    print(r_2)
    