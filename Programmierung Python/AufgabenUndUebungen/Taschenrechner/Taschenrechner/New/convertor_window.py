import window_class as win
import tkinter as tk


class ConvertorWindow(win.Window):
    def __init__(self):
        super().__init__()
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        modeMenu = tk.Menu(menubar, tearoff=0)
        modeMenu.add_command(label="Calculator", command=lambda: self.change())

        menubar.add_cascade(label="Modes", menu=modeMenu, underline=0)
        super().add_buttons_for_convertor()

    def change(self):
        x = self.winfo_x()
        y = self.winfo_y()
        self.destroy()
        import app
        app.App.switch_to_calculator(app.App, x, y)
