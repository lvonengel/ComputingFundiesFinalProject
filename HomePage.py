"""
This file creates the main App class and HomePage.
The App class manages navigation between pages, 
while HomePage is the starting point for users
"""

import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image
from PIL import ImageTk
from BuyPage import BuyPage
from ViewPage import ViewPage
from DairyPage import DairyPage
from ProducePage import ProducePage
from HouseholdPage import HouseholdPage
from SnacksPage import SnacksPage
from BeveragesPage import BeveragesPage


# main application class for Shopping Cart Manager.
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shopping Cart Manager")
        self.geometry("500x600")

        # shared item list
        self.shopping_cart = []

        # create a container to hold the different pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        # adds each page to the container
        for F in (HomePage, BuyPage, ViewPage, DairyPage, ProducePage,
                  HouseholdPage, SnacksPage, BeveragesPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # start by showing the Home Page
        self.show_frame("HomePage")

    
    
    # bring a specified page to the front for the user to see
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    
    # adds an item to the shopping cart and refreshes the ViewPage display
    def add_to_cart(self, item_name, item_price, image):
        # adds item name, price, and image to shopping cart
        item = {"name": item_name,
                "price": item_price,
                "image": image}
        self.shopping_cart.append(item)
        print(f"Added {item_name} to the cart at price {item_price}.")
        print("Current cart:", self.shopping_cart)

        # update the ViewPage with the new cart contents
        self.frames["ViewPage"].update_cart_display()


    # remove an item from the shopping cart and refresh the ViewPage display
    def remove_from_cart(self, item_name, item_price, image):
        '''Add item to the shopping cart'''
        item = {"name": item_name, 
                "price": item_price, 
                "image": image}
        for i in range(len(self.shopping_cart)):
            if self.shopping_cart[i] == item:
                del self.shopping_cart[i]
                break
        print(f"Removed {item_name} from the cart.")
        print("Current cart:", self.shopping_cart)

        # update the ViewPage with the new cart contents
        self.frames["ViewPage"].update_cart_display()


# home page and where the user starts in
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # title label for the page
        label = tk.Label(self,
                         text="Shopping Cart Manager",
                         font=("Arial", 24))
        label.pack(pady=20)

        # displays a shopping cart image
        try:
            cart_image = Image.open(
                "imgCategories/shoppingcart.png").resize((150, 150))
            self.cart_photo = ImageTk.PhotoImage(cart_image)
        except Exception as e:
            print(f"Error loading shopping cart image: {e}")
            self.cart_photo = None

        # if image loads succesfully, then show it
        if self.cart_photo:
            cart_label = tk.Label(self, image=self.cart_photo)
            cart_label.pack(pady=10)

        # button to go to Buy Page
        button1 = tk.Button(self, text="Buy Items",
                            width=20,
                            height=3,
                            command=lambda:
                            controller.show_frame("BuyPage"))
        button1.pack(pady=10)

        # button to go to View Page
        button3 = tk.Button(self, text="View/Remove Items",
                            width=20,
                            height=3,
                            command=lambda:
                            controller.show_frame("ViewPage"))
        button3.pack(pady=10)


# runs application
if __name__ == "__main__":
    app = App()
    app.mainloop()
