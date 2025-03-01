import heapq



def bellman_ford(graph, weights, source):
     distance = {v: float('inf') for v in graph}
     distance[source] = 0
     
     for _ in range(len(graph) - 1):
         for u in graph:
             for v in graph[u]:
                 if distance[u] + weights[(u, v)] < distance[v]:
                     distance[v] = distance[u] + weights[(u, v)]
     
     for u in graph:
         for v in graph[u]:
             if distance[u] + weights[(u, v)] < distance[v]:
                 return None, None  # Negative-weight cycle detected
     
     return distance, True

def dijkstra(graph, weights, source):
     pq = [(0, source)]
     distance = {v: float('inf') for v in graph}
     distance[source] = 0
     
     while pq:
          d, u = heapq.heappop(pq)
          if d > distance[u]:
              continue
         
          for v in graph[u]:
               alt = distance[u] + weights[(u, v)]
               if alt < distance[v]:
                   distance[v] = alt
                   heapq.heappush(pq, (alt, v))
    
     return distance

def johnson(graph, weights):
    """
    Johnson's Algorithm for All-Pairs Shortest Paths

    This algorithm computes the shortest paths between all pairs of vertices in a weighted, directed graph. 
    It efficiently handles graphs with negative weights but not negative-weight cycles.

    Algorithm Steps:
    1. Augment the graph by adding a new vertex connected to all other vertices with zero-weight edges.
    2. Run Bellman-Ford from the new vertex to compute potential values.
    3. Reweight the original edges to ensure all weights are non-negative.
    4. Run Dijkstra's algorithm from each vertex to compute shortest paths.
    5. Adjust the results to obtain correct distances in the original graph.

    Time Complexity:
    - Bellman-Ford: O(VE)
    - Dijkstra (using a priority queue): O((V + E) log V)
    - Overall: O(VE + V log V) in the worst case

    Space Complexity:
    - O(V^2) for storing the distance matrix
    """
    new_graph = {v: set(neighbors) for v, neighbors in graph.items()}
    new_graph['s'] = set(graph.keys())
    new_weights = weights.copy()
    for v in graph:
        new_weights[('s', v)] = 0
    
    h, valid = bellman_ford(new_graph, new_weights, 's')
    if not valid:
        print("The input graph contains a negative-weight cycle")
        return None
    
    reweighted_weights = {}
    for (u, v), w in weights.items():
        reweighted_weights[(u, v)] = w + h[u] - h[v]
    
    D = {}
    for u in graph:
        shortest_paths = dijkstra(graph, reweighted_weights, u)
        D[u] = {v: shortest_paths[v] + h[v] - h[u] for v in graph}
    
    return D


if __name__ == '__main__':
     graph = {
    'A': {'B', 'C'},
    'B': {'C', 'D'},
    'C': {'D'},
    'D': set()
}
     weights = {
    ('A', 'B'): 1,
    ('A', 'C'): 4,
    ('B', 'C'): 2,
    ('B', 'D'): 5,
    ('C', 'D'): 1
}

     shortest_paths = johnson(graph, weights)
     print(shortest_paths)
