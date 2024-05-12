from tkinter import *
from tkinter import ttk

root = Tk()

# Paned Window
pw = ttk.PanedWindow(root, orient='horizontal')
pw.pack(fill='both', expand=True)
frame1 = ttk.Frame(pw, width=100, height=500, relief='sunken')
frame2 = ttk.Frame(pw, width=100, height=500, relief='sunken')
frame3 = ttk.Frame(pw, width=75, height=500, relief='sunken')
pw.add(frame1, weight=1)
pw.add(frame2, weight=3)
pw.insert(1, frame3) # add frame 3 and index 1; between frame1 and frame 2

labelFrame = Label(frame1, text='Hello').grid(row=0, column=0, pady=25)
buttonFrame = ttk.Button(frame1, text='Click Me').grid(row=1, column=0, pady=25, padx=25)


# Close window with Escape
def closeWindow(x): root.destroy()
root.bind('<Escape>', lambda x: closeWindow(x))

root.geometry('650x650+650+250')
root.mainloop()