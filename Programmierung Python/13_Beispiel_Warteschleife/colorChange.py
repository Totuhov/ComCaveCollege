import tkinter as tk
from tkinter import ttk
import time

class ColorCange(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Color Change Demo")
        self.geometry("300x100")

        self.style = ttk.Style()

        self.button = ttk.Button(self, text="Warte 5 Sekunden...", command=self.buttonClicked)
        self.button.pack(expand=True, ipadx=10, ipady=5)

    def buttonClicked(self):
        self.changeColor("red")
        #time.sleep(5) #Lässt das ganze Programm für 5 Sekunden schlafen
        #self.changeColor("black")
        self.after(5000, lambda: self.changeColor("black"))


    def changeColor(self, color):
        self.style.configure("TButton", foreground=color)


if __name__ == "__main__":
    app = ColorCange()
    app.mainloop()