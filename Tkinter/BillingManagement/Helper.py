from tkinter import *
import sqlite3
from Constants import Constants

class Helper:
    def getImage(name: str) -> PhotoImage:
        return PhotoImage(file=f'{name}')
    
    def dataBootstrap():
        print('Data Bootstrapping Started')
        with sqlite3.connect('./database.db') as con:
            cur = con.cursor()
            # Table: ITEMS
            res = cur.execute(f"SELECT * FROM SQLITE_MASTER WHERE TBL_NAME = '{Constants.DB_TABLE_ITEMS}'")
            if len(res.fetchall()) == 0:
                cur.execute(f'CREATE TABLE {Constants.DB_TABLE_ITEMS} (NAME TEXT PRIMARY KEY, PRICE FLOAT)')
                con.commit()
                print(f'Create table: {Constants.DB_TABLE_ITEMS}')
            else:
                print(f'Table: {Constants.DB_TABLE_ITEMS}, already exits. Skipping table creation')
            # Table: ORDERS
            res = cur.execute(f"SELECT * FROM SQLITE_MASTER WHERE TBL_NAME = '{Constants.DB_TABLE_ORDERS}'")
            if len(res.fetchall()) == 0:
                cur.execute(f'CREATE TABLE {Constants.DB_TABLE_ORDERS} (BUYER TEXT, TOTALITEMS INTEGER, SUBTOTAL FLOAT, ITEMS TEXT, TIME INTEGER)')
                con.commit()
                print(f'Create table: {Constants.DB_TABLE_ORDERS}')
            else:
                print(f'Table: {Constants.DB_TABLE_ORDERS}, already exits. Skipping table creation')
        print('Data Bootstrapping Finished')
    
    def executeQuery(query, args = ()):
        with sqlite3.connect('./database.db') as con:
            cur = con.cursor()
            if args: return cur.execute(query, args).fetchall()
            else: return cur.execute(query).fetchall()
    
    def getDBCursor():
        connection = sqlite3.connect('./database.db')
        cursor = connection.cursor()
        return cursor


# Helper.executeQuery(f'DROP TABLE {Constants.DB_TABLE_ITEMS}')
# Helper.executeQuery(f'DROP TABLE {Constants.DB_TABLE_ORDERS}')
# Helper.dataBootstrap()