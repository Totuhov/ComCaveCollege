#Themes (Aussehen / Look&Feel) einstellen
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Theme Demo")
window.geometry("400x300")
style =  ttk.Style(window)

label = ttk.Label(window, text="Name:")
label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

entry = ttk.Entry(window)
entry.grid(column=1, row=0, padx=10, pady=10,  sticky='w')

button = ttk.Button(window, text="Anzeigen")
button.grid(column=2, row=0, padx=10, pady=10,  sticky='w')

selectedTheme = tk.StringVar()
theme_frame = ttk.LabelFrame(window, text="Themes")
theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20,  sticky="w")

def changeTheme():
    style.theme_use(selectedTheme.get())

for themeName in style.theme_names():
    radiobutton = ttk.Radiobutton(theme_frame,  text=themeName, value=themeName, variable=selectedTheme, command=changeTheme)
    radiobutton.pack(expand=True, fill="both")


window.mainloop()