li = [9,1,8,2,7,3,6,4,5]

li_sorted = sorted(li) # returns new list

print('Original: {}'.format(li))

print('Sorted: {}'.format(li_sorted))

# li.sort() # sort list inplace and return None

print('Original: {}'.format(li))

li_sorted_rev = sorted(li, reverse=True) # reverse sort

print('Reverse Sorted: {}'.format(li_sorted_rev))


# sort() does not work on tuple. Use sorted()

tup = (9,1,8,2,7,3,6,4,5)
tup_sorted = sorted(tup)

print('Original Tuple: {}'.format(tup))

print('Sorted Tuple: {}'.format(tup_sorted))



di = {'name': 'Rahul', 'job': 'Developer', 'age': 'None', 'os': 'Mac'}
di_sorted = sorted(di)

print('Original Dictionary: {}'.format(di))

print('Sorted Dictionay: {}'.format(di_sorted)) # sort the keys


# sort based on absolute values

li = [-6, -5, -4, 1, 2, 3]
li_s = sorted(li, key=abs) # key uses absolute function

print('Original List: {}'.format(li))

print('Sorted List: {}'.format(li_s)) 


# Key parameter useful for named objects

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Rahul', 20, 1000)
e2 = Employee('Sarah', 22, 800)
e3 = Employee('Carl', 24, 2000)

employees = [e1, e2, e3]

# When sorting objects, its necessary to create function which return the value used for sorting
def e_sort(emp):
    return emp.name

s_employee = sorted(employees, key = e_sort, reverse = True) # key is mandatory

print(s_employee)

# Another way using Lambda
s_employee = sorted(employees, key = lambda e: e.age, reverse = True) # key is mandatory

print(s_employee)


# Another approach using attrgetter where you specify the key. This eleminates the use of lambda function
from operator import attrgetter

s_employee = sorted(employees, key = attrgetter('salary'), reverse = True) # key is mandatory

print(s_employee)