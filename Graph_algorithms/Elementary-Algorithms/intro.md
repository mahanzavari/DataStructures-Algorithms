Here’s the updated and corrected markdown with improvements to grammar, formatting, and clarity:


# **Graph Introduction**

In computer programs, graphs can be represented in two ways:  
1. **Adjacency List**  
2. **Adjacency Matrix**

## **Adjacency Matrix**
An adjacency matrix is a 2D array where the rows and columns represent the vertices of the graph. The value at `matrix[i][j]` indicates whether there is an edge between vertex `i` and vertex `j`.

### **Unweighted Graph Representation**
- `matrix[i][j] = 1` if there is an edge between vertex `i` and vertex `j`.
- `matrix[i][j] = 0` if there is no edge.

### **Weighted Graph Representation**
- `matrix[i][j]` stores the weight of the edge between vertex `i` and vertex `j`.
- `matrix[i][j] = ∞` (infinity) or a special value (e.g., `-1`) if there is no edge.

#### **Example Code**
```python
class Graph:
    def __init__(self, vertices_num):
        self.vertices_num = vertices_num
        self.matrix = [[0] * vertices_num for _ in range(vertices_num)]

    def add_edge(self, u1, u2):
        self.matrix[u1][u2] = 1
        self.matrix[u2][u1] = 1  # For undirected graphs

    def print_graph(self):
        for row in self.matrix:
            print(row)
```

### **Applications**
- Suitable for **dense graphs** (where the number of edges is close to the maximum possible).
- Efficient for checking if an edge exists between two vertices (`O(1)` time complexity).
- Used in algorithms like **Floyd-Warshall** (all-pairs shortest paths).

### **Pros**
- Simple and easy to implement.
- Fast edge lookup (`O(1)`).

### **Cons**
- Requires `O(V^2)` space, which is inefficient for sparse graphs.
- Adding or removing vertices is expensive.

---

## **Adjacency List**
An adjacency list represents a graph as an array of lists. Each vertex has a list of its adjacent vertices.

### **Representation**
- **Unweighted Graph**:  
  Use a list of lists, where each inner list contains the neighbors of a vertex.

- **Weighted Graph**:  
  Use a list of lists of tuples, where each tuple contains a neighbor and the corresponding edge weight.

#### **Example Code**
```python
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)  # For undirected graphs

    def display(self):
        for i, neighbors in enumerate(self.adj_list):
            print(f"{i}: {neighbors}")
```

### **Applications**
- Suitable for **sparse graphs** (where the number of edges is much smaller than the maximum possible).
- Used in algorithms like **Dijkstra’s** and **Prim’s** (for weighted graphs).

### **Pros**
- Space-efficient for sparse graphs (`O(V + E)`).
- Easy to add or remove vertices and edges.

### **Cons**
- Edge lookup can take up to `O(V)` in the worst case.
- Slightly more complex to implement compared to adjacency matrices.

---

## **Comparison Table**

| Feature             | **Adjacency Matrix**        | **Adjacency List**           |
|-----------|------------------------------|--------------------------------|
| **Space Complexity**   | `O(V^2)`                           | `O(V + E)`                     |
| **Edge Lookup**        | `O(1)`                         | `O(V)` in the worst case           |
| **Adding a Vertex**    | `O(V^2)` (resizing required)     | `O(1)`                         |
| **Adding an Edge**     | `O(1)`                             | `O(1)`                             |
| **Removing a Vertex**  | `O(V^2)`                         | `O(E)`                             |
| **Removing an Edge**   | `O(1)`                            | `O(V)`                           |
| **Best Use Case**      | Dense graphs                    | Sparse graphs                      |


### Updates and Fixes:
1. **Grammar**: Corrected minor grammatical errors, e.g., “Graph Introdunction” → “Graph Introduction.”
2. **Formatting**: Improved markdown structure with bold headers, consistent code formatting, and organized sections.
3. **Code Fixes**: Corrected errors in the Python code, e.g., replaced `num` with `vertices_num` and fixed the typo `marix` → `matrix`.
4. **Clarity**: Added clear subheadings, explanations, and example code for better readability.

**for more information about the graph representation checkout the ```rep.py``` file**