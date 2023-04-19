import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.resizable(False, False)
window.geometry("500x300")

langs = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')

auswahl = tk.Variable(value=langs)

listenbox = tk.Listbox(window, listvariable=auswahl, height=10, selectmode=tk.MULTIPLE)
listenbox.pack()

def zeigeWerte():
    print(auswahl.get())
    print(listenbox.curselection())
    print(listenbox.selection_get())

button = ttk.Button(window, text="Zeige Werte", command=zeigeWerte)
button.pack()

window.mainloop()