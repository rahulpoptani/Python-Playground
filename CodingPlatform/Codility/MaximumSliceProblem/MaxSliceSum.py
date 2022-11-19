'''
A non-empty array A consisting of N integers is given. 
A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. 
The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:
A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0

the function should return 5 because:

        (3, 4) is a slice of A that has sum 4,
        (2, 2) is a slice of A that has sum −6,
        (0, 1) is a slice of A that has sum 5,
        no other slice of A has sum greater than (0, 1).
'''
import sys

def solution(A):
    if len(A) < 1:
        return 0
    global_sum = 0
    local_sum = 0
    for x in A:
        local_sum = max(local_sum + x, x)
        global_sum = max(global_sum, local_sum)
    return global_sum

print(solution([3, 2, -6, 4, 0]))
print(solution([3, 2, -6, 4, 1, 1]))
print(solution([]))