'''
You are given an array A consisting of N integers.
For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6

For the following elements:

        A[0] = 3, the non-divisors are: 2, 6,
        A[1] = 1, the non-divisors are: 3, 2, 3, 6,
        A[2] = 2, the non-divisors are: 3, 3, 6,
        A[3] = 3, the non-divisors are: 2, 6,
        A[4] = 6, there aren't any non-divisors.

the function should return [2, 4, 3, 2, 0], as explained above.
Given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.
'''

from math import sqrt

def solution(A):
    # create map of occurrences
    freq = {}
    for x in A:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    # print(freq)

    # create number of divisors count
    divCountMap = {}
    for key, value in freq.items():
        divisorCount = 0
        for x in range(1, int(sqrt(key))+1):
            if key % x == 0:
                if x in freq:
                    divisorCount += freq[x]
                if x < sqrt(key):
                    opp = key / x
                    if opp in freq:
                        divisorCount += freq[opp]
        divCountMap[key] = divisorCount
    
    # print(divCountMap)

    nonDivisor = [0] * len(A)

    for x in range(len(A)):
        nonDivisor[x] = len(A) - divCountMap[A[x]]
    
    # print(nonDivisor)

    return nonDivisor


print(solution([3, 1, 2, 3, 6]))
