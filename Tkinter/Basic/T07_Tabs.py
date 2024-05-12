from tkinter import *
from tkinter import ttk

root = Tk()

# Tabs
icon1 = PhotoImage(file='Basic/icons_basic/1.png')
icon2 = PhotoImage(file='Basic/icons_basic/2.png')

tabs = ttk.Notebook(root)
tabs.pack(fill='both', expand=True)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tabs.add(tab1, text='First', image=icon1, compound='left')
tabs.add(tab2, text='Second', image=icon2, compound='left')
ttk.Label(tab1, text='Hello', font='Arial 20').place(x=200, y=50)

# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.geometry('650x650+650+250')
root.mainloop()