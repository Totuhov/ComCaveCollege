import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Taschenrechner")
        screen_width = self.winfo_screenwidth()
        screen_heigth = self.winfo_screenheight()
        center_x = int(screen_width / 2 - 340 / 2)
        center_y = int(screen_heigth / 2 - 480 / 2)
        self.geometry(f"340x480+{center_x}+{center_y}")
        self.minsize(width=340, height=480)