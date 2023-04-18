import window_class
import tkinter as tk

#expand = Expandieren um den freien Platz einzunehmen

window = window_class.Window()

boxEins = tk.Label(window, text="Box 1", bg="green", fg="white")
boxEins.pack(ipadx=10, ipady=10, fill=tk.BOTH, expand=True)

boxZwei = tk.Label(window, text="Box 2", bg="red", fg="white")
boxZwei.pack(ipadx=10, ipady=10, fill=tk.Y)

window.mainloop()