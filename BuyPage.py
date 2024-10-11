import tkinter as tk

class BuyPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Label for the page
        label = tk.Label(self, text="Buy Items in Cart", font=("Arial", 24))
        label.pack(pady=20)

        # New text field to input the name of an item to buy
        self.item_entry = tk.Entry(self)
        self.item_entry.pack(pady=10)

        # Button to "buy" the item (store it in a shared list)
        buy_button = tk.Button(self, text="Buy Item", command=self.buy_item)
        buy_button.pack(pady=10)

        # Button to go back to Home Page
        back_button = tk.Button(self, text="Back to Home", 
                                command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)

    def buy_item(self):
        # Get the item from the entry field
        item = self.item_entry.get()

        # Add the item to a shared list (in the controller)
        if item:
            self.controller.item_list.append(item)
            print(f"Bought item: {item}")
            self.item_entry.delete(0, tk.END)  # Clear the entry field
