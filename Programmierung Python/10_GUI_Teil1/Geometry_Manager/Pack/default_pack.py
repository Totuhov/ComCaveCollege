import window_class
import tkinter as tk

window = window_class.Window()

boxEins = tk.Label(window, text="Box 1", bg="green", fg="white")
boxEins.pack()

boxZwei = tk.Label(window, text="Box 2", bg="red", fg="white")
boxZwei.pack()

window.mainloop()