import tkinter as tk #Import von tkinter zum Erstellen von GUIs

#Erstellen des Fensters
window = tk.Tk()
window.title("GUI Demo in Python")

#Fenstergröße und Position - geometry
# geometry
# breitexhöhe+x+y
# +x von links nach rechts -x von rechts nach links
# +y von oben nach unten -y von unten nach oben
window.geometry("640x480-150-250")

#Fenster in der Bildschirmmitte zentrieren
# Bildschirmgrößen holen
screen_width = window.winfo_screenwidth()
screen_heigth = window.winfo_screenheight()

center_x = int(screen_width / 2 - 640 / 2)
center_y = int(screen_heigth / 2 - 480 / 2)

window.geometry(f"640x480+{center_x}+{center_y}")

#Transparenz einstellen
window.attributes('-alpha',0.5)

print(str(screen_width) + " " + str(screen_heigth))
#Anzeigen des Fensters
window.mainloop()