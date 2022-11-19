'''
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. 
The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. 
These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:
    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20

The number of semiprimes within each of these ranges is as follows:

        (1, 26) is 10,
        (4, 10) is 4,
        (16, 20) is 0.

the function should return the values [10, 4, 0], as explained above.
'''

def solution(N, P, Q):
    semiprimes = [False] * (N+1)  # we will not be able to use 0 index, array should be 1 -> N. Hence N+1
    # 1. populate the list with numbers which are not prime
    for x in range(2, (N//2) + 1):
        for y in range(x*2, N+1, x): # multiple of 2s are not prime. Ex: 4,6,8..6,9,12..8,12,16..10,15,20..12,18,24....
            semiprimes[y] = True
    
    # for x, y in enumerate(semiprimes):
    #     print(x, y)
    
    # Reverse loop: if element index/2 is marked as True then mark current index element as False.
    # Basically removing elements which are (notprime * 2) which exists in list. These are not semiprimes
    for x in range(len(semiprimes), 0, -1):
        if x % 2 == 0:
            if semiprimes[x//2]:
                semiprimes[x] = False
    
    # for x, y in enumerate(semiprimes):
    #     print(x, y)

    result = []

    for x, y in zip(P, Q):
        count = 0
        for z in semiprimes[x:(y+1)]:
            if z: 
                count +=1
        result.append(count)
    
    # print(result)
    return result






print(solution(26, [1, 4, 16], [26, 10, 20]))


