import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.resizable(False, False)
window.geometry("300x200")
window.title("Slider Demo")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

current_value = tk.DoubleVar()


slider_label = ttk.Label(window, text="Slider:")
slider_label.grid(column=0, row= 0, sticky="w")

def formatValue():
    return "{: .2f}".format(current_value.get())

def slider_changed(event):
    slider_value_label.configure(text=formatValue())

slider = ttk.Scale(window, from_=0, to=100, orient="horizontal", command=slider_changed, variable=current_value)
slider.grid(column=1, row=0, sticky="we")

slider_value_label = ttk.Label(window)
slider_value_label.grid(column=0, row=1, sticky="we", columnspan=2)

def setzSlider():
    slider.set(value=current_value.get()+5.00)

buttonSlider = ttk.Button(window, text="Setze Slider auf 50.00", command=setzSlider)
buttonSlider.grid(row=2, column=0)

window.mainloop()

