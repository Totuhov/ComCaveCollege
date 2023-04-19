import tkinter as tk
from tkinter import ttk
import window_class

window = window_class.Window()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=3)

#window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=3)
#window.rowconfigure(2, weight=1)
#window.rowconfigure(3, weight=1)

boxEins = ttk.Label(window, text="Eins", background="green")
boxZwei = ttk.Label(window, text="Zwei", background="red")
boxDrei = ttk.Label(window, text="Drei", background="blue")
boxVier = ttk.Label(window, text="Vier", background="black", foreground="white")
boxFuenf = ttk.Label(window, text="Fünf", background="green")
boxSechs = ttk.Label(window, text="Sechs", background="red")
boxSieben = ttk.Label(window, text="Sieben", background="green")
boxAcht = ttk.Label(window, text="Acht", background="red")
boxNeun = ttk.Label(window, text="Neun", background="blue")

boxEins.grid(column=0, row=0, sticky="NSEW")
boxZwei.grid(column=1, row=0, sticky="NSEW")
boxDrei.grid(column=2, row=0, sticky="NSEW")
boxVier.grid(column=0, row=1, columnspan=3, sticky="NSEW")
boxFuenf.grid(column=0, row=2, rowspan=2, sticky="NSEW")
boxSechs.grid(column=1, row=2, sticky="NSEW",ipadx=5,ipady=5)
boxSieben.grid(column=2, row=2, sticky="NSEW")
boxAcht.grid(column=1, row=3, sticky="NSEW")
#boxNeun.grid(column=2,row=3, sticky="NSEW")

window.mainloop()