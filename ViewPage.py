# ViewPage.py

import tkinter as tk
from PIL import Image, ImageTk

class ViewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="View Items in Cart", font=("Arial", 24))
        label.pack(pady=20)

        # Frame to hold the cart items
        self.cart_frame = tk.Frame(self)
        self.cart_frame.pack(pady=10)

        # Store image references to prevent garbage collection
        self.images = []

        # Button to go back to Home Page
        back_button = tk.Button(self, text="Back to Home", 
                                command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)

    def update_cart_display(self):
        '''Refresh the display of items in the shopping cart'''

        # Clear the cart frame
        for widget in self.cart_frame.winfo_children():
            widget.destroy()

        # Get the current cart
        current_cart = self.controller.shopping_cart
        print("Current cart:", current_cart)

        # Populate the cart frame with updated items
        for i, item in enumerate(current_cart):
            try:
                # Load and resize the image using PIL
                pil_image = Image.open(item["image"]).resize((50, 50))
                image = ImageTk.PhotoImage(pil_image)
                self.images.append(image)  # Prevent garbage collection
            except Exception as e:
                print(f"Could not load image for {item['name']}. Error: {e}")
                image = None

            # Image button for the item
            button = tk.Button(self.cart_frame, image=image, compound="top")
            button.grid(row=(i // 3) * 3 + 1, column=(i % 3), padx=10, pady=10)

            # Item name label below the button
            name_label = tk.Label(self.cart_frame, text=item["name"], font=("Arial", 12))
            name_label.grid(row=(i // 3) * 3 + 2, column=(i % 3), padx=5)

            # Price label below the name
            price_label = tk.Label(self.cart_frame, text=item["price"], font=("Arial", 10))
            price_label.grid(row=(i // 3) * 3 + 3, column=(i % 3), padx=5)
