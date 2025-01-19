# Sorting Algorithm Comparisons

This Python program compares the performance of several common sorting algorithms:

*   **Quicksort**
*   **Randomized Quicksort**
*   **Insertion Sort**
*   **Merge Sort**
*   **Bubble Sort**
*   **Selection Sort**
*   **Heapsort**
*   **Bottom-Up Quicksort**

It allows you to input numbers, and when you type "SORT," it will sort the entered numbers using each of the algorithms, and display the sorted array as well as the running time of each algorithm.

## Sorting Algorithm Introductions

Here is a summary of each sorting algorithm used in this program:

### Quicksort

*   **Description:** A divide-and-conquer algorithm that works by partitioning the input array around a pivot element and then recursively sorting the sub-arrays. It's known for its efficiency in practice but has a worst-case time complexity.
*   **Memory Order:** Θ(n) due to recursion.
*   **Time Complexity:**
    *   **Worst-case:** O(n^2)
    *   **Average-case:** O(n log n)
    *   **Best-case:** O(n log n)
*   **In-place:** Yes
*   **Stability:** No

### Randomized Quicksort

*   **Description:** Similar to quicksort, but it selects a random element as the pivot to prevent worst-case scenarios for some input arrays.
*   **Memory Order:** Θ(n) due to recursion.
*   **Time Complexity:**
    *   **Worst-case:** O(n^2)
    *   **Average-case:** O(n log n)
    *   **Best-case:** O(n log n)
*   **In-place:** Yes
*   **Stability:** No

### Insertion Sort

*   **Description:** A simple sorting algorithm that builds the final sorted array one item at a time. It is efficient for small datasets and nearly sorted data.
*   **Memory Order:** Θ(1).
*   **Time Complexity:**
    *   **Worst-case:** O(n^2)
    *   **Average-case:** O(n^2)
    *   **Best-case:** O(n)
*   **In-place:** Yes
*   **Stability:** Yes

### Merge Sort

*   **Description:** A divide-and-conquer algorithm that divides the array into halves, recursively sorts each half, and then merges the sorted halves. It's stable and has consistent performance.
*  **Memory Order:** Θ(n) due to use of temp arrays.
*   **Time Complexity:**
    *   **Worst-case:** O(n log n)
    *   **Average-case:** O(n log n)
    *   **Best-case:** O(n log n)
*   **In-place:** No (requires additional space for merging)
*   **Stability:** Yes

### Bubble Sort

*   **Description:** A simple algorithm that repeatedly steps through the array, compares adjacent elements, and swaps them if they are in the wrong order. Inefficient for large datasets.
*  **Memory Order:** Θ(1).
*   **Time Complexity:**
    *   **Worst-case:** O(n^2)
    *   **Average-case:** O(n^2)
    *   **Best-case:** O(n)
*   **In-place:** Yes
*   **Stability:** Yes

### Selection Sort

*   **Description:** An algorithm that repeatedly finds the minimum element from the unsorted part of the array and places it at the beginning. Not very efficient.
*   **Memory Order:** Θ(1).
*   **Time Complexity:**
    *   **Worst-case:** O(n^2)
    *   **Average-case:** O(n^2)
    *   **Best-case:** O(n^2)
*   **In-place:** Yes
*   **Stability:** No

### Heapsort

*   **Description:** A comparison-based sorting algorithm that uses a heap data structure. It is efficient and has a consistent time complexity.
*   **Memory Order:** Θ(1)
*   **Time Complexity:**
    *   **Worst-case:** O(n log n)
    *   **Average-case:** O(n log n)
    *   **Best-case:** O(n log n)
*   **In-place:** Yes
*   **Stability:** No

### Bottom-Up Quicksort

*   **Description:** An iterative implementation of Quicksort, using a stack to simulate recursion. It avoids the overhead of recursive calls.
*    **Memory Order:**  Θ(n) due to use of stack.
*   **Time Complexity:**
    *   **Worst-case:** O(n^2)
    *   **Average-case:** O(n log n)
    *   **Best-case:** O(n log n)
*   **In-place:** Yes
*   **Stability:** No

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mahanzavari/DSA]
    cd [DSA]
    ```
2.  **Run the script:**
    ```bash
    python Sort_comparisons.py
    ```
3.  **Input:**
    *   Enter numbers one by one when prompted.
    *   Type `SORT` to execute all the sorting algorithms on your numbers and see running times.
    *   Type `EXIT` to terminate the program.

## Code Overview

*   **`Sort_comparisons.py`**: The main Python script containing the implementation of all sorting algorithms, timing and input/output.
    *   `swap(A, i, j)`: Helper function to swap elements in the array `A`.
    *   `partition(A, low, high)`: Helper function to partition for quicksort.
    *   `randomized_partition(A, low, high)`: Helper function to partition with random pivot for randomized quicksort.
    *   `quicksort(A, p, r)`: Recursive implementation of the quicksort algorithm.
    *   `randomized_quicksort(A, p, r)`: Recursive implementation of the randomized quicksort algorithm.
    *   `insertion_sort(A)`:  Implementation of the insertion sort algorithm.
    *   `merge(A, left, right)`: Helper function to merge for merge sort.
    *   `merge_sort(A)`: Recursive implementation of the merge sort algorithm.
    *   `bubble_sort(A)`:  Implementation of the bubble sort algorithm.
    *   `selection_sort(A)`:  Implementation of the selection sort algorithm.
    *   `heapify(A, n, i)`: Helper function to heapify for heapsort.
    *   `heapsort(A)`:  Implementation of the heapsort algorithm.
    *   `bottom_up_quicksort(A)`: Iterative implementation of quicksort using a stack.
    *  `measure_running_time(sort_func, A, p=None, r=None, trials=100)`: Helper function to measure the running time of an algorithm
*   The `if __name__ == "__main__":` block handles the user input, calls the sorting functions and prints the output.

## Notes

*   The time measurements are based on the average of 100 trials for more stability.
*   The arrays are copied before being passed to each sorting algorithm to ensure each runs on the same input array.
*   The output shows the sorted array and the running time of each sorting algorithm.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to create an issue or submit a pull request.
