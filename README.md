# Red-Black Tree with Visualization and Command Interface

## Overview
This project provides an implementation of a **Red-Black Tree** in Python with visualization capabilities and an interactive command interface. A Red-Black Tree is a balanced binary search tree that ensures efficient operations while maintaining specific color and structural properties. This implementation includes:

- Red-Black Tree operations such as **insert**, **delete**, and **search**.
- Tree visualization using **Graphviz**, with visual outputs saved as PNG files in a timestamped directory.
- An interactive console interface for performing operations on the tree.

## Features

### Core Functionality
- **Red-Black Tree Operations**:
  - **Insertion**: Adds a node to the tree while maintaining Red-Black Tree properties.
  - **Deletion**: Removes a node and rebalances the tree if necessary.
  - **Search**: Locates nodes based on their values.

### Visualization
- Automatically generates a graphical representation of the tree after each insertion or deletion.
- Node colors are represented accurately (red or black).
- Visualizations are saved as PNG files in a uniquely timestamped directory.

### Command Interface
- **Insert Nodes**: Add nodes interactively using the `insert <number>` command.
- **Delete Nodes**: Remove nodes interactively using the `delete <number>` command.
- **Exit Program**: End the session with the `exit` command.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Required Python libraries:
  - `graphviz`
  - `os`
  - `uuid`
  - `datetime`

Install the required libraries using pip:
```bash
pip install graphviz
```

### Running the Program
1. Save the script as `red_black_tree_visual.py`.
2. Execute the script:
   ```bash
   python red_black_tree_visual.py
   ```
3. Interact with the tree using the commands described below.

### Interactive Commands
- **Insert a node**:
  ```
  insert <number>
  ```
  Example:
  ```
  insert 10
  insert -5
  ```

- **Delete a node**:
  ```
  delete <number>
  ```
  Example:
  ```
  delete 10
  delete -5
  ```

- **Exit the program**:
  ```
  exit
  ```

### Example Usage
```plaintext
Enter command (insert <num>, delete <num>, or exit): insert 10
Inserting 10
Tree visualization saved as ./Red_Black_20241225_123456/rb_tree_<uuid>.png

Enter command (insert <num>, delete <num>, or exit): delete 10
Deleting 10
Tree visualization saved as ./Red_Black_20241225_123456/rb_tree_<uuid>.png

Enter command (insert <num>, delete <num>, or exit): exit
Exiting program.
```

## File Structure
- **`red_black_tree_visual.py`**: Main script containing the Red-Black Tree implementation and visualization functionality.
- **`Red_Black_<timestamp>`**: Folder containing visualized PNG files of the tree structure for each operation.

## Implementation Details

### Core Components
1. **Node Class**:
   - Represents each node in the Red-Black Tree.
   - Stores data, color, and references to left, right, and parent nodes.

2. **RedBlackTree Class**:
   - Implements Red-Black Tree operations such as insertion, deletion, and search.
   - Handles rebalancing and rotations to maintain tree properties.

3. **VisualRedBlackTree Class**:
   - Extends the `RedBlackTree` class with visualization capabilities using **Graphviz**.
   - Creates a timestamped directory to store visualizations of the tree.

## Examples
### Insertion Example
```plaintext
Inserting 10
Tree visualization saved as ./Red_Black_20241225_123456/rb_tree_<uuid>.png
```

### Deletion Example
```plaintext
Deleting 10
Tree visualization saved as ./Red_Black_20241225_123456/rb_tree_<uuid>.png
```

## Acknowledgments
- **Graphviz**: For generating the visualizations.
- **UUID and Datetime**: For unique filenames and folder naming conventions.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---
Feel free to extend the implementation with additional features such as tree traversal visualizations, performance metrics, or custom visualization styles.

