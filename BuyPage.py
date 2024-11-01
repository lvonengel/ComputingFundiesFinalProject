import tkinter as tk
from PIL import Image, ImageTk

class BuyPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Label for the page title
        label = tk.Label(self, text="Select a Category", font=("Arial", 24))
        label.grid(row=0, column=0, columnspan=2, pady=20)

        # List of category names, associated page names, and image paths
        categories = [
            ("Dairy", "DairyPage", "imgCategories/dairy.png"),
            ("Produce", "ProducePage", "imgCategories/produce.jpg"),
            ("Household", "HouseholdPage", "imgCategories/household.jpg"),
            ("Snacks", "SnacksPage", "imgCategories/pantry.png"),
            ("Beverages", "BeveragesPage", "imgCategories/beverages.jpg")
        ]

        # Store image references to prevent garbage collection
        self.images = []

        # Load and resize images, then create buttons in a grid
        for i, (category_name, page_name, image_path) in enumerate(categories):
            try:
                # Open, resize, and convert the image with Pillow
                pil_image = Image.open(image_path).resize((100, 100))  # Resize to 100x100 pixels
                image = ImageTk.PhotoImage(pil_image)
                self.images.append(image)  # Prevent garbage collection
            except Exception as e:
                print(f"Could not load image at {image_path}. Error: {e}")
                image = None

            # Create button with resized image
            button = tk.Button(self, text=category_name, image=image, compound="top",
                               command=lambda page=page_name: controller.show_frame(page))
            button.grid(row=(i // 2) + 1, column=i % 2, padx=10, pady=10, sticky="ew")

        # Back button to return to Home Page
        back_button = tk.Button(self, text="Back to Home", 
                                command=lambda: controller.show_frame("HomePage"))
        back_button.grid(row=4, column=0, columnspan=2, pady=20)
