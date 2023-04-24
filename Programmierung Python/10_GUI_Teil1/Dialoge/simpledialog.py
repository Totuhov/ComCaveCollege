import tkinter as tk
from tkinter import  ttk
from tkinter import simpledialog


root = tk.Tk()
root.title("SimpleDialog Demo")
root.resizable(False, False)
root.geometry("300x150")

def eingabe():
    answer = simpledialog.askstring(title="Geben Sie etwas ein", parent=root, prompt="Wie heißen Sie?")
    print(answer)

def zahlEingeben():
    answer = simpledialog.askinteger(title="Geben Sie eine Zahl ein",  parent=root, prompt="Wie alt sind Sie?",minvalue=-300, maxvalue=100)
    print(answer)

def dezimalEingeben():
    answer =  simpledialog.askfloat(title="Geben sie eine Dezimalzahl ein", parent=root, prompt="Was ist ihr Gehalt?",maxvalue=2000.0)
    print(answer)

ttk.Button(root, text="Gebe etwas ein", command=eingabe).pack()
ttk.Button(root, text="Gebe eine ganze Zahl ein", command=zahlEingeben).pack()
ttk.Button(root, text="Gebe eine Dezimalzahl ein", command=dezimalEingeben).pack()

root.mainloop()