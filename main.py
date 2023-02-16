import tkinter as tk
from tkinter import ttk

import sqlite3


class POS:
    def __init__(self, master):
        self.master = master
        master.title("Simple POS")
        
        # Create labels, entry fields, and buttons for the UI
        self.product_label = ttk.Label(master, text="Product:")
        self.product_label.grid(row=0, column=0, padx=5, pady=5)
        self.product_entry = ttk.Entry(master)
        self.product_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.quantity_label = ttk.Label(master, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, padx=5, pady=5)
        self.quantity_entry = ttk.Entry(master)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.add_button = ttk.Button(master, text="Add to Cart", command=self.add_to_cart)
        self.add_button.grid(row=2, column=1, padx=5, pady=5)
        
        self.cart_label = ttk.Label(master, text="Shopping Cart:")
        self.cart_label.grid(row=3, column=0, padx=5, pady=5)
        self.cart_listbox = tk.Listbox(master)
        self.cart_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        self.total_label = ttk.Label(master, text="Total:")
        self.total_label.grid(row=5, column=0, padx=5, pady=5)
        self.total_amount_label = ttk.Label(master, text="$0.00")
        self.total_amount_label.grid(row=5, column=1, padx=5, pady=5)
        
        self.checkout_button = ttk.Button(master, text="Checkout", command=self.checkout)
        self.checkout_button.grid(row=6, column=1, padx=5, pady=5)
        
        # Initialize cart and total amount
        self.cart = []
        self.total_amount = 0.0
        
    def add_to_cart(self):
        # Get product and quantity from input fields
        product = self.product_entry.get()
        quantity = int(self.quantity_entry.get())
        
        # Add item to cart and update total amount
        self.cart.append((product, quantity))
        self.total_amount += quantity * 10.0
        
        # Update cart and total amount display
        self.cart_listbox.insert(tk.END, f"{product} x {quantity}")
        self.total_amount_label.config(text=f"${self.total_amount:.2f}")
        
        # Clear input fields
        self.product_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        
    def checkout(self):
        # Generate receipt and clear cart and total amount
        receipt = "Receipt:\n\n"
        for item in self.cart:
            receipt += f"{item[0]} x {item[1]} = ${item[1] * 10.0:.2f}\n"
        receipt += f"\nTotal Amount: ${self.total_amount:.2f}"
        tk.messagebox.showinfo("Checkout", receipt)
        self.cart = []
        self.total_amount = 0.0
        self.cart_listbox.delete(0, tk.END)
        self.total_amount_label.config(text="$0.00")

root = tk.Tk()
pos = POS(root)
root.mainloop()
