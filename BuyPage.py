"""
This file creates the BuyPage class.
This page lets the users select which category 
they want to buy items from
"""

import tkinter as tk
from PIL import Image
from PIL import ImageTk

# page where users can choose item categories
class BuyPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # title label for the page
        label = tk.Label(self, 
                         text="Select a Category", 
                         font=("Arial", 24))
        label.grid(row=0, column=0, columnspan=2, pady=20)

        # categories with their display name, target page, and image path
        categories = [
            ("Dairy", "DairyPage", "imgCategories/dairy.png"),
            ("Produce", "ProducePage", "imgCategories/produce.jpg"),
            ("Household", "HouseholdPage", "imgCategories/household.jpg"),
            ("Snacks", "SnacksPage", "imgCategories/pantry.png"),
            ("Beverages", "BeveragesPage", "imgCategories/beverages.jpg")
        ]

        # list to store image references to prevent garbage collection
        self.images = []

        # create buttons for each category
        for i, (category_name, page_name, image_path) in enumerate(categories):
            try:
                # open, resize, and convert the image with Pillow
                pil_image = Image.open(image_path).resize(
                    (100, 100))  # Resize to 100x100 pixels
                image = ImageTk.PhotoImage(pil_image)
                # keeps reference of images
                self.images.append(image) 
            except Exception as e:
                # handle cases where the image cannot be loaded
                print(f"Could not load image at {image_path}. Error: {e}")
                image = None

            # create button with image and category name
            button = tk.Button(self, 
                               text=category_name, 
                               image=image, compound="top",
                               command=lambda page=page_name: 
                               controller.show_frame(page))
            button.grid(row=(i // 2) + 1, column=i %
                        2, padx=10, pady=10, sticky="ew")

        # back button to return to Home Page
        back_button = tk.Button(self, text="Back to Home",
                                command=lambda: 
                                controller.show_frame("HomePage"))
        back_button.grid(row=4, column=0, columnspan=2, pady=20)
