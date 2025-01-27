"""
Depth-First Search (DFS) Traversal (Recursive Version)

Description:
    DFS is a graph traversal algorithm that explores as far as possible along each branch before
    backtracking. It starts at a given source vertex and explores one of its neighbors, then
    recursively explores the neighbor's neighbors, and so on. DFS is useful for detecting cycles,
    topological sorting, and exploring all connected components of a graph.

Algorithm:
    1. Start from a source vertex and mark it as visited.
    2. Explore one of its unvisited neighbors, mark it as visited, and recursively apply DFS.
    3. Backtrack and repeat for other unvisited neighbors.
    4. Continue until all reachable vertices are visited.

Parameters:
    graph (dict): The graph represented as an adjacency list. Keys are vertices, and values are
                  lists of adjacent vertices.
    start (int): The starting vertex for the DFS traversal.

Returns:
    list: A list of vertices in the order they were visited during the DFS traversal.

Time Complexity:
    O(V + E), where V is the number of vertices and E is the number of edges.

Space Complexity:
    O(V), for storing the recursion stack and visited set.
"""


def DFS_recursive(graph, start):
    """
    Perform Depth-First Search (DFS) traversal on a graph using recursion.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start (int): The starting vertex for the DFS traversal.

    Returns:
        list: A list of vertices in the order they were visited.
    """
    visited = set()
    traversal_order = []

    def dfs_helper(vertex):
        # Mark the current vertex as visited
        visited.add(vertex)
        traversal_order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    # Start DFS from the given vertex
    dfs_helper(start)
    return traversal_order


def DFS_iterative(graph, start):
    """
    Perform Depth-First Search (DFS) traversal on a graph using an explicit stack.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start (int): The starting vertex for the DFS traversal.

    Returns:
        list: A list of vertices in the order they were visited.
    """
    stack = [start]
    visited = set()
    traversal_order = []

    while stack:
        # Pop a vertex from the stack
        vertex = stack.pop()

        if vertex not in visited:

            visited.add(vertex)
            traversal_order.append(vertex)

            # Push all unvisited neighbors onto the stack
            for neighbor in reversed(graph[vertex]):  # Reverse to maintain the same order as recursive DFS
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order
graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2]
    }
dfs_traversal = DFS_recursive(graph, 0) # or DFS_iterative
print(dfs_traversal)  