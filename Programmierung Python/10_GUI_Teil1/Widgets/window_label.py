import tkinter as tk
from tkinter import ttk # Themed TK

window = tk.Tk()
window.geometry("640x480")
window.title("Label Demo")
# Label hinzufügen - Label = Beschriftungsfelder - tk.label = alte Variante mit Einschränkungen | ttk.label Neue, themed Variante

message = ttk.Label(window, text="Dies ist ein Label", font=("Arial", 20))
message.pack()

message.config(text="Ein neuer Text")


window.mainloop()