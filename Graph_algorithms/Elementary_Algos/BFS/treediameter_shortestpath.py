from collections import deque

"""Problem:
The diameter of a tree T = (V, E) is defined as max {δ(u, v) : u, v ∈ V},
that is, the largest of all shortest-path distances in the tree. Give an
efficient algorithm to compute the diameter of a tree, and analyze the
running time of your algorithm
"""
# T(n) = O(|V|) because of using BFS two times (recall that T_BFS(n) = O(|V| + |E|) )
# memory = O(|V|) (for deque and set)
def BFS(graph, start):
     # naive BFS implementation is placed in BFS.py
     """
     Perform BFS to find the farthest node from the starting node and its distance.  
     Args:
         graph (dict): The tree represented as an adjacency list.
         start (int): The starting node for BFS.  
     Returns:
         tuple: (farthest_node, distance)
             - farthest_node (int): The farthest node from the starting node.
             - distance (int): The distance to the farthest node.
     """
     queue = deque([(start, 0)])  #(node, distance)
     visited = set([start])
     farthest_node = start
     max_distance = 0    
     while queue:
         current, distance = queue.popleft()
         if distance > max_distance:
             max_distance = distance
             farthest_node = current    
         for neighbor in graph[current]:
             if neighbor not in visited:
                 visited.add(neighbor)
                 queue.append((neighbor, distance + 1))     
     return farthest_node, max_distance

def tree_diameter(graph):
     # Step 1: Find the farthest node from an arbitrary starting node
     arbitrary_node = next(iter(graph))  # Pick any node in the graph
     farthest_node, _ = BFS(graph, arbitrary_node) 
     # Step 2: Find the farthest node from the farthest node found in Step 1
     diameter_node, diameter = BFS(graph, farthest_node)     
     return diameter , diameter_node



graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
n , m = tree_diameter(graph)
print(n)
print(m)