class DisjointSet:
    """
    A Disjoint Set (Union-Find) data structure to manage and detect cycles in Kruskal's algorithm.

    Attributes:
        parent (dict): A dictionary to store the parent of each vertex.
        rank (dict): A dictionary to store the rank of each vertex for union by rank.
    """

    def __init__(self, vertices):
        """
        Initialize the DisjointSet with each vertex as its own parent and rank 0.

        Args:
            vertices (list): A list of vertices in the graph.
        """
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        """
        Find the root of the set containing `item` with path compression.

        Args:
            item: The vertex to find the root for.

        Returns:
            The root of the set containing `item`.
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, set1, set2):
        """
        Union the sets containing `set1` and `set2` using union by rank.

        Args:
            set1: The first vertex.
            set2: The second vertex.
        """
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1


def kruskal(graph):
    """
    Kruskal's Algorithm for finding the Minimum Spanning Tree (MST) of a connected, undirected graph.

    Kruskal's algorithm is a greedy algorithm that builds the MST by adding the smallest available edge
    that does not form a cycle. It uses a Disjoint Set (Union-Find) data structure to efficiently manage
    and detect cycles.

    Steps:
    1. Sort all edges in the graph in non-decreasing order of their weight.
    2. Initialize a Disjoint Set to keep track of connected components.
    3. Iterate through the sorted edges:
       - For each edge, check if adding it forms a cycle (using the Disjoint Set).
       - If it does not form a cycle, add it to the MST and merge the two sets in the Disjoint Set.
    4. Repeat until there are (V-1) edges in the MST, where V is the number of vertices.

    Time Complexity: O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices.

    Args:
        graph (dict): The graph represented as an adjacency list.
                      Example: {'A': [('B', 2), ('D', 6)], 'B': [('A', 2), ('C', 3)], ...}

    Returns:
        list: A list of edges in the MST, where each edge is represented as a tuple (u, v, weight).
    """
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    edges.sort()  # Sort edges by weight

    vertices = set(graph.keys())
    ds = DisjointSet(vertices)
    mst = []

    for weight, u, v in edges:
        if ds.find(u) != ds.find(v):  # Check if adding the edge forms a cycle
            mst.append((u, v, weight))
            ds.union(u, v)

    return mst



if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('D', 6)],
        'B': [('A', 2), ('C', 3), ('D', 8)],
        'C': [('B', 3), ('D', 5)],
        'D': [('A', 6), ('B', 8), ('C', 5)],
    }

    mst = kruskal(graph)
    print("Minimum Spanning Tree (Kruskal's Algorithm):")
    for u, v, weight in mst:
        print(f"{u} -- {v} : {weight}")