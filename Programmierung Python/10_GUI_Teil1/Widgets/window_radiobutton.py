import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.resizable(False, False)
window.geometry("500x300")

selectedRadioButton = tk.StringVar()
select = tk.StringVar()

radiobutton1 = ttk.Radiobutton(window, text="Groß", value="Large", variable=selectedRadioButton)
radiobutton2 = ttk.Radiobutton(window, text="Extra Groß", value="Extra Large", variable=selectedRadioButton)
radiobutton3 = ttk.Radiobutton(window, text="Weiteres", value="Weiterers", variable=select)

radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

window.mainloop()