from tkinter import *
import sqlite3
from helper.constants import Constants
# from constants import Constants

class Helper:
    def getImage(name: str) -> PhotoImage:
        return PhotoImage(file=f'BillingManagement/icons/{name}')
    
    def dataBootstrap():
        print('Data Bootstrapping Started')
        with sqlite3.connect('BillingManagement/helper/database.db') as con:
            cur = con.cursor()
            res = cur.execute(f"SELECT * FROM SQLITE_MASTER WHERE TBL_NAME = '{Constants.DB_TABLE_ITEMS}'")
            if len(res.fetchall()) == 0:
                cur.execute(f'CREATE TABLE {Constants.DB_TABLE_ITEMS}(NAME TEXT PRIMARY KEY, PRICE FLOAT, QUANTITY INTEGER)')
                con.commit()
                print(f'Create table: {Constants.DB_TABLE_ITEMS}')
            else:
                print(f'Table: {Constants.DB_TABLE_ITEMS}, already exits. Skipping table creation')
        print('Data Bootstrapping Finished')
    
    def executeQuery(query, args = ()):
        with sqlite3.connect('BillingManagement/helper/database.db') as con:
            cur = con.cursor()
            if args: return cur.execute(query, args).fetchall()
            else: return cur.execute(query).fetchall()
            # try:
            #     if args: return cur.execute(query, args).fetchall()
            #     else: return cur.execute(query).fetchall()
            # except sqlite3.DataError as er:
            #     print(er.args) 
    
    def getDBCursor():
        connection = sqlite3.connect('BillingManagement/helper/database.db')
        cursor = connection.cursor()
        return cursor
    
    def populateDummyData():
        import random, string
        query = f'INSERT INTO {Constants.DB_TABLE_ITEMS} (NAME, PRICE, QUANTITY) VALUES (?, ?, ?)'
        for x in range(10):
            itemName = 'Item-' + ''.join( [random.choice(string.ascii_letters).lower() for i in range(3)] )
            itemPrice = random.randint(10, 100)
            itemQty = random.randint(1, 20)
            # print(itemName, itemPrice, itemQty)
            Helper.executeQuery(query, (itemName, itemPrice, itemQty))


# Helper.dataBootstrap()

# Helper.executeQuery(f'DROP TABLE {Constants.DB_TABLE_ITEMS}')

# Helper.populateDummyData()

# print(Helper.executeQuery(f'SELECT ITEM_NAME, ITEM_PRICE, ITEM_QUANTITY FROM ITEMS WHERE LOWER(ITEM_NAME) LIKE "%r%"'))
# print(Helper.executeQuery('UPDATE ITEMS SET ITEM_NAME = "Item-rnl-LL" WHERE ITEM_NAME = "Item-rnl" '))
# print(Helper.executeQuery(f'SELECT ITEM_NAME, ITEM_PRICE, ITEM_QUANTITY FROM ITEMS WHERE LOWER(ITEM_NAME) LIKE "%r%"'))

