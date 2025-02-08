'''
An important property of the remainder is that in addition, subtraction and multiplication, the remainder can be taken before the operation:
(a + b) mod m = (a mod m + b mod m) mod m
(a - b) mod m = (a mod m - b mod m) mod m
(a · b) mod m = (a mod m · b mod m) mod m
'''

# Factorial of a number, and take MOD

def modAfterMultiple(n, m):
    for i in range(1, n):
        n *= i
    return n % m

def modDuringMultiple(n, m):
    for i in range(1, n):
        n = (n*i) % m
    return n % m

print(modAfterMultiple(5, 7) == modDuringMultiple(5, 7))
print(modAfterMultiple(9, 11) == modDuringMultiple(9, 11))