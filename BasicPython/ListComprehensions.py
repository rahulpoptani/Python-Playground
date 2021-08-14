# Traditional way to copy a list into list
nums = [1,2,3,4,5,6,7,8,9]
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)


# Using List Comprehensions
my_list_com = [ n for n in nums ]
print(my_list_com)


# Using Lambda
my_list_lambda = map(lambda n: n+1, nums)
print(list(my_list_lambda))


# Traditional way - filter even numbers from list
my_list_even = []
for n in nums:
    if n%2 == 0:
        my_list_even.append(n)
print(my_list_even)


# Using list comprehension
my_list_even_list_com = [ n for n in nums if n%2 == 0 ]
print(my_list_even_list_com)

# Using Lambda way for filter
my_list_even_lambda = list(filter(lambda x: x%2 == 0, nums))
print(my_list_even_lambda)


# Create list using nested loops
my_nested_list = []
for letter in 'abcd':
    for num in range(4):
        my_nested_list.append((letter, num))
print(my_nested_list)

# Using List Comprehensions
my_nested_list_com = [ (letter, num) for letter in 'abcd' for num in range(4) ]
print(my_nested_list_com)


# Dictionay Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(list(zip(names, heros)))

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

my_dict_com = { name: hero for name, hero in zip(names, heros) }
print(my_dict_com)



# Create a set of unique numbers
nums = [1,1,1,1,3,4,3,4,3,2,5,5]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)


# Using comprehension
my_set_com = {n for n in nums}
print(my_set_com)




