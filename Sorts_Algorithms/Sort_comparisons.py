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
def quicksort(A, p, r):
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
        
def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def merge(A, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1

def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(A, left, right)

def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def selection_sort(A):
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

def heapsort(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    for i in range(n - 1, 0, -1):
        swap(A, 0, i)
        heapify(A, i, 0)

def bottom_up_quicksort(A):
    stack = [(0, len(A) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            q = partition(A, low, high)
            stack.append((low, q - 1))
            stack.append((q + 1, high))

def measure_running_time(sort_func, A, p=None, r=None, trials=100):
     total_time = 0
     for _ in range(trials):
         start_time = time.perf_counter()
         if p is None or r is None:
             sort_func(A.copy())
         else:
             sort_func(A.copy(), p, r) 
         end_time = time.perf_counter()
         total_time += (end_time - start_time)
     return total_time/trials

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

            elif n.upper() == "EXIT":
                break
            else:
                n = int(n)
                size += 1
                A.append(n)
        except ValueError as e:
            print(f"Error found: {e}")