def factorial(n):
    if n == 0:
        return 1
    return (n * factorial(n-1))

print(factorial(0))

print(factorial(1))

# 5! = 5 * 4 * 3 * 2 * 1 = 120
print(factorial(5))
