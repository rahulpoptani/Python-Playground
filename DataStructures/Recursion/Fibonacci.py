def fibonacci(n):
    if n < 1:
        return -1
    if n == 1 or n == 2:
       return n-1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...


# 5th Element: 3
print(fibonacci(5))

# 10th Element: 34
print(fibonacci(10))