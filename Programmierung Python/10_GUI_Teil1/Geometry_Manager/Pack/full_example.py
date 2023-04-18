import window_class
import tkinter as tk

window = window_class.Window()

boxNorthWest = tk.Label(window, text="NorthWest", bg="red", fg="white")
boxNorthWest.pack(ipadx=10, ipady=10, anchor=tk.NW, side=tk.LEFT)

boxNorth = tk.Label(window, text="North", bg="green", fg="white")
boxNorth.pack(ipadx=10, ipady=10, anchor=tk.N, side=tk.LEFT, fill=tk.X, expand=True)

boxNorthEast = tk.Label(window, text="NorthEast", bg="red", fg="white")
boxNorthEast.pack(ipadx=10, ipady=10, anchor=tk.NE)

boxEast = tk.Label(window, text="East", bg="blue", fg="white")
boxEast.pack(ipadx=10, ipady=10, anchor=tk.E)

boxSouth = tk.Label(window, text="South", bg="red", fg="white")
boxSouth.pack(ipadx=10, ipady=10, anchor=tk.S)

boxSouthWest = tk.Label(window, text="SouthWest", bg="blue", fg="white")
boxSouthWest.pack(ipadx=10, ipady=10, anchor=tk.SW)

boxWest = tk.Label(window, text="West", bg="green", fg="white")
boxWest.pack(ipadx=10, ipady=10, anchor=tk.W)

boxNorthWest = tk.Label(window, text="NorthWest", bg="red", fg="white")
boxNorthWest.pack(ipadx=10, ipady=10, anchor=tk.NW)

boxCenter = tk.Label(window, text="Center", bg="black", fg="white")
boxCenter.pack(ipadx=10, ipady=10, anchor=tk.CENTER)

boxSouthEast = tk.Label(window, text="SouthEast", bg="green", fg="white")
boxSouthEast.pack(ipadx=10, ipady=10, anchor=tk.SE)


window.mainloop()