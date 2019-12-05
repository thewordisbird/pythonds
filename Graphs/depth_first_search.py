# Depth First Search Implementation For A Graph
# The result of the dfs is an object that holds all the data related to the path of search
# This can be used to determine the following:
#   For Cyclic Graphs:
#       - Define Tree, Forward, Backward and Cross edges
#       - Validate path between two nodes
#   For Directed Acyclic Graphs (D.A.G.'s):
#       - Define Tree, Forward and Cross Edges
#       - Perform Topological Sort


class DFSResult:
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.edges = {}
        self.order = []
        self.t = 0

def dfs(g):
    result = DFSResult()
    for vertex in g.adj_list:
        if vertex not in result.parent:
            dfs_visit(g, vertex, result)
    return result

def dfs_visit(g, v, result, parent=None):
    # Setup for given node:
    result.parent[v] = parent
    result.t += 1
    result.start_time[v] = result.t

    # Classify Edges
    if parent:
        result.edges[(parent, v)] = 'Tree'
    for n in g.adj_list[v]:
        if n not in result.parent:
            dfs_visit(g, n, result, v)
        elif n not in result.finish_time:
            result.edges[(v,n)] = 'Back'
        elif result.start_time[v] < result.start_time[n]:
            result.edges[(v,n)] = 'Forward'
        else:
            result.edges[(v,n)] = 'Cross'

    result.t += 1
    result.finish_time[v] = result.t
    result.order.append(v)

def topological_sort(g):
    dfs_result = DFSResult()
    dfs_result.order.reverse()
    return dfs_result.order