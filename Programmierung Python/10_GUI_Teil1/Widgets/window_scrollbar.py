import tkinter as tk
from tkinter import ttk

# Scrollbar - Widget zum Anzeigen einer Scrollleiste

window = tk.Tk()
#window.geometry("300x250")
#window.resizable(False, False)
window.title("Entry Demo")


login_frame = ttk.Frame(window).pack(fill="x", expand=True)

text_eingabe = tk.Text(login_frame, height=8)
text_eingabe.pack(side="left")

for i in range(1,50):
    position = f'{i}.0'
    text_eingabe.insert(position,f'Line {i}\n');

scrollbar = ttk.Scrollbar(login_frame, orient="vertical", command=text_eingabe.yview) # Erstellen der Scrollbar
scrollbar.pack(side="left", fill="y")
text_eingabe['yscrollcommand'] = scrollbar.set #Zuweisen der Scrollbar an das Widget


def login():
    print("Login Gedrückt")
    print(text_eingabe.get("1.0", "end-1c")) # Beim get Start, Ende angeben - Zeilen von 1 - Zeichen von 0 beginnend

login_button = ttk.Button(login_frame, text="Login", command=login).pack(fill="x", expand=True)

window.mainloop()