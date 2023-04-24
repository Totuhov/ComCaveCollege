import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

root = tk.Tk()
root.title('Tkinter Color Chooser')
root.geometry('300x150')

def changeColor():
    colors =  askcolor(title="Farbe auswählen")
    root.configure(bg=colors[1])
    print(colors)

ttk.Button(root,  text="Wähle Farbe",  command=changeColor).pack(expand=True)

root.mainloop()