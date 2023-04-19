import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = ttk.Frame(notebook, width=400, height=200)
frame2 = ttk.Frame(notebook, width=400, height=200)
frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)

frame1_label = ttk.Label(frame1, text="Mich sieht man nur im Frame 1")
frame1_label.pack(fill="both", expand=True)

frame2_label = ttk.Label(frame2, text="Mich sieht man nur im Frame 2")
frame2_label.pack(fill="both", expand=True)

notebook.add(frame1, text="Allgemein")
notebook.add(frame2, text="Profil")

root.mainloop()