'''
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.
For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

the function may return 0, 2, 4, 6 or 7, as explained above.

Given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. 
The function should return −1 if array A does not have a dominator.
'''

def solution(A):
    freq = {}
    halfSize = len(A)//2
    for x in range(len(A)):
        if A[x] in freq:
            freq[A[x]] = freq[A[x]] + 1
            if freq[A[x]] > halfSize:
                return x
        else:
            freq[A[x]] = 1
    return -1

print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
print(solution([]))

