"""
This file creates the ViewPage class.
ViewPage lets users see items in their 
shopping cart and remove them if wanted
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


# page where users can view and manage their shopping cart
class ViewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # title label for the page
        label = tk.Label(self, 
                         text="View Items in Cart", 
                         font=("Arial", 24))
        label.pack(pady=10)

        # canvas and scrollbar to display the list of items
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview)
        
        # frame inside the canvas to hold the item widgets
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all"))
        )

        # add the scrollable frame to the canvas
        self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # store image references
        self.images = []

        # try to load the "remove item" icon
        try:
            self.x_image = Image.open(
                "imgCategories/x_mark.png").resize((20, 20))
            self.x_photo = ImageTk.PhotoImage(self.x_image)
        except Exception as e:
            print(f"Error x_mark image: {e}")
            self.x_photo = None

        # make total and quantity counter
        self.quantity = 0
        self.total = 0
        self.total_label = tk.Label(
            self, text="Quantity: ", font=("Arial", 10))
        self.total_label.pack(pady=5)
        self.quantity_label = tk.Label(
            self, text="Total: $", font=("Arial", 10))
        self.quantity_label.pack(pady=10)

        # back button to go back to Home Page
        back_button = tk.Button(self, text="Back to Home",
                                command=lambda: 
                                controller.show_frame("HomePage"))
        back_button.pack(pady=10)

    # refreshes display of items in the shopping cart
    def update_cart_display(self):

        # clears current display of the cart
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # resets quantity and total price
        self.quantity = 0
        self.total = 0

        # gets the current cart
        current_cart = self.controller.shopping_cart

        # loops through the cart frame to add updated items
        for i, item in enumerate(current_cart):
            try:
                # load and resize the image using PIL
                pil_image = Image.open(item["image"]).resize((50, 50))
                image = ImageTk.PhotoImage(pil_image)
                self.images.append(image)
                self.total += round(float(item["price"][1:]), 2)
                self.quantity += 1
            # handle cases where image can't load
            except Exception as e:
                print(f"Could not load image for {item['name']}. Error: {e}")
                image = None

            # image button for the item
            button = tk.Button(self.scrollable_frame,
                               image=image, compound="top")
            button.grid(row=(i // 3) * 4 + 1, 
                        column=(i % 3), 
                        padx=10, pady=10)

            # item name label below the button
            name_label = tk.Label(self.scrollable_frame,
                                  text=item["name"], 
                                  font=("Arial", 9))
            name_label.grid(row=(i // 3) * 4 + 2, 
                            column=(i % 3), 
                            padx=5)

            # price label below the name
            price_label = tk.Label(self.scrollable_frame,
                                   text=item["price"], 
                                   font=("Arial", 7))
            price_label.grid(row=(i // 3) * 4 + 3, 
                             column=(i % 3), 
                             padx=5)

            # button to remove item
            remove_button = tk.Button(self.scrollable_frame, 
                                      image=self.x_photo, 
                                      compound="top",
                                      command=lambda name=item["name"], 
                                      price=item["price"], 
                                      image=item["image"]:
                                      self.controller.remove_from_cart(name, price, image))
            remove_button.grid(row=(i // 3) * 4 + 4,
                               column=(i % 3), 
                               padx=10, pady=10)

        self.quantity_label.config(text="Quantity: " + str(self.quantity))
        self.total_label.config(text="Total: $" + "{:.2f}".format(self.total))

        print("Total:", self.total)
        print("Quantity:", self.quantity)
