from graph import Graph

# Setup graph and process to find a sequence of moves that allows the night to hit every
# square on a given chess board from a arbitrary starting point

# Function to load chess board into graph
def board_to_knight_graph(board_size):
    knight_graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = get_node_position(row, col, board_size)
            # Find legal positions from the node_id
            node_neighbors = get_legal_moves(row, col, board_size)
            for neighbor in node_neighbors:
                neighbor_node_id = get_node_position(neighbor[0], neighbor[1], board_size)
                knight_graph.add_edge_undirected(node_id, neighbor_node_id)
    return knight_graph


def get_node_position(row, col, board_size):
    return (row * board_size) + col

def get_legal_moves(row, col, board_size):
    new_moves = []
    move_offsets = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

    for offset in move_offsets:
        new_x = row + offset[0]
        new_y = col + offset[1]
        if legal_coord(new_x, board_size) and legal_coord(new_y, board_size):
            new_moves.append((new_x, new_y))
    return new_moves
    
def legal_coord(component, board_size):
    if component >= 0 and component < board_size:
        return True
    return False

# def knights_tour(graph, depth=0, visited=[], node, limit):
#     visted.append(node)
#     if depth < limit:
#         neighbors = graph.adj_list[node]
#         for neighbor in neighbors:
#             if neighbors not in visited:
#                 return knights_tour(graph, depth + 1, visited, neighbor, limit)
     
# def knights_tour(graph, start_node):
#     print(start_node)
#     visited = []
#     return _knights_tour(graph, start_node, visited)

def knights_tour(graph, node, visited=[]):
    
    visited.append(node)
    if len(visited) == graph.get_size() :
        finished = True
        return finished
    if len(visited) < graph.get_size():
        finished = False
        for neighbor in graph.adj_list[node]:
            if neighbor not in visited:
                finished = knights_tour(graph, neighbor, visited)
        if not finished:
            visited.pop()
    return finished

def kt(grap, node, visited=[]):
    # Record source node as visited
    visited.append(node)
  
    if len(visited) < grap.get_size():
        # Set finished trigger to False, since the puzzel is only finished once all nodes
        # have been visted
        finished = False
        # Try moving to all neighbors
        for neighbor in grap.adj_list[node]:
            # Check if neighbor node has been visted
            if neighbor not in visited:
                finished = kt(grap, neighbor, visited)
        if not finished:
            visited.pop()
    
    else:
        return True
    
    if finished == True:
        return visited
    else:
        return finished





if __name__ == "__main__":
    # build knight graph
    kg = board_to_knight_graph(6)

    k = kt(kg, 23)
    print(k)
   