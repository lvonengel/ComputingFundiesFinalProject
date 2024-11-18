"""
This file creates the BeveragesPage class
BeveragesPage allows users to view and add 
beverage items to their shopping cart
"""

import tkinter as tk
from PIL import Image
from PIL import ImageTk


# page where users can browse and add beverages to their cart.
class BeveragesPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # title label for the page
        label = tk.Label(self, 
                         text="Beverages Items", 
                         font=("Arial", 24))
        label.grid(row=0, column=0, columnspan=3, pady=20)

        # list of beverage items with their name, price, and image path
        dairy_items = [
            {"name": "8 Pack of Water", "price": "$2.00",
                "image": "imgBeverages/water.jpg"},
            {"name": "8 Pack of Coke", "price": "$3.50",
                "image": "imgBeverages/coke.png"},
            {"name": "Milkshake", "price": "$2.50",
                "image": "imgBeverages/milkshake.jpg"},
            {"name": "16oz Orange Juice", "price": "$4.00",
                "image": "imgBeverages/orangejuice.jpg"},
            {"name": "16oz Lemonade", "price": "$3.50",
                "image": "imgBeverages/lemonade.jpg"},
            {"name": "16oz Apple Cider", "price": "$3.75",
                "image": "imgBeverages/applecider.jpg"}
        ]

        # store image references to prevent garbage collection
        self.images = []

        # create grid layout for beverage items
        for i, item in enumerate(dairy_items):
            try:
                # load and resize the image using PIL
                pil_image = Image.open(item["image"]).resize((100, 100))
                image = ImageTk.PhotoImage(pil_image)
                self.images.append(image)  # Prevent garbage collection
            except Exception as e:
                # handle image load errors gracefully
                print(f"Could not load image for {item['name']}. Error: {e}")
                image = None

            # create a button with the image only (no text in button)
            button = tk.Button(self, 
                               image=image, 
                               compound="top",
                               command=lambda name=item["name"], 
                               price=item["price"], 
                               image=item["image"]:
                               controller.add_to_cart(name, price, image))
            button.grid(row=(i // 3) * 3 + 1, 
                        column=(i % 3), 
                        padx=10, pady=10)

            # item name label below the button
            name_label = tk.Label(self, 
                                  text=item["name"], 
                                  font=("Arial", 12))
            name_label.grid(row=(i // 3) * 3 + 2, column=(i % 3), padx=5)

            # price label below the name
            price_label = tk.Label(
                self, text=item["price"], font=("Arial", 10))
            price_label.grid(row=(i // 3) * 3 + 3, column=(i % 3), padx=5)

        # back button to return to Buy Page
        back_button = tk.Button(self, text="Back to Buy Page",
                                command=lambda: 
                                controller.show_frame("BuyPage"))
        back_button.grid(row=(len(dairy_items) // 3) * 3 +
                         4, column=0, columnspan=3, pady=20)

    # sends message to terminal when an item is added to the cart
    def add_to_cart(self, item_name):
        print(f"Added {item_name} to cart.")
