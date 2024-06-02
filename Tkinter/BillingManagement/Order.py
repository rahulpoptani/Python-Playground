from tkinter import *

class Order(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f'{screenWidth}x{screenHeight}')
        self.title('Order')
        self.bind('<Escape>', lambda x: self.closeWindow())
    
    def closeWindow(self): self.destroy()