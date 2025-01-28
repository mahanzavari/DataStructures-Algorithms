import heapq

class Graph:
     def __init__(self, vertices):
         self.V = vertices  # Number of vertices
         self.graph = [[] for _ in range(vertices)]  # Adjacency list
 
     def add_edge(self, u, v, w):
         """
         Adds a directed edge from vertex u to vertex v with weight w.
         """
         self.graph[u].append((v, w))
 
     def Dijkstra(self, src):
          """
          Implements Dijkstra's algorithm to find the shortest paths from a source vertex to all other vertices in a weighted graph with non-negative edge weights.

          The algorithm works as follows:
          1. Initialize distances from the source vertex to all other vertices as infinity, except the source itself (distance 0).
          2. Use a priority queue (min-heap) to track the next vertex to explore based on the smallest tentative distance.
          3. Extract the vertex with the smallest distance from the heap, relax its outgoing edges, and update distances if a shorter path is found.
          4. Repeat until all reachable vertices are processed.  
          Dijkstra's algorithm cannot handle graphs with negative edge weights. 
          Time Complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges.
          Space Complexity: O(V + E) for the adjacency list and O(V) for the distance array and priority queue.    
          Args:
              src (int): The source vertex from which to compute shortest paths.     
          Returns:
              list: An array where each index represents a vertex, and the value is the shortest distance from the source to that vertex.
          """
          # distances initialization
          dist = [float("inf")] * self.V
          dist[src] = 0  
          # heap: (distance, vertex)
          heap = []
          heapq.heappush(heap, (0, src))     
          while heap:
              current_dist, u = heapq.heappop(heap)    
              # Skip if a shorter path to vertex u has already been found
              if current_dist > dist[u]:
                  continue    
              # Step 3: Relax all outgoing edges from u
              for v, w in self.graph[u]:
                  if dist[v] > dist[u] + w:
                      dist[v] = dist[u] + w
                      heapq.heappush(heap, (dist[v], v))    
          return dist    
     def print_solution(self, dist):
          print("Vertex \t Distance from Source")
          for i in range(self.V):
               print(f"{i}\t\t{dist[i]}")


if __name__ == "__main__":
     graph = Graph(5)
     graph.add_edge(0, 1, 4)
     graph.add_edge(0, 2, 1)
     graph.add_edge(1, 3, 1)
     graph.add_edge(2, 1, 2)
     graph.add_edge(2, 3, 5)
     graph.add_edge(3, 4, 3)

     print(graph.graph)
     distances = graph.Dijkstra(0)
     graph.print_solution(distances)