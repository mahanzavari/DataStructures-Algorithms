# problem 20.2-7 - CLRS book

"""
Problem: 

There are two types of professional wrestlers: “faces” (short for
“babyfaces,” i.e., “good guys”) and “heels” (“bad guys”). Between any
pair of professional wrestlers, there may or may not be a rivalry. You
are given the names of n professional wrestlers and a list of r pairs of
wrestlers for which there are rivalries. Give an O(n + r)-time algorithm
that determines whether it is possible to designate some of the wrestlers
as faces and the remainder as heels such that each rivalry is between a
face and a heel. If it is possible to perform such a designation, your
algorithm should produce it.
"""
from collections import deque

def is_bipartite(graph, n):
     """
     Determine if the graph is bipartite and return the designation of wrestlers.
 
     Description:
         A bipartite graph is a graph whose vertices can be divided into two disjoint sets
         such that no two vertices within the same set are adjacent. In the context of this
         problem, the two sets represent "faces" (good guys) and "heels" (bad guys), and the
         edges represent rivalries. The goal is to determine if it is possible to assign each
         wrestler to one of the two sets such that every rivalry is between a face and a heel.
 
         This problem is equivalent to checking if the graph is bipartite. If the graph is
         bipartite, a valid designation of wrestlers into faces and heels exists; otherwise,
         it does not.
 
     Algorithm:
         1. Represent the wrestlers and rivalries as an adjacency list.
         2. Use BFS to traverse the graph and assign wrestlers to two groups (faces and heels).
         3. Start with an arbitrary wrestler and assign it to the "face" group.
         4. Assign all its rivals to the "heel" group.
         5. Continue this process, ensuring that no two rivals are in the same group.
         6. If a conflict is detected (i.e., a wrestler is assigned to both groups), the graph
            is not bipartite, and the designation is impossible.
         7. If no conflicts are found, return the valid designation of wrestlers into faces
            and heels.
 
     Parameters:
         graph (dict): The graph represented as an adjacency list. Keys are vertices (wrestlers),
                       and values are lists of adjacent vertices (rivals).
         n (int): The number of wrestlers.
 
     Returns:
         tuple: (is_bipartite, designation)
             - is_bipartite (bool): True if the graph is bipartite, False otherwise.
             - designation (dict): A dictionary mapping wrestlers to "face" or "heel".
 
     Time Complexity:
         O(n + r), where n is the number of wrestlers and r is the number of rivalries.
 
     Space Complexity:
         O(n + r), for storing the adjacency list and the designation dictionary.
 
     """
     # Initialize a dictionary to store the designation of each wrestler
     designation = {}
     for wrestler in range(n):
         if wrestler not in designation:
             # Start BFS from the current wrestler
             queue = deque([wrestler])
             designation[wrestler] = "face"  # Assign the starting wrestler to "face"
 
             while queue:
                 current = queue.popleft()
                 current_group = designation[current]
                 
                 for rival in graph[current]:
                     if rival not in designation:
                         designation[rival] = "heel" if current_group == "face" else "face"
                         queue.append(rival)
                     elif designation[rival] == current_group:
                         # Conflict detected: rival is in the same group as current wrestler
                         return False, {}
 
     return True, designation
# Example:
n = 4  # Wrestlers: 0, 1, 2, 3
rivalries = [(0, 1), (1, 2), (2, 3), (3, 0)]  # Rivalries
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [2, 0]
}
is_bipartite, designation = is_bipartite(graph, n)
print(is_bipartite)  
print(designation)   