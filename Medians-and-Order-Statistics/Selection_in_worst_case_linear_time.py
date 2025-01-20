def SELECT(A, p, r, i):
     """The selection algorithm presented in this section achieves
linear time in the worst case, but it is not nearly as practical as
RANDOMIZED-SELECT. It is mostly of theoretical interest.
     """
     
     # Step 1: Ensure (r - p + 1) is divisible by 5
     while (r - p + 1) % 5 != 0:
         for j in range(p + 1, r + 1):
             if A[p] > A[j]:
                 A[p], A[j] = A[j], A[p]  # Swap A[p] with A[j]
         if i == 1:
             return A[p]  # Return the minimum of A[p:r+1]
         p += 1
         i -= 1
 
     # Step 2: Group elements into groups of 5 and sort each group
     g = (r - p + 1) // 5  # Number of 5-element groups
     for j in range(g):
         start = p + j * 5
         group = A[start:start + 5]
         group.sort()
         A[start:start + 5] = group
 
     # Step 3: Find the median of medians
     medians_start = p + 2
     medians_end = p + 2 + g - 1
     median_of_medians_index = (g + 1) // 2
     x = SELECT(A, medians_start, medians_end, median_of_medians_index)
 
     # Step 4: Partition around the pivot (x)
     q = PARTITION_AROUND(A, p, r, x)
 
     # Step 5: Recursive selection based on partition result
     k = q - p + 1
     if i == k:
         return A[q]  # The pivot value is the answer
     elif i < k:
         return SELECT(A, p, q - 1, i)
     else:
         return SELECT(A, q + 1, r, i - k)

def PARTITION_AROUND(A, p, r, pivot):
     """Partitions the array around the given pivot value."""
     pivot_index = A.index(pivot)
     A[pivot_index], A[r] = A[r], A[pivot_index]  # Move pivot to the end
     i = p - 1
     for j in range(p, r):
         if A[j] <= pivot:
             i += 1
             A[i], A[j] = A[j], A[i]
     A[i + 1], A[r] = A[r], A[i + 1]  # Place pivot in its final position
     return i + 1
