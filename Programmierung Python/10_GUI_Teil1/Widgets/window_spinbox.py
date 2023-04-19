import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.resizable(False, False)
window.geometry("300x200")
window.title("Spinbox Demo")

current_value = tk.StringVar(value=2)

spinBox = ttk.Spinbox(window, from_=0, to=50, textvariable=current_value, wrap=False, values=(0,5,10,15), state="readonly")
spinBox.pack()

window.mainloop()