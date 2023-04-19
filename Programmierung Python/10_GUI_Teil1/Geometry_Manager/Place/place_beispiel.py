import tkinter as tk
import window_class
from tkinter import ttk

window = window_class.Window()

boxEins = ttk.Label(window, text="Box Eins - Absolut", background="#2ad8b3")
boxZwei = ttk.Label(window, text="Box Zwei - Relativ", background="#0000ff")

boxEins.place(x=20, y=10, width=150, height=75)
boxZwei.place(relx=0.8, rely=0.2, relwidth=0.5, anchor="ne")

window.mainloop()