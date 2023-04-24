import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import  showerror, showinfo, showwarning

root = tk.Tk()
root.title("Messagebox Demo")
root.resizable(False, False)
root.geometry("300x150")

options = {"fill": "both", "padx": 10, "pady": 10,  "ipadx": 5}

ttk.Button(
    root, 
    text="Fehlermeldung anzeigen", 
    command= lambda: showerror(
        title="Fehlermeldung", 
        message="Dies ist eine Fehlermeldung")
    ).pack(**options)

ttk.Button(
    root, 
    text="Info anzeigen", 
    command= lambda: showinfo(
        title="Info", 
        message="Dies ist eine Information")
    ).pack(**options)

ttk.Button(
    root, 
    text="Warnung anzeigen", 
    command= lambda: showwarning(
        title="Warnmeldung", 
        message="Dies ist eine Warnmeldung")
    ).pack(**options)

root.mainloop()