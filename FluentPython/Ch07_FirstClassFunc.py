from functools import reduce

# factorial
def factorial(x):
    return reduce(lambda a, b: a*b, range(1, x+1))

def fibonaci(n):
    return reduce(lambda x, _: x + [ x[-1] + x[-2] ], range(n-2), [0, 1])

print(factorial(5))

print(fibonaci(5))