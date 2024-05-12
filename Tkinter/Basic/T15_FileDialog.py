# pip install ttkthemes

from tkinter import *
from tkinter import filedialog, colorchooser

root = Tk()

# File Dialog
def openFile():
    file_name = filedialog.askopenfilename(initialdir='.', title='Select a file', filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))
    content = open(file_name).read()
    textEditor.delete(1.0, END) # delete any previous text
    textEditor.insert(END, content)

def saveFile():
    myFile = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if myFile is None: return
    content = textEditor.get(1.0, END)
    myFile.write(content)

def choseColor():
    color = colorchooser.askcolor()
    textEditor.configure(fg=color[1])

textEditor = Text(root, width=25, height=15)
textEditor.pack()
button = Button(root, text='Open', command=openFile).pack(side='left', padx=(170,20))
button1 = Button(root, text='Save', command=saveFile).pack(side='left')
button2 = Button(root, text='Color', command=choseColor).pack(side='left')

# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.geometry('450x350+350+250')
root.mainloop()