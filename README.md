# Data Structures and Algorithms Implementation

This repository contains implementations of various data structures and algorithms in Python. It is organized into distinct modules for sorting algorithms and different types of trees.

## Directory Structure
```
mahanzavari-datastructures-algorithms/
├── README.md                                  
├── LICENSE                                    # License information for the project
├── Augmenting_Data_Structures/                # Directory for augmented data structure implementations
│   ├── RedBlackTree_size.py                   # Red-Black tree implementation with size augmentation
│   └── IntervalTree/                          # Directory for Interval Tree implementation
│       ├── IntervalTree.py                    # Interval Tree implementation
│       └── Interval_tree_in_practice.py       # Practice script for Interval Trees
├── Medians-and-Order-Statistics/              # Directory for median and order statistics implementations
│   ├── Selection_in_expected_linear_time.py   # Implementation of randomized selection
│   └── Selection_in_worst_case_linear_time.py # Implementation of deterministic selection
├── Sorts_Algorithms/                          # Directory for sorting algorithm implementations
│   ├── README.md                              # README for sorting algorithms
│   ├── Sort_comparisons.py                    # Python script for comparing sorting algorithms
│   └── bucket_sort.py                         # Implementation of bucket sort
└── Trees/                                     # Directory for tree data structure implementations
    ├── AVLTree/                               # Directory for AVL Tree implementation
    │   ├── AVLTree.py                         # AVL Tree implementation
    │   ├── GUI.py                             # GUI for AVL Tree visualization
    │   ├── main.py                            # Main script to run the AVL Tree GUI
    │   └── utils.py                           # Utility functions for AVL Tree
    ├── BTrees/                                # Directory for B+ Tree implementation
    │   └── BPlussTree.py                      # Python script for B+ Tree implementation
    └── RedBlackTree/                          # Directory for Red-Black Tree implementation
        ├── README.md                          
        └── RedBlackTree.py                    # Python script for Red-Black Tree implementation
```

## Project Overview

This project is designed to demonstrate the implementation and behavior of common data structures and algorithms. It is divided into two main sections:

1.  **Sorting Algorithms**: This section provides implementations of various sorting algorithms and a script to compare their performance.
2.  **Trees**: This section includes implementations of different types of balanced and un-balanced tree data structures.
3. **Augmenting Data Structures**: This section includes implementations of data structures augmented with additional information to support new operations.
4.  **Medians and Order Statistics**: This section provides implementations for selecting the kth smallest element in an array.

Each section has its own `README.md` with detailed information about the implementation, usage, and specific algorithms.

## Getting Started

### Prerequisites

-   Python 3.8 or higher
-   Required libraries are listed within the `README.md` of each individual module (found within `/Sorts_Algorithms`, `/Trees/AVLTree` and `/Trees/RedBlackTree`).
-   Graphviz (see `Trees/RedBlackTree/README.md` and `Trees/AVLTree/README.md` for installation)

### Cloning the repository

```bash
git clone [https://github.com/mahanzavari/DataStructures-Algorithms]
cd [DataStructures-Algorithms]
```
### Running the programs

Each module can be run separately. Please refer to the module's `README.md` for specific execution instructions:

*   **Sorting Algorithms:** Instructions in `Sorts_Algorithms/README.md`.
*   **AVL Tree:** Instructions in `Trees/AVLTree/README.md`.
*   **B+ Tree:** Instructions within `Trees/BTrees/BPlussTree.py`
*   **Red-Black Tree:** Instructions in `Trees/RedBlackTree/README.md`.

## Modules

### 1. Sorting Algorithms (`Sorts_Algorithms/`)

This module contains implementations and time comparisons for:

*   Quicksort
*   Randomized Quicksort
*   Insertion Sort
*   Merge Sort
*   Bubble Sort
*   Selection Sort
*   Heapsort
*   Bottom-Up Quicksort

Refer to `Sorts_Algorithms/README.md` for detailed information.
To run the program:
```bash
cd Sorts_Algorithms
python Sort_comparisons.py
```

### 2. Trees (`Trees/`)

This module contains implementations of different types of tree data structures:

*   **AVL Tree (`Trees/AVLTree/`)**: A self-balancing binary search tree with a GUI for visualization. This module contains:
    *   `AVLTree.py`: The core implementation of the AVL tree.
    *   `GUI.py`: A graphical user interface for interacting with and visualizing the tree.
    *   `main.py`: Runs the GUI application.
    *   `utils.py`: Includes utility function to perform basic operations on the tree.
    Refer to `Trees/AVLTree/README.md` for detailed information on how to run the GUI.
    To run the program:
    ```bash
    cd Trees/AVLTree
    python main.py
    ```
*   **B+ Tree (`Trees/BTrees/`)**: An implementation of a B+ tree data structure used in database indexing.
     To run the program:
     ```bash
     cd Trees/BTrees
     python BPlussTree.py --order [B+Tree order]
     ```
*   **Red-Black Tree (`Trees/RedBlackTree/`)**: A self-balancing binary search tree with command interface and visualizations using Graphviz.  This module contains:
    *   `RedBlackTree.py`: Implementation of the Red-Black Tree.
     Refer to `Trees/RedBlackTree/README.md` for details and instructions.
     To run the program:
    ```bash
     cd Trees/RedBlackTree
     python RedBlackTree.py
     ```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

