import tkinter as tk
from tkinter import messagebox
from math import cos, sin, radians

def floats_are_equal(a, b, eps=1e-3):
    return abs(a - b) < eps


class Interval:
    def __init__(self, low, high, data=None):
        self.low = low
        self.high = high
        self.data = data

    def __repr__(self):
        return f"[{self.low}, {self.high}]"

class Node:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.high
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.color = 'BLACK' # Added color attribute

class IntervalTree:
    def __init__(self):
        self.root = None

    def _update_size(self, node):
        if node is None:
            return
        node.size = (node.left.size if node.left else 0) + (node.right.size if node.right else 0) + 1

    def _update_max(self, node):
        if node is None:
            return
        node.max = max(node.interval.high,
                      node.left.max if node.left else node.interval.high,
                       node.right.max if node.right else node.interval.high
                      )

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent
        
        current = v
        while current:
            self._update_size(current)
            self._update_max(current)
            current = current.parent
        
    def _minimum(self, node):
        while node.left:
            node = node.left
        return node

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

        self._update_size(x)
        self._update_max(x)
        self._update_size(y)
        self._update_max(y)

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x
        
        self._update_size(y)
        self._update_max(y)
        self._update_size(x)
        self._update_max(x)

    def _update_ancestor_size_on_insert(self,node):
        current = node.parent
        while current:
          self._update_size(current)
          self._update_max(current)
          current = current.parent
    
    def _fix_insert(self, z):
            z.color = 'RED'
            while z != self.root and z.parent.color == 'RED':
                if z.parent == z.parent.parent.left:
                    y = z.parent.parent.right
                    if y and y.color == 'RED':
                        z.parent.color = 'BLACK'
                        y.color = 'BLACK'
                        z.parent.parent.color = 'RED'
                        z = z.parent.parent
                    else:
                        if z == z.parent.right:
                            z = z.parent
                            self._left_rotate(z)
                        z.parent.color = 'BLACK'
                        z.parent.parent.color = 'RED'
                        self._right_rotate(z.parent.parent)
                else:
                    y = z.parent.parent.left
                    if y and y.color == 'RED':
                        z.parent.color = 'BLACK'
                        y.color = 'BLACK'
                        z.parent.parent.color = 'RED'
                        z = z.parent.parent
                    else:
                        if z == z.parent.left:
                            z = z.parent
                            self._right_rotate(z)
                        z.parent.color = 'BLACK'
                        z.parent.parent.color = 'RED'
                        self._left_rotate(z.parent.parent)
            self.root.color = 'BLACK'
            
            
    def insert(self, interval):
        new_node = Node(interval)
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            parent = None
            while curr:
                parent = curr
                if interval.low < curr.interval.low:
                    curr = curr.left
                else:
                    curr = curr.right
            new_node.parent = parent
            if interval.low < parent.interval.low:
               parent.left = new_node
            else:
              parent.right = new_node
        
        self._update_ancestor_size_on_insert(new_node)
        self._fix_insert(new_node)

    def _fix_delete(self, x):
      while x != self.root and (x.max < (x.parent.max if x.parent else 0) ):
          if x == x.parent.left:
              s = x.parent.right
              if s and (s.max >= (x.parent.max if x.parent else 0)):
                 break
              if s and s.max < (x.parent.max if x.parent else 0):
                if s.right and s.right.max >= (x.parent.max if x.parent else 0):
                   s.max = x.parent.max if x.parent else 0
                   self._left_rotate(x.parent)
                   x = self.root
                else:
                    if s.left and s.left.max >= (x.parent.max if x.parent else 0) :
                      self._right_rotate(s)
                      s = x.parent.right
                    
                    s.max = x.parent.max if x.parent else 0
                    self._left_rotate(x.parent)
                    x = self.root
                    
          else:
              s = x.parent.left
              if s and s.max >= (x.parent.max if x.parent else 0):
                break
              if s and s.max < (x.parent.max if x.parent else 0):
                  if s.left and s.left.max >= (x.parent.max if x.parent else 0):
                      s.max = x.parent.max if x.parent else 0
                      self._right_rotate(x.parent)
                      x = self.root
                  else:
                    if s.right and s.right.max >= (x.parent.max if x.parent else 0):
                      self._left_rotate(s)
                      s = x.parent.left
                      
                    s.max = x.parent.max if x.parent else 0
                    self._right_rotate(x.parent)
                    x = self.root
      if x.max < self.root.max:
         self.root.max = self.root.right.max if self.root.right else self.root.interval.high
         
    def _delete_fix_color(self, node):
        if node:
          node.color = 'BLACK'


    def delete(self, interval):
      node = self.root
      z = None
      while node:
        if floats_are_equal(node.interval.low,interval.low) and floats_are_equal(node.interval.high, interval.high):
           z = node
           break
        if interval.low < node.interval.low:
          node = node.left
        else:
          node = node.right
      
      if z is None:
        print("Couldn't find the interval in tree")
        return
      
      if z.left is None:
        x = z.right
        self._transplant(z, z.right)
      elif z.right is None:
        x = z.left
        self._transplant(z, z.left)
      else:
        y = self._minimum(z.right)
        x = y.right
        if y.parent != z:
          self._transplant(y, y.right)
          y.right = z.right
          y.right.parent = y
        self._transplant(z, y)
        y.left = z.left
        y.left.parent = y
      if x:
         self._fix_delete(x)
         self._delete_fix_color(x)

    def search(self, interval):
      curr = self.root
      while curr:
        if floats_are_equal(curr.interval.low, interval.low) and floats_are_equal(curr.interval.high, interval.high):
           return curr
        if interval.low < curr.interval.low:
          curr = curr.left
        else:
          curr = curr.right
      return None
    
    def overlap_search(self, interval):
        node = self.root
        while node:
           if self._overlap(node.interval,interval):
              return node
           if node.left and node.left.max >= interval.low:
              node = node.left
           else:
             node = node.right
        return None

    def _overlap(self, interval_a, interval_b):
        return interval_a.low <= interval_b.high and interval_b.low <= interval_a.high


