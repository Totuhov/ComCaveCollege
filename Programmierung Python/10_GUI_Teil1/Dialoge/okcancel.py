import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, WARNING, ERROR

root = tk.Tk()
root.title("Messagebox Demo")
root.resizable(False, False)
root.geometry("300x150")

def confirm():
    answer = askokcancel(title="Ok/Abbrechen", message="Bitte bestätigen!", icon=ERROR)

    if answer:
        showinfo(title="Danke", message="Alle daten gelöscht!")

ttk.Button(root, text="Alles löschen?", command=confirm).pack(expand=True)
root.mainloop()