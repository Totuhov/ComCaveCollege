import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Frame Demo")
window.geometry("640x480")

# Frames - Organisation von Widgets - Frame = Rahmen
mixFrame = ttk.Frame(window, borderwidth=10, relief="solid")
labelFrame = ttk.Frame(mixFrame, borderwidth=5, relief="raised")
buttonFrame = ttk.Frame(mixFrame, borderwidth=5, relief="sunken")

label_eins = ttk.Label(labelFrame, text="Label Eins", background="green", foreground="white").grid(column=0, row=0, sticky="NSEW")
label_zwei = ttk.Label(labelFrame, text="Label Zwei", background="red", foreground="white").grid(column=1, row=0, sticky="NSEW")
label_drei = ttk.Label(labelFrame, text="Label Drei", background="#2ad8b3", foreground="white").grid(column=0, row=1, sticky="NSEW")
label_vier = ttk.Label(labelFrame, text="Label Vier", background="black", foreground="white").grid(column=1, row=1, sticky="NSEW")
labelFrame.pack(side="left")

button_eins = ttk.Button(buttonFrame, text="Button 1", command=None)
button_zwei = ttk.Button(buttonFrame, text="Button Zwei", command=None)
button_eins.pack()
button_zwei.pack()
buttonFrame.pack(side="left")

mixFrame.place(x=25, y=300)

window.mainloop()
