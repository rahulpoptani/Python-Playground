'''
A non-empty array A consisting of N integers is given.
A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.
The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

contains the following example double slices:

        double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
        double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
        double slice (3, 4, 5), sum is 0.

the function should return 17, because no double slice of array A has a sum of greater than 17.
'''

def solution(A):
    forward = [0] * len(A)
    backward = [0] * len(A)

    if len(A) == 3: return 0

    for x in range(1, len(A)-1):   # Do not consider first and last element
        forward[x] = max(A[x], forward[x-1] + A[x])
    
    for x in range(len(A)-2, 0, -1):   # Do not consider last2 and first element
        backward[x] = max(A[x], backward[x+1] + A[x])
    
    maximum = 0
    for x in range(1, len(A)-1):
        maximum = max(forward[x-1] + backward[x+1], maximum)
    
    return maximum

print(solution([3, 2, 6, -1, 4, 5, -1, 2]))
