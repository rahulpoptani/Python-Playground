import json
from tkinter import *
from tkinter import ttk, messagebox
from docxtpl import DocxTemplate
from datetime import datetime
from Helper import Helper
from Constants import Constants

class Order(Toplevel):
    CURR_DIR = '/'.join(__file__.split('/')[:-1])
    def __init__(self):
        Toplevel.__init__(self)
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f'{screenWidth}x{screenHeight}')
        self.title('Order')
        self.bind('<Escape>', lambda x: self.closeWindow())

        # TopFrame
        self.topFrame = LabelFrame(self, text='', bg=Constants.TOPFRAME_BG)
        self.topFrame.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        self.backImage = Helper.getImage(f'{Order.CURR_DIR}/IMG_Back.png')
        self.backButton = Button(self.topFrame, text='Back', image=self.backImage, height=Constants.BIG_BUTTON_HEIGHT, font=Constants.BIG_BUTTON_FONT, compound=LEFT, command=self.destroy)
        self.backButton.pack(side=LEFT, padx=10, pady=10)
        
        self.orderHistoryImage = Helper.getImage(f'{Order.CURR_DIR}/IMG_Order_History.png')
        self.orderHistoryButton = Button(self.topFrame, text='Order History', image=self.orderHistoryImage, height=Constants.BIG_BUTTON_HEIGHT, font=Constants.BIG_BUTTON_FONT, compound=LEFT)
        self.orderHistoryButton.pack(side=RIGHT, padx=10, pady=10)

        # Bottom Left Frame
        self.bottomLeftFrame = LabelFrame(self, text='')
        self.bottomLeftFrame.pack(padx=10, pady=10, side=LEFT, fill=BOTH, expand=True)
        self.bottomLeftFrame.bind('<Button 1>', lambda x: self.clearSelection())

        # Bottom Left Top Frame
        self.bottomLeftTopFrame = LabelFrame(self.bottomLeftFrame, text='Order Details')
        self.bottomLeftTopFrame.pack(padx=10, pady=10, side=TOP, fill=BOTH, expand=True)

        self.style = ttk.Style()
        self.style.configure('Treeview.Heading', font=Constants.LISTBOX_FONT)
        self.style.configure('Treeview', font=Constants.LISTBOX_FONT, rowheight=30)

        self.itemTViewOrder = ttk.Treeview(self.bottomLeftTopFrame, columns=(1,2,3,4), show='headings')
        self.itemTViewOrder.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.itemTViewOrder.heading(1, text='Item')
        self.itemTViewOrder.heading(2, text='Price')
        self.itemTViewOrder.heading(3, text='Quantity')
        self.itemTViewOrder.heading(4, text='Total')
        self.itemTViewOrder.column(1, anchor=CENTER, minwidth=20)
        self.itemTViewOrder.column(2, anchor=CENTER, minwidth=5, width=10)
        self.itemTViewOrder.column(3, anchor=CENTER, minwidth=5, width=10)
        self.itemTViewOrder.column(4, anchor=CENTER, minwidth=5, width=10)
        self.itemTViewOrder.bind('<Double 1>', self.updateEntryBoxes)

        # Bottom Left Middle Frame
        self.bottomLeftMiddleFrame = LabelFrame(self.bottomLeftFrame, text='Add / Update Items')
        self.bottomLeftMiddleFrame.pack(padx=10, pady=10, side=TOP, fill=BOTH)

        self.itemLabelName = Label(self.bottomLeftMiddleFrame, font=Constants.ENTRY_FONT, text='Item:')
        self.itemLabelName.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)
        self.itemLabelValue = Label(self.bottomLeftMiddleFrame, font=Constants.ENTRY_FONT, text=' ')
        self.itemLabelValue.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)
        
        self.itemEntryPrice = Entry(self.bottomLeftMiddleFrame, font=Constants.ENTRY_FONT)
        self.itemEntryPrice.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)
        
        self.itemEntryQty = Entry(self.bottomLeftMiddleFrame, font=Constants.ENTRY_FONT)
        self.itemEntryQty.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

        self.itemLabelTotalName = Label(self.bottomLeftMiddleFrame, font=Constants.ENTRY_FONT, text='Total:')
        self.itemLabelTotalName.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)
        self.itemLabelTotalValue = Label(self.bottomLeftMiddleFrame, font=Constants.ENTRY_FONT, text=' ')
        self.itemLabelTotalValue.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

        self.itemButtonUpdate = Button(self.bottomLeftMiddleFrame, text='Update', font=Constants.OPTION_BUTTON_FONT, height=2, command=self.updateOrderTreeView)
        self.itemButtonUpdate.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)
        
        self.itemButtonDelete = Button(self.bottomLeftMiddleFrame, text='Delete', font=Constants.OPTION_BUTTON_FONT, height=2, command=self.deleteOrderTreeView)
        self.itemButtonDelete.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)
        
        # Bottom Left Bottom Frame
        self.bottomLeftBottomFrame = LabelFrame(self.bottomLeftFrame, text='Order Summary')
        self.bottomLeftBottomFrame.pack(padx=10, pady=10, side=TOP, fill=BOTH)

        self.generateInvoiceButton = Button(self.bottomLeftBottomFrame, text='Generate Invoice', font=Constants.OPTION_BUTTON_FONT, height=2, command=self.generateInvoice)
        self.generateInvoiceButton.pack(side=RIGHT, padx=10, pady=10, fill=X)
        
        self.totalValue = Label(self.bottomLeftBottomFrame, text='0.0', font=Constants.ENTRY_FONT)
        self.totalValue.pack(side=RIGHT, padx=(0,20), pady=10)
        self.totalName = Label(self.bottomLeftBottomFrame, text='Total:', font=Constants.ENTRY_FONT)
        self.totalName.pack(side=RIGHT, padx=10, pady=10)
        
        self.totalItemsValue = Label(self.bottomLeftBottomFrame, text='0', font=Constants.ENTRY_FONT)
        self.totalItemsValue.pack(side=RIGHT, padx=(0,20), pady=10)
        self.totalItemsName = Label(self.bottomLeftBottomFrame, text='Items:', font=Constants.ENTRY_FONT)
        self.totalItemsName.pack(side=RIGHT, padx=10, pady=10)

        self.buyerNameLabel = Label(self.bottomLeftBottomFrame, text='Buyer:', font=Constants.ENTRY_FONT)
        self.buyerNameLabel.pack(side=LEFT, padx=10, pady=10)
        self.buyerNameValue = Entry(self.bottomLeftBottomFrame, font=Constants.ENTRY_FONT, width=25)
        self.buyerNameValue.pack(side=LEFT, padx=10, pady=10, fill=X)

        # Error Label
        self.errorLabelName = Label(self.bottomLeftFrame, text='Message: ', foreground='Black')
        self.errorLabelName.pack(padx=10, pady=10, side=LEFT, fill=BOTH)
        self.errorLabelValue = Label(self.bottomLeftFrame, text='')
        self.errorLabelValue.pack(pady=10, side=LEFT, fill=BOTH)

        # Bottom Right Frame
        self.bottomRightFrame = LabelFrame(self, text='Inventory')
        self.bottomRightFrame.pack(padx=(0,10), pady=10, side=RIGHT, fill=BOTH)

        self.searchEntry = Entry(self.bottomRightFrame, font=Constants.ENTRY_FONT, width=50)
        self.searchEntry.insert(0, 'Search Item')
        self.searchEntry.bind('<FocusIn>', lambda x: self.searchEntry.delete(0, END))
        self.searchEntry.bind('<Return>', lambda x: self.updateSearchResults())
        self.searchEntry.pack(padx=10, pady=10, fill=X)

        self.itemTView = ttk.Treeview(self.bottomRightFrame, columns=(1,2), show='headings')
        self.itemTView.heading(1, text='Item')
        self.itemTView.heading(2, text='Price')
        self.itemTView.column(1, anchor=CENTER, minwidth=20)
        self.itemTView.column(2, anchor=CENTER, minwidth=5, width=10)
        self.itemTView.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.itemTView.bind('<Double 1>', self.pushToMainTree)

        self.loadTreeView()
        
    def updateInventoryTreeView(self, resultSet):
        self.itemTView.delete(*self.itemTView.get_children())
        for result in resultSet:
            self.itemTView.insert('', END, values=result)

    def loadTreeView(self):
        resultSet = Helper.executeQuery('SELECT NAME, PRICE FROM ITEMS ORDER BY NAME')
        self.updateInventoryTreeView(resultSet)
    
    def updateSearchResults(self): 
        searchText = self.searchEntry.get()
        query = f'SELECT NAME, PRICE FROM ITEMS WHERE LOWER(NAME) LIKE LOWER("%{searchText}%") ORDER BY NAME'
        resultSet = Helper.executeQuery(query)
        self.updateInventoryTreeView(resultSet)
    
    def populateTotalSumAndItems(self):
        totalSum = 0
        totalItems = 0
        for child in self.itemTViewOrder.get_children():
            item, price, quantity, total = self.itemTViewOrder.item(child)['values']
            totalSum += float(price) * int(quantity)
            totalItems += int(quantity)
        self.totalValue['text'] = totalSum
        self.totalItemsValue['text'] = totalItems
    
    def pushToMainTree(self, event): 
        self.currentInventoryTreeSelection = self.itemTView.item(self.itemTView.focus())
        item, price = self.currentInventoryTreeSelection['values']
        if item not in [ self.itemTViewOrder.item(child)['values'][0] for child in self.itemTViewOrder.get_children() ]:
            self.itemTViewOrder.insert('', END, values=[item, price, 1, price])
            self.populateTotalSumAndItems()
    
    def updateEntryBoxes(self, event): 
        # print([ [child, self.itemTViewOrder.item(child)['values']] for child in self.itemTViewOrder.get_children() ])
        self.currentOrderTreeSelection = self.itemTViewOrder.item(self.itemTViewOrder.focus())
        item, price, quantity, total = self.currentOrderTreeSelection['values']
        self.itemLabelValue['text'] = item
        self.itemEntryPrice.delete(0, END)
        self.itemEntryQty.delete(0, END)
        self.itemEntryPrice.insert(0, price)
        self.itemEntryQty.insert(0, quantity)
        self.itemLabelTotalValue['text'] = price * quantity
    
    def updateOrderTreeView(self):
        if self.itemEntryPrice.get() and self.itemEntryQty.get():
            if int(self.itemEntryQty.get()) > 0:
                currentTVOrderList = [ [child, self.itemTViewOrder.item(child)['values']] for child in self.itemTViewOrder.get_children() ]
                for idx, (id, (name, price, qty, total)) in enumerate(currentTVOrderList):
                    # print(id, name, price, qty, total, self.itemLabelValue['text'])
                    if name == self.itemLabelValue['text']:
                        self.itemTViewOrder.delete(id)
                        self.itemTViewOrder.insert('', idx, values=[name, float(self.itemEntryPrice.get()), int(self.itemEntryQty.get()), (float(self.itemEntryPrice.get()) * int(self.itemEntryQty.get()))])
                        self.clearSelection()
                        self.changeErrorLabelValue('Item Updated Successfully', 'Green')
                        break
                self.populateTotalSumAndItems()
            else:
                self.changeErrorLabelValue('Quantity cannot be less than or equal to 0', 'Red')    
        else:
            self.changeErrorLabelValue('Select an Item for Updation (Double Click)', 'Red')
    
    def deleteOrderTreeView(self):
        if len(self.itemTViewOrder.selection()) > 0:
            response = messagebox.askquestion('Delete', f'Are you sure you want to delete {len(self.itemTViewOrder.selection())} items')
            if response == 'yes':
                for x in self.itemTViewOrder.selection():
                    self.itemTViewOrder.delete(x)
                    self.populateTotalSumAndItems()
                self.changeErrorLabelValue('Items Deleted', 'Green')
        else:
            self.changeErrorLabelValue('Select one or more Items for Deletion (CTRL + Click for multiple selection)', 'Red')
    
    def clearSelection(self):
        self.itemTView.selection_remove(self.itemTView.selection())
        self.itemTViewOrder.selection_remove(self.itemTViewOrder.selection())
        self.itemLabelValue['text'] = ''
        self.itemLabelTotalValue['text'] = ''
        self.itemEntryPrice.delete(0, END)
        self.itemEntryQty.delete(0, END)
    
    def generateInvoice(self): 
        if len(self.itemTViewOrder.get_children()):
            if self.buyerNameValue.get().strip():
                current_timestamp = int((datetime.now() - datetime(1970,1,1)).total_seconds())
                buyerName = self.buyerNameValue.get().strip()
                totalSum = 0
                totalItems = 0
                items = []
                for child in self.itemTViewOrder.get_children():
                    item, price, quantity, total = self.itemTViewOrder.item(child)['values']
                    items.append([item, price, quantity, total])
                    totalSum += float(price) * int(quantity)
                    totalItems += int(quantity)
                doc = DocxTemplate(f"{Order.CURR_DIR}/BillingTemplate.docx")                
                doc.render({"name": buyerName, "items": items, "count": totalItems, "total": totalSum})
                filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{buyerName}.docx"
                doc.save(filename)
                messagebox.showinfo('Info', f'Invoice Generated \n{filename}')
                self.changeErrorLabelValue(f'Invoice Generated! (File: {filename})', 'Green')

                # Save Information Into Order Table
                try:
                    query = f'INSERT INTO {Constants.DB_TABLE_ORDERS} (BUYER, TOTALITEMS, SUBTOTAL, ITEMS, TIME) VALUES (?, ?, ?, ?, ?)'
                    Helper.executeQuery(query, (buyerName, totalItems, totalSum, json.dumps(items), current_timestamp))
                except Exception as e:
                    self.changeErrorLabelValue(e, 'Red')
            else:
                self.changeErrorLabelValue('Enter Buyer Name', 'Red')    
        else:
            self.changeErrorLabelValue('Add Items to order', 'Red')

    def changeErrorLabelValue(self, message, color):
        self.errorLabelValue['foreground'] = color
        self.errorLabelValue['text'] = message
    
    def closeWindow(self): self.destroy()

def main():
    root = Tk()
    app = Order()
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