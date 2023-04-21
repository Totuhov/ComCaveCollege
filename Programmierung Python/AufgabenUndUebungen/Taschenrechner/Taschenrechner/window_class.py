import tkinter as tk
import os
from tkinter import Menu


# 1.1 Get the path to the directory containing the script
dir_path = os.path.dirname(os.path.realpath(__file__))

# 1.2 Set the path to the file in the same directory
file_path = os.path.join(dir_path, "icon.ico")


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Taschenrechner v1.0")
        screen_width = self.winfo_screenwidth()
        screen_heigth = self.winfo_screenheight()
        center_x = int(screen_width / 2 - 330 / 2)
        center_y = int(screen_heigth / 2 - 450 / 2)
        self.geometry(f"330x450+{center_x}+{center_y}")
        self.resizable(False, False)
        self.iconbitmap(file_path)  # 1.3 insert the path to the file as string
        self.configure(background="white")

        menubar = Menu(self)
        self.config(menu=menubar)

        modeMenu = Menu(menubar, tearoff=0)
        modeMenu.add_command(label="Binar Convertor")

        menubar.add_cascade(label="Modes", menu=modeMenu, underline=0)

        

