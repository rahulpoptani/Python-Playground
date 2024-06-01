import sqlite3

class Helper:
    def dataBootstrap():
        print('Data Bootstrapping Started')
        with sqlite3.connect('AddressBook/helper/database.db') as con:
            cur = con.cursor()
            res = cur.execute("SELECT * FROM SQLITE_MASTER WHERE TBL_NAME = 'PEOPLE'")
            if len(res.fetchall()) == 0:
                cur.execute('CREATE TABLE PEOPLE(PEOPLE_ID INTEGER PRIMARY KEY AUTOINCREMENT, FNAME TEXT, LNAME TEXT, EMAIL TEXT, PHONE TEXT, ADDRESS TEXT)')
                con.commit()
                print('Create table: PEOPLE')
            else:
                print('Table: PEOPLE, already exits. Skipping table creation')
        print('Data Bootstrapping Finished')
    
    def getDBCursor():
        connection = sqlite3.connect('AddressBook/helper/database.db')
        cursor = connection.cursor()
        return cursor
    
    def executeQuery(query, args = ()):
        with sqlite3.connect('AddressBook/helper/database.db') as con:
            cur = con.cursor()
            try:
                if args: return cur.execute(query, args).fetchall()
                else: return cur.execute(query).fetchall()
            except Exception as e:
                print(e)
    
    
    

# Helper.executeQuery('DROP TABLE PEOPLE')
# Helper.dataBootstrap()


# 
# Helper.executeQuery(query, ('Fname1','Lname1', 'fname1lname1@gmail.com', '0001', 'loc1'))
# Helper.executeQuery(query, ('Fname2','Lname2', 'fname2lname2@gmail.com', '0002', 'loc2'))
# Helper.executeQuery(query, ('Fname3','Lname3', 'fname3lname3@gmail.com', '0003', 'loc3'))
