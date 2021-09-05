
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return 'First: {} | Last: {} | Pay: {} | Email: {}'.format(self.first, self.last, self.pay, self.email)
        

print(Employee.num_of_emps)

emp_1 = Employee('Rahul', 'P', 123)
emp_2 = Employee('Test', 'T', 234)

print(Employee.num_of_emps)

