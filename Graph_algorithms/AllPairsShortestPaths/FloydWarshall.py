import sys

def floyd_warsall(graph):
     """
    Floyd-Warshall Algorithm to find all-pairs shortest paths in a weighted graph.

    Parameters:
        graph (list of list of int): Adjacency matrix representation of the graph.
                                     graph[i][j] represents the weight of the edge from vertex i to vertex j.
                                     If there is no edge, graph[i][j] should be set to infinity (sys.maxsize).

    Returns:
        dist (list of list of int): A 2D list where dist[i][j] is the shortest distance from vertex i to vertex j.
        next_vertex (list of list of int): A 2D list used to reconstruct the shortest paths.

    Running Time:
        The algorithm runs in Θ(V^3) time, where V is the number of vertices in the graph.
     """
     # |V| = V
     V = len(graph)
     dist = [[graph[i][j] for j in range(V)] for i in range(V)]
     # next_vertex matrxi for path reconstruction
     next_vertex = [[j if graph[i][j] != sys.maxsize else None for j in range(V)] for i in range(V)]
     
     # floydWarshall algorithm
     
     for k in range(V): # intermediary vertex
          for i in range(V): # source vertex
               for j in range(V): # destination vertex
                    if dist[i][k] != sys.maxsize and dist[k][j] != sys.maxsize \
                    and dist[i][j] > dist[i][k] + dist[k][j]:
                         dist[i][j] = dist[i][k] + dist[k][j]
                         next_vertex[i][j] = next_vertex[i][k]
                         
     for i in range(V):
          if dist[i][i] < 0:
               raise ValueError("Graph contains a negetive cycle")
          
     return dist , next_vertex

def reconstruct_path(next_vertex , start , end):
     """
    Reconstruct the shortest path from start to end using the next_vertex matrix.

    Parameters:
        next_vertex (list of list of int): The next_vertex matrix from the Floyd-Warshall algorithm.
        start (int): The starting vertex.
        end (int): The destination vertex.

    Returns:
        path (list of int): The shortest path from start to end.
     """
     if next_vertex[start][end] is None:
          return [] # no path 
     path = [start]
     while start != end:
          start = next_vertex[start][end]
          path.append(start)
     return path

if __name__ == "__main__":
     # here I have used sys.maxsize for representing infinity
     graph = [
        [0, 3, sys.maxsize, 7],
        [8, 0, 2, sys.maxsize],
        [5, sys.maxsize, 0, 1],
        [2, sys.maxsize, sys.maxsize, 0]
     ]
     dist , next_vertex = floyd_warsall(graph)
     
     print("Shortest distances between all pairs of vertices:")
     for row in dist:
         print(row)
     
     # reconstruct and print the shortest path from vertex 0 to vertex 3
     # you can change this  
     start, end = 0, 3
     path = reconstruct_path(next_vertex, start, end)
     print(f"\nShortest path from {start} to {end}: {path}")