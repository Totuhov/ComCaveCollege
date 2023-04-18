import window_class
import tkinter as tk

# side = Umstellen der Packrichtung.
# Links nach rechts = LEFT | Rechts nach links = RIGHT
# Oben nach unten = TOP | Unten nach oben = BOTTOM

window = window_class.Window()

boxEins = tk.Label(window, text="Box 1", bg="green", fg="white")
boxEins.pack(ipadx=20, ipady=20, side=tk.BOTTOM)

boxZwei = tk.Label(window, text="Box 2", bg="red", fg="white")
boxZwei.pack(ipadx=20, ipady=20, side=tk.BOTTOM)

window.mainloop()