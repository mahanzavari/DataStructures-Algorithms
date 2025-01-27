
def matrix_chain_order(dims):
     """
     Compute the minimum number of scalar multiplications needed
     to multiply a chain of matrices.
      m[i, j] = m[i, k] + m[k + 1, j] + pi−1 pk pj.
 
     Args:
         dims (list): Dimensions of matrices such that the i-th matrix has dimensions
                      dims[i-1] x dims[i].
 
     Returns:
         tuple: A tuple containing:
             - min_cost (int): Minimum number of scalar multiplications.
             - s (list): A table used to reconstruct the optimal parenthesization.
     """
     n = len(dims) - 1  # Number of matrices
     m = [[0] * n for _ in range(n)]  # Minimum cost table
     s = [[0] * n for _ in range(n)]  # Table to store splits
 
     # Length of the chain (l is the number of matrices being multiplied)
     for l in range(2, n + 1):  # l = 2 means pairs, l = 3 means triplets, and so on
         for i in range(n - l + 1):
             j = i + l - 1
             m[i][j] = float('inf')  # Initialize to infinity
             # Test all possible places to split the product
             for k in range(i, j):
                 cost = m[i][k] + m[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                 if cost < m[i][j]:
                     m[i][j] = cost
                     s[i][j] = k
 
     return m[0][n - 1], s
 
 
def  print_optimal_parens(s, i, j):
     """
     Utility to print the optimal parenthesization.
 
     Args:
         s (list): Table used to reconstruct the optimal parenthesization.
         i (int): Starting index of the chain.
         j (int): Ending index of the chain.
 
     Returns:
         str: Optimal parenthesization as a string.
     """
     if i == j:
         return f"M{i + 1}"
     else:
         return f"({print_optimal_parens(s, i, s[i][j])} x {print_optimal_parens(s, s[i][j] + 1, j)})"
 
 
# Example usage
if  __name__ == "__main__":
     # Dimensions of matrices: M1 = 10x20, M2 = 20x30, M3 = 30x40, M4 = 40x30
     # 10 20 30 40 
     
     dims = [20, 40, 30, 40, 50]
     min_cost, s = matrix_chain_order(dims)
     print("Minimum number of scalar multiplications:", min_cost)
     print("Optimal parenthesization:", print_optimal_parens(s, 0, len(dims) - 2))
