import sqlite3
from SqlLite3_Employee import Employee

# conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:') # creates inmemory database

c = conn.cursor()

c.execute("""
create table employees (
    first text,
    last text,
    pay integer
    )
""")

# c.execute("insert into employees values ('Marry', 'Schafer', 5000)")

# c.execute("select * from employees")
# print(c.fetchall())

#########################################################################################################

emp_1 = Employee('John', 'Doe', 8000)
emp_2 = Employee('Jane', 'Doe', 9000)

# There are two approches of pushing the data into DB
# First Approach: Values as tupple
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()

# Second Approach: Values as dictionary placeholders
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})
# conn.commit()

# c.execute("select * from employees where last = :last", {'last': 'Doe'})
# print(c.fetchall())

# conn.close()


#########################################################################################################

# Try using context manager which takes care of commit and rollback of transaction automatically. No explicit commit required
# Context managers (connection in this case, file handler in case of files, etc.) are used as "with something:"

def insert_emp(emp):
    with conn: # with connection
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""", 
                    {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})



insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 9500)

remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

# conn.close()
