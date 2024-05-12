from tkinter import *
from tkinter import ttk

root = Tk()

# Canvas
canvas = Canvas(root, width=650, height=550)
canvas.pack()
line = canvas.create_line(100, 250, 360, 25)
canvas.itemconfig(line, fill='red', width=10)

canvas.create_line(200, 250, 300, 350, 400, 350, 200, 250, fill='green', width=5)
canvas.create_text(500, 200, text='Hello Python', font='Arial 20 bold')

canvas.create_rectangle(200, 400, 300, 500, fill='green', width=5)

oneIcon = PhotoImage(file='Basic/icons_basic/1.png')
canvas.create_image(500, 400, image=oneIcon)

# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.geometry('650x550+300+300')
root.mainloop()