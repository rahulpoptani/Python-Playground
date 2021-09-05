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
    
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
    
    # When we add two employees together, it will give combine pay
    def __add__(self, other):
        return self.pay + other.pay
    
    # override length method to return length of fullname
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 1000)
emp_2 = Employee('Test', 'Employee', 2000)

print(repr(emp_1))
print(str(emp_1))

# Same can be called like this

print(emp_1.__repr__())
print(emp_1.__str__())


print(emp_1) # naked call to object will try to find str method if not found will fallback to repr


# Integer and Strings have thier own dunder methods

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))


print(emp_1 + emp_2)


# Length of fullname using dunder method
print(len(emp_1)) 