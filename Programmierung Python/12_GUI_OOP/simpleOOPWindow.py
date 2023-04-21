import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import myFancyLabel as mfl

# tk.Tk() - Fenster als eigene Klasse
class SimpleOopWindw(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("OOP Window Demo")
        self.geometry("300x50")

        self.label = ttk.Label(self, text="Hallo Welt")
        self.label.pack()

        self.fancyLabel = mfl.MyFancyLabel(self, text="Mein eigenes Label")
        self.fancyLabel.pack()

        self.button = ttk.Button(self, text="Klick mich!", command=self.buttonClicked)
        self.button.pack()

    
    def buttonClicked(self):
        showinfo(title="Information", message="Der Button wurde geklickt.")