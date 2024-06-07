from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import sqlite3
import pandas as pd
from datetime import datetime
from Helper import Helper
from Constants import Constants

class Inventory(Toplevel):
    CURR_DIR = '/'.join(__file__.split('/')[:-1])
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
        self.backupButton = Button(self.topFrame, text='Backup', image=self.backupImage, height=Constants.BIG_BUTTON_HEIGHT, font=Constants.BIG_BUTTON_FONT, compound=LEFT, command=self.backupInventory)
        self.backupButton.pack(side=RIGHT, padx=10, pady=10, anchor=NW)
        
        self.restoreImage = Helper.getImage('IMG_Restore.png')
        self.restoreButton = Button(self.topFrame, text='Restore', image=self.restoreImage, height=Constants.BIG_BUTTON_HEIGHT, font=Constants.BIG_BUTTON_FONT, compound=LEFT, command=self.restoreInventory)
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

        self.itemTView = ttk.Treeview(self.bottomLeftTopFrame, columns=(1,2), show='headings')
        self.itemTView.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.itemTView.heading(1, text='Item')
        self.itemTView.heading(2, text='Price')
        self.itemTView.column(1, anchor=CENTER)
        self.itemTView.column(2, anchor=CENTER)
        self.itemTView.bind('<Double 1>', self.getSelectedItem)

        self.loadTreeView()

        # Bottom Left Bottom Frame
        self.bottomLeftBottomFrame = LabelFrame(self.bottomLeftFrame, text='Add / Update')
        self.bottomLeftBottomFrame.pack(padx=10, pady=10, side=TOP, fill=BOTH)

        self.itemNameLabel = Label(self.bottomLeftBottomFrame, text='Item:', font=Constants.ENTRY_FONT)
        self.itemNameLabel.pack(side=LEFT, padx=10, pady=10)
        self.itemNameEntry = Entry(self.bottomLeftBottomFrame, font=Constants.ENTRY_FONT)
        self.itemNameEntry.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

        self.itemPriceLabel = Label(self.bottomLeftBottomFrame, text='Price:', font=Constants.ENTRY_FONT)
        self.itemPriceLabel.pack(side=LEFT, padx=10, pady=10)
        self.itemPrice = Entry(self.bottomLeftBottomFrame, font=Constants.ENTRY_FONT)
        self.itemPrice.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

        # Error Label
        self.errorLabelName = Label(self.bottomLeftFrame, text='Message: ', foreground='Black')
        self.errorLabelName.pack(padx=10, pady=10, side=LEFT, fill=BOTH)
        self.errorLabelValue = Label(self.bottomLeftFrame, text='')
        self.errorLabelValue.pack(pady=10, side=LEFT, fill=BOTH)

        # Bottom Right Frame
        self.bottomRightFrame = LabelFrame(self, text='')
        self.bottomRightFrame.pack(padx=(0,10), pady=10, side=RIGHT, fill=BOTH)
        self.bottomRightFrame.bind('<Button 1>', lambda x: self.clearSelection())

        self.searchEntry = Entry(self.bottomRightFrame, font=Constants.ENTRY_FONT, width=50)
        self.searchEntry.insert(0, 'Search Item')
        self.searchEntry.bind('<FocusIn>', lambda x: self.searchEntry.delete(0, END))
        self.searchEntry.bind('<Return>', lambda x: self.updateSearchResults())
        self.searchEntry.pack(padx=10, pady=10, fill=X)
        
        self.addButton = Button(self.bottomRightFrame, text='Add', font=Constants.OPTION_BUTTON_FONT, height=2, command=self.addItem)
        self.addButton.pack(padx=10, pady=10, fill=X)
        
        self.updateButton = Button(self.bottomRightFrame, text='Update', font=Constants.OPTION_BUTTON_FONT, height=2, command=self.updateItem)
        self.updateButton.pack(padx=10, pady=10, fill=X)
        
        self.deleteButton = Button(self.bottomRightFrame, text='Delete', font=Constants.OPTION_BUTTON_FONT, height=2, command=self.deleteItem)
        self.deleteButton.pack(padx=10, pady=10, fill=X)
        
    def backupInventory(self):
        if messagebox.askyesno('Backup', 'Do you want to backup the inventory?'):
            resultSet = Helper.executeQuery('SELECT NAME, PRICE FROM ITEMS')
            df = pd.DataFrame(resultSet)
            filename = f"Inventory_Backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv" 
            df.to_csv(filename, index=False, header=False)
            self.changeErrorLabelValue(f'Inventory Backup Completed! (File: {filename})', 'Green')
    
    def restoreInventory(self):
        if messagebox.askyesno('Restore', 'Do you want to restore the inventory?'):
            path = filedialog.askopenfilename(initialdir='./', title='Select A File', filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
            try:
                df = pd.read_csv(path, header=None, names=['itemname', 'price'])
                if len(df.index) > 0:
                    Helper.executeQuery(f'DELETE FROM {Constants.DB_TABLE_ITEMS}')
                    for _, row in df.iterrows():
                        Helper.executeQuery(f'INSERT INTO {Constants.DB_TABLE_ITEMS} (NAME, PRICE) VALUES (?, ?)', (row.itemname, row.price))
                    self.loadTreeView()
                    self.changeErrorLabelValue('Inventory Restored!', 'Green')
            except Exception as exe:
                messagebox.showerror('Error',f'Unable to load file: {path} {exe}')

    
    def updateTreeView(self, resultSet):
        self.itemTView.delete(*self.itemTView.get_children())
        for result in resultSet:
            self.itemTView.insert('', END, values=result)
    
    def updateSearchResults(self): 
        searchText = self.searchEntry.get()
        query = f'SELECT NAME, PRICE FROM ITEMS WHERE LOWER(NAME) LIKE LOWER("%{searchText}%") ORDER BY NAME'
        resultSet = Helper.executeQuery(query)
        self.updateTreeView(resultSet)
    
    def loadTreeView(self):
        resultSet = Helper.executeQuery('SELECT NAME, PRICE FROM ITEMS ORDER BY NAME')
        self.updateTreeView(resultSet)
    
    def getSelectedItem(self, event):
        self.currentTreeSelection = self.itemTView.item(self.itemTView.focus())
        self.itemNameEntry.delete(0, END)
        self.itemNameEntry.insert(0, self.currentTreeSelection['values'][0])
        self.itemPrice.delete(0, END)
        self.itemPrice.insert(0, self.currentTreeSelection['values'][1])
    
    def clearSelection(self):
        self.itemNameEntry.delete(0, END)
        self.itemPrice.delete(0, END)
        self.itemTView.selection_remove(self.itemTView.selection())
        self.errorLabelValue['text'] = ''

    def addItem(self): 
        itemName = self.itemNameEntry.get()
        itemPrice = float(self.itemPrice.get()) if self.itemPrice.get() else None
        if itemName and itemPrice:
            query = f"INSERT INTO {Constants.DB_TABLE_ITEMS} (NAME, PRICE) VALUES (?, ?)"
            try:
                Helper.executeQuery(query, (itemName, itemPrice))
                print(query)
                self.loadTreeView()
                self.changeErrorLabelValue('Item added successfully', 'Green')
            except sqlite3.IntegrityError as err:
                self.changeErrorLabelValue('Item already in database', 'Red')
        else:
            self.changeErrorLabelValue('Enter Item Name and Price', 'Red')
    
    def updateItem(self): 
        itemName = self.itemNameEntry.get()
        itemPrice = float(self.itemPrice.get()) if self.itemPrice.get() else None
        if itemName and itemPrice:
            query = f"UPDATE {Constants.DB_TABLE_ITEMS} SET NAME = '{itemName}', PRICE = {itemPrice} WHERE NAME = '{self.currentTreeSelection['values'][0]}'"
            try:
                Helper.executeQuery(query)
                print(query)
                self.loadTreeView()
                self.clearSelection()
                self.changeErrorLabelValue('Item Updated Successfully', 'Green')
            except sqlite3.IntegrityError as err:
                messagebox.showerror('Error', 'Item already in database', icon='error')
        else:
            self.changeErrorLabelValue('Select an Item for Updation (Double Click)', 'Red')
    
    def deleteItem(self):
        if len(self.itemTView.selection()) > 0:
            response = messagebox.askquestion('Delete', f'Are you sure you want to delete {len(self.itemTView.selection())} items')
            if response == 'yes':
                for x in self.itemTView.selection():
                    itemName, _ = self.itemTView.item(x)['values']
                    query = f"DELETE FROM {Constants.DB_TABLE_ITEMS} WHERE NAME = '{itemName}'"
                    print(query)
                    Helper.executeQuery(query)
                self.clearSelection()
                self.loadTreeView()
                self.changeErrorLabelValue('Item deleted successfully', 'Green')
        else:
            self.changeErrorLabelValue('Select one or more Items for Deletion (CTRL + Click for multiple selection)', 'Red')
    
    def changeErrorLabelValue(self, message, color):
        self.errorLabelValue['foreground'] = color
        self.errorLabelValue['text'] = message
    
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