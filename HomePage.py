import tkinter as tk
from BuyPage import BuyPage
from RemovePage import RemovePage
from ViewPage import ViewPage
from DairyPage import DairyPage  # Import DairyPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shopping Cart Manager")
        self.geometry("400x300")

        # Shared item list
        self.item_list = []

        # Create a container to hold the different pages
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        # Adds each page (HomePage, BuyPage, RemovePage, ViewPage, DairyPage) to the container
        for F in (HomePage, BuyPage, RemovePage, ViewPage, DairyPage):
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

# Home Page
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Home Page", font=("Arial", 24))
        label.pack(pady=20)

        # Button to go to Buy Page
        button1 = tk.Button(self, text="Go to Buy Page", 
                            command=lambda: controller.show_frame("BuyPage"))
        button1.pack(pady=10)

        # Button to go to Remove Page
        button2 = tk.Button(self, text="Go to Remove Page", 
                            command=lambda: controller.show_frame("RemovePage"))
        button2.pack(pady=10)

        # Button to go to View Page
        button3 = tk.Button(self, text="Go to View Page", 
                            command=lambda: controller.show_frame("ViewPage"))
        button3.pack(pady=10)

# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()
