# Undirected Adjacency Matrix Using Upper Triangular Matrix
# in an undirected graph the adjacency matrix is symmetric because the 
# adjacency of the nodes i and j means that the elements [i][j] , [j][i] = 1
# This symmetry allows us to save memory by storing only the upper triangular part of 
# the matrix (including the diagonal). This reduces the space complexity from O(V^2) to O(V(V+1)/2), where V is the number of vertices.

# is useful for 
# algorithms that require adjacency matrix (e.g Floyd-Warshall)
# dense graphs
# cons: Not as straightforward as a full adjacency matrix or adjacency list

class UpperTriangularMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.size = (num_vertices * (num_vertices + 1)) // 2  # Size of the upper triangular matrix
        self.matrix = [0] * self.size  

    def get_index(self, i, j):
        # i <= j
        if i > j:
            i, j = j, i
        return i * self.num_vertices + j - (i * (i + 1)) // 2

    def add_edge(self, v1, v2):
        index = self.get_index(v1, v2)
        self.matrix[index] = 1  # unweighted graph!!

    def has_edge(self, v1, v2):
        index = self.get_index(v1, v2)
        return self.matrix[index] == 1

    def display(self):
        for i in range(self.num_vertices):
            row = []
            for j in range(self.num_vertices):
                if i <= j:
                    row.append(self.matrix[self.get_index(i, j)])
                else:
                    row.append(self.matrix[self.get_index(j, i)])
            print(row)

# example using graph:
## below is a mini-social networks of friends
# We have a social network with n users. each user can be friends with other users.
# we need to efficiently store and query friendships using an upper triangular adjacency matrix.

class SocialNetwork:
     def __init__(self , num_users):
          """
          initializing the social network with a given number of users
          """
          self.num_users = num_users
          self.size = (num_users * (num_users + 1)) // 2
          self.matrix = [0] * self.size
     def get_index(self , user1 , user2):
          """
          calculate the index in 1D array"""
          if user1 > user2:
               user2 , user1 = user1 , user2
          return user1 * self.num_users + user2 - (user1 * (user1 + 1)) // 2
     def add_friendship(self, user1, user2):
          """
          Add a friendship between two users.
          :param user1: First user.
          :param user2: Second user.
          """
          index = self.get_index(user1, user2)
          self.matrix[index] = 1 # friended!
     def are_friends(self, user1, user2):
          """
          Check if two users are friends.
          :return: True if they are friends, False otherwise.
          """
          index = self.get_index(user1, user2)
          return self.matrix[index] == 1
     def display_friendships(self):
          """
          Display the friendships in the network as a matrix.
          """
          for i in range(self.num_users):
              row = []
              for j in range(self.num_users):
                  if i <= j:
                      row.append(self.matrix[self.get_index(i, j)])
                  else:
                      row.append(self.matrix[self.get_index(j, i)])
              print(row)

# The **transpose** of a directed graph \( G = (V, E) \) is a graph \( G^T = (V, E^T) \),
# where \( E^T = \{(v, u) \in V \times V : (u, v) \in E\} \). In other words, \( G^T \) is obtained
# by reversing all the edges of \( G \).
# it's like complement in boolean algebra or not operator(!) 

def transpose_graph(graph):
     graph_T = {v: set() for v in graph}
     
     for u in graph:
          for v in graph[u]:
               if u!=v:
                    # used set so that the multiple edges are avoided
                    graph_T[u].add[v]
                    graph_T[v].add[u]
     # convert set to list          
     for u in graph_T:
          graph_T[u] = list(graph_T[u])
          
     return graph_T
 
def find_universal_sink(adj_matrix): #O(V)
     n = len(adj_matrix) # n = |V|
     candidates = 0
     
     for u in range(n):
          if adj_matrix[candidates][u] == 1:
               candidates = u
               
     for u in range(n):
          if adj_matrix[candidates][u] == 1:  # If there is an outgoing edge
               return None # it is not a universal sink
        
def convert_multigraph_to_simple_graph(graph):
     """
     Convert a multigraph to an equivalent undirected simple graph.
     also calculates the complement of the the given graph G, denoted G` 
 
     Args:
         graph (dict): The multigraph represented as an adjacency list.
 
     Returns:
         dict: The adjacency list representation of the equivalent undirected graph.
     """
     # Initialize the adjacency list for G'
     simple_graph = {v: set() for v in graph}
 
     # Iterate through each vertex in the original graph
     for u in graph:
         for v in graph[u]: 
             if u != v:  # Skip self-loops
                 # Add the edge (u, v) if it hasn't been added already
                 simple_graph[u].add(v)
                 simple_graph[v].add(u)  # Undirected graph so both directions should be added
 

     for u in simple_graph:
         simple_graph[u] = list(simple_graph[u])
 
     return simple_graph
  
          
# in transpose we need to remove all self-loops 
# If there are multiple edges between two vertices u and v, replace them with a single edge.






# # for transpose graph:
# graph = {
#     1: [2, 2, 3],  # Multiple edges between 1 and 2
#     2: [1, 1, 3],  # Multiple edges between 2 and 1, and 2 and 3
#     3: [1, 2, 3],  # Self-loop at 3
#     4: []          # Isolated vertex
# }
# print(transpose_graph(graph))             

# # for using UpperTriangularMatrix
# g = UpperTriangularMatrix(4)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.display()

# for UpperTriangularMatrix application
# network = SocialNetwork(4)
# network.add_friendship(0, 1)  # User 0 is friends with User 1
# network.add_friendship(0, 2)  # User 0 is friends with User 2
# network.add_friendship(1, 2)  # User 1 is friends with User 2
# network.add_friendship(2, 3)  # User 2 is friends with User 3
# print("Friendships Matrix:")
# network.display_friendships()
# print("\nAre User 0 and User 1 friends?", network.are_friends(0, 1))  
# print("Are User 1 and User 3 friends?", network.are_friends(1, 3))  



