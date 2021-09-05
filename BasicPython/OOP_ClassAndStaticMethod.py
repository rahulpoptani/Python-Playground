class Employee:
    
    raise_amt = 1.04
    num_of_employees = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_employees += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    # alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # If you are not using self or cls reference, then its a regular method and should be static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Alpaca', 'User', 3000)
emp_2 = Employee('Some', 'User', 2000)

print(Employee.num_of_employees)

print(Employee.raise_amt)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)

# -----------------------------------------------

emp_str_1 = 'John-Dave-2200'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.__dict__)

# -----------------------------------------------

import datetime
my_date = datetime.date(2021, 9, 2)

print(Employee.is_workday(my_date))