class IntervalTreeGUI:
    def __init__(self):
        self.tree = IntervalTree()
        self.window = tk.Tk()
        self.window.title("Interval Tree GUI")
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="white")
        self.canvas.pack()

        # Input controls
        self.control_frame = tk.Frame(self.window)
        self.control_frame.pack()
        
        # Insert Controls
        self.insert_label = tk.Label(self.control_frame, text="Insert Interval (Low, High):")
        self.insert_label.grid(row=0, column=0)
        self.insert_low_entry = tk.Entry(self.control_frame)
        self.insert_low_entry.grid(row=0, column=1)
        self.insert_high_entry = tk.Entry(self.control_frame)
        self.insert_high_entry.grid(row=0, column=2)
        self.insert_button = tk.Button(self.control_frame, text="Insert", command=self.insert_interval)
        self.insert_button.grid(row=0, column=3)

        # Delete Controls
        self.delete_label = tk.Label(self.control_frame, text="Delete Interval (Low, High):")
        self.delete_label.grid(row=1, column=0)
        self.delete_low_entry = tk.Entry(self.control_frame)
        self.delete_low_entry.grid(row=1, column=1)
        self.delete_high_entry = tk.Entry(self.control_frame)
        self.delete_high_entry.grid(row=1, column=2)
        self.delete_button = tk.Button(self.control_frame, text="Delete", command=self.delete_interval)
        self.delete_button.grid(row=1, column=3)
        
        # Search Controls
        self.search_label = tk.Label(self.control_frame, text="Search Interval (Low, High):")
        self.search_label.grid(row=2, column = 0)
        self.search_low_entry = tk.Entry(self.control_frame)
        self.search_low_entry.grid(row = 2, column = 1)
        self.search_high_entry = tk.Entry(self.control_frame)
        self.search_high_entry.grid(row = 2, column = 2)
        self.search_button = tk.Button(self.control_frame, text = "Search", command = self.search_interval)
        self.search_button.grid(row = 2, column = 3)

        # Overlap Search Controls
        self.overlap_label = tk.Label(self.control_frame, text = "Overlap Search (Low, High):")
        self.overlap_label.grid(row = 3, column = 0)
        self.overlap_low_entry = tk.Entry(self.control_frame)
        self.overlap_low_entry.grid(row = 3, column = 1)
        self.overlap_high_entry = tk.Entry(self.control_frame)
        self.overlap_high_entry.grid(row = 3, column = 2)
        self.overlap_button = tk.Button(self.control_frame, text = "Overlap Search", command = self.overlap_search)
        self.overlap_button.grid(row = 3, column = 3)

    def insert_interval(self):
        low_str = self.insert_low_entry.get().strip()
        high_str = self.insert_high_entry.get().strip()
        if not low_str or not high_str:
            messagebox.showerror("Error", "Please enter both low and high values.")
            return
        try:
            low = float(low_str)
            high = float(high_str)
            self.tree.insert(Interval(low, high))
            self.insert_low_entry.delete(0, tk.END)
            self.insert_high_entry.delete(0, tk.END)
            self.draw_tree()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for low and high.")

    def delete_interval(self):
        low_str = self.delete_low_entry.get().strip()
        high_str = self.delete_high_entry.get().strip()
        if not low_str or not high_str:
            messagebox.showerror("Error", "Please enter both low and high values.")
            return
        try:
            low = float(low_str)
            high = float(high_str)
            self.tree.delete(Interval(low, high))
            self.delete_low_entry.delete(0, tk.END)
            self.delete_high_entry.delete(0, tk.END)
            self.draw_tree()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for low and high.")
    
    def search_interval(self):
        low_str = self.search_low_entry.get().strip()
        high_str = self.search_high_entry.get().strip()
        if not low_str or not high_str:
          messagebox.showerror("Error", "Please enter both low and high values.")
          return
        try:
          low = float(low_str)
          high = float(high_str)
          result = self.tree.search(Interval(low,high))
          if result:
            messagebox.showinfo("Search Result", f"Found interval: {result.interval}")
          else:
            messagebox.showinfo("Search Result", "Interval not found.")
        except ValueError:
           messagebox.showerror("Error", "Please enter valid numbers for low and high.")
           
    def overlap_search(self):
        low_str = self.overlap_low_entry.get().strip()
        high_str = self.overlap_high_entry.get().strip()
        if not low_str or not high_str:
            messagebox.showerror("Error", "Please enter both low and high values.")
            return
        try:
          low = float(low_str)
          high = float(high_str)
          result = self.tree.overlap_search(Interval(low, high))
          if result:
              messagebox.showinfo("Overlap Search Result", f"Found overlapping interval: {result.interval}")
          else:
              messagebox.showinfo("Overlap Search Result", "No overlapping interval found.")
        except ValueError:
           messagebox.showerror("Error", "Please enter valid numbers for low and high")

    def draw_tree(self):
        self.canvas.delete("all")
        if self.tree.root:
            self._draw_tree(self.tree.root, 400, 50, 150)

    def _draw_tree(self, node, x, y, x_offset):
        if node.left:
            self.canvas.create_line(x, y, x - x_offset, y + 80)
            self._draw_tree(node.left, x - x_offset, y + 80, x_offset // 2)
        if node.right:
            self.canvas.create_line(x, y, x + x_offset, y + 80)
            self._draw_tree(node.right, x + x_offset, y + 80, x_offset // 2)
        
        label = f"[{node.interval.low}, {node.interval.high}]\nmax={node.max}\nsize={node.size}"
        
        fill_color = "red" if node.color == 'RED' else 'lightblue'
        self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill=fill_color)
        self.canvas.create_text(x, y, text=label)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = IntervalTreeGUI()
    gui.run()