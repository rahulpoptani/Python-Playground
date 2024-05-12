from tkinter import *
from tkinter import messagebox

root = Tk()

# Menu
def exitFunction():
    mbox = messagebox.askquestion('Exit', 'Are you Sure?', icon='warning')
    if mbox == 'yes': root.destroy()

menuBar = Menu(root)
root.config(menu=menuBar)
file = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=file)
file.add_command(label='New')
file.add_separator()
file.add_command(label='Open')
file.add_command(label='Save')
exitIcon = PhotoImage(file='Basic/icons_basic/exit.png')
file.add_command(label='Exit', image=exitIcon, compound='left', command=exitFunction)

edit = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Undo')
edit.add_command(label='Redo')
edit.add_command(label='Cut')
edit.add_command(label='Copy')
edit.add_command(label='Paste')

# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.geometry('350x350')
root.mainloop()