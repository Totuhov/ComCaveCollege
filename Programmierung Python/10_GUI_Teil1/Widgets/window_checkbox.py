import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.resizable(False, False)
window.geometry("500x200")
window.title("Checkbox Demo")

check = tk.BooleanVar()

label = tk.Label(text="Checkbox checked!")

def checkbox_changed():
    print(check.get())
    if check.get():
        label.pack()
    else:
        label.pack_forget()

checkbox = ttk.Checkbutton(window, command=checkbox_changed, variable=check, onvalue=True, offvalue=False, text="Einverstanden?")
checkbox.pack()

window.mainloop()