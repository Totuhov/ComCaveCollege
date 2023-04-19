import tkinter as tk
from tkinter import ttk

# Entry = Einzeilige Eingaben

window = tk.Tk()
window.geometry("300x150")
window.resizable(False, False)
window.title("Entry Demo")

# Für das Auslesen von Entry benötigen wir StringVar Objekte - Im Entry als textvariable angeben
username = tk.StringVar()
password = tk.StringVar()

def login():
    print("Login Gedrückt")
    print(f"User:{username.get()} - Password:{password.get()}")

login_frame = ttk.Frame(window).pack(fill="x", expand=True)

username_label = ttk.Label(login_frame, text="Username:").pack(fill="x", expand=True)
username_entry = ttk.Entry(login_frame, textvariable=username).pack(fill="x", expand=True)

password_label = ttk.Label(login_frame, text="Password:").pack(fill="x", expand=True)
password_entry = ttk.Entry(login_frame, textvariable=password, show="*").pack(fill="x", expand=True)


login_button = ttk.Button(login_frame, text="Login", command=login).pack(fill="x", expand=True)

window.mainloop()