import tkinter as tk
from tkinter import ttk

import sqlite3



class POS:
    def __init__(self, master):
        self.master = master
        master.title("GenTech POS")

        # Connect to SQLite database
        self.conn = sqlite3.connect('products.db')
        self.c = self.conn.cursor()

        # Create products table if it doesn't exist
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')
        self.conn.commit()
        
        # Create product input section
        product_frame = ttk.LabelFrame(master, text="Product Information")
        product_frame.grid(row=0, column=0, padx=10, pady=10)
        
        self.product_label = ttk.Label(product_frame, text="Product:")
        self.product_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.product_entry = ttk.Entry(product_frame, width=30)
        self.product_entry.grid(row=0, column=1, padx=5, pady=5)

        self.price_label = ttk.Label(product_frame, text="Price:")
        self.price_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.price_entry = ttk.Entry(product_frame, width=30)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        self.quantity_label = ttk.Label(product_frame, text="Quantity:")
        self.quantity_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.quantity_entry = ttk.Entry(product_frame, width=30)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create buttons section
        button_frame = ttk.Frame(master)
        button_frame.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.add_button = ttk.Button(button_frame, text="Create Product", command=self.add_product)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = ttk.Button(button_frame, text="Add to Cart", command=self.add_to_cart)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        # Create cart section
        cart_frame = ttk.LabelFrame(master, text="Shopping Cart")
        cart_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)

        self.cart_listbox = tk.Listbox(cart_frame, height=10, width=40)
        self.cart_listbox.grid(row=0, column=0, padx=5, pady=5)

        self.total_label = ttk.Label(cart_frame, text="Total:")
        self.total_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.total_amount_label = ttk.Label(cart_frame, text="$0.00")
        self.total_amount_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

        self.checkout_button = ttk.Button(cart_frame, text="Checkout", command=self.checkout)
        self.checkout_button.grid(row=2, column=0, padx=5, pady=5)
        
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

    def add_product(self):
        # Get product info from input fields
        name = self.product_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())

        # Add product to database
        self.c.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
        self.conn.commit()

        # Clear input fields
        self.product_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

root = tk.Tk()
pos = POS(root)
root.mainloop()
