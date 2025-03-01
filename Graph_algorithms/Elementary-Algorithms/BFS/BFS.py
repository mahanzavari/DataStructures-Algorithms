from collections import deque

def BFS(graph, start):
     """
Breadth-First Search (BFS) Traversal

Description:
    BFS is a graph traversal algorithm that explores all the vertices of a graph level by level.
    It starts at a given source vertex and explores all its neighbors before moving on to the
    neighbors of its neighbors. BFS is useful for finding the shortest path in an unweighted graph
    and for exploring all connected components of a graph.

Algorithm:
    1. Start from a source vertex and mark it as visited.
    2. Add the source vertex to a queue.
    3. While the queue is not empty:
        a. Dequeue a vertex from the queue.
        b. Explore all its unvisited neighbors, mark them as visited, and enqueue them.
    4. Repeat until the queue is empty.

Parameters:
    graph (dict): The graph represented as an adjacency list. Keys are vertices, and values are
                  lists of adjacent vertices.
    start (int): The starting vertex for the BFS traversal.

Returns:
    list: A list of vertices in the order they were visited during the BFS traversal.

Time Complexity:
    O(V + E), where V is the number of vertices and E is the number of edges.

Space Complexity:
    O(V), for storing the queue and visited set.

    Perform Breadth-First Search (BFS) traversal on a graph.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start (int): The starting vertex for the BFS traversal.

    Returns:
        list: A list of vertices in the order they were visited.
    """
     # Initialize a queue for BFS
     queue = deque([start])
     visited = set([start])
     traversal_order = []
 
     while queue:
         # Dequeue a vertex from the queue
         vertex = queue.popleft()
         traversal_order.append(vertex)
 
         # Explore all neighbors of the current vertex
         for neighbor in graph[vertex]:
             if neighbor not in visited:
                 visited.add(neighbor)
                 queue.append(neighbor)
 
     return traversal_order
# # for using bfs 
# graph = {
#         0: [1, 2],
#         1: [0, 3, 4],
#         2: [0, 5],
#         3: [1],
#         4: [1],
#         5: [2]
#     }
# bfs_traversal = BFS(graph, 0)
# print(bfs_traversal) 

