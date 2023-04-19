import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo')

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(anchor=tk.CENTER, expand=True)

# Auf dem Canvas zeichen:
canvas.create_line((50, 50), (100, 100), width=4, fill="red")
canvas.create_line((100, 100), (150, 50), width=4, fill="red")
line = canvas.create_line((100, 100), (100, 200), width=4, fill="red")
canvas.create_text((300, 100), text= "Canvas Demo", fill="orange", font="Helvetica 20")

canvas.tag_bind(line, "<Button-1>", lambda e: canvas.delete(line))
root.mainloop()