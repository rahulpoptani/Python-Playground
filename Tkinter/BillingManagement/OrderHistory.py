import json
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from Constants import Constants
from Helper import Helper

class OrderHistory(Toplevel):
    CURR_DIR = '/'.join(__file__.split('/')[:-1])
    def __init__(self):
        Toplevel.__init__(self)
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f'{screenWidth}x{screenHeight}')
        self.title('Order History')
        self.bind('<Escape>', lambda x: self.closeWindow())

        # Top Frame
        self.topFrame = LabelFrame(self, text='', bg=Constants.TOPFRAME_BG)
        self.topFrame.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        self.backImage = Helper.getImage(f'{OrderHistory.CURR_DIR}/IMG_Back.png')
        self.backButton = Button(self.topFrame, text='Back', image=self.backImage, height=Constants.BIG_BUTTON_HEIGHT, font=Constants.BIG_BUTTON_FONT, compound=LEFT, command=self.destroy)
        self.backButton.pack(side=LEFT, padx=10, pady=10)
        
        # Bottom Frame
        self.upperBottomFrame = LabelFrame(self, text='Order History')
        self.upperBottomFrame.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        
        self.style = ttk.Style()
        self.style.configure('Treeview.Heading', font=Constants.LISTBOX_FONT)
        self.style.configure('Treeview', font=Constants.LISTBOX_FONT, rowheight=30)

        self.orderHistoryTV = ttk.Treeview(self.upperBottomFrame, columns=(1,2,3,4,5), show='headings')
        self.orderHistoryTV.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.orderHistoryTV.heading(1, text='Date')
        self.orderHistoryTV.heading(2, text='Buyer')
        self.orderHistoryTV.heading(3, text='Items')
        self.orderHistoryTV.heading(4, text='Total Items')
        self.orderHistoryTV.heading(5, text='Sub Total')
        self.orderHistoryTV.column(1, anchor=CENTER)
        self.orderHistoryTV.column(2, anchor=CENTER)
        self.orderHistoryTV.column(3, anchor=CENTER, minwidth=500, stretch=True)
        self.orderHistoryTV.column(4, anchor=CENTER)
        self.orderHistoryTV.column(5, anchor=CENTER)
        
        self.loadOrderHistory()

        # Lower Bottom Frame
        self.lowerbottomFrame = LabelFrame(self, text='Order Operations')
        self.lowerbottomFrame.pack(side=BOTTOM, padx=10, pady=10, fill=BOTH)

        self.orderSearchLabel = Label(self.lowerbottomFrame, text='Search: ', foreground='Black')
        self.orderSearchLabel.pack(padx=10, pady=10, side=LEFT, fill=BOTH)

        self.orderSearchEntry = Entry(self.lowerbottomFrame, font=Constants.ENTRY_FONT, width=50)
        self.orderSearchEntry.pack(padx=10, pady=10, side=LEFT)
        self.orderSearchEntry.bind('<Return>', lambda x: self.updateSearchResults())
        
        self.itemButtonDelete = Button(self.lowerbottomFrame, text='Delete', font=Constants.OPTION_BUTTON_FONT, height=2, command=self.deleteOrderHistory)
        self.itemButtonDelete.pack(side=LEFT, padx=10, pady=10)

    def updateOrderHistoryTV(self, resultSet):
        self.orderHistoryTV.delete(*self.orderHistoryTV.get_children())
        for result in resultSet:
            time, buyer, items, totalItems, subTotal = result
            time = datetime.fromtimestamp(time)
            items = json.loads(items)
            for itemName, itemPrice, itemQty, itemSubTotal in items:
                currentItem = f'Item={itemName} | Price={itemPrice} | Qty={itemQty} | SubTotal={itemSubTotal}'
                self.orderHistoryTV.insert('', END, values=[time, buyer, currentItem, totalItems, subTotal])
    
    def loadOrderHistory(self):
        resultSet = Helper.executeQuery(f'SELECT TIME, BUYER, ITEMS, TOTALITEMS, SUBTOTAL FROM {Constants.DB_TABLE_ORDERS} ORDER BY TIME DESC')
        self.updateOrderHistoryTV(resultSet)
    
    def deleteOrderHistory(self):
        if len(self.orderHistoryTV.selection()) > 0:
            response = messagebox.askquestion('Delete', f'Are you sure you want to delete?')
            if response == 'yes':
                for x in self.orderHistoryTV.selection():
                    orderTime, buyerName, items, totalItems, subTotal = self.orderHistoryTV.item(x)['values']
                    orderTime = int(datetime.strptime(orderTime, '%Y-%m-%d %H:%M:%S').timestamp())
                    query = f"DELETE FROM {Constants.DB_TABLE_ORDERS} WHERE TIME = '{orderTime}' and BUYER = '{buyerName}'"
                    print(query)
                    Helper.executeQuery(query)
                self.loadOrderHistory()
        else:
            pass
    
    def updateSearchResults(self):
        searchText = self.orderSearchEntry.get()
        query = f'SELECT TIME, BUYER, ITEMS, TOTALITEMS, SUBTOTAL FROM {Constants.DB_TABLE_ORDERS} WHERE LOWER(BUYER) LIKE LOWER("%{searchText}%") ORDER BY TIME DESC'
        resultSet = Helper.executeQuery(query)
        self.updateOrderHistoryTV(resultSet)
    
    def closeWindow(self): self.destroy()

# def main():
#     root = Tk()
#     app = OrderHistory()
#     app.attributes('-topmost',True)
#     screenWidth = root.winfo_screenwidth()
#     screenHeight = root.winfo_screenheight()
#     root.geometry(f'{screenWidth}x{screenHeight}')
#     root.resizable(False, False)
#     root.bind('<Escape>', lambda x: closeWindow(root))
#     root.mainloop()

# def closeWindow(self): self.destroy()

# if __name__ == '__main__':
#     main()