from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Frames')

# Frames
frame = Frame(root, width=300, height=300, bg='red', bd=7)
frame.pack(fill=X)
button1 = Button(frame, text='Button 1')
button2 = Button(frame, text='Button 2')
button1.pack(side='left', padx=20, pady=15)
button2.pack(side='left', padx=20, pady=15)

# Label Frame
searchBar = LabelFrame(root, text='Search Box', padx=20, pady=20, bg='#fcd45d')
Label(searchBar, text='Enter').pack(side='left', padx=10)
Entry(searchBar).pack(side='left', padx=10)
Button(searchBar, text='Search').pack(side='left', padx=10)
searchBar.pack(side='top')

root.geometry('650x650+450+200')
root.mainloop()
