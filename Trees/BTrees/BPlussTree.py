import argparse
from graphviz import Digraph

class BPlusTree:
    def __init__(self, order):
        if order < 3:
             raise ValueError("Order must be at least 3 for B+ tree.")
        self.order = order
        self.root = LeafNode(order)

    def insert(self, key, value):
         if not isinstance(key , int):
              raise TypeError("Key must be an integer.")
         if self.search(key) is not None:
             raise ValueError(f"Duplicate key {key}. Key must be unique for B+ tree.") 
         self.root.insert(key, value)
         if self.root.is_full():
              new_root = InternalNode(self.order)
              new_root.children.append(self.root)
              new_root.split(0, self.root)
              self.root = new_root

    def delete(self, key):
        if not isinstance(key, int):
             raise TypeError("Key must be an integer")
        if not self.search(key):
            raise ValueError(f"Cannot delete {key}, it does not exist in the B+ tree.")
        self.root.delete(key)
        if isinstance(self.root, InternalNode) and len(self.root.children) == 1:
             self.root = self.root.children[0]
        
    def search(self, key):
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")
        return self.root.search(key)
  
    def visualize(self):
        def recurse(node, depth):
            if isinstance(node, LeafNode):
                return f"{'  ' * depth}Leaf: {node.keys}\n"
            elif isinstance(node, InternalNode):
                result = f"{'  ' * depth}Internal: {node.keys}\n"
                for child in node.children:
                    result += recurse(child, depth + 1)
                return result
        return recurse(self.root, 0)

    def visualize_graphical(self, filename="bplustree"):
        graph = Digraph("BPlusTree", format="png")
        graph.attr("node", shape="record")

        def add_node(node, node_id):
            if isinstance(node, LeafNode):
                label = f"Leaf | {{ {' | '.join(map(str, node.keys))} }}"
                graph.node(node_id, label)
            elif isinstance(node, InternalNode):
                label = f"Internal | {{ {' | '.join(map(str, node.keys))} }}"
                graph.node(node_id, label)
            return node_id

        def recurse(node, node_id):
            add_node(node, node_id)
            if isinstance(node, InternalNode):
                for i, child in enumerate(node.children):
                    child_id = f"{node_id}_{i}"
                    graph.edge(node_id, child_id)
                    recurse(child, child_id)

        recurse(self.root, "root")
        graph.render(filename, view=True)

    def __str__(self):
        return self.visualize()

class Node:
    def __init__(self, order):
        self.order = order
        self.keys = [] 

    def is_full(self):
        return len(self.keys) >= self.order

    def is_underflow(self):
        return len(self.keys) < (self.order + 1) // 2

class InternalNode(Node):
    def __init__(self, order):
        super().__init__(order)
        self.children = []

    def insert(self, key, value):
        child = self.find_child(key)
        child.insert(key, value)
        if child.is_full():
            index = self.children.index(child)
            self.split(index, child)

    def delete(self, key):
        child = self.find_child(key)
        child.delete(key)
        if child.is_underflow():
            index = self.children.index(child)
            self.rebalance(index)

    def rebalance(self, index):
        child = self.children[index]
        if isinstance(child, LeafNode):
            # Handle underflow in leaf nodes
            if index > 0 and len(self.children[index - 1].keys) > (self.order - 1) // 2:
                child.borrow_from_left(self.children[index - 1])
            elif index < len(self.children) - 1 and len(self.children[index + 1].keys) > (self.order - 1) // 2:
                child.borrow_from_right(self.children[index + 1])
            else:
                if index > 0:
                    self.merge(index - 1)
                else:
                    self.merge(index)
        else:
            # Internal node underflow
            if index > 0 and len(self.children[index - 1].keys) > (self.order - 1) // 2:
                self.borrow_left(index)
            elif index < len(self.children) - 1 and len(self.children[index + 1].keys) > (self.order - 1) // 2:
                self.borrow_right(index)
            else:
                if index > 0:
                    self.merge(index - 1)
                else:
                    self.merge(index)

    def merge(self, index):
        child = self.children[index]
        sibling = self.children[index + 1]
        # Move the separator key to child
        child.keys.append(self.keys.pop(index))
        # Append sibling's keys and children to child
        child.keys.extend(sibling.keys)
        child.children.extend(sibling.children)
        # Remove sibling from children
        self.children.pop(index + 1)

    def borrow_left(self, index):
        child = self.children[index]
        left_sibling = self.children[index - 1]
        # Move the separator key from parent to child
        child.keys.insert(0, self.keys[index - 1])
        # Move the rightmost child of left_sibling to child
        child.children.insert(0, left_sibling.children.pop())
        # Update the separator key in parent
        self.keys[index - 1] = left_sibling.keys.pop()

    def borrow_right(self, index):
        child = self.children[index]
        right_sibling = self.children[index + 1]
        # Move the separator key from parent to child
        child.keys.append(self.keys[index])
        # Move the leftmost child of right_sibling to child
        child.children.append(right_sibling.children.pop(0))
        # Update the separator key in parent
        self.keys[index] = right_sibling.keys.pop(0)

    def find_child(self, key):
        for i, k in enumerate(self.keys):
            if key < k:
                return self.children[i]
        return self.children[-1]

    def search(self, key):
        return self.find_child(key).search(key)

    def __str__(self):
        return f"InternalNode(keys={self.keys}, children={[str(child) for child in self.children]})" 
    
class LeafNode(Node):
    def __init__(self, order):
        super().__init__(order)
        self.values = []
        self.next = None

    def insert(self, key, value):
        index = self.find_index(key)
        self.keys.insert(index, key)
        self.values.insert(index, value)

    def delete(self, key):
        index = self.find_index(key)
        if index < len(self.keys) and self.keys[index] == key:
            self.keys.pop(index)
            self.values.pop(index)
            # Check for underflow and handle it
            if self.is_underflow():
                # Try borrowing from left sibling
                left_sibling = self.get_prev_leaf()
                if left_sibling and not left_sibling.is_underflow():
                    self.borrow_from_left(left_sibling)
                else:
                    # Try borrowing from right sibling
                    right_sibling = self.get_next_leaf()
                    if right_sibling and not right_sibling.is_underflow():
                        self.borrow_from_right(right_sibling)
                    else:
                        # Merge with a sibling
                        if left_sibling:
                            left_sibling.merge_with_next(self)
                            # Update parent to remove the separator key
                            parent = self.find_parent()
                            if parent:
                                parent.keys.pop(parent.children.index(self))
                                parent.children.remove(self)
                        elif right_sibling:
                            self.merge_with_next(right_sibling)
                            # Update parent to remove the separator key
                            parent = self.find_parent()
                            if parent:
                                parent.keys.pop(parent.children.index(right_sibling))
                                parent.children.remove(right_sibling)

    def find_index(self, key):
        for i, k in enumerate(self.keys):
            if key < k:
                return i
        return len(self.keys)

    def search(self, key):
        for i, k in enumerate(self.keys):
            if k == key:
                return self.values[i]
        return None

    def get_prev_leaf(self):
        current = self
        while current.next:
            current = current.next
        if current.next == self:
            return None  # Circular linked list
        return current

    def get_next_leaf(self):
        return self.next

    def borrow_from_left(self, left_sibling):
        # Borrow a key from the left sibling
        borrowed_key = left_sibling.keys.pop()
        borrowed_value = left_sibling.values.pop()
        # Insert the borrowed key and value at the beginning of self
        self.keys.insert(0, borrowed_key)
        self.values.insert(0, borrowed_value)
        # Update parent node's key if necessary
        parent = self.find_parent()
        if parent:
            index = parent.children.index(self)
            parent.keys[index - 1] = left_sibling.keys[-1]

    def borrow_from_right(self, right_sibling):
        # Borrow a key from the right sibling
        borrowed_key = right_sibling.keys.pop(0)
        borrowed_value = right_sibling.values.pop(0)
        # Append the borrowed key and value to self
        self.keys.append(borrowed_key)
        self.values.append(borrowed_value)
        # Update parent node's key if necessary
        parent = self.find_parent()
        if parent:
            index = parent.children.index(self)
            parent.keys[index] = right_sibling.keys[0]

    def merge_with_next(self, next_leaf):
        # Merge self with the next leaf
        self.keys.extend(next_leaf.keys)
        self.values.extend(next_leaf.values)
        self.next = next_leaf.next
        # Remove next_leaf from the tree
        # Update parent node to remove the separator key
        parent = self.find_parent()
        if parent:
            parent.keys.pop(parent.children.index(next_leaf))
            parent.children.remove(next_leaf)

    def find_parent(self):
        # Traverse up from the node to find its parent
        # This requires adding a 'parent' reference in nodes or traversing the tree
        # For simplicity, assume a way to find the parent is implemented
        pass  # Implementation depends on how parent references are managed

    def is_underflow(self):
        return len(self.keys) < (self.order - 1) // 2

    def __str__(self):
        return f"LeafNode(keys={self.keys}, values={self.values}, next={'next leaf' if self.next else 'None'})"
if __name__ == "__main__":
     parser = argparse.ArgumentParser(description="B+ Tree CLI")
     parser.add_argument("--order", type=int, default=4, help="Order of the B+ Tree")
     args = parser.parse_args()
 
     bptree = BPlusTree(order=args.order)
 
     while True:
          print("\nChoose an operation:")
          print("1. Insert key and value")
          print("2. Delete key")
          print("3. Search key")
          print("4. Visualize tree")
          print("5. Visualize tree graphically")
          print("6. Exit")
  
          choice = input("Enter your choice: ")
  
          try:
              if choice == "1":
                  key = int(input("Enter key: "))
                  value = input("Enter value: ")
                  bptree.insert(key, value)
                  print(f"Inserted key {key} with value '{value}'")
  
              elif choice == "2":
                  key = int(input("Enter key to delete: "))
                  bptree.delete(key)
                  print(f"Deleted key {key}")
  
              elif choice == "3":
                  key = int(input("Enter key to search: "))
                  result = bptree.search(key)
                  if result is not None:
                      print(f"Key {key} found with value '{result}'")
                  else:
                      print(f"Key {key} not found")
 
              elif choice == "4":
                  print("\nTree Visualization:")
                  print(bptree.visualize())
 
              elif choice == "5":
                  filename = input("Enter filename for graphical visualization (default: bplustree): ") or "bplustree"
                  print("Generating graphical visualization...")
                  bptree.visualize_graphical(filename)
  
              elif choice == "6":
                  print("Exiting...")
                  break
  
              else:
                  print("Invalid choice. Please try again.")
          
          except (ValueError, TypeError) as e:
               print(f"Error: {e}")