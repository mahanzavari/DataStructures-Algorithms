def visualize_tree_by_text(root):
     if not root:
          return "<empty>"
     
     results = []
     def traverse(node , level = 0):
          if node:
               traverse(node.right , level + 1)
               results.append(" " * 4 * level + f"{node.key}\n")

          traverse(root)
          return "".join(results)
     
class AVLTreeError(Exception):
     pass