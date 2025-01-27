from collections import defaultdict
# from CLRS unit 20.5

# a strongly connected component of a
# directed graph G = (V, E) is a maximal set of vertices C ⊆ V such that
# for every pair of vertices u, v ∈ C, both u ⇝ v and v ⇝ u, that is, vertices
# u and v are reachable from each other


def find_sccs(graph):
    """
    Finds all Strongly Connected Components (SCCs) in a directed graph using Kosaraju's Algorithm.

    Steps of the algorithm:
    1. Perform a DFS to compute the finishing times of vertices.
    2. Reverse the graph.(Transpose of the graph which was covered in the rep.py file of intro to graphs)
    3. Perform a DFS on the reversed graph in the order of decreasing finishing times to extract SCCs.

    Args:
        graph (dict): A dictionary representing the directed graph, where the keys are vertices
                      and the values are lists of adjacent vertices.

    Returns:
        List[List[int]]: A list of SCCs, where each SCC is represented as a list of vertices.
    """
    def dfs1(node):
        """Performs the first DFS to compute finishing times."""
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs1(neighbor)
        stack.append(node)

    def dfs2(node, scc):
        """Performs the second DFS to extract SCCs on the reversed graph."""
        visited.add(node)
        scc.append(node)
        for neighbor in reversed_graph[node]:
            if neighbor not in visited:
                dfs2(neighbor, scc)

    # Step 1: Perform a DFS to compute finishing times
    visited = set()
    stack = []
    for v in graph:
        if v not in visited:
            dfs1(v)

    # Step 2: Reverse the graph
    reversed_graph = defaultdict(list)
    for v in graph:
        for neighbor in graph[v]:
            reversed_graph[neighbor].append(v)

    # Step 3: Perform a DFS on the reversed graph in the order of decreasing finishing times
    visited.clear()
    sccs = []
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs2(node, scc)
            sccs.append(scc)

    return sccs

# Example Usage
if __name__ == "__main__":
    # Define a directed graph as an adjacency list
    graph = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [4],
        4: [],
        5: [6],
        6: [5],
    }

    sccs = find_sccs(graph)
    print("Strongly Connected Components:", sccs)

# Real-World Application Example
def real_world_sccs_example():
    """
    A real-world scenario: Imagine a social network where each node is a user, and an edge from node A to node B indicates that user A follows user B.
    Finding SCCs in this graph helps identify groups of users who are all mutually connected.
    """
    social_network = {
        'Alice': ['Bob'],
        'Bob': ['Charlie'],
        'Charlie': ['Alice', 'David'],
        'David': ['Emily'],
        'Emily': [],
        'Frank': ['Grace'],
        'Grace': ['Frank'],
    }

    sccs = find_sccs(social_network)
    print("Strongly Connected Components in the Social Network:", sccs)

real_world_sccs_example()
