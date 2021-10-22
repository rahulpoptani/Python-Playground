import itertools, operator

nums = [1,2,3,4,5]

# Cummulative Sum
result = itertools.accumulate(nums, operator.add)

for x in result:
    print(x)


# Cummulative Multiplication
result = itertools.accumulate(nums, operator.mul)

for x in result:
    print(x)