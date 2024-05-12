from tkinter import *
from tkinter import ttk

root = Tk()

# Scroll Bar
textBox = Text(root, width=30, height=10, wrap='word')
textBox.grid(row=0, column=0)

scroll = ttk.Scrollbar(root, orient='vertical', command=textBox.yview)
scroll.grid(row=0, column=1, sticky=N+S)

textBox.config(yscrollcommand=scroll.set)

# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.geometry('500x450')
root.mainloop()