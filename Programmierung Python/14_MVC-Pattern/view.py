import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    def __init__(self):
        super().__init__()

        self.frame = ttk.Frame(self)
        self.frame.grid(row=0, column=0,padx=10, pady=10)

        self.label = ttk.Label(self.frame, text="E-Mail:")
        self.label.grid(row=1, column=0)

        self.emailVar = tk.StringVar()
        self.emailEntry = ttk.Entry(self.frame, textvariable=self.emailVar, width=30)
        self.emailEntry.grid(row=1, column=1, sticky=tk.NSEW)

        self.saveButton = ttk.Button(self.frame, text="Speichern", command=self.save)
        self.saveButton.grid(row=1, column=3, padx=10)

        self.messageLabel = ttk.Label(self.frame, text="", foreground="red")
        self.messageLabel.grid(row=2, column=1, sticky=tk.W)

        self.controller = None

    def setController(self, controller):
        self.controller = controller

    def save(self):
        if self.controller:
            self.controller.save(self.emailVar.get())

    def showError(self, message):
        self.messageLabel['text'] = message
        self.messageLabel['foreground'] = "red"
        self.messageLabel.after(5000, self.hideMessage)

    def showSuccess(self, message):
        self.messageLabel['text'] = message
        self.messageLabel['foreground'] = "green"
        self.messageLabel.after(5000, self.hideMessage)

        self.emailVar.set("")

    def hideMessage(self):
        self.messageLabel['text'] = ""