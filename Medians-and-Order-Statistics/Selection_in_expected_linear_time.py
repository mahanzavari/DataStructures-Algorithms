import random
# the time complexity in worst case for this algorithm is O(n^2)
def partition(A, low, high):
    # Check if all elements in the subarray are equal
    all_equal = True
    first_element = A[low]
    for i in range(low + 1, high + 1):
        if A[i] != first_element:
            all_equal = False
            break
    if all_equal:
        return (low + high) // 2

    # Normal partitioning
    pivot = A[high]
    i = low - 1

    for j in range(low, high):
        if A[j] <= pivot:  # Change to >= for monotonically decreasing order
            i += 1
            swap(A, i, j)

    swap(A, high, i + 1)
    return i + 1

def swap(A , i , j):
     A[i] , A[j] = A[j] , A[i]
def randomized_partition(A, low, high):

    i = random.randint(low, high)  # Randomly select a pivot index
    swap(A, i, high)
    return partition(A, low, high)
def randomized_Select(A : list, low : int, high : int , i : int) -> int | float:
     """finds the ith minimum number in an array A
     in Order of Θ(n)

     Args:
         A (Array/List): The intended array
         low (int): 
         high (int): 
         i (int): ith static order

     Returns:
         the ith minimum number
     """
     if low == high:
          return A[low]
     q = randomized_partition(A , low , high)
     k = q - low + 1 # number of elements
     if i == k:
          return A[q] # the pivot value is the answer
     elif i < k:
          return randomized_Select(A , low , q - 1 , i)
     else: return randomized_Select(A , q + 1 , high , i - k)
     
     
     
b = []  
b = [1 , 5, 46, 7 , 4 , 6 , 12 , 0 , 4 , 2]
b = randomized_Select(b , 0 , (len(b) - 1) , 6 )
print(b)