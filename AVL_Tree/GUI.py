import tkinter as tk
from tkinter import messagebox
from math import cos, sin, radians
from AVLTree import AVLTree, AVLNode


class AVLTreeGUI:
    def __init__(self):
        self.tree = AVLTree()
        self.tree.root = None
        self.window = tk.Tk()
        self.window.title("AVL Tree GUI")
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="white")
        self.canvas.pack()

        # Input controls
        self.control_frame = tk.Frame(self.window)
        self.control_frame.pack()
        
        # Insert Controls
        self.insert_label = tk.Label(self.control_frame, text="Insert Key:")
        self.insert_label.grid(row=0, column=0)
        self.insert_entry = tk.Entry(self.control_frame)
        self.insert_entry.grid(row=0, column=1)
        self.insert_button = tk.Button(self.control_frame, text="Insert", command=self.insert_key)
        self.insert_button.grid(row=0, column=2)

        # Delete Controls
        self.delete_label = tk.Label(self.control_frame, text="Delete Key:")
        self.delete_label.grid(row=1, column=0)
        self.delete_entry = tk.Entry(self.control_frame)
        self.delete_entry.grid(row=1, column=1)
        self.delete_button = tk.Button(self.control_frame, text="Delete", command=self.delete_key)
        self.delete_button.grid(row=1, column=2)

        # Method Selection
        self.method_frame = tk.Frame(self.window)
        self.method_frame.pack()
        self.method_label = tk.Label(self.method_frame, text="Select Method:")
        self.method_label.grid(row=0, column=0)

        self.method_var = tk.StringVar(value="recursive")
        self.recursive_radio = tk.Radiobutton(self.method_frame, text="Recursive", variable=self.method_var, value="recursive")
        self.recursive_radio.grid(row=0, column=1)
        self.iterative_radio = tk.Radiobutton(self.method_frame, text="Iterative", variable=self.method_var, value="iterative")
        self.iterative_radio.grid(row=0, column=2)

    def insert_key(self):
        key_str = self.insert_entry.get().strip()  # Get and strip any extra spaces
        if not key_str:  # Check if the input is empty
            messagebox.showerror("Error", "Please enter a key.")
            return
        try:
            key = float(self.insert_entry.get())
            method = self.method_var.get()
            if method == "recursive":
                self.tree.root = self.tree.insert_recursive(self.tree.root, key)
            else:
                self.tree.root = self.tree.insert_iterative(self.tree.root, key)
            self.insert_entry.delete(0, tk.END)
            self.draw_tree()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def delete_key(self):
        key_str = self.delete_entry.get().strip()  # Get and strip any extra spaces
        if not key_str:  # Check if the input is empty
            messagebox.showerror("Error", "Please enter a key.")
            return
        try:
            key = float(self.delete_entry.get())
            method = self.method_var.get()
            if method == "recursive":
                self.tree.root = self.tree.delete_recursive(self.tree.root, key)
            else:
                self.tree.root = self.tree.delete_iterative(self.tree.root, key)
            self.delete_entry.delete(0, tk.END)
            self.draw_tree()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def draw_tree(self):
        self.canvas.delete("all")
        if self.tree.root:
            self._draw_tree(self.tree.root, 400, 50, 200)

    def _draw_tree(self, node, x, y, x_offset):
        if node.left:
            self.canvas.create_line(x, y, x - x_offset, y + 60)
            self._draw_tree(node.left, x - x_offset, y + 60, x_offset // 2)
        if node.right:
            self.canvas.create_line(x, y, x + x_offset, y + 60)
            self._draw_tree(node.right, x + x_offset, y + 60, x_offset // 2)
        self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="lightblue")
        self.canvas.create_text(x, y, text=str(node.key))

    def run(self):
        self.window.mainloop()
