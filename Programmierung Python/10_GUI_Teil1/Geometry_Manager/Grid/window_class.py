import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Demo Fenster")
        self.geometry("350x200")