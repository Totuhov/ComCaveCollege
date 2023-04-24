import tkinter as tk
from tkinter import ttk
import time

class practicalExample(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Praktisches Beispiel")
        self.resizable(False,False)
        self.geometry("600x80")
        self['bg'] = "black"
        self.configure(background="black")

        # Windows - Entfernen der minimieren/maximieren Buttons
        self.attributes("-toolwindow", True)

        self.style = ttk.Style(self)
        self.style.configure("TLabel", background="black", foreground="red")

        self.label = ttk.Label(self, text=self.timeString(), font=("Arial", 40))
        self.label.pack(expand=True)

        self.label.after(1000, self.update)


    def timeString(self):
        return time.strftime("%d.%m.%Y - %H:%M:%S") # strftime gibt die aktuelle Zeit in einem angegebenen Format.
    
    def update(self):
        self.label.configure(text=self.timeString())
        self.label.after(1000, self.update)


if __name__ == "__main__":
    app = practicalExample()
    app.mainloop()