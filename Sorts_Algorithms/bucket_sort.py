import time

def insertion_sort(A: list) -> list:
    """
    Sorts a list using Insertion Sort.
    """
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


def bucket_sort(A: list) -> list:
    """
    Sorts an array of floating-point numbers using Bucket Sort.

    Args:
        A (List): Input array to be sorted. Must contain floating-point numbers in the range [0, 1).

    Returns:
        List: Sorted array.
    """
    if not A:
        return A  # Return empty list if input is empty

    # Input validation: Ensure all elements are floats in the range [0, 1)
    if not all(isinstance(num, float) and 0.0 <= num < 1.0 for num in A):
        raise ValueError("All elements in the input array must be floats in the range [0, 1).")

    n = len(A)
    buckets = [[] for _ in range(n)]  # Create n empty buckets

    # Distribute elements into buckets
    for num in A:
        bucket_index = int(n * num)
        buckets[bucket_index].append(num)

    # Sort elements within each bucket (using insertion sort)
    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i])

    # Concatenate the sorted buckets
    sorted_A = []
    for bucket in buckets:
        sorted_A.extend(bucket)

    return sorted_A

def measure_running_time(sort_func, A):
    """
    Measures the running time of a sorting function.

    Args:
        sort_func (function): The sorting function to measure.
        A (List): The input array to be sorted.

    Returns:
        float: The running time in seconds.
    """
    start_time = time.perf_counter()
    sort_func(A)
    end_time = time.perf_counter()
    return end_time - start_time


if __name__ == "__main__":
    A = []
    size = 0

    while True:
        try:
            n = input("Enter a floating-point number in the range [0, 1), or press SORT to sort or EXIT to terminate: ")
            if n.upper() == "SORT":
                if size == 0:
                    print("No numbers entered. Please enter numbers first.")
                    continue

                A_copy = A.copy()  # Create a copy of the input array

                # Measure the running time of Bucket Sort
                bucket_sort_running_time = measure_running_time(bucket_sort, A_copy)

                # Display the sorted array and running time
                print(f"Bucket-sort sorted array: {bucket_sort(A_copy)}")
                print(f"Bucket-sort running time: {bucket_sort_running_time:.6f} seconds")

            elif n.upper() == "EXIT":
                break
            else:
                n = float(n)  # Convert input to float
                if 0.0 <= n < 1.0:  # Ensure the number is in the range [0, 1)
                    size += 1
                    A.append(n)
                else:
                    print("Invalid input. Please enter a floating-point number in the range [0, 1).")
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number or 'SORT'/'EXIT'.")