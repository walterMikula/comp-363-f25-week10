def khan(graph: list[list[int]]) -> list[int]:

    """Comprehensive implementation of Kahn's algorithm for topological sorting."""

    # Data integrity check - a bit much but I was having fun with it.
    if (
         graph is None
        or not isinstance(graph, list)
        or len(graph) == 0
        or not all(isinstance(row, list) for row in graph)
        or not all(len(row) == len(graph) for row in graph)
    ):
        raise ValueError("Input must be a non-empty square adjacency matrix.")

    # Ease of reference
    N = len(graph)
    NO_EDGE = graph[0][0]

    # Calculate in-degrees of all vertices.
    in_degrees = [0] * N
    for u in range(N):
        for v in range(N):
            if graph[u][v] != NO_EDGE:
                # In edge u --> v we compute the in-degree of v
                in_degrees[v] += 1

    # Initialize list of source vertices
    sources = []
    for i in range(N):
        if in_degrees[i] == 0:
            sources.append(i)

    # List to store the topological order
    topological_order = []

    # Progressively remove sources and update in-degrees
    while len(sources) > 0:
        # Remove a source vertex
        vertex = sources.pop(0)
        # Add it to the topological order
        topological_order.append(vertex)
        # Decrease in-degrees of its neighbors
        for neighbor in range(N):
            if graph[vertex][neighbor] != NO_EDGE:
                in_degrees[neighbor] -= 1
                # If in-degree becomes zero, add it to sources
                if in_degrees[neighbor] == 0:
                    sources.append(neighbor)

    # Done
    return topological_order

def DFS(G, v, marked):
    # Mark the current vertex as visited
    marked.append(v)
    # Consider all the neighbors of v
    for w in range(len(G)):
        # For any edge v --> w, if w is unmarked,
        # plan to visit it.
        if G[v][w] != G[0][0] and w not in marked:
            # Plan to visit w
            DFS(G, w, marked)
    return marked

def DFS_helper(G, v):
    """Helper method to launch a DFS from vertex v."""
    # Launch DFS from v with empty marked list
    return DFS(G, v, [])

# Show how to obtain the topological sorting of a DAG 
#using recursive DFS by timing how long each vertex "stays" in the stack.
def dfs_topo_sort(G):
    N = len(G)
    NO_EDGE = G[0][0]
    marked = [False] *N
    discovery_time = [0] *N
    finish_time = [0] *N

    time = 0
    order = []
    def dfs_visit(v):
        nonlocal time
        marked[v]= True
        discovery_time[v] = time #push on stack
        time += 1

        #get to all the neighbors
        for w in range(N):
            if G[v][w] != NO_EDGE and not marked[w]:
                dfs_visit(w)

        finish_time[v] = time #pop from stack
        time += 1
        order.append(v)

    for v in range(N):
        if not marked[v]:
            dfs_visit(v)
    
    order.reverse() #reverse the order to get topological sort
    time_in_stack = [finish_time[i] - discovery_time[i] for i in range(N)]

    return order, finish_time, discovery_time, time_in_stack

G1 = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

G2 = [
    [0,0,1,0,1,1],
    [0,0,1,0,0,0],
    [0,0,0,0,1,1],
    [0,1,2,0,0,1],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0],
]

if __name__ == "__main__":
    print("khans sorting of G1:", khan(G1))
    print("DFS sorting of G1:", dfs_topo_sort(G1)[0])
    print("khans sorting of G2:", khan(G2))
    print("DFS sorting of G2:", dfs_topo_sort(G2)[0])
