
person = {'name' : 'Rahul', 'age': 31}
sentence = 'My name is {} and I\'m {} years old'.format(person['name'], person['age'])
print(sentence)

sentence = 'My name is {0} and I\'m {1} years old'.format(person['name'], person['age'])
print(sentence)

sentence = 'My name is {0[name]} and I\'m {0[age]} years old'.format(person)
print(sentence)

sentence = 'My name is {name} and I\'m {age} years old'.format(age=31, name='Rahul')
print(sentence)

# Accessing element from list
l = ['Rahul', 31]
sentence = 'My name is {0[0]} and I\'m {0[1]} years old'.format(l)
print(sentence)

# Accessing from class variable
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Rahul', 31)

sentence = 'My name is {0.name} and I\'m {0.age} years old'.format(p1)
print(sentence)

sentence = 'My name is {name} and I\'m {age} years old'.format(**person)
print(sentence)

# Pad zero to single digits
for i in range(1,11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

# Print till 2 decimal places
pi = 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)

# Comma seperated values with 2 decimal places
sentence = '1MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)

# Print dates
import datetime
my_date = datetime.datetime(2021, 9, 9, 12, 30, 10)
print(my_date)
print('{:%B %d, %Y}'.format(my_date))
print('{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)) # 0 is added before format to refer my_date placeholder, otherwise we have to provide my_date three times