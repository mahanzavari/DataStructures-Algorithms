from typing import Optional


def floats_are_equal(a, b, eps=1e-3):
    """Returns True if a and b are within eps of each other"""
    return abs(a - b) < eps


class AVLNode:
     def __init__(self , key):
          self.key = key
          self.left = None
          self.right = None
          self.height = 1
          
class AVLTree:
     """
     Instatiates a AVL Tree 
     Args:
          'use_recursive'(Default = True): instantiates the tree that uses recursion for deletion and insertion 
     """
     def __init__(self , use_recursive = True):
          self.use_recursive = use_recursive
         
     def insert(self , root , key):
          if self.use_recursive:
               return self.insert_recursive(root , key)
          else:
               return self.insert_iterative(root , key)
     def delete(self , root , key):
          if self.use_recursive:
               return self.delete_recursive(root , key)
          else:
               return self.delete_iterative(root , key)
     def get_height(self , node):
          if not node:
               return 0
          return node.height
     
     def get_size(self , root):
          if not root:
               return 0 
          return 1 + self.get_size(root.left) + self.get_size(root.right)
     
     def get_balance(self , node):
          if not node:
               return 0
          return self.get_height(node.left) - self.get_height(node.right)
     # Rotation is a bit different than the one used in Red-Black trees
     def left_rotate(self , z):
          y = z.right
          x = y.left
          y.left = z
          z.right = x
          # the height of z and y has changed 
          z.height = 1 + max(self.get_height(z.left) , self.get_height(z.right))
          y.height = 1 + max(self.get_height(y.left) , self.get_height(y.right))
          return y 
     
     def right_rotate(self , z):
          y = z.left
          x = y.right
          y.right = z
          z.left = x
          # the height of z and y has changed
          z.height = 1 + max(self.get_height(z.left) , self.get_height(z.right))
          y.height = 1 + max(self.get_height(y.left) , self.get_height(y.right))
          return y
     
     def search(self , root , key):
          if not root or floats_are_equal(root.key, key):
               return root
          if key < root.key:
               return self.search(root.left , key)
  
          return self.search(root.right , key)
     def insert_iterative(self, root: Optional[AVLNode], key: float) -> AVLNode:
         """
         Iterative insertion in AVL tree with rebalancing.
               
         Args:
             root (AVLNode): Root of the AVL tree.
             key (float): Key to insert.
               
         Returns:
              AVLNode: New root of the AVL tree after insertion.
         """
         if not root:
             return AVLNode(key)
     
         stack = []
         node = root
     
         while node:
             stack.append(node)
             if key < node.key:
                 if not node.left:
                     node.left = AVLNode(key)
                     break
                 node = node.left
             elif key > node.key:
                 if not node.right:
                     node.right = AVLNode(key)
                     break
                 node = node.right
             else:
                 return root
     
         while stack:
             current = stack.pop()
             current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
     
             balance = self.get_balance(current)
     
             if balance > 1 and key < current.left.key:  # Left Left
                 if stack and stack[-1].left == current:
                     stack[-1].left = self.right_rotate(current)
                 elif stack:
                     stack[-1].right = self.right_rotate(current)
                 else:
                     return self.right_rotate(current)
                     
     
             if balance < -1 and key > current.right.key:  # Right Right
                 if stack and stack[-1].left == current:
                     stack[-1].left = self.left_rotate(current)
                 elif stack:
                     stack[-1].right = self.left_rotate(current)
                 else:
                     return self.left_rotate(current)
     
             if balance > 1 and key > current.left.key:  # Left Right
                 current.left = self.left_rotate(current.left)
                 if stack and stack[-1].left == current:
                      stack[-1].left = self.right_rotate(current)
                 elif stack:
                     stack[-1].right = self.right_rotate(current)
                 else:
                      return self.right_rotate(current)
     
             if balance < -1 and key < current.right.key:  # Right Left
                 current.right = self.right_rotate(current.right)
                 if stack and stack[-1].left == current:
                      stack[-1].left = self.left_rotate(current)
                 elif stack:
                     stack[-1].right = self.left_rotate(current)
                 else:
                      return self.left_rotate(current)
         return root
     
     
     def delete_iterative(self, root, key):
          """
          Iterative deletion in AVL tree with rebalancing.
  
          Args:
              root (AVLNode): Root of the AVL tree.
              key (float): Key to delete.
  
          Returns:
              AVLNode: New root of the AVL tree after deletion.
          """
          if not root:
              return root
  
          stack = []
          parent = None
          curr = root
  
          # Find the node to delete
          while curr and not floats_are_equal(curr.key , key):
              stack.append(curr)
              parent = curr
              if key < curr.key:
                  curr = curr.left
              else:
                  curr = curr.right
  
          if not curr:  # Key not found
              return root
  
          # Case 1: Node has no children or one child
          if not curr.left or not curr.right:
              child = curr.left if curr.left else curr.right
              if not stack:
                  return child  # Deleting the root
              if stack[-1].left == curr:
                  stack[-1].left = child
              else:
                  stack[-1].right = child
  
          # Case 2: Node has two children
          else:
              # Find the in-order successor (leftmost node in the right subtree)
              succ_stack = []
              succ = curr.right
              while succ.left:
                  succ_stack.append(succ)
                  succ = succ.left
  
              # Replace the value
              curr.key = succ.key
  
              # Remove the successor node
              if succ_stack:
                  succ_stack[-1].left = succ.right
              else:
                  curr.right = succ.right
  
          # Rebalance from the bottom up
          while stack:
              node = stack.pop()
              node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
              balance_factor = self.get_balance(node)
  
              # Left-heavy subtree
              if balance_factor > 1:
                  if self.get_balance(node.left) >= 0:  # Left-Left case
                      if stack:
                          if stack[-1].left == node:
                              stack[-1].left = self.right_rotate(node)
                          else:
                              stack[-1].right = self.right_rotate(node)
                      else:
                          root = self.right_rotate(node)
                  else:  # Left-Right case
                      node.left = self.left_rotate(node.left)
                      if stack:
                          if stack[-1].left == node:
                              stack[-1].left = self.right_rotate(node)
                          else:
                              stack[-1].right = self.right_rotate(node)
                      else:
                          root = self.right_rotate(node)
  
              # Right-heavy subtree
              if balance_factor < -1:
                  if self.get_balance(node.right) <= 0:  # Right-Right case
                      if stack:
                          if stack[-1].left == node:
                              stack[-1].left = self.left_rotate(node)
                          else:
                              stack[-1].right = self.left_rotate(node)
                      else:
                          root = self.left_rotate(node)
                  else:  # Right-Left case
                      node.right = self.right_rotate(node.right)
                      if stack:
                          if stack[-1].left == node:
                              stack[-1].left = self.left_rotate(node)
                          else:
                              stack[-1].right = self.left_rotate(node)
                      else:
                          root = self.left_rotate(node)
  
          return root

     

               
     def insert_recursive(self, root: 'AVLNode | None', key: float) -> 'AVLNode | None':
          """
          Recursively insert a key into the AVL tree.

          Args:
              root (AVLNode | None): The root of the subtree.
              key (float): The key to insert.

          Returns:
              AVLNode | None: The new root of the subtree.
          """
          # 1. BST insert_recursiveion
          if not root:
               return AVLNode(key)
          elif key < root.key:
               root.left = self.insert_recursive(root.left , key)
          elif key > root.key:
               root.right = self.insert_recursive(root.right , key)
          else:
             return root # Key already exists, no need to insert
          # 2. update height 
          root.height = 1 + max(self.get_height(root.left) , self.get_height(root.right))
          
          # 3. balance factor
          balance_factor = self.get_balance(root)
          
          # 4. fix up operations if needed : similar functionality to the fix_insert_recursive in Red-Black trees
          # Left Left case:
          if balance_factor > 1 and key < root.left.key:
               return self.right_rotate(root)
          
          # Right Right case (dual of the previous case)):
          if balance_factor < -1 and key > root.right.key:
               return self.left_rotate(root)
          # Left Right case:
          if balance_factor > 1 and key > root.left.key:
               root.left = self.left_rotate(root.left)
               return self.right_rotate(root)
          # Right Left case (dual of the previous case):
          if balance_factor < - 1 and key < root.right.key:
               root.right = self.right_rotate(root.right)
               return self.left_rotate(root)
          return root
     def delete_recursive(self, root: 'AVLNode | None', key: float) -> 'AVLNode | None':
          """
          Recursively deletes a key from the AVL tree.

          Args:
               root (AVLNode | None): The root of the subtree.
               key (float): The key to delete.

          Returns:
               AVLNode | None: The new root of the subtree.
          """
          if not root:
               return root
          # BST deletion
          if key < root.key:
               root.left = self.delete_recursive(root.left , key)
          elif key > root.key:
               root.right = self.delete_recursive(root.right , key)
          else:
               if not root.left:
                    return root.right
               elif not root.right:
                    return root.left
               # if the node has two non-null children then find the inorder succesor (similar to what we had in Red-Black trees)
               temp = self.get_min_val_node(root.right)
               root.key = temp.key 
               root.right = self.delete_recursive(root.right , temp.key)
          if not root:  # If node was deleted and subtree is now empty
            return None
          # update the height
          root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

          balance_factor = self.get_balance(root)
          # Left Left case 
          if balance_factor > 1 and self.get_balance(root.left) >= 0:
               return self.right_rotate(root)
          # Left Right case
          if balance_factor > 1 and self.get_balance(root.left) < 0:
               root.left = self.left_rotate(root.left)
               return self.right_rotate(root)
          # Right Right case
          if balance_factor < -1 and self.get_balance(root.right) <= 0:
               return self.left_rotate(root)
          # Right Left case
          if balance_factor< -1 and self.get_balance(root.right) > 0:
               root.right = self.right_rotate(root.right)
               return self.left_rotate(root)
          
          return root
               
     def get_min_val_node(self , node):
          curr = node
          while curr.left:
               curr = curr.left
          return curr
     # Traversals 
     # for preorder traversal (root -> left -> right)
     def pre_order(self , root):
          if root:
               print(root.key , end = "")
               self.preorder(root.left)
               self.preorder(root.right)
     # for inorder traversal (left -> root -> right)
     def in_order(self , root):
          if root:
               self.in_order(root.left)
               print(root.key , end = "")
               self.in_order(root.right)
     # for postorder traversal (left -> right -> root)
     def post_order(self , root):
          if root:
               self.post_order(root.left)
               self.post_order(root.right)
               print(root.key , end = "")
     def morris_traversal(self , root):
          current = root
          while current:
               if not current.left:
                    print(current.key , end = "")
                    current = current.right
               else:
                    pre = current.left
                    while pre.right and pre.right != current:
                         pre = pre.right
                    if not pre.right:
                         pre.right = current
                         current = current.left
                    else:
                         pre.right = None
                         print(current.key , end = "")
                         current = current.right

     def get_max_val_node(self, node):
      """
      Finds the node with the largest key in the subtree rooted at the given node.

      Args:
          node: The root of the subtree.
      Returns:
           The node with the largest key.
      """
      curr = node
      while curr.right:
          curr = curr.right
      return curr                 
     
     def remove_right_most(self , root):
          """
          Finds and removes the rightmost node from the subtree rooted at `root`.
          Returns:
               A tuple containing the updated tree and the removed node.
          """
          
          if not root:
               return None , None 
          if not root.right:
               return root.left , root
          parent = None
          curr = root
          while curr.right:
               parent = curr
               curr = curr.right
               
          if parent:
               parent.right = curr.left
          
          return root , curr
                                                 

     def right_most_node(self , root):
          """
          Finds the rightmost node from the subtree rooted at 'root'.
          

          Args:
              root (AVLNode): the root of the subtree
          """
          while root.right and root:
               root = root.right
          return root
     def merge_join_based(self , root1 , root2):
          """
          Merges two AVL trees using a join-based method. assumes keys in root 1 < key in root2
          Args:
               root1: The root node of the first AVL tree.
               root2: The root node of the second AVL tree.
          Returns:
               The root of the merged AVL tree.
          """                    
          if not root1:
               return root2
          if not root2:
               return root1
          
          updated_root , removed_node = self.remove_right_most(root1)
          new_root = AVLNode(removed_node.key)
          new_root.left = updated_root
          new_root.right = root2
          
          return self.rebalance_from_node(new_root)                         
                         
               
     def split_node(self , root , key):
          """Splits the subtree rooted at `root` based on the provided key

          Args:
              root (AVLNode): The root node of the subtree to split
              key : The key to split around
          Returns:
                A tuple with two nodes, the first one is the tree containing all elements smaller than the key,
                and the second one has all elements greater than the key.
          """
          if not root:
               return None , None
          if key < root.key:
               left_tree , right_tree = self.split_node(root.left , key)
               root.left = right_tree
               return left_tree , self.rebalance_from_node(root)
          
          elif key > root.key:
               left_tree , right_tree = self.split_node(root.right , key)
               root.right = left_tree
               return self.rebalance_from_node(root) , right_tree
          else:
               return root.left , root.right
          
     def rebalance_from_node(self , node):
          """
          Rebalances the AVL tree from the given node upwards

          Args:
              node (AVLNode): The node from which to start rebalancing. 
          
          Returns: 
               The root of the balanced tree 
          """
              # Update the height of the current node
          node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

          # Calculate the balance factor
          balance_factor = self.get_balance(node)

          # Left-heavy subtree
          if balance_factor > 1:
              if self.get_balance(node.left) >= 0:
                  # Left-Left case
                  return self.right_rotate(node)
              else:
                  # Left-Right case
                  node.left = self.left_rotate(node.left)
                  return self.right_rotate(node)

          # Right-heavy subtree
          if balance_factor < -1:
              if self.get_balance(node.right) <= 0:
                  # Right-Right case
                  return self.left_rotate(node)
              else:
                  # Right-Left case
                  node.right = self.right_rotate(node.right)
                  return self.left_rotate(node)

          # Return the (possibly updated) node
          return node
                    
                    
          
     def merge_split_based(self , root1 , root2) :
          """ Purpose: Implements the merge operation using a split-based approach. It splits the tree and then merges
          the resulting trees using the join based approach.
          Algorithm:
               Base Cases: Return the other node if one of the node is None.
               Find the maximum node of root1: Find the max of the first tree using get_max_val_node
               Split root2: Split the second tree using split_node based on the key of the maximum node of root1, obtaining the left and right subtrees of root2 (left_tree, right_tree).
               Merge Trees: Merge the first tree with left_tree using merge_join_based. Then merge the merged tree from the previous step with right_tree again using merge_join_based.

          Args:
              root1 (AVLTree): The root node of the first AVL tree.
              root2 (AVLTree): The root node of the second AVL tree.

          Returns:
              root: The root node of the merged AVL tree
          """
          if not root1:
               return root2
          if not root2:
               return root1
          max_val_node = self.get_max_val_node(root1)  
          left_tree , right_tree = self.split_node(root2 , max_val_node.key)
          merged_tree = self.merge_join_based(root1 , left_tree)  
          return self.merge_join_based(merged_tree ,right_tree)                 

                            
                              
# if __name__ == "__main__":
#     avl = AVLTree()
#     root = None
#     elements = [10, 20, 30, 40, 50, 25]

#     for element in elements:
#         root = avl.insert_recursive(root, element)

#     print("Inorder Traversal (after insert_recursiveion):")
#     avl.in_order(root)
#     print("\n")

#     print("Preorder Traversal (after insert_recursiveion):")
#     avl.pre_order(root)
#     print("\n")

#     print("Postorder Traversal (after insert_recursiveion):")
#     avl.post_order(root)
#     print("\n")

#     print("Morris Traversal (after insert_recursiveion):")
#     avl.morris_traversal(root)
#     print("\n")

#     print("Size : ", avl.get_size(root))
#     print("\n")
    
#     search_key = 30
#     search_result = avl.search(root, search_key)
#     if search_result:
#         print(f"Found node with key {search_key}")
#     else:
#         print(f"Node with key {search_key} not found")

#     delete_recursive_key = 25
#     root = avl.delete_recursive(root, delete_recursive_key)
#     print(f"\nInorder Traversal after deleting node with key {delete_recursive_key}:")
#     avl.in_order(root)
# #     print("\n")

#     print("Size : ", avl.get_size(root))
#     print(AVLTree.insert_recursive.__doc__) # docstringreslove errors in the attached project, also add error and edge cases handeling to the AVL trees