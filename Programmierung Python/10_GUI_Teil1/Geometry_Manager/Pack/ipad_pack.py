import window_class
import tkinter as tk

#ipad = ipadx , ipady - internal padding - Abstand im inneren

window = window_class.Window()

boxEins = tk.Label(window, text="Box 1", bg="green", fg="white")
boxEins.pack(ipadx=20, ipady=20)

boxZwei = tk.Label(window, text="Box 2", bg="red", fg="white")
boxZwei.pack(ipadx=50, ipady=50)

window.mainloop()