# pip install ttkthemes

from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as Tk

root = Tk.ThemedTk()
print(root.get_themes())
root.set_theme('ubuntu')

# Style
textFname = ttk.Label(root, text='First Name: ').grid(row=0, column=0, pady=20)
textSname = ttk.Label(root, text='Surame: ').grid(row=1, column=0)

# textMsg = ttk.Label(root, text='Message:')
nameInput = ttk.Entry(root, width=30).grid(row=0, column=1)
surNameInput = ttk.Entry(root, width=30).grid(row=1, column=1)

ttk.Radiobutton(root, text='male', value='male').grid(row=2, column=1)
ttk.Radiobutton(root, text='female', value='female').grid(row=2, column=1, sticky='E', pady=15)

msgText = Text(root, width=25, height=15, wrap='word').grid(row=3, column=1)

ttk.Button(root, text='Send', width=10).grid(row=4, column=1, sticky=W)
ttk.Button(root, text='Clear', width=10).grid(row=4, column=1, sticky=E)

# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.geometry('400x550+300+300')
root.mainloop()