import math

# I have used AI for fibonacci heaps since they are not used often in industry
# please double check for the fibonacci heap
class FibonacciHeapNode:
    def __init__(self, key, value):
        """
        Represents a node in the Fibonacci Heap.

        Attributes:
            key (int): The key (priority) of the node.
            value (any): The value stored in the node.
            degree (int): The number of children of the node.
            parent (FibonacciHeapNode): Pointer to the parent node.
            child (FibonacciHeapNode): Pointer to one of the child nodes.
            left (FibonacciHeapNode): Pointer to the left sibling.
            right (FibonacciHeapNode): Pointer to the right sibling.
            marked (bool): Indicates whether the node has lost a child since it became a child of another node.
        """
        self.key = key
        self.value = value
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.marked = False


class FibonacciHeap:
    def __init__(self):
        """
        Initializes an empty Fibonacci Heap.

        Attributes:
            min_node (FibonacciHeapNode): Pointer to the node with the minimum key.
            num_nodes (int): The total number of nodes in the heap.
        """
        self.min_node = None
        self.num_nodes = 0

    def insert(self, key, value):
        """
        Inserts a new node into the Fibonacci Heap.

        Args:
            key (int): The key (priority) of the node.
            value (any): The value to be stored in the node.
        """
        node = FibonacciHeapNode(key, value)
        if self.min_node is None:
            self.min_node = node
        else:
            self._add_to_root_list(node)
            if node.key < self.min_node.key:
                self.min_node = node
        self.num_nodes += 1

    def _add_to_root_list(self, node):
        """
        Adds a node to the root list of the Fibonacci Heap.

        Args:
            node (FibonacciHeapNode): The node to be added to the root list.
        """
        node.left = self.min_node
        node.right = self.min_node.right
        self.min_node.right.left = node
        self.min_node.right = node

    def extract_min(self):
        """
        Extracts and returns the node with the minimum key from the Fibonacci Heap.

        Returns:
            FibonacciHeapNode: The node with the minimum key.
        """
        z = self.min_node
        if z is not None:
            if z.child is not None:
                children = self._get_children(z)
                for child in children:
                    self._add_to_root_list(child)
                    child.parent = None
            self._remove_from_root_list(z)
            if z == z.right:
                self.min_node = None
            else:
                self.min_node = z.right
                self._consolidate()
            self.num_nodes -= 1
        return z

    def _get_children(self, node):
        """
        Retrieves all children of a given node.

        Args:
            node (FibonacciHeapNode): The node whose children are to be retrieved.

        Returns:
            list: A list of children nodes.
        """
        children = []
        current = node.child
        while True:
            children.append(current)
            if current.right == node.child:
                break
            current = current.right
        return children

    def _remove_from_root_list(self, node):
        """
        Removes a node from the root list.

        Args:
            node (FibonacciHeapNode): The node to be removed from the root list.
        """
        node.left.right = node.right
        node.right.left = node.left

    def _consolidate(self):
        """
        Consolidates the Fibonacci Heap by combining trees of the same degree.
        """
        degree_table = [None] * self.num_nodes
        nodes = self._get_root_nodes()
        for node in nodes:
            degree = node.degree
            while degree_table[degree] is not None:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link(other, node)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node
        self.min_node = None
        for node in degree_table:
            if node is not None:
                if self.min_node is None:
                    self.min_node = node
                elif node.key < self.min_node.key:
                    self.min_node = node

    def _get_root_nodes(self):
        """
        Retrieves all nodes in the root list.

        Returns:
            list: A list of nodes in the root list.
        """
        nodes = []
        current = self.min_node
        while True:
            nodes.append(current)
            if current.right == self.min_node:
                break
            current = current.right
        return nodes

    def _link(self, child, parent):
        """
        Links two trees by making one node the child of another.

        Args:
            child (FibonacciHeapNode): The node to become the child.
            parent (FibonacciHeapNode): The node to become the parent.
        """
        self._remove_from_root_list(child)
        child.parent = parent
        if parent.child is None:
            parent.child = child
            child.left = child
            child.right = child
        else:
            child.left = parent.child
            child.right = parent.child.right
            parent.child.right.left = child
            parent.child.right = child
        parent.degree += 1
        child.marked = False

    def decrease_key(self, node, new_key):
        """
        Decreases the key of a node in the Fibonacci Heap.

        Args:
            node (FibonacciHeapNode): The node whose key is to be decreased.
            new_key (int): The new key value.

        Raises:
            ValueError: If the new key is greater than the current key.
        """
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        node.key = new_key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if node.key < self.min_node.key:
            self.min_node = node

    def _cut(self, node, parent):
        """
        Cuts a node from its parent and adds it to the root list.

        Args:
            node (FibonacciHeapNode): The node to be cut.
            parent (FibonacciHeapNode): The parent node.
        """
        self._remove_from_child_list(parent, node)
        parent.degree -= 1
        self._add_to_root_list(node)
        node.parent = None
        node.marked = False

    def _remove_from_child_list(self, parent, node):
        """
        Removes a node from its parent's child list.

        Args:
            parent (FibonacciHeapNode): The parent node.
            node (FibonacciHeapNode): The node to be removed.
        """
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
        node.left.right = node.right
        node.right.left = node.left

    def _cascading_cut(self, node):
        """
        Performs a cascading cut operation to maintain the heap properties.

        Args:
            node (FibonacciHeapNode): The node to start the cascading cut from.
        """
        parent = node.parent
        if parent is not None:
            if not node.marked:
                node.marked = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)


def prim_fibonacci_heap(graph, start_vertex):
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph using a Fibonacci Heap.

    Args:
        graph (dict): The graph represented as a dictionary of adjacency lists.
                      Example: {'A': {'B': 2, 'C': 4}, 'B': {'A': 2, 'C': 1}, 'C': {'A': 4, 'B': 1}}
        start_vertex (any): The starting vertex for the algorithm.

    Returns:
        tuple: A tuple containing:
            - mst (dict): A dictionary representing the MST, where keys are vertices and values are their minimum edge weights.
            - total_weight (int): The total weight of the MST.
    """
    heap = FibonacciHeap()
    vertex_to_node = {}
    mst = {}
    total_weight = 0

    # Initialize the heap with all vertices
    for vertex in graph:
        if vertex == start_vertex:
            heap.insert(0, vertex)
        else:
            heap.insert(math.inf, vertex)
        vertex_to_node[vertex] = heap.min_node

    # Build the MST
    while heap.num_nodes > 0:
        min_node = heap.extract_min()
        current_vertex = min_node.value
        mst[current_vertex] = min_node.key
        total_weight += min_node.key

        # Update keys of adjacent vertices
        for neighbor, weight in graph[current_vertex].items():
            if neighbor not in mst:
                neighbor_node = vertex_to_node[neighbor]
                if weight < neighbor_node.key:
                    heap.decrease_key(neighbor_node, weight)

    return mst, total_weight


graph = {
    'A': {'B': 2, 'D': 6},
    'B': {'A': 2, 'C': 3, 'D': 8, 'E': 5},
    'C': {'B': 3, 'E': 7},
    'D': {'A': 6, 'B': 8, 'E': 9},
    'E': {'B': 5, 'C': 7, 'D': 9}
}

mst, total_weight = prim_fibonacci_heap(graph, 'A')
print("Minimum Spanning Tree:", mst)
print("Total Weight:", total_weight)