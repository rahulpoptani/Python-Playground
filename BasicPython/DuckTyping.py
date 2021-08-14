
# class Duck:
#     def quack(self):
#         print('Quack, quack')
#     def fly(self):
#         print('Flap, flap')

# # 1. Another class which behavous like Duck
# class Person:
#     def quack(self):
#         print('Quacking like a Duck')
#     def fly(self):
#         print('Flapping my Arms')

# def quack_and_fly(thing):
#     if isinstance(thing, Duck):
#         thing.quack()
#         thing.fly()
#     else:
#         print('Not Duck')
#     print()


# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)

# 2. Approach with LBYL

# def quack_and_fly_LBYL(thing):
#     # NON PYTHONIC Way. Look Before You Leap
#     if hasattr(thing, 'quack'):        # checks for attribute exists
#         if callable(thing.quack):      # checks is it callable
#             thing.quack()
#     if hasattr(thing, 'fly'):
#         if callable(thing.fly):
#             thing.fly()
#     print()


# quack_and_fly_LBYL(d)
# quack_and_fly_LBYL(p)


# def quack_and_fly_EAFP(thing):
#     # PYTHONIC Way. Easier to Ask Forgiveness than Permission
#     try:
#         thing.quack()
#         thing.fly()
#         thing.bark()    # throws attribute error
#         print()
#     except AttributeError as e:
#         print(e)

# quack_and_fly_EAFP(d)
# quack_and_fly_EAFP(p)


# Final Example:

person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}
# person = {'name': 'Jess', 'age': 23}

# LBYL (Non-Pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    # print('Name: {name} | Age: {age} | Job: {job}'.format(name = 'Rahul', age = 22, job = 'Dev'))
    print('Name: {name} | Age: {age} | Job: {job}'.format(**person))
else:
    print('Missing some keys')


# EAFP (Pythonic)
try:
    print('Name: {name} | Age: {age} | Job: {job}'.format(**person))
except KeyError as e:
    print('Missing {} key'.format(e))