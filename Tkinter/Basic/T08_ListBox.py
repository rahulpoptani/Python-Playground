from tkinter import *
from tkinter import ttk

root = Tk()

# ListBox
listbox = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
listbox.pack(pady=25)
listbox.insert(0, 'Python')
listbox.insert(1, 'GoLang')
listbox.insert(2, 'Java')
listbox.insert(3, 'JS')

def printMe(): 
    selectedItems = listbox.curselection()
    for item in selectedItems: print(listbox.get(item))
def deleteMe(): 
    selectedItems = listbox.curselection()
    for item in selectedItems: listbox.delete(item)
Button(root, text='Print', command=printMe).place(x=250, y=300)
Button(root, text='Delete', command=deleteMe).place(x=350, y=300)

# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.geometry('650x650+650+250')
root.mainloop()