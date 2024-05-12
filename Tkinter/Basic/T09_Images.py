from tkinter import *
from tkinter import ttk

root = Tk()

# Images
label = Label(root, text='Using Images', font='Times 18')
logo = PhotoImage(file='Basic/icons_basic/1.png')
labelImage = Label(root, image=logo)
labelImage.pack()

# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.geometry('350x350')
root.mainloop()