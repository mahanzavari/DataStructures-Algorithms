class AVLNode:
     def __init__(self , key):
          self.key = key
          self.left = None
          self.right = None
          self.height = 1
          
class AVLTree:
     def get_height(self , node):
          if not node:
               return 0
          return node.height
     
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
          z.height = 1 + max(self.get_height(z.left) . self.get_height(z.right))
          y.height = 1 + max(self.get_height(y.left) . self.get_height(y.right))
          return y
     
     def search(self , root , key):
          if not root or root.key == key:
               return root
          if key < root.key:
               return self.search(root.left , key)
          return self.search(root.right , key)
     
     
     def insert(self , root , key):
          # 1. BST insertion
          if not root:
               return AVLNode(key)
          elif key < root.key:
               root.left = self.insert(root.left , key)
          else:
               root.right = self.insert(root.right , key)
          # 2. update height 
          root.height = 1 + max(self.get_height(root.left) , self.get_height(root.right))
          
          # 3. balance factor
          balance_favctor = self.get_balance(root)
          
          # 4. fix up operations if needed : similar functionality to the fix_insert in Red-Black trees
          # Left Left case:
          if balance_favctor > 1 and key < root.left.key:
               return self.right_rotate(root)
          
          # Right Right case (dual of the previous case)):
          if balance_favctor < -1 and key > root.right.key:
               return self.left_rotate(root)
          
          # Left Right case:
          if balance_favctor > 1 and key > root.left.key:
               root.left = self.left_rotate(root.left)
               return self.right_rotate(root)
          # Right Left case (dual of the previous case):
          if balance_favctor < - 1 and key < root.left.key:
               root.right = self.right_rotate(root.right)
               return self.left_rotate(root)
     def delete(self , root , key):
          if not root:
               return root
          # BST deletion
          if key < root.key:
               root.left = self.delete(root.left , key)
          elif key > root.key:
               root.right = self.delete(root.right , key)
          else:
               if not root.left:
                    return root.right
               elif not root.right:
                    return root.left
               # if the node has two non-null children then find the inorder succesor (similar to what we had in Red-Black trees)
               temp = self.get_min_value_node(root.right)
               root.key = temp.key 
               root.right = self.delete(root.right , temp.key)
          
          # update the height
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
               self.left_rotate(root)
          # Right Left case
          if balance_factor< -1 and self.get_balance(root.right) > 0:
               root.right = self.right_rotate(root.right)
               return self.left_rotate(root)
          
          return root
               
     def get_min_val_node(self , node):
          curr = root
          while curr.left:
               curr = curr.left
          return curr
     # Traversals 
     # for preorder traversal (left -> right -> root)
     def pre_order(self , root):
          if root:
               print(root.key , end = "")
               self.preorder(root.left)
               self.preorder(root.right)
     # for inorder traversal (left -> root -> right)
     def in_order(self , root):
          if root:
               self.preorder(root.left)
               print(root.key , end = "")
               self.preorder(root.right)
     # for postorder traversal (left -> right -> root)
     def post_order(self , root):
          if root:
               self.preorder(root.left)
               self.preorder(root.right)
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
                              
                              
                              
# if __name__ == "__main__":
#      avl = AVLTree()
#      root = None
#      elements = []
#      for int(input("add : ")):
          
          