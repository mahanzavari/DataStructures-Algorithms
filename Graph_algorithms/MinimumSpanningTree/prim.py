import heapq
def prim(graph, start):
    """
    Prim's Algorithm for finding the Minimum Spanning Tree (MST) of a connected, undirected graph.

    Prim's algorithm is a greedy algorithm that builds the MST by starting from an arbitrary vertex
    and repeatedly adding the smallest edge that connects a vertex in the MST to a vertex outside the MST.

    Steps:
    1. Initialize a priority queue (min-heap) to store edges and a set to track vertices included in the MST.
    2. Start with an arbitrary vertex and add all its edges to the priority queue.
    3. While the priority queue is not empty:
       - Extract the edge with the smallest weight.
       - If the edge connects a vertex not in the MST, add it to the MST and add all edges of the new vertex to the priority queue.
    4. Repeat until all vertices are included in the MST.

    Time Complexity: O(E log V) using a binary heap, where E is the number of edges and V is the number of vertices.

    Args:
        graph (dict): The graph represented as an adjacency list.
                      Example: {'A': [('B', 2), ('D', 6)], 'B': [('A', 2), ('C', 3)], ...}
        start: The starting vertex for the algorithm.

    Returns:
        list: A list of edges in the MST, where each edge is represented as a tuple (u, v, weight).
    """
    mst = []
    visited = set()
    edges = [(weight, start, v) for v, weight in graph[start]]
    heapq.heapify(edges)
    visited.add(start)

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, v, neighbor))

    return mst



if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('D', 6)],
        'B': [('A', 2), ('C', 3), ('D', 8)],
        'C': [('B', 3), ('D', 5)],
        'D': [('A', 6), ('B', 8), ('C', 5)],
    }

    mst = prim(graph, 'A')
    print("Minimum Spanning Tree (Prim's Algorithm):")
    for u, v, weight in mst:
        print(f"{u} -- {v} : {weight}")