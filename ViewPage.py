import tkinter as tk

class ViewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="View Items in Cart", font=("Arial", 24))
        label.pack(pady=20)

        # Button to go back to Home Page
        back_button = tk.Button(self, text="Back to Home", 
                                command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)
