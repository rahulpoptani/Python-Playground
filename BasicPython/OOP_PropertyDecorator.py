class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # this allow you to set the first name and last name values using the fullname setter method where we implement the assignments
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp1 = Employee('John', 'Smith')

emp1.first = 'Jim'

emp1.fullname = 'Mark Taylor'

print(emp1.first)
print(emp1.email) # instead of calling email(), calling email. Adding property decorator allow the method call as if its an attribute
print(emp1.fullname)

del emp1.fullname

print(emp1.first)
print(emp1.email) 
print(emp1.fullname)