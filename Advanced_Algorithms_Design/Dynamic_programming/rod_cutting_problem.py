import time  # Import the time module to measure execution time
from typing import Tuple , List
"""
Given a rod of length n
inches and a table of prices pi for i = 1, 2, …, n, determine the maximumrevenue r
n obtainable by cutting up the rod and selling the pieces. If the
price pn for a rod of length n is large enough, an optimal solution might
require no cutting at all.
"""

# this function may get so slow when n grow large(more than 35)
# this program take so long to compute the solution because it recusively calls itself with the same parameter  
# time complexity using recursion tree: T(n) == O(2^n)
# so we need to use dynamic programming to achieve higher speed
def CUT_ROD(P: list, n: int) -> int:
    if n == 0 or len(P) == 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
        q = max(q, P[i - 1] + CUT_ROD(P, n - i))
    return q


# aving subproblem solutions comes with a cost: the additional
# memory needed to store solutions. Dynamic programming thus serves
# as an example of a time-memory trade-off
# T(n) == O(n^2)
# we can use two approaches 
# 1. top-down with memoization In this approach
# 2. bottom-up method
# you write the procedure recursively in a natural manner, but modified to
# save the result of each subproblem (usually in an array or hash table).
# These two approaches yield algorithms with the same asymptotic
# running time, except in unusual circumstances where the top-down
# approach does not actually recurse to examine all possible subproblems.
# The bottom-up approach often has much better constant factors, since
# it has lower overhead for procedure calls.

def Memoized_CUT_ROD_AUX(p: list, n: int, r: list):
    if r[n] >= 0:  # check if there is already a found solution
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n + 1):
            q = max(q, p[i - 1] + Memoized_CUT_ROD_AUX(p, n - i, r))
    r[n] = q  # remember the solution value for length n
    return q

def Memoized_CUT_ROD(p: list, n: int):
    r = [float('-inf')] * (n + 1)
    return Memoized_CUT_ROD_AUX(p, n, r)

def BOTTOM_UP_CUT_ROD(p: list, n: int) -> int:
    r = [0] * (n + 1)
    r[0] = 0
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            q = max(q, p[i - 1] + r[j - i])
        r[j] = q
    return r[n]



def EXTENDED_BOTTOM_UP_CUT_ROD(p: List[int], n: int) -> Tuple[List[int], List[int]]:
    r = [0] * (n + 1)
    s = [0] * n
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j - 1] = i
        r[j] = q
    return r[1:], s

if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 22, 25, 26, 28, 30, 32, 34, 56, 34, 50, 59, 66]  # Example prices for rod lengths
    n = len(prices)  # Length of the rod

    # Measure time for CUT_ROD
    start_time = time.perf_counter()
    result = CUT_ROD(prices, n)
    end_time = time.perf_counter()
    print(f"Maximum revenue for cutting the rod is: {result}")
    print(f"Time taken by CUT_ROD: {end_time - start_time:.6f} seconds\n")

    # Measure time for Memoized_CUT_ROD
    start_time = time.perf_counter()
    result = Memoized_CUT_ROD(prices, n)
    end_time = time.perf_counter()
    print(f"Maximum revenue for cutting the rod (Memoized): {result}")
    print(f"Time taken by Memoized_CUT_ROD: {end_time - start_time:.6f} seconds\n")

    # Measure time for BOTTOM_UP_CUT_ROD
    start_time = time.perf_counter()
    result = BOTTOM_UP_CUT_ROD(prices, n)
    end_time = time.perf_counter()
    print(f"Maximum revenue for cutting the rod (Bottom-Up): {result}")
    print(f"Time taken by BOTTOM_UP_CUT_ROD: {end_time - start_time:.6f} seconds\n")
    
    start_time = time.perf_counter()
    result = EXTENDED_BOTTOM_UP_CUT_ROD(prices , n)
    end_time = time.perf_counter()
    print(f"Maximum revenue for cutting the rod (Extended Bottom Up): {result}")
    print(f"time taken by (Extended Bottom Up): {end_time - start_time:.6f}")