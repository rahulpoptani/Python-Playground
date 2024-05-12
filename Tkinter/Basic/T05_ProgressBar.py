from tkinter import *
from tkinter import ttk

root = Tk()

# Progress Bar
progBar = ttk.Progressbar(root, orient='horizontal', length=200)
progBar.pack(pady=20)
progBar.config(mode='indeterminate')
progBar.start()
progBar1 = ttk.Progressbar(root, orient='horizontal', length=200)
progBar1.pack(pady=20)
progBar1.config(mode='determinate', maximum=50.0, value=10.0)
progBar1.start()
progBar2 = ttk.Progressbar(root, orient='horizontal', length=200)
progBar2.pack(pady=20)
progBar2.config(mode='determinate', maximum=50.0, value=10.0)

# Scale
scaleVar = DoubleVar()
progBar2.config(variable=scaleVar)
scale = ttk.Scale(root, orient='horizontal', length=200, variable=scaleVar, from_=0.0, to=50.0)
scale.pack()

root.geometry('450x450+650+350')
root.mainloop()