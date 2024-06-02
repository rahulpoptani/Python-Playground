from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from Helper import Helper
from Constants import Constants

class Inventory(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        screenWidth = self.winfo_screenwidth()
        screenHeight = int(self.winfo_screenheight()*0.9)
        self.geometry(f'{screenWidth}x{screenHeight}')
        self.title('Inventory')
        self.resizable(False, False)
        self.bind('<Escape>', lambda x: self.closeWindow())

        # TopFrame
        self.topFrame = LabelFrame(self, text='', bg=Constants.TOPFRAME_BG)
        self.topFrame.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        self.backImage = Helper.getImage('IMG_Back.png')
        self.backButton = Button(self.topFrame, text='Back', image=self.backImage, height=Constants.BIG_BUTTON_HEIGHT, font=Constants.BIG_BUTTON_FONT, compound=LEFT, command=self.destroy)
        self.backButton.pack(side=LEFT, padx=10, pady=10, anchor=NE)

        self.backupImage = Helper.getImage('IMG_Backup.png')
        self.backupButton = Button(self.topFrame, text='Backup', image=self.backupImage, height=Constants.BIG_BUTTON_HEIGHT, font=Constants.BIG_BUTTON_FONT, compound=LEFT)
        self.backupButton.pack(side=RIGHT, padx=10, pady=10, anchor=NW)
        
        self.restoreImage = Helper.getImage('IMG_Restore.png')
        self.restoreButton = Button(self.topFrame, text='Restore', image=self.restoreImage, height=Constants.BIG_BUTTON_HEIGHT, font=Constants.BIG_BUTTON_FONT, compound=LEFT)
        self.restoreButton.pack(side=RIGHT, padx=10, pady=10, anchor=NW)

        # Bottom Left Frame
        self.bottomLeftFrame = LabelFrame(self, text='')
        self.bottomLeftFrame.pack(padx=10, pady=10, side=LEFT, fill=BOTH, expand=True)

        # Bottom Left Top Frame
        self.bottomLeftTopFrame = LabelFrame(self.bottomLeftFrame, text='')
        self.bottomLeftTopFrame.pack(padx=10, pady=10, side=TOP, fill=BOTH, expand=True)

        self.style = ttk.Style()
        self.style.configure('Treeview.Heading', font=Constants.LISTBOX_FONT)
        self.style.configure('Treeview', font=Constants.LISTBOX_FONT, rowheight=30)

        self.itemTView = ttk.Treeview(self.bottomLeftTopFrame, columns=(1,2,3), show='headings')
        self.itemTView.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.itemTView.heading(1, text='Item')
        self.itemTView.heading(2, text='Price')
        self.itemTView.heading(3, text='Quantity')
        self.itemTView.column(1, anchor=CENTER)
        self.itemTView.column(2, anchor=CENTER)
        self.itemTView.column(3, anchor=CENTER)
        self.itemTView.bind('<Double 1>', self.getSelectedItem)

        self.loadTreeView()

        # Bottom Left Bottom Frame
        self.bottomLeftBottomFrame = LabelFrame(self.bottomLeftFrame, text='Add / Update')
        self.bottomLeftBottomFrame.pack(padx=10, pady=10, side=TOP, fill=BOTH)

        self.itemNameEntry = Entry(self.bottomLeftBottomFrame, font=Constants.ENTRY_FONT)
        self.itemNameEntry.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

        self.itemPrice = Entry(self.bottomLeftBottomFrame, font=Constants.ENTRY_FONT)
        self.itemPrice.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

        self.itemQty = Entry(self.bottomLeftBottomFrame, font=Constants.ENTRY_FONT)
        self.itemQty.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

        # Error Label
        self.errorLabel = Label(self.bottomLeftFrame, text='Message: ')
        self.errorLabel.pack(padx=10, pady=10, side=LEFT, fill=BOTH)

        # Bottom Right Frame
        self.bottomRightFrame = LabelFrame(self, text='')
        self.bottomRightFrame.pack(padx=(0,10), pady=10, side=RIGHT, fill=BOTH)
        self.bottomRightFrame.bind('<Button 1>', lambda x: self.clearSelection())

        self.searchEntry = Entry(self.bottomRightFrame, font=Constants.ENTRY_FONT)
        self.searchEntry.insert(0, 'Search Item')
        self.searchEntry.bind('<FocusIn>', lambda x: self.searchEntry.delete(0, END))
        self.searchEntry.bind('<Return>', lambda x: self.updateSearchResults())
        self.searchEntry.pack(padx=10, pady=10, fill=X)
        
        self.addButton = Button(self.bottomRightFrame, text='Add', font=Constants.OPTION_BUTTON_FONT, command=self.addItem)
        self.addButton.pack(padx=10, pady=10, fill=X)
        
        self.updateButton = Button(self.bottomRightFrame, text='Update', font=Constants.OPTION_BUTTON_FONT, command=self.updateItem)
        self.updateButton.pack(padx=10, pady=10, fill=X)
        
        self.deleteButton = Button(self.bottomRightFrame, text='Delete', font=Constants.OPTION_BUTTON_FONT, command=self.deleteItem)
        self.deleteButton.pack(padx=10, pady=10, fill=X)
        
    def updateTreeView(self, resultSet):
        self.itemTView.delete(*self.itemTView.get_children())
        for result in resultSet:
            self.itemTView.insert('', END, values=result)
    
    def updateSearchResults(self): 
        searchText = self.searchEntry.get()
        query = f'SELECT NAME, PRICE, QUANTITY FROM ITEMS WHERE LOWER(NAME) LIKE LOWER("%{searchText}%")'
        resultSet = Helper.executeQuery(query)
        self.updateTreeView(resultSet)
    
    def loadTreeView(self):
        resultSet = Helper.executeQuery('SELECT NAME, PRICE, QUANTITY FROM ITEMS')
        self.updateTreeView(resultSet)
    
    def getSelectedItem(self, event):
        self.currentTreeSelection = self.itemTView.item(self.itemTView.focus())
        self.itemNameEntry.delete(0, END)
        self.itemNameEntry.insert(0, self.currentTreeSelection['values'][0])
        self.itemPrice.delete(0, END)
        self.itemPrice.insert(0, self.currentTreeSelection['values'][1])
        self.itemQty.delete(0, END)
        self.itemQty.insert(0, self.currentTreeSelection['values'][2])
    
    def clearSelection(self):
        self.itemNameEntry.delete(0, END)
        self.itemPrice.delete(0, END)
        self.itemQty.delete(0, END)
        self.itemTView.selection_remove(self.itemTView.selection())

    def addItem(self): 
        itemName = self.itemNameEntry.get()
        itemPrice = float(self.itemPrice.get()) if self.itemPrice.get() else None
        itemQty = int(self.itemQty.get()) if self.itemQty.get() else None
        if itemName and itemPrice and itemQty:
            query = f"INSERT INTO {Constants.DB_TABLE_ITEMS} (NAME, PRICE, QUANTITY) VALUES (?, ?, ?)"
            try:
                Helper.executeQuery(query, (itemName, itemPrice, itemQty))
                print(query)
                self.loadTreeView()
            except sqlite3.IntegrityError as err:
                messagebox.showerror('Error', 'Item already in database', icon='error')
    
    def updateItem(self): 
        itemName = self.itemNameEntry.get()
        itemPrice = float(self.itemPrice.get()) if self.itemPrice.get() else None
        itemQty = int(self.itemQty.get()) if self.itemQty.get() else None
        if itemName and itemPrice and itemQty:
            query = f"UPDATE {Constants.DB_TABLE_ITEMS} SET NAME = '{itemName}', PRICE = {itemPrice}, QUANTITY = {itemQty} WHERE NAME = '{self.currentTreeSelection['values'][0]}'"
            try:
                Helper.executeQuery(query)
                print(query)
                self.loadTreeView()
            except sqlite3.IntegrityError as err:
                messagebox.showerror('Error', 'Item already in database', icon='error')
            
    
    def deleteItem(self):
        if len(self.itemTView.selection()) > 0:
            response = messagebox.askquestion('Delete', f'Are you sure you want to delete {len(self.itemTView.selection())} records')
            if response == 'yes':
                for x in self.itemTView.selection():
                    itemName, _, _ = self.itemTView.item(x)['values']
                    query = f"DELETE FROM {Constants.DB_TABLE_ITEMS} WHERE NAME = '{itemName}'"
                    print(query)
                    Helper.executeQuery(query)
                self.clearSelection()
                self.loadTreeView()
        


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