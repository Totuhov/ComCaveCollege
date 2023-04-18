import window_class
import tkinter as tk

#fill - Füllen des vorhandenen Platzes

window = window_class.Window()

boxEins = tk.Label(window, text="Box 1", bg="green", fg="white")
boxEins.pack(ipadx=10, ipady=10, fill=tk.X)

boxZwei = tk.Label(window, text="Box 2", bg="red", fg="white")
boxZwei.pack(ipadx=10, ipady=10, fill=tk.Y)

window.mainloop()