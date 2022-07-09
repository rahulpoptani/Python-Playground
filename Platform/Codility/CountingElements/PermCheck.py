'''
A non-empty array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.
For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, the function should return 1.
    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing. The function should return 0.
'''


def solution(A):
    myset = set()
    for x in range(1, len(A)+1):
        myset.add(x)
    for x in A:
        try:
            myset.remove(x)
        except KeyError:
            return 0
    return 1

print(solution([4, 1, 3, 2]))
print(solution([4, 1, 3]))
