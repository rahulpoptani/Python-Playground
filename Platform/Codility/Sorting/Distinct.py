'''
Given an array A consisting of N integers, returns the number of distinct values in array A.
For example, given array A consisting of six elements such that:
 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1

the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.
'''

def solution(A):
    myset = set()
    for x in A:
        myset.add(x)
    return len(myset)

print(solution([2, 1, 1, 2, 3, 1]))
print(solution([-1, 0, -1, 1, 2]))
print(solution([]))