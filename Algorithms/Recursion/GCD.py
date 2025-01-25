# Greatest Common Divisor
# gcd(m,n) = 
# m, if m == n
# gcd(m-n, n), if m > n
# gcd(m, n-m), if m < n

def gcd(value1, value2):
    if value1 == value2:
        return value1
    if value1 > value2:
        return gcd(value1 - value2, value2)
    else:
        return gcd(value1, value2 - value1)


print(f'GCD({42},{56}): {gcd(42,56)}')