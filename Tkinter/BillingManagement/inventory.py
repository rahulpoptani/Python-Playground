from tkinter import *
from helper.helper import Helper
from helper.constants import Constants

class Inventory(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f'{screenWidth}x{screenHeight}')
        self.title('Inventory')
        self.resizable(False, False)
        self.bind('<Escape>', lambda x: self.closeWindow())

        # Top Frame
        self.topFrameHeight = screenHeight * 0.1
        self.topFrame = Frame(self, bg=Constants.TOPFRAME_BG, height=self.topFrameHeight, width=screenWidth)
        self.topFrame.pack(side=TOP, fill=BOTH)
        
        # Bottom Frame
        self.bottomFrameHeight = screenHeight * 0.9
        self.bottomFrame = Frame(self, bg=Constants.BOTTOMFRAME_BG, height=self.bottomFrameHeight, width=screenWidth)
        self.bottomFrame.pack(side=TOP, fill=BOTH)

        # Add Button to Top Frame
        self.backImage = Helper.getImage('back.png')
        self.backButton = Button(self.topFrame, text='Back', image=self.backImage, height=Constants.BUTTON_HEIGHT, font=Constants.BUTTON_FONT, compound=LEFT)
        self.backButton.pack(side=LEFT, padx=10, pady=10)
        
        self.backupImage = Helper.getImage('backup.png')
        self.backupButton = Button(self.topFrame, text='Backup', image=self.backupImage, height=Constants.BUTTON_HEIGHT, font=Constants.BUTTON_FONT, compound=LEFT)
        self.backupButton.pack(side=RIGHT, padx=10, pady=10)
        
        self.restoreImage = Helper.getImage('restore.png')
        self.restoreButton = Button(self.topFrame, text='Restore', image=self.restoreImage, height=Constants.BUTTON_HEIGHT, font=Constants.BUTTON_FONT, compound=LEFT)
        self.restoreButton.pack(side=RIGHT, padx=10, pady=10)

        # Add Label to Top Frame
        self.InventoryLabel = Label(self.topFrame, text='Inventory', bg=Constants.TOPFRAME_BG, fg=Constants.HEADING_FG, font=Constants.HEADING_FONT)
        self.InventoryLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Add Left and Right Frame to Bottom Frame
        self.leftBottomFrame = Frame(self.bottomFrame, bg=Constants.BOTTOMFRAME_BG, height=self.bottomFrameHeight*0.90, width=screenWidth*0.8)
        self.leftBottomFrame.pack(side=LEFT, fill=BOTH)
        self.rightBottomFrame = Frame(self.bottomFrame, bg='#ECECEC', height=self.bottomFrameHeight*0.90, width=screenWidth*0.2)
        self.rightBottomFrame.pack(side=RIGHT, fill=BOTH)

        
    
    def closeWindow(self): self.destroy()

def main():
    root = Tk()
    app = Inventory()
    app.attributes('-topmost',True)
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f'{screenWidth}x{screenHeight}')
    root.resizable(False, False)
    root.bind('<Escape>', lambda x: closeWindow(root))
    root.mainloop()

def closeWindow(self): self.destroy()

if __name__ == '__main__':
    main()