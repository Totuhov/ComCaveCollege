import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('LabelFrame Demo')

labelFrame = ttk.LabelFrame(root, text="Alignment")
labelFrame.grid(column=0, row=0, padx=20, pady=20)

alignment_var = tk.StringVar()
alignments = ("Left", "Center", "Right")

r1 = ttk.Radiobutton(labelFrame, text=alignments[0], value=alignments[0], variable=alignment_var)
r2 = ttk.Radiobutton(labelFrame, text=alignments[1], value=alignments[1], variable=alignment_var)
r3 = ttk.Radiobutton(labelFrame, text=alignments[2], value=alignments[2], variable=alignment_var)

r1.grid(column=0, row=0, ipadx=10, ipady=10)
r2.grid(column=1, row=0, ipadx=10, ipady=10)
r3.grid(column=2, row=0, ipadx=10, ipady=10)

root.mainloop()