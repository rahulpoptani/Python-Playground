'''
Two positive integers N and M are given. 
Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.
'''

def gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)

def solution(N,M):
    return int(N / gcd(N,M))

def solution2(N, M):
    chocolatesEaten = 0
    chocolatesAvailable = [1] * N
    pointer = 0
    while True:
        if chocolatesAvailable[pointer] == 1:
            chocolatesAvailable[pointer] = 0
            chocolatesEaten += 1
            pointer = (pointer + M) % N
        else:
            break
    return chocolatesEaten

print(solution(10, 4))
