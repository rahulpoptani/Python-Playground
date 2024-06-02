from tkinter import *
from Helper import Helper
from Constants import Constants
from Inventory import Inventory
from Order import Order

class Main(object):
    def __init__(self, master: Tk) -> None:
        self.master = master

        Helper.dataBootstrap()

        # Set the screen width and height
        self.screenWidth = self.master.winfo_screenwidth()
        self.screenHeight = int(self.master.winfo_screenheight()*0.9)

        # Main Frame
        mainFrame = Frame(self.master, bg='#385170', width=self.screenWidth, height=self.screenHeight)
        mainFrame.pack()

        # Create Buttons
        self.inventoryImage = Helper.getImage('IMG_Inventory.png')
        inventoryButton = Button(mainFrame, text='Inventory', compound=LEFT, bg='white', image=self.inventoryImage, font=Constants.BIG_BUTTON_FONT, command=self.openInventory)
        inventoryButton.place(relx=0.39, rely=0.4, anchor=CENTER, relwidth=0.2, relheight=0.2)
        
        self.orderImage = Helper.getImage('IMG_Order.png')
        orderButton = Button(mainFrame, text='Order', compound=LEFT, bg='white', image=self.orderImage, font=Constants.BIG_BUTTON_FONT, command=self.openOrder)
        orderButton.place(relx=0.61, rely=0.4, anchor=CENTER, relwidth=0.2, relheight=0.2)
                
    def openInventory(self):
        inventory = Inventory()
    
    def openOrder(self):
        inventory = Order()

def main():
    root = Tk()
    app = Main(root)
    screenWidth = root.winfo_screenwidth()
    screenHeight = int(root.winfo_screenheight()*0.9)
    root.title('Sixson Sons')
    root.geometry(f'{screenWidth}x{screenHeight}')
    root.resizable(False, False)
    root.bind('<Escape>', lambda x: closeWindow(root))
    root.mainloop()

def closeWindow(x): x.destroy()

if __name__ == '__main__':
    main()