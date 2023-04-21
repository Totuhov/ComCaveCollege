from window_class import Window
import tkinter as tk
from constant_class import Constant


class CalculatorWindow(Window):

    def __init__(self):
        super().__init__()
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        modeMenu = tk.Menu(menubar, tearoff=0)
        modeMenu.add_command(label="Binar Convertor",
                             command=lambda: self.change())

        menubar.add_cascade(label="Modes", menu=modeMenu, underline=0)
        super().add_buttons_for_calculator()

    def change(self):
        x = self.winfo_x()
        y = self.winfo_y()
        self.destroy()
        import app
        app.App.switch_to_convertor(app.App, x, y)

    def command_on_click(self):
        super().command_on_click()
