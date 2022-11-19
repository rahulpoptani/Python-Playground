'''
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.
For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Given a positive integer N, returns the number of its factors.
For example, given N = 24, the function should return 8, because 24 has 8 factors, 
namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.
'''

from math import sqrt

def solution(N):
    factors = 0
    for x in range(1, int(sqrt(N))+1):
        if N % x == 0:
            if sqrt(N) != x:
                factors += 2
            else:
                factors += 1
    return factors

print(solution(24))
print(solution(36))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
