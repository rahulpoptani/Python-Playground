
# Traditional way
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)


# Using Yield - Generator do not hold the entire result in memory, it yeild one result at a time
def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums_yield = square_numbers([1,2,3,4,5])
for num in my_nums_yield:
    print(num)


# Generator way - Generators are better with performance because its not holding all the values in memory
my_nums_gen = ( x*x for x in [1,2,3,4,5] ) # this will return generator object
print(list(my_nums_gen)) # you will lose the performance if you convert to list

