import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')

progressBar = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=280)
progressBar.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

start_button = ttk.Button(root, text="Start", command=progressBar.start)
stop_button = ttk.Button(root, text="Stop", command=progressBar.stop)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

root.mainloop()