"""
This file creates the DairyPage class
DairyPage allows users to view and add 
dairy items to their shopping cart
"""

import tkinter as tk
from PIL import Image
from PIL import ImageTk

# page where users can browse and add dairy items to their cart.
class DairyPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # title label for the page
        label = tk.Label(self, 
                         text="Dairy Items", 
                         font=("Arial", 24))
        label.grid(row=0, column=0, columnspan=3, pady=20)

        # list of dairy items with their name, price, and image path
        dairy_items = [
            {"name": "16oz Milk", "price": "$3.50",
                "image": "imgDairy/milk.jpg"},
            {"name": "Cheese", "price": "$7.00", 
                "image": "imgDairy/cheese.png"},
            {"name": "4 pack of Yogurt", "price": "$3.00",
                "image": "imgDairy/yogurt.jpg"},
            {"name": "Butter", "price": "$5.00", 
                "image": "imgDairy/butter.jpg"},
            {"name": "Whipped Cream", "price": "$3.00",
                "image": "imgDairy/cream.jpg"},
            {"name": "Cottage Cheese", "price": "$3.75",
                "image": "imgDairy/cottagecheese.png"}
        ]

        # store image references to prevent garbage collection
        self.images = []

        # create grid layout for dairy items
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
            button = tk.Button(self, image=image, compound="top",
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
        back_button = tk.Button(self, text="Back to Buy Page",
                                command=lambda: 
                                controller.show_frame("BuyPage"))
        back_button.grid(row=(len(dairy_items) // 3) * 3 +
                         4, column=0, columnspan=3, pady=20)

    # sends message to terminal when an item is added to the cart
    def add_to_cart(self, item_name):
        print(f"Added {item_name} to cart.")
