import tkinter as tk
from PIL import Image
from PIL import ImageTk


class ProducePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, 
                         text="Produce Items", 
                         font=("Arial", 24))
        label.grid(row=0, column=0, columnspan=3, pady=20)

        # List of dairy items with name, price, and image path
        dairy_items = [
            {"name": "Apple", "price": "$0.75", 
                "image": "imgProduce/apple.png"},
            {"name": "Banana", "price": "$0.60", 
                "image": "imgProduce/banana.png"},
            {"name": "Cauliflower", "price": "$2.50",
                "image": "imgProduce/cauliflower.jpg"},
            {"name": "Pack of Green Beans", "price": "$2.50",
                "image": "imgProduce/greenbeans.jpg"},
            {"name": "Pear", "price": "$1.25", 
                "image": "imgProduce/pear.png"},
            {"name": "3 Pack Peppers", "price": "$4.00",
                "image": "imgProduce/peppers.jpg"}
        ]

        # Store image references to prevent garbage collection
        self.images = []

        # Create grid layout for dairy items
        for i, item in enumerate(dairy_items):
            try:
                # Load and resize the image using PIL
                pil_image = Image.open(
                    item["image"]).resize((100, 100))
                image = ImageTk.PhotoImage(pil_image)
                self.images.append(image) 
            except Exception as e:
                print(f"Could not load image for 
                      {item['name']}. Error: {e}")
                image = None

            # Create a button with the image only (no text in button)
            button = tk.Button(self, image=image, 
                               compound="top",
                               command=lambda name=item["name"], 
                               price=item["price"],
                               image=item["image"]:
                               controller.add_to_cart(name, price, image))
            button.grid(row=(i // 3) * 3 + 1, 
                        column=(i % 3), 
                        padx=10, pady=10)

            # Item name label below the button
            name_label = tk.Label(self, 
                                  text=item["name"], 
                                  font=("Arial", 12))
            name_label.grid(row=(i // 3) * 3 + 2, 
                            column=(i % 3), 
                            padx=5)

            # Price label below the name
            price_label = tk.Label(
                self, text=item["price"], 
                font=("Arial", 10))
            price_label.grid(row=(i // 3) * 3 + 3, 
                             column=(i % 3), 
                             padx=5)

        # Back button to return to Buy Page
        back_button = tk.Button(self, 
                                text="Back to Buy Page",
                                command=lambda: 
                                controller.show_frame("BuyPage"))
        back_button.grid(row=(len(dairy_items) // 3) * 3 +
                         4, column=0, columnspan=3, pady=20)

    def add_to_cart(self, item_name):
        print(f"Added {item_name} to cart.")
