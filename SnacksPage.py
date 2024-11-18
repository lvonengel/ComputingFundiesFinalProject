"""
This file creates the SnacksPage class
SnacksPage allows users to view and add 
snacks to their shopping cart
"""

import tkinter as tk
from PIL import Image
from PIL import ImageTk

# page where users can browse and add snacks to their cart.
class SnacksPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # title label for the page
        label = tk.Label(self, 
                         text="Snacks Items", 
                         font=("Arial", 24))
        label.grid(row=0, column=0, columnspan=3, pady=20)

        # list of snacks with their name, price, and image path
        snack_items = [
            {"name": "4 Pack of Chips", "price": "$3.00",
                "image": "imgSnacks/chips.jpg"},
            {"name": "Popcorn", "price": "$3.25",
                "image": "imgSnacks/popcorn.jpg"},
            {"name": "Nuts", "price": "$7.50", "image": "imgSnacks/nuts.jpg"},
            {"name": "Crackers", "price": "$3.50",
                "image": "imgSnacks/crackers.jpg"},
            {"name": "Pack of Cookies", "price": "$4.00",
                "image": "imgSnacks/cookies.png"},
            {"name": "Bar of Chocolate", "price": "$2.75",
                "image": "imgSnacks/chocolate.jpg"}
        ]

        # store image references to prevent garbage collection
        self.images = []

        # create grid layout for snacks
        for i, item in enumerate(snack_items):
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
            name_label.grid(row=(i // 3) * 3 + 2, 
                            column=(i % 3), 
                            padx=5)

            # price label below the name
            price_label = tk.Label(self, 
                                   text=item["price"], 
                                   font=("Arial", 10))
            price_label.grid(row=(i // 3) * 3 + 3, 
                             column=(i % 3), 
                             padx=5)

        # back button to return to Buy Page
        back_button = tk.Button(self, 
                                text="Back to Buy Page",
                                command=lambda: 
                                controller.show_frame("BuyPage"))
        back_button.grid(row=(len(snack_items) // 3) * 3 +
                         4, column=0, 
                         columnspan=3, 
                         pady=20)
    # sends message to terminal when an item is added to the cart
    def add_to_cart(self, item_name):
        print(f"Added {item_name} to cart.")
