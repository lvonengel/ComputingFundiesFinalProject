import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from BuyPage import BuyPage
from ViewPage import ViewPage
from DairyPage import DairyPage
from ProducePage import ProducePage
from HouseholdPage import HouseholdPage
from SnacksPage import SnacksPage
from BeveragesPage import BeveragesPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shopping Cart Manager")
        self.geometry("500x600")

        # Shared item list
        self.shopping_cart = []

        # Create a container to hold the different pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        # Adds each page to the container
        for F in (HomePage, BuyPage, ViewPage, DairyPage, ProducePage, HouseholdPage, SnacksPage, BeveragesPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start by showing the Home Page
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Bring the frame (page) to the front'''
        frame = self.frames[page_name]
        frame.tkraise()

    def add_to_cart(self, item_name, item_price, image):
        '''Add item to the shopping cart'''
        item = {"name": item_name, "price": item_price, "image": image}
        self.shopping_cart.append(item)
        print(f"Added {item_name} to the cart at price {item_price}.")
        print("Current cart:", self.shopping_cart)
        
        # Update the ViewPage with the new cart contents
        self.frames["ViewPage"].update_cart_display()

    def remove_from_cart(self, item_name, item_price, image):
        '''Add item to the shopping cart'''
        item = {"name": item_name, "price": item_price, "image": image}
        for i in range(len(self.shopping_cart)):
            if self.shopping_cart[i] == item:
                del self.shopping_cart[i]
                break
        print(f"Removed {item_name} from the cart.")
        print("Current cart:", self.shopping_cart)
        
        # Update the ViewPage with the new cart contents
        self.frames["ViewPage"].update_cart_display()

# Home Page
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Shopping Cart Manager", font=("Arial", 24))
        label.pack(pady=20)
        
        # Display a shopping cart image
        try:
            cart_image = Image.open("imgCategories/shoppingcart.png").resize((150, 150)) 
            self.cart_photo = ImageTk.PhotoImage(cart_image)
        except Exception as e:
            print(f"Error loading shopping cart image: {e}")
            self.cart_photo = None

        # Display shopping cart image
        if self.cart_photo:
            cart_label = tk.Label(self, image=self.cart_photo)
            cart_label.pack(pady=10)
        

        # Button to go to Buy Page
        button1 = tk.Button(self, text="Buy Items", 
                            width=20,
                            height=3,
                            command=lambda: controller.show_frame("BuyPage"))
        button1.pack(pady=10)

        # Button to go to View Page
        button3 = tk.Button(self, text="View/Remove Items", 
                            width=20,
                            height=3,
                            command=lambda: controller.show_frame("ViewPage"))
        button3.pack(pady=10)

# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()
