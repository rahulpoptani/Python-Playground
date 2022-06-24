'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def smallestMultiple(n):
    num = n
    while True:
        div = True
        for x in range(1, n+1):
            if num % x != 0:
                div = False
        if not div:
            num += 1
        else:
            return num

import math

def smallestMultiple2(n):
    result = 1
    for x in range(1, n+1):
        result *= x // math.gcd(x, result)
    return result

print(smallestMultiple2(10))
print(smallestMultiple2(20))
