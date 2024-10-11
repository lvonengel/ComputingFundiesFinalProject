import tkinter as tk

class RemovePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Remove Items from Cart", font=("Arial", 24))
        label.pack(pady=20)

        # Button to go back to Home Page
        back_button = tk.Button(self, text="Back to Home", 
                                command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=10)
