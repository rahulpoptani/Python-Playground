'''
Rotate an array to the right by a given number of steps.
For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
For example, given
    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

For another example, given        
    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given
    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]    
'''

def solution(A, K):
    size = len(A)
    if (K == 0 or size == 0 or K == size): return A
    result = [None] * size
    for i in range(size):
        pos = (i + K) % size
        result[pos] = A[i]
    return result


print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 1))
print(solution([1, 2, 3, 4], 4))
