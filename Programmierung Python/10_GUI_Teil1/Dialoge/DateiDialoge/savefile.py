import tkinter as tk
from tkinter import  ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Filedialog Demo")
root.resizable(False, False)
root.geometry("300x150")

def waehleDatei():
    filetypes = (('Textdateien', "*.txt"), ("PDF", "*.pdf"), ("Alle", "*.*"))

    filename = filedialog.asksaveasfile(title="Wähle eine Datei", initialdir="/", filetypes=filetypes, defaultextension=filetypes)
    
    if filename != None:
        showinfo(title="Gewälte Datei",  message=filename)

ttk.Button(root, text="Öffne eine Datei", command=waehleDatei).pack(expand=True)

root.mainloop()