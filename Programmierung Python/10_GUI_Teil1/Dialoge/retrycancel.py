import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askretrycancel, showinfo, WARNING, ERROR

root = tk.Tk()
root.title("Retry/Cancel Demo")
root.resizable(False, False)
root.geometry("300x150")

def confirm():
    answer = askretrycancel(title="Retry/Cancel", message="Bitte bestätigen!")

    if answer:
        showinfo(title="Danke", message="Alle daten gelöscht!")

ttk.Button(root, text="Alles löschen?", command=confirm).pack(expand=True)
root.mainloop()