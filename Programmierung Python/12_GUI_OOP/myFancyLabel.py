from tkinter import ttk

class MyFancyLabel(ttk.Label):
    def __init__(self, container, text):
        super().__init__(container, text=text)

        self.configure(background="red", foreground="white", font=("Arial", 20))