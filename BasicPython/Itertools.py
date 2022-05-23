import itertools

counter = itertools.count(start=5, step=5)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


counter = itertools.cycle([1,2,3])


# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


counter = itertools.cycle(('On', 'Off'))


# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


counter = itertools.repeat(2, times=3)

for x in counter:
    # print(x)
    pass


##########################################################################

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.combinations(letters, 2) # works all combination like a,b but not b,a
# result = itertools.permutations(letters, 2) # view all permutations like a,b and b,a

for item in result:
    # print(item)
    pass

# Create a 4 digit code Product function will allow repeat

result = itertools.product(numbers, repeat=4)

for item in result:
    # print(item)
    pass


# Equivalent to product method
result = itertools.combinations_with_replacement(numbers, 4)

for item in result:
    # print(item)
    pass


###################

# chaining multiple list together

# combined = letters + numbers + names
combined = itertools.chain(letters +  numbers + names)

for item in combined:
    # print(item)
    pass


result = itertools.islice(range(10), 1, 5) # it also allows step
# Why this is usefull when you can easily slice a list? - Lets say you reading something big
# converting into list will take memory, instead when you need a slice can easily slice the required from the iterator and use 
# Useful for reading big files where you dont want to load in memory

for item in result:
    # print(item)
    pass



letters = ['a', 'b', 'c', 'd']
selector = [True, True, False, True]
result = itertools.compress(letters, selector)
for item in result:
    # print(item)
    pass
# Returned value a, b, and d but NOT c because its coresponding selector is false

# Another aproach 
def lt_2(n):
    if n < 2:
        return True
    else:
        return False



import operator
numbers1 = [1,2,3,4]

# Running total
result = itertools.accumulate(numbers1, operator.add)
for item in result:
    # print(item)
    pass


# Running Multiply
result = itertools.accumulate(numbers1, operator.mul)
for item in result:
    # print(item)
    pass



################################################################################################################

def get_state(person):
    return person['state']

people = [
    {
        'name': 'John',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Nicole',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jane',
        'city': 'Faketown',
        'state': 'NC'
    }
]

person_group = itertools.groupby(people, get_state)

for state, group in person_group:
    print(state)
    for people in group:
        print(people)
        pass
