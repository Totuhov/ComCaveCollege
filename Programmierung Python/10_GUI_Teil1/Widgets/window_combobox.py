import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.resizable(False, False)
window.geometry("500x300")

auswahl = tk.StringVar()

monatsAuswahl = ttk.Combobox(window, textvariable=auswahl)
monatsAuswahl.pack()

monatsAuswahl['values'] = ("Januar", "Februar", "März", "April", "Mai")
monatsAuswahl['state'] = "readonly"
monatsAuswahl.set("Januar")

window.mainloop()