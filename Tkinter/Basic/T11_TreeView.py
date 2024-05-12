from tkinter import *
from tkinter import ttk

root = Tk()

# TreeView
treeView = ttk.Treeview(root)
treeView.pack()

treeView.insert('', 0, 'item1', text='First Item')
treeView.insert('', 1, 'item2', text='Second Item')
treeView.insert('', 2, 'item3', text='Third Item')
treeView.insert('', 3, 'item4', text='Fourth Item')
treeView.move('item3', 'item1', 'end')

def callback(event):
    item = treeView.identify('item', event.x, event.y)
    print(f'You Clicked {treeView.item(item, "text")}')
treeView.bind('<Double-1>', callback) # double-click

# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.geometry('350x350')
root.mainloop()