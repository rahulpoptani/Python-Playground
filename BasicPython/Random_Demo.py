import random


value = random.randint(1, 10)
print(value)


greetings = ['Hello', 'Hi', 'Hey']
value = random.choice(greetings)
print(value)


greetings = ['Hello', 'Hi', 'Hey']
value = random.choices(greetings, k=5) # k=5 means, pick 5 random values from list
print(value)


greetings = ['Red', 'Black', 'Green']
value = random.choices(greetings, weights=[18, 18, 2], k=5) # 18+18+2 = 38 -> Here, Red has 18/36 chance of getting selected
print(value)