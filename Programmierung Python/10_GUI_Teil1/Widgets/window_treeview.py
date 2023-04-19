import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

columns = ("Vorname", "Nachname", "E-Mail")

# Erstellen der Treeview mit den Headings (Überschriften)
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading('Vorname', text="Vorname")
tree.heading('Nachname', text="Nachname")
tree.heading('E-Mail', text="E-Mail")

#Inhalt erzeugen
contacts = []
for n in range(1, 100):
    contacts.append((f"first {n}", f"last {n}", f"email{n}@example.com"))

for contact in contacts:
    tree.insert("", tk.END, values=contact)


tree.grid(row=0, column=0, sticky="nsew")

root.mainloop()