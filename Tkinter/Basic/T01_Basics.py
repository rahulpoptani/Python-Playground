from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x400")

######### Labels #########
label = Label(root)
label.config(text='Sample GUI Program.', font='Areal 30', foreground='red', background='Yellow')
label.pack()

######### Buttons #########
def callback():
    label.config(text='You Clicked Me', foreground='green')
    button['state'] = 'disabled' # example when you want to disable the button
button = Button(root, text='Click Me', command=callback)
button.pack()

######### Entry #########
entry = ttk.Entry(root, width=30)
entryPass = ttk.Entry(root, width=30)
entry.insert(0, 'Enter your name') # pre-populated text
entryPass.config(show='*') # for passwords
entry.pack()
entryPass.pack()
def disableText():
    entry.state(['disabled']) # or entry['state'] = 'disabled'
entryButton = Button(root, text='Click Me', command=disableText)
entryButton.pack()

root.mainloop()