import tkinter as tk
from tkinter import ttk # Themed TK

window = tk.Tk()
window.geometry("640x480")
window.title("Button Demo")

def klick(event):
    print("Button gedrückt!")

def klick_copy():
    klick(None)

oldButton = tk.Button(window,text="Ein Button",command=klick)
oldButton.pack()

newButton = ttk.Button(window, text="Der neue Button", command=klick_copy)
newButton.pack(ipadx=10, ipady=50)

#Button soll auf Tastatur-Taste reagieren - Funktionen müssen ein Event annehmen
newButton.bind("<Return>", klick)


def sageButton(text):
    print(text)
    print(textButton['text'])

textButton = ttk.Button(window,text="Mein Button", command=lambda: sageButton("Ich bin ein Button"))
textButton.pack()

window.mainloop()
