import random
import time

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition(A, low, high):
    all_equal = True
    first_element = A[low]
    for i in range(low + 1, high + 1):
        if A[i] != first_element:
            all_equal = False
            break
    if all_equal:
        return (low + high) // 2
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            swap(A, i, j)
    swap(A, high, i + 1)
    return i + 1

def randomized_partition(A, low, high):
    i = random.randint(low, high)
    swap(A, i, high)
    return partition(A, low, high)

# QuickSort

# Memory Order: Θ(n)
# Time complexity: T(n) = T(n – 1) + T(0) + Θ(n) = T (n – 1) + Θ(n) == O(n^2);
# substitution method can be used to prove that the recurrence
# T(n) = 2T (n/2) + Θ(n) = O(nlogn) if balanced (use master theorem for evaluating the recursive expression)
# The average running time of quicksort is O(nlgn) because even if the 
# partition function, splits the n elements into a 9n/10 and n/10 sections
# solving the recurrence relation shows that the time complexity would be O(nlgn)
def quicksort(A : list, p : int, r : int ) -> list:
    """The quicksort algorithm has a worst-case running time of Θ(n^2) on an
input Aay of n numbers. Despite this slow worst-case running time,
quicksort is often the best practical choice for sorting because it is
remarkably efficient on average: its expected running time is Θ(n lg n)
when all numbers are distinct, and the constant factors hidden in the
Θ(n lg n) notation are small. Unlike merge sort, it also has the
advantage of sorting in place , and it works well even in
virtual-memory environments"""
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)
        
def insertion_sort(A : list) -> list:
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        
def merge_sort(A : list) -> list:
    if len(A) > 1:
        mid = len(A) // 2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        return merge(left, right)
    return A

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def bubble_sort(A : list) -> list:
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def selection_sort(A : list) -> list:
    n = len(A)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        swap(A, i, min_idx)

def heapify(A, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != i:
        swap(A, i, largest)
        heapify(A, n, largest)

def heapsort(A : list) -> list:
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    for i in range(n - 1, 0, -1):
        swap(A, 0, i)
        heapify(A, i, 0)

def bottom_up_quicksort(A : list) -> list:
    stack = [(0, len(A) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            q = partition(A, low, high)
            stack.append((low, q - 1))
            stack.append((q + 1, high))

# non-comparison sorting - counting sort
# Time-comlexity = Θ(n)
def count_sort(A: list) -> list:
    """
    Sorts an array of integers in ascending order using Counting Sort.

    Args:
        A (List): Input array to be sorted. Must contain integers (positive or negative).

    Returns:
        List: Sorted array in ascending order.

    Raises:
        ValueError: If the input array contains non-integer values.
    """
    # Ensure all elements are integers
    if not all(isinstance(num, int) for num in A):
        raise ValueError("All elements in the input array must be integers.")

    if not A:
        return A

    min_val = min(A)
    max_val = max(A)

    # Handle negative numbers by shifting the range
    range_of_values = max_val - min_val + 1
    count_array = [0] * range_of_values

    # Frequency of each element
    for num in A:
        count_array[num - min_val] += 1

    # Cumulative frequency (for ascending order this time)
    for i in range(1, range_of_values):
        count_array[i] += count_array[i - 1]

    # Build the output array in ascending order
    output = [0] * len(A)
    for i in range(0, len(A)):  # Iterate from the start
        output[count_array[A[i] - min_val] - 1] = A[i]
        count_array[A[i] - min_val] -= 1

    return output

# Radix sort
def counting_sort(A, exp):
    """
    A helper function to perform counting sort on the array based on the digit represented by exp.
    """
    n = len(A)
    output = [0] * n  
    count = [0] * 10  # Count array to store 10 numbers

    #frequency
    for i in range(n):
        index = (A[i] // exp) % 10
        count[index] += 1
    #update coutn
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (A[i] // exp) % 10
        output[count[index] - 1] = A[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements back into the original array
    for i in range(n):
        A[i] = output[i]

def radix_sort(A: list) -> list:
    """
    Sorts an array of non-negative integers using Radix Sort.

    Args:
        A (List): Input array to be sorted. Must contain non-negative integers.

    Returns:
        List: Sorted array.

    Raises:
        ValueError: If the input array contains non-integer or negative values.
    """
    # Input validation: Ensure all elements are non-negative integers
    if not all(isinstance(num, int) and num >= 0 for num in A):
        raise ValueError("All elements in the input array must be non-negative integers.")

    if not A:
        return

    # Find the maximum number to determine the number of digits
    maximum = max(A)

    # Perform counting sort for each digit, starting from the least significant digit (LSD)
    digit = 1
    while maximum // digit > 0:
        counting_sort(A, digit)
        digit *= 10  # Move to the next digit (e.g., units, tens, hundreds, etc.)

    return A

def cocktail_shaker_sort(A: list) -> list:
    """
    Sorts a list using cocktail_shaker Sort (also known as Shaker Sort).

    Args:
      A (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(A)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Traverse from left to right (like Bubble Sort)
        for i in range(start, end):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True

        if not swapped:
            break  # If no swap occurred in the forward pass, the array is sorted

        swapped = False
        end -= 1  # Reduce the end boundary

        # Traverse from right to left
        for i in range(end - 1, start - 1, -1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True

        start += 1 

    return A

def pigeonhole_sort(A: list) -> list:
    """
    Sorts a list of integers using Pigeonhole Sort.

    Args:
        A (list): The list to be sorted (must contain integers).

    Returns:
        list: The sorted list.
    """
    if not A:
        return A  

    min_val = min(A)
    max_val = max(A)
    size = max_val - min_val + 1  

    # Create pigeonholes (buckets)
    pigeonholes = [0] * size

    for num in A:
        pigeonholes[num - min_val] += 1

    # Reconstruct the sorted array
    sorted_A = []
    for index, count in enumerate(pigeonholes):
        value = index + min_val
        sorted_A.extend([value] * count)  # Append 'value' 'count' times

    return sorted_A


def flash_sort(A: list) -> list:
    """
    Sorts a list of numbers using Flash Sort.

    Args:
        A (list): The list to be sorted (should contain comparable numbers).

    Returns:
        list: The sorted list.
    """
    n = len(A)
    if n <= 1:
        return A  # Base case for empty or single-element list

    min_val = min(A)
    max_val = max(A)

    if min_val == max_val:
        return A # handle all elements having same value

    # Calculate class sizes (number of buckets)
    m = int(0.43 * n)  # empirically chosen factor, can vary
    if m < 1:
        m = 1 # min 1 class

    # Create the "L" array (class distribution)
    L = [0] * m

    # Classify the elements
    for num in A:
        k = int(((num - min_val) / (max_val - min_val)) * (m - 1))
        L[k] += 1

    # Calculate starting positions in the buckets
    for k in range(1, m):
      L[k] += L[k - 1]

    # Permutation phase
    hold = A[0]
    move = 0
    j = 0
    k = m - 1  # last class for start
    while move < n - 1:
        while j > L[k]-1:
          k -= 1 # find the new class
        if k < 0:
          k = 0
        while j <= L[k]-1: # find the new place for hold
          j +=1
        if move > 0 and j >= n:
            break # if not first move and all elements are traversed then break out
        
        temp = A[j]
        A[j] = hold
        hold = temp
        L[k] -= 1
        move += 1
       
    # Insertion sort phase within each class
    for i in range(1,n):
      hold = A[i]
      j = i-1
      while j >= 0 and A[j] > hold:
        A[j+1] = A[j]
        j -=1
      A[j+1] = hold

    return A


# The array A is sorted in place
def measure_running_time(sort_func, A, p=None, r=None, trials=100):
    total_time = 0
    for _ in range(trials):
        start_time = time.perf_counter()
        if p is None or r is None:
            sort_func(A)
        else:
            sort_func(A, p, r)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    return total_time / trials

# def measure_running_time(sort_func, A, p=None, r=None):
#     start_time = time.time()
#     if p is None or r is None:
#       sort_func(A)
#     else:
#       sort_func(A, p, r)
#     end_time = time.time()
#     return end_time - start_time

if __name__ == "__main__":
    A = []
    size = 0

    while True:
        try:
            n = input("Enter your number, Otherwise press SORT to sort or EXIT for termination: ")
            if n.upper() == "SORT":
                if size == 0:
                    print("No numbers entered. Please enter numbers first.")
                    continue

                A_normal = A.copy()
                A_randomized = A.copy()
                A_insertion = A.copy()
                A_merge = A.copy()
                A_bubble = A.copy()
                A_selection = A.copy()
                A_heap = A.copy()
                A_bottom_up = A.copy()
                A_counting = A.copy()
                A_radix = A.copy()
                A_cocktail_shaker = A.copy()
                A_pigeonhole = A.copy()
                A_flash = A.copy()
                
                quicksort_time = measure_running_time(quicksort, A_normal, 0, size - 1)
                print(f"Quicksort sorted array: {A_normal}")
                print(f"Quicksort running time: {quicksort_time:.6f} seconds")

                randomized_quicksort_time = measure_running_time(randomized_quicksort, A_randomized, 0, size - 1)
                print(f"Randomized Quicksort sorted array: {A_randomized}")
                print(f"Randomized Quicksort running time: {randomized_quicksort_time:.6f} seconds")

                insertion_sort_time = measure_running_time(insertion_sort, A_insertion)
                print(f"Insertion Sort sorted array: {A_insertion}")
                print(f"Insertion Sort running time: {insertion_sort_time:.6f} seconds")

                merge_sort_time = measure_running_time(merge_sort, A_merge)
                print(f"Merge Sort sorted array: {A_merge}")
                print(f"Merge Sort running time: {merge_sort_time:.6f} seconds")

                bubble_sort_time = measure_running_time(bubble_sort, A_bubble)
                print(f"Bubble Sort sorted array: {A_bubble}")
                print(f"Bubble Sort running time: {bubble_sort_time:.6f} seconds")

                selection_sort_time = measure_running_time(selection_sort, A_selection)
                print(f"Selection Sort sorted array: {A_selection}")
                print(f"Selection Sort running time: {selection_sort_time:.6f} seconds")

                heapsort_time = measure_running_time(heapsort, A_heap)
                print(f"Heapsort sorted array: {A_heap}")
                print(f"Heapsort running time: {heapsort_time:.6f} seconds")

                bottom_up_quicksort_time = measure_running_time(bottom_up_quicksort, A_bottom_up)
                print(f"Bottom-Up Quicksort sorted array: {A_bottom_up}")
                print(f"Bottom-Up Quicksort running time: {bottom_up_quicksort_time:.6f} seconds")
                
                counting_sort_time = measure_running_time(count_sort , A_counting)
                print(f"Counting-sort sorted array: {A_counting}")
                print(f"Counting-sort running time: {counting_sort_time:.6f} seconds")
                
                radix_sort_time = measure_running_time(radix_sort , A_radix)
                print(f"radix-sort sorted array: {A_radix}")
                print(f"radix-sort running time: {radix_sort_time:.6f} seconds")
                
                cocktail_shaker_sort_time = measure_running_time(cocktail_shaker_sort , A_cocktail_shaker)
                print(f"cocktail_shaker/shaker-sort sorted array: {A_cocktail_shaker}")
                print(f"cocktail_shaker/shaker-sort running time: {cocktail_shaker_sort_time:.6f} seconds")
                
                pigeonhole_sort_time = measure_running_time(pigeonhole_sort , A_pigeonhole)
                print(f"cocktail_shaker/shaker-sort sorted array: {A_pigeonhole}")
                print(f"cocktail_shaker/shaker-sort running time: {pigeonhole_sort_time:.6f} seconds")
                
                flash_sort_time = measure_running_time(flash_sort , A_flash)
                print(f"cocktail_shaker/shaker-sort sorted array: {A_flash}")
                print(f"cocktail_shaker/shaker-sort running time: {flash_sort_time:.6f} seconds")
                
            elif n.upper() == "EXIT":
                break
            else:
                n = int(n)
                size += 1
                A.append(n)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'SORT'/'EXIT'.")