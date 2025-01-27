from collections import deque
from typing import Dict, List

"""
A topological sort of a directed acyclic graph (DAG) G = (V, E) is a linear
ordering of all its vertices such that if G contains an edge (u, v), then u
appears before v in the ordering. Topological sorting is defined only on
directed graphs that are acyclic; no linear ordering is possible when a
directed graph contains a cycle.
"""

# Method 1: Kahn's Algorithm (Using In-degrees and a Queue)
def topological_sort_kahn(graph: Dict) -> None | List:
    """
    Perform topological sort on a directed acyclic graph (DAG) using Kahn's algorithm.
    Time Complexity: T(n) = O(|V| + |E|), where |V| is the number of vertices and |E| is the number of edges.
    
    Args:
        graph (dict): The graph represented as an adjacency list. 
                      Example: {'A': ['B', 'C'], 'B': ['C'], 'C': []}
    
    Returns:
        list: A list of vertices in topological order, or None if the graph has a cycle.
    """
    
    # Step 1: Compute in-degree for all vertices
    # In-degree of a vertex is the number of edges pointing to it.
    in_degree = {u: 0 for u in graph}  # Initialize in-degree of all vertices to 0
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1  # Increment in-degree for each edge (u -> v)
    
    # Step 2: Initialize a queue with vertices of in-degree zero
    # These vertices have no prerequisites and can be processed first.
    queue = deque([u for u in graph if in_degree[u] == 0])
    
    # Step 3: Perform topological sort
    topo_sort = []  # List to store the topological order of vertices
    while queue:
        u = queue.popleft()  # Remove a vertex with in-degree zero
        topo_sort.append(u)  # Add it to the topological order
        
        # Decrement the in-degree of all adjacent vertices (v) of u
        for v in graph[u]:
            in_degree[v] -= 1
            # If in-degree of v becomes zero, add it to the queue
            if in_degree[v] == 0:
                queue.append(v)
    
    # Step 4: Check if the topological sort contains all vertices
    # If not, the graph has a cycle, and no valid topological order exists.
    if len(topo_sort) == len(graph):
        return topo_sort 
    else:
        return None  


# Method 2: DFS-based Topological Sort
def topological_sort_dfs(graph: Dict) -> None | List:
    """
    Perform topological sort on a directed acyclic graph (DAG) using DFS.
    Time Complexity: T(n) = O(|V| + |E|)
    
    Args:
        graph (dict): The graph represented as an adjacency list. 
                      Example: {'A': ['B', 'C'], 'B': ['C'], 'C': []}
    
    Returns:
        list: A list of vertices in topological order, or None if the graph has a cycle.
    """
    
    # Helper function for DFS
    def DFS(u):
        nonlocal has_cycle
        if u in visited:
            return
        if u in recursion_stack:
            has_cycle = True  
            return
        recursion_stack.add(u)  # Add to recursion stack
        for v in graph[u]:
            DFS(v)  
        recursion_stack.remove(u)  
        visited.add(u)  # Mark as visited
        topo_sort.append(u)  # Add to topological order
    
    
    visited = set()  
    recursion_stack = set()  # Set to detect cycles
    topo_sort = []  
    has_cycle = False  
    
    # Perform DFS for all unvisited nodes
    for u in graph:
        if u not in visited:
            DFS(u)
    
    # If a cycle is detected, return None
    if has_cycle:
        return None
    else:
        return topo_sort[::-1]  # Reverse the list to get the correct order


def schedule_courses(courses, prerequisites, method='kahn'):
    """
    Schedule courses based on their prerequisites using topological sort.
    
    Args:
        courses (list): A list of course names.
        prerequisites (list): A list of prerequisite pairs, where each pair [a, b] indicates that course 'a' must be taken before course 'b'.
        method (str): The method to use for topological sort. Options: 'kahn' (default) or 'dfs'.
    
    Returns:
        list: A list of courses in a valid order, or None if no valid schedule exists.
    """
    
    # Step 1: Build the graph as an adjacency list
    graph = {course: [] for course in courses}  # Initialize graph with empty adjacency lists
    for a, b in prerequisites:
        graph[a].append(b)  # Add edge (a -> b) to represent the prerequisite relationship
    
    # Step 2: Perform topological sort on the graph using the specified method
    if method == 'kahn':
        return topological_sort_kahn(graph)
    elif method == 'dfs':
        return topological_sort_dfs(graph)
    else:
        raise ValueError("Invalid method. Choose 'kahn' or 'dfs'.")



courses = ['math_1', 'math_2', 'phy_1', 'phy_2', 'computer_intro', 'AP',
           'discrete_math', 'DSA', 'DLD', 'Stats&probs', 'signals']

prerequisites = [
    ['math_1', 'math_2'],  # math_1 must be taken before math_2
    ['phy_1', 'phy_2'],    # phy_1 must be taken before phy_2
    ['math_1', 'discrete_math'], 
    ['computer_intro', 'AP'],  
    ['AP', 'DSA'],  
    ['discrete_math', 'DSA'],  
    ['math_1', 'Stats&probs'],  
    ['Stats&probs', 'signals']  
]

# Get the course schedule using Kahn's algorithm
schedule_kahn = schedule_courses(courses, prerequisites, method='kahn')
if schedule_kahn:
    print(f'Course schedule (Kahn\'s Algorithm): {schedule_kahn}')
else:
    print("No valid schedule exists due to cyclic prerequisites.")

# Get the course schedule using DFS-based topological sort
schedule_dfs = schedule_courses(courses, prerequisites, method='dfs')
if schedule_dfs:
    print(f'Course schedule (DFS-based): {schedule_dfs}')
else:
    print("No valid schedule exists due to cyclic prerequisites.")