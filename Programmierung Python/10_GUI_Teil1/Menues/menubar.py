import tkinter as tk #Import von tkinter zum Erstellen von GUIs
from tkinter import ttk
from tkinter import Menu

#Erstellen des Fensters
window = tk.Tk()
window.title("GUI Demo in Python")

screen_width = window.winfo_screenwidth()
screen_heigth = window.winfo_screenheight()

center_x = int(screen_width / 2 - 640 / 2)
center_y = int(screen_heigth / 2 - 480 / 2)

window.geometry(f"640x480+{center_x}+{center_y}")

#Menüband erstellen
menubar =  Menu(window)
window.config(menu=menubar)

#Menü im Menüband erstellen und Funktionen hinzufügen
dateiMenu = Menu(menubar, tearoff=0)

settingsMenu = Menu(dateiMenu, tearoff=0)
settingsMenu.add_command(label="Fenstereinstellungen")

dateiMenu.add_command(label="Neu")
dateiMenu.add_command(label="Öffnen")
dateiMenu.add_command(label="Speichern")
dateiMenu.add_separator()
dateiMenu.add_cascade(label="Einstellungen", menu=settingsMenu) # Untermenü in einem Menü
dateiMenu.add_separator()
dateiMenu.add_command(label="Beenden", command=window.destroy, underline=0)
dateiMenu.add_checkbutton(label="Checkbutton")
dateiMenu.add_radiobutton(label="Radiobutton1")
dateiMenu.add_radiobutton(label="Radiobutton2")
dateiMenu.add_radiobutton(label="Radiobutton3")

settingsMenu = Menu(dateiMenu, tearoff=0)

menubar.add_cascade(label="Datei", menu=dateiMenu, underline=0)
menubar.add_cascade(label="Hilfe")

#Anzeigen des Fensters
window.mainloop()