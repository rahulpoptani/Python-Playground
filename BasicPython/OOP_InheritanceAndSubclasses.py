class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amt = 1.5

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())



dev_1 = Developer('FirstName1', 'LastName1', 1000, 'Python')
dev_2 = Developer('FirstName2', 'LastName2', 2000, 'Java')

print(dev_1.email)
print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise() # picked the raise_amt value from Developer class but functionality from parent class Employee
print(dev_1.pay)

print(dev_1.prog_lang)
print(dev_2.prog_lang)


mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])

print(mgr_1.email)
print('-------------------------------')
mgr_1.print_emps()

mgr_1.add_emp(dev_2)
print('-------------------------------')
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
print('-------------------------------')
mgr_1.print_emps()


print(isinstance(mgr_1, Manager)) # True 
print(isinstance(mgr_1, Employee)) # True - Because Manager is inherited from Employee
print(isinstance(mgr_1, Developer)) # False 

print('-------------------------------')

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
