import tkinter as tk #Import von tkinter zum Erstellen von GUIs

#Erstellen des Fensters
window = tk.Tk()
window.title("GUI Demo in Python")
screen_width = window.winfo_screenwidth()
screen_heigth = window.winfo_screenheight()
center_x = int(screen_width / 2 - 640 / 2)
center_y = int(screen_heigth / 2 - 480 / 2)
window.geometry(f"640x480+{center_x}+{center_y}")


#Verhindern vom Resize des Fensters
#resizable(breite, höhe)
window.resizable(True, True)

#Minimalgrößen
window.minsize(320, 240)
#Maximalgrößen
window.maxsize(960,720)

#Anzeigen des Fensters
window.mainloop()