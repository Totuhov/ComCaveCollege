import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

root = tk.Tk()
root.title("Messagebox Demo")
root.resizable(False, False)
root.geometry("300x150")

def confirm():
    answer = askyesno(title="Frage Ja/Nein", message="Wirklich beeenden?")

    if answer:
        root.destroy()

ttk.Button(root, text="Beenden", command=confirm).pack(expand=True)

root.mainloop()