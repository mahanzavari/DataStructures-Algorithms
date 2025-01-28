# lets create a custom and naive graph for 
# bellman-ford algorithm 

"""
useful sources:
https://youtu.be/FtN3BYH2Zes?si=FSRzUDhS_zH1eFGU : Abdul bari
CLRS book: chapter 22 - section 1 - The Bellman-Ford algorithm
""" 


class Graph:
     def __init__(self , vertices):
          self.V = vertices
          self.graph = [] # for edges
     # for adding weighted edges
     def add_edge(self , u , v, w):
          self.graph.append([u , v, w])
          
     def Bellman_Ford(self , start):
          """
        Implements the Bellman-Ford algorithm to find the shortest paths from a source vertex to all other vertices in a weighted graph.

        The Bellman-Ford algorithm works as follows:
        1. Initialize distances from the source vertex to all other vertices as infinity, except the source itself, which is set to 0.
        2. Relax all edges |V| - 1 times, where |V| is the number of vertices. Relaxation is the process of updating the distance to a vertex if a shorter path is found.
        - if d[u] + C[(u , v)] < d[v] then d[v] = d[u] + C[(u , v)]
        - make sure all edges are checked
        3. After relaxing all edges, check for negative-weight cycles. If a shorter path is still found, it means there is a negative-weight cycle in the graph.

        The algorithm can handle graphs with negative edge weights and detects negative-weight cycles.

        Time Complexity: O(V * E), where V is the number of vertices and E is the number of edges.
        Space Complexity: O(V), where V is the number of vertices (for storing distances).

        Args:
            src (int): The source vertex from which to compute shortest paths.

        Returns:
            None: Prints the shortest distances from the source vertex to all other vertices.
                  If a negative-weight cycle is detected, it prints a message and returns.
          """
          distances = [float('inf')] * self.V
          distances[start] = 0
          
          for _ in range(self.V - 1):
               for u , v, w in self.graph:
                    if distances[u] != float('inf') and distances[u] + w < distances[v]:
                         distances[v] = distances[u] + w
                         
          for u , v, w in self.graph:
               if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    print("negetive weight cycle detected")
                    return 
          self.print_solution(distances)
          
     def print_solution(self, dist):
          print("Vertex Distance from Source")
          for i in range(self.V):
               print(f"{i}\t\t{dist[i]}")
if __name__ == '__main__':
     graph = Graph(5)
     graph.add_edge(0, 1, -1)
     graph.add_edge(0, 2, 4)
     graph.add_edge(1, 2, 3)
     graph.add_edge(1, 3, 2)
     graph.add_edge(1, 4, 2)
     graph.add_edge(3, 2, 5)
     graph.add_edge(3, 1, 1)
     graph.add_edge(4, 3, -3)
     print(graph.graph)
     graph.Bellman_Ford(0)   
 