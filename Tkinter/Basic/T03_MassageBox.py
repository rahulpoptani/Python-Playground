from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

# MessageBox
def callbackDelete(): 
    mbox = messagebox.askquestion('Delete', 'Are you sure', icon='warning')
    if mbox == 'yes': print('Deleted')
    else: print('Not Deleted')
def callbackInfo(): 
    messagebox.showinfo('Success', 'Well Done', icon='info')
deleteButton = ttk.Button(root, text='Delete', command=callbackDelete).grid(row=0, column=0, pady=25, padx=50)
InfoButton = ttk.Button(root, text='Info', command=callbackInfo).grid(row=0, column=1)

# Text Editor
textEditor = Text(root, width=30, height=10, font='Arial 15', wrap='word')
textEditor.grid(row=1, column=0, pady=20, padx=40)
button = Button(root, text='Save', width=10, height=1)
button.grid(row=2, column=0)

root.geometry('500x400')
root.mainloop()